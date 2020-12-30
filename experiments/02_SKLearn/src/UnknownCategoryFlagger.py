from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd
import numpy as np
import re

class UnknownCategoryFlagger(TransformerMixin, BaseEstimator):
    """
        This feature transformer will convert any categorical column
         into a numeric value indicating the presence of a string from a set of
         values that indicate that the feature is unknown.
 
        This is useful in dirty datasets that can have multiple codings or sources
         that mean a value is unknown. E.g. unknown, null, ?, not captured.
    """

    def __init__(self, unknowns=['unknown','null','\?','','not avilable','not mapped','unavailable']):
        self.unknowns = unknowns
        self.pattern = '^' + '$|^'.join(unknowns) + '$'

    def fit(self, X, y=None, **fit_params):
        return self
    
    def transform(self, X, y=None, **transform_params):
        """
            Transform the matrix of values
             -- need to deal with single or multiple columns
        """
        r = re.compile(self.pattern, flags=re.IGNORECASE)

        vmatch = np.vectorize(lambda x: int(bool(r.match(str(x)))) )

        if X.__class__.__name__ == "DataFrame":
            X = X.values

        if len( X.shape ) > 1:
            for i in range(X.shape[1] ):
                X[:,i] = vmatch(X[:,i])
        else:
            X = vmatch(X)

        return pd.DataFrame(X)


