
import argparse
import joblib
#from sklearn.externals import joblib
import os

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score

from sklearn.compose import ColumnTransformer
#, make_column_selector
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Binarizer, StandardScaler, OneHotEncoder
import UnknownFeatureGenerator as ufg

# inference functions ---------------
def model_fn(model_dir):
    clf = joblib.load(os.path.join(model_dir, "model.joblib"))
    return clf


if __name__ =='__main__':
    
    #------------------------------- parsing input parameters (from command line)
    print('extracting arguments')
    parser = argparse.ArgumentParser()

    # RandomForest hyperparameters
    parser.add_argument('--n_estimators', type=int, default=150)
    parser.add_argument('--min_samples_leaf', type=int, default=20)
    parser.add_argument('--max_depth', type=int, default=9)
    
    # Data, model, and output directories
    parser.add_argument('--model_dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    parser.add_argument('--train_dir', type=str, default=os.environ.get('SM_CHANNEL_TRAIN'))
    parser.add_argument('--test_dir', type=str, default=os.environ.get('SM_CHANNEL_TEST'))
    parser.add_argument('--train_file', type=str, default='train.csv')
    parser.add_argument('--test_file', type=str, default='validation.csv')
    parser.add_argument('--features', type=str, default='')  # explicitly name which features to use
    parser.add_argument('--target_variable', type=str)  # explicitly name the column to be used as target

    args, _ = parser.parse_known_args()
    
    #------------------------------- data preparation
    print('reading data')
    train_df = pd.read_csv(os.path.join(args.train_dir, args.train_file))
    test_df = pd.read_csv(os.path.join(args.test_dir, args.test_file))

    features = args.features.split()
    if features == []:
        features = list(train_df.columns)
        features.remove(args.target_variable)
    
    print('building training and testing datasets')
    X_train = train_df[features]
    X_test = test_df[features]
    y_train = train_df[args.target_variable]
    y_test = test_df[args.target_variable]
    
    
    numeric_cols = list( X_train.select_dtypes(include="number").columns)
    categorical_cols = list( X_train.select_dtypes(exclude="number").columns)
    
    #------------------------------- setup the preprocessing
    print('preprocesser setup')
    
    feature_gen = Pipeline([
        ("unknown", ufg.UnknownFeatureGenerator("admission_type_id", "UNKNOWN_admission_type") )
    ])
    
    numeric_transformer = make_pipeline(
        SimpleImputer(strategy='median'),
        StandardScaler()
    )

    categorical_transformer = make_pipeline(
        SimpleImputer(strategy='constant', fill_value='missing'),
        OneHotEncoder(handle_unknown='ignore')
    )

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_cols),
            ("cat", categorical_transformer, categorical_cols)
        ]
    )
    
    #------------------------------- model training
    print('training model')
    rfcl = RandomForestClassifier(
        n_estimators=args.n_estimators,
        min_samples_leaf=args.min_samples_leaf,
        max_depth=args.max_depth,
        n_jobs=-1)
    
    model = Pipeline(steps=[
        ('feature_gen', feature_gen),
        ('preprocessor', preprocessor),
        ('rf', rfcl )
    ])
    
    model.fit(X_train, y_train)
    
    #-------------------------------  model testing
    print('testing model')

    test_preds = model.predict_proba(X_test)
    roc_auc = roc_auc_score(y_test, test_preds[:,1])
    print("Validation AUC: ", roc_auc)
        
    #------------------------------- save model
    path = os.path.join(args.model_dir, "model.joblib")
    joblib.dump(model, path)
    print('model saved at ' + path)
