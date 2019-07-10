import pandas as pd 
import os
import pickle

TEST_DATA = os.path.dirname(os.path.realpath(__file__)) + '/saved_model/model.sav'

def make_prediction(data):
  model = pickle.load(open(TEST_DATA,'rb'))
  return model.predict(data)