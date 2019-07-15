from flask import Flask 
from .ModelView import prediction_app
from .config import ProductionConfig
def create_app():
  server = Flask('car_prediction')
  server.config.from_object(ProductionConfig)
  server.register_blueprint(prediction_app)
  return server