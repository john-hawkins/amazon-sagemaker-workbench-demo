from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd
import numpy as np
import re

class UnknownCategoryFlagger(TransformerMixin, BaseEstimator):
    """
        This fature transformer will convert any categorical column
         into a numeric value indicating the presence of a set of
         potential Unknown values. 
        This is useful in dirty datasets that can have multiple codings
         that mean a value is unknown. E.g. unknown, null, ?, not captured.
    """

    def __init__(self, unknowns=['unknown','null','?','','not avilable']):
        self.unknowns = unknowns
        self.pattern = '^' + '$|^'.join(unknowns) + '$'

    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, X, y=None, **transform_params):
        for i in range(X.shape[1] ):
            X[:,i] = X[:,i].str.count(self.pattern,flags=re.IGNORECASE)

        return X


