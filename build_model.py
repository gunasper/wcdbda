"""
    This file aims to build and persist a pre-trained model
"""
import joblib

MODEL_FOLDER = 'persistence/models/'
MODEL_NAME = 'cls.pkl'
classifier_file = MODEL_FOLDER + MODEL_NAME

# load the csv data that will be used to train the model
data = ...

# apply feature engineering techniques
####
#
#   Your code here!
#
####
X, y = ...

# train the model
####
#
#   Your code here!
#
####
clf = ...

# persist the model
####
#
#   Your code here!
#
####
joblib.dump(clf, classifier_file)
