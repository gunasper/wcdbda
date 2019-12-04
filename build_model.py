"""
    This file aims to build and persist a pre-trained model
"""
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import joblib

# custom code
from src.custom_transformers import PassthroughTransformer

DATA_FILE = "data/credit_data.csv"
MODEL_FOLDER = 'persistence/models/'
MODEL_NAME = 'cls.pkl'
classifier_file = MODEL_FOLDER + MODEL_NAME

# load the csv data that will be used to train the model
credit_df = pd.read_csv(DATA_FILE)

# apply feature engineering techniques
#Dados Booleanos
credit_df['Records'].replace({'no': False, 'yes': True}, inplace=True)
credit_df['Records'] = credit_df['Records'].astype('bool')
credit_df['Approved'] = credit_df['Status'].replace({'bad': False, 'good': True})
credit_df.drop(columns=['Status'], inplace=True)

#Dados Categóricos
categories_column = ['Home','Marital','Job']
for column in categories_column:
    credit_df[column] = credit_df[column].astype('category')

#Dados decimais
categories_column = ['Amount','Price']
for column in categories_column:
    credit_df[column] = credit_df[column].astype('float64')

credit_df = credit_df.dropna()

y = credit_df['Approved']
X = credit_df.drop(columns='Approved')
print("Para fazer predições, lembre-se, as features devem estar nessa ordem:")
print(credit_df.columns)

# column transformers
categorical_columns = ['Home', 'Marital', 'Job']
other_columns = list(set(X.columns) - set(categorical_columns))
ct = ColumnTransformer(
    [
        ('oh_enc', OneHotEncoder(categories='auto', sparse=False), categorical_columns),  # the column numbers I want to apply OH_ENC
        ('pt', PassthroughTransformer(validate=True), other_columns)
    ],
)

# creation of a pipeline
param = {'criterion': 'gini', 'max_depth': 10, 'n_estimators': 200}
clf = RandomForestClassifier(**param)

# train the model
model_pipeline = Pipeline(
    ([('ct', ct),
      ('rf', clf)])
)

model_pipeline.fit(X, y)

# persist the model
joblib.dump(model_pipeline, classifier_file)
