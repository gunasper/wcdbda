import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.preprocessing import FunctionTransformer

class PassthroughTransformer(FunctionTransformer, BaseEstimator):
    """
        This class just pass through features that shouldn't be
        modified during column transformation step
    """
    def transform(self, X: pd.DataFrame):
        self.X = X
        return X

    def get_feature_names(self):
        return self.X.columns.to_list()
