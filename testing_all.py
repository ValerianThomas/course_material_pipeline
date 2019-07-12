from model.run_pipeline import read_train
from model.prediction import make_prediction
import os
import pandas as pd

TEST_DATA = {"curb-weight":3015,"engine-size":200},{"curb-weight":3004,"engine-size":121},{"curb-weight":4004,"engine-size":100}

print(make_prediction(TEST_DATA))