import pandas as pd 
import os  
from model.pipeline_preparation import prediction_pipeline
from sklearn.model_selection import train_test_split

print("real", os.path.realpath(__file__))
TRAINING_DATA_FILE = os.path.dirname(os.path.realpath(__file__)) + '/datasets/train.csv'
TESTING_DATA_FILE = os.path.dirname(os.path.realpath(__file__)) + '/datasets/test.csv'
def _remove_missing_y (df):
  df = df.copy()
  df.dropna(subset=['price'],axis=0, inplace=True)
  return df

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
  print(prediction_pipeline.score(X_test,y_test))


if __name__ == '__main__':
  read_train()