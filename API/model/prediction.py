import pandas as pd 
import os
import pickle
import pandas as pd
import json
TEST_DATA = os.path.dirname(os.path.realpath(__file__)) + '/saved_model/model.sav'

def make_prediction(input_data):
  if type(input_data) is dict:
    data = pd.DataFrame(input_data, index=[0])
  else :
    data = pd.DataFrame(input_data)
  
  model = pickle.load(open(TEST_DATA,'rb'))
  return model.predict(data)