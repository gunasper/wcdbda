from datetime import datetime
import json

from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

from persistence.model_persistence import ModelPersistence

#load model
my_model = ModelPersistence.read_model()

app = Flask(__name__)
CORS(app)

@app.route("/health", methods=['GET'])
def health():
    result = {
        "msg": "Hello World! I'm up!",
        "now": datetime.now()
    }
    return result

@app.route("/v0/predict", methods=['POST'])
def predict():
    """
        Process received data in the way classifier expects to receive in order to make a prediction.
        Its important to maintain the relative order of the attributes to have the right result.
    """
    if request.method == 'POST':
        data = request.data
        data = json.loads(data.decode())

        ####
        # expected_data = {
        #   "expenses": 521654.65,
        #   "income": 6546.54,
        #   "assets": 6546.54,
        #   "debt": 6.54,
        #   "amount": 6.54,
        #   "price": 654.65,
        #   "seniority": "5",
        #   "home": "kajshakj",
        #   "time": "5466",
        #   "age": "654654",
        #   "marital": "married",
        #   "records": true,
        #   "job": "2321",
        #   "approved": true
        # }
        ####

        ####
        #
        #   Your code here! It will be a little tricky to recreate the "dummies"! Careful.
        #   parsed_data = {}
        #   parsed_data['Job_partime'] = 1 if data['job'] == 'parttime' else 0
        #   parsed_data['Job_others'] = 1 if data['job'] == 'others' else 0
        #
        ####
        value = True
        prob = 0.6

        result = {
            "prediction": {
                "value": value,
                "probability": 0.6
            },
            "prediction_time": datetime.now()
        }
        return result

@app.route("/v0/model_info", methods=['GET'])
def model_info():
    """
        This method aims to parse classifier information and send it to the caller;
        It also serves as a classifier health checker.
    """
    ####
    #
    #   Your code here!
    #   You should parse the feature importances of your classifier here
    #
    ####

    # Expected minimum variables
    name = "Random Forest Classifier"
    num_trees = 100
    max_depth = 7
    feature_importances = {
        'LSTAT': 0.5298,
        'RM': 0.4116,
        'DIS': 0.0252,
        'CRIM': 0.0172,
        'NOX': 0.0065,
        'PTRATIO': 0.0035
    }
    model_created_at = '2020-01-01 00:00:00'

    result = {
        'model_name': name,
        'num_trees': num_trees,
        'max_depth': max_depth,
        'feature_importances' : feature_importances,
        'model_created_at': model_created_at
    }
    return result
