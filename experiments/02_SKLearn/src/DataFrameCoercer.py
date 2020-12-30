from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd

class DataFrameCoercer(TransformerMixin, BaseEstimator):
    """
        This transformer can be used to ensure that a dataset
        passing through a Pipeline, will be a DataFrame,

        Note: We presume that the initial fit is called with 
              pandas DataFrame
    """


    def __init__(self, columns=[]):
        self.columns = columns 


    def fit(self, X, y=None, **fit_params):
        if X.__class__.__name__ == "DataFrame":
            mycols = list(X.columns)
            self.columns = mycols 
        return self
    

    def transform(self, X, y=None, **transform_params):
        """
            Transform the matrix of values to be a DataFrame
        """

        if X.__class__.__name__ == "DataFrame":
            return X
        else:
            return pd.DataFrame(X, columns=self.columns)

