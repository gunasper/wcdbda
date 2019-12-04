from datetime import datetime
import json

from flask import Flask
from flask import request, jsonify
from flask_cors import CORS

import pandas as pd

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

        # features must have the same values as in training data, so we must make some processment to maintain categorical values
        job_values = {
            'fixo': 'fixed',
            'freelancer': 'freelance',
            'outros': 'others',
            'parcial': 'partime',
            'fixed': 'fixed',
            'freelance': 'freelance',
            'others': 'others',
            'partime': 'partime'
        }
        data['job'] = job_values[data['job']] if data['job'] in job_values else 'fixed'

        marital_values = {
            'divorciado': 'divorced',
            'casado': 'married',
            'separado': 'separated',
            'solteiro': 'single',
            'viuvo': 'widow',
            'divorced': 'divorced',
            'married': 'married',
            'separated': 'separated',
            'single': 'single',
            'widow': 'widow'
        }
        data['marital'] = marital_values[data['marital']] if data['marital'] in marital_values else 'single'

        home_values = {
            'ignorar': 'ignore',
            'outro': 'other',
            'propria': 'owner',
            'pais': 'parents',
            'privado': 'priv',
            'aluguel': 'rent',
            'ignore': 'ignore',
            'other': 'other',
            'owner': 'owner',
            'parents': 'parents',
            'priv': 'priv',
            'rent': 'rent'
        }

        parsed_data = {}
        data['home'] = home_values[data['home']] if data['home'] in home_values else 'rent'

        input_data = pd.DataFrame([
            (
                data['seniority'],
                data['home'],
                data['time'],
                data['age'],
                data['marital'],
                data['records'],
                data['job'],
                data['expenses'],
                data['income'],
                data['assets'],
                data['debt'],
                data['amount'],
                data['price']
            )
        ],
        columns=['Seniority', 'Home', 'Time', 'Age', 'Marital', 'Records', 'Job', 'Expenses', 'Income', 'Assets', 'Debt', 'Amount', 'Price'])

        ####
        # expected_data = {
        #     "expenses": 521654.65,
        #     "income": 6546.54,
        #     "assets": 6546.54,
        #     "debt": 6.54,
        #     "amount": 6.54,
        #     "price": 654.65,
        #     "seniority": "5",
        #     "home": "rent",
        #     "time": 5466,
        #     "age": 65,
        #     "marital": "married",
        #     "records": true,
        #     "job": "partial",
        #     "approved": true
        # }
        ####
        value = my_model.predict(input_data)
        prob = my_model.predict_proba(input_data)

        result = {
            "prediction": {
                "value": bool(value[0]),
                "probability": max(prob[0])
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
    importances = my_model['rf'].feature_importances_
    feature_names = list(my_model['ct'].get_feature_names())

    feature_importances = {y : x for x, y in zip(importances, feature_names)}

    # Expected minimum variables
    name = my_model['rf'].__class__.__name__
    num_trees = len(my_model['rf'].estimators_)
    max_depth = my_model['rf'].n_features_
    model_created_at = '2020-01-01 00:00:00'

    result = {
        'model_name': name,
        'num_trees': num_trees,
        'num_features': max_depth,
        'feature_importances' : feature_importances,
        'model_created_at': ModelPersistence.get_model_update_date()
    }
    return result
