"""
    This file aims to test if we can read our model using ModelPersistence class
"""
from persistence.model_persistence import ModelPersistence

my_model = ModelPersistence.read_model()

print(my_model.feature_importances_)