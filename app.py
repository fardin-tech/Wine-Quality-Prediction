from flask import Flask,render_template,request
from waitress import serve
import pandas as pd
import numpy as np
import joblib
from mlproject.utlis.common import read_yaml
from mlproject.constants import SCHEMA_FILE_PATH
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    schema=read_yaml(SCHEMA_FILE_PATH)
    print(schema)
    d=dict(fixed_acidity=request.form['fixed_acidity'],
    volatile_acidity=request.form['volatile_acidity'],
    citric_acid=request.form['citric_acid'],
    residual_sugar=request.form['residual_sugar'],
    chlorides=request.form['chlorides'],
    free_sulfur_dioxide=request.form['free_sulfur_dioxide'],
    total_sulfur_dioxide=request.form['total_sulfur_dioxide'],
    density=request.form['density'],
    pH=request.form['pH'],
    sulphates=request.form['sulphates'],
    alcohol=request.form['alcohol'])
    model=joblib.load('artifacts/model_trainer/model.joblib')
    array=np.array(list(d.values()),dtype='float64').reshape(1,-1)
    predict=model.predict(array)

    return render_template('index.html',name=predict[0])

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=50100, threads=1)
