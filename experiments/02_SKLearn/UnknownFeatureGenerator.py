import pandas as pd
import numpy as np
import re

class UnknownFeatureGenerator():
    def __init__(self, feature, new_feature):
        self.feature = feature
        self.new_feature = new_feature
        
    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, input_df, **transform_params):
        input_df_ = input_df.copy() # creating a copy to avoid changes to original dataset
        unk_pat = "Not Available|NULL|Not Mapped|unknown"
        input_df_[self.new_feature] = input_df_[self.feature].str.count(
            unk_pat, 
            flags=re.IGNORECASE
        )
        return input_df_


