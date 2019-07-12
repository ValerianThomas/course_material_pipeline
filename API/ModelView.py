from flask import Blueprint, request, jsonify
from model.prediction import make_prediction

prediction_app = Blueprint('prediction_route',__name__)

@prediction_app.route('/prediction',methods=['POST'])
def predict():
  req_data = request.get_json()
  prediction = make_prediction(req_data).tolist()


  return jsonify({'success':True,"prediction": prediction})

@prediction_app.route('/health',methods=['GET'])
def check_health():
  return "Server running"