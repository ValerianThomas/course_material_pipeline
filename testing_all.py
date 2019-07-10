from model.run_pipeline import read_train
from model.prediction import make_prediction
import os
import pandas as pd
TEST_DATA = os.path.dirname(os.path.realpath(__file__))+'/model/datasets/test.csv'
data = pd.read_csv(TEST_DATA)
X 
print(make_prediction(X))