import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class UnknownFeatureGenerator(BaseEstimator, TransformerMixin):
    
  def __init__(self, feature_name, new_feature_name):
    print('\n>>>>>>>init() on CustomFeatureGenerator called.\n')
    self.feature_name = feature_name
    self.new_feature_name = new_feature_name
 
  def fit(self, X, y = None):
    print('\n>>>>>>>fit() on CustomFeatureGenerator called.\n')
    return self

  def transform(self, X, y = None):
    print('\n>>>>>>>transform() on CustomFeatureGenerator called.\n')
    X_ = X.copy() # creating a copy to avoid changes to original dataset

    X_[self.new_feature_name] = np.where(X_[self.feature_name] in ['Not Available','NULL','Not Mapped', 'Unknown','','?','null','unknown'],1,0)
    return X_
