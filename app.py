from flask import Flask, request, render_template
from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

app = Flask(__name__)

with open('model.pkl','wb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_value= float(request.form['input_value'])
    prediction = model.predict(np.array([[input_value]]))

    return render_template('index.html', input_value=input_value, prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)