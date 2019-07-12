import pandas as pd 
import os
import pickle
from .pipeline_preparation import prediction_pipeline

print("real", os.path.realpath(__file__))
TRAINING_DATA_FILE = os.path.dirname(os.path.realpath(__file__)) + '/datasets/train.csv'
TESTING_DATA_FILE = os.path.dirname(os.path.realpath(__file__)) + '/datasets/test.csv'
MODEL_PATH = os.path.dirname(os.path.realpath(__file__)) + '/saved_model/model.sav'
def _remove_missing_y (df):
  df = df.copy()
  df.dropna(subset=['price'],axis=0, inplace=True)
  return df

def _save_model(model) :
  pickle.dump(model,open(MODEL_PATH,'wb'))

def read_train():
  data = pd.read_csv(TRAINING_DATA_FILE)
  test_data = pd.read_csv(TESTING_DATA_FILE)
  data = _remove_missing_y(data)
  test_data = _remove_missing_y(test_data)

  X_train = data
  y_train = data['price']

  X_test = test_data
  y_test = test_data['price']

  prediction_pipeline.fit(X_train,y_train)
  _save_model(prediction_pipeline)  

if __name__ == '__main__':
  read_train()