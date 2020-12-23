
import numpy as np
import pandas as pd
import boto3
import sagemaker
import sys

sys.path.append("../")
import utils.config as cfg

config = cfg.get_config()
bucket_name = config['bucket_name']
bucket_prefix = config['bucket_prefix']
sgmk_session = config['sgmk_session']
sgmk_role = config['sgmk_role']

train_uri = cfg.get_s3_path('train')
val_uri = cfg.get_s3_path('validation')

# specify container
training_image = sagemaker.image_uris.retrieve("xgboost", region=region, version="1.0-1")

# Define the data input channels for the training job:
s3_input_train = sagemaker.inputs.TrainingInput(train_uri, content_type="csv")
s3_input_validation = sagemaker.inputs.TrainingInput(val_uri, content_type="csv")

print(f"{s3_input_train.config}\n\n{s3_input_validation.config}")

# Instantiate an XGBoost estimator object
estimator = sagemaker.estimator.Estimator(
    image_uri=training_image,  # XGBoost algorithm container
    instance_type="ml.m5.xlarge",  # type of training instance
    instance_count=1,  # number of instances to be used
    role=sgmk_role,  # IAM role to be used
    max_run=20*60,  # Maximum allowed active runtime
    use_spot_instances=True,  # Use spot instances to reduce cost
    max_wait=30*60,  # Maximum clock time (including spot delays)
)

# define its hyperparameters
estimator.set_hyperparameters(
    num_round=150,     # int: [1,300]
    max_depth=5,     # int: [1,10]
    alpha=2.5,         # float: [0,5]
    eta=0.5,           # float: [0,1]
    objective="binary:logistic",
)

# start a training (fitting) job
estimator.fit({ "train": s3_input_train, "validation": s3_input_validation })


# Real-time endpoint:
predictor = estimator.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large",
    # wait=False,  # Remember, predictor.predict() won't work until deployment finishes!
)

print(predictor)



