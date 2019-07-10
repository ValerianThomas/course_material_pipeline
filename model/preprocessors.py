import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class Replace_nan_numerical_values (BaseEstimator, TransformerMixin):
  def __init__(self, features):
    self.features = features

  def fit(self,X,y):
    return self
  def transform(self,X):
    X = X.copy()
    for feature in self.features :
      X[feature] = X[feature].fillna(X[feature].mode()[0])
    return X


class Get_Dummies (BaseEstimator, TransformerMixin):
  
  def fit(self,X,y):

    return self

  def transform(self,X):
    X = X.copy()
    X = pd.get_dummies(X, drop_first=True)
    return X


class Replace_missing_Dummies (BaseEstimator, TransformerMixin):
  def __init__(self, features):
    self.features = features

  def fit(self,X,y):
    return self

  def transform(self,X):
    X = X.copy()
    for feature in self.features:
      if feature not in X.columns:
        X[feature] = [0]*len(X.index)
    return X


class Select_all_usefull_features (BaseEstimator, TransformerMixin):
  def __init__ (self,features):
    self.features = features
  
  def fit(self,X,y):
    return self
  def transform(self,X):
    X = X.copy()
    X = X[self.features]
    print("final features",X.columns)
    return X
