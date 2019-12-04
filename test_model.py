"""
    This file aims to test if we can read our model using ModelPersistence class
"""
from persistence.model_persistence import ModelPersistence

my_model = ModelPersistence.read_model()

importances = my_model['rf'].feature_importances_
feature_names = list(my_model['ct'].get_feature_names())

for x, y in zip(importances, feature_names):
    print(x, y)

assert(len(importances) == len(feature_names))