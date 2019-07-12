import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from model.preprocessors import Select_all_usefull_features, Replace_nan_numerical_values, Get_Dummies, Replace_missing_Dummies
from sklearn.impute import SimpleImputer

NUMERICAL_FEATURES = ['curb-weight', 'engine-size']
DUMMIES_FEATURES  = ['make_mercedes-benz', 'num-of-cylinders_four']
ALL_FEATURES = NUMERICAL_FEATURES + DUMMIES_FEATURES
prediction_pipeline = Pipeline(
  [
  ('replace nan in selected features', Replace_nan_numerical_values(NUMERICAL_FEATURES)),
  ('get dummies variables', Get_Dummies()),
  ('replace all missing dummies', Replace_missing_Dummies(DUMMIES_FEATURES)),
  ('X select features',Select_all_usefull_features(ALL_FEATURES)),
  ('model_creation',RandomForestRegressor())
]
)

