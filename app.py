from flask import Flask, request, render_template
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pickle
from ucimlrepo import fetch_ucirepo 

app = Flask(__name__)

wine_quality = fetch_ucirepo(id=186) 
  
# data (as pandas dataframes) 
x = wine_quality.data.features 
y = wine_quality.data.targets 
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=42)

with open('model.pkl','rb') as file:
    model = pickle.load(file)
model.fit(x_train,y_train)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    fixed_acidity = float(request.form['fixed_acidity'])
    volatile_acidity = float(request.form['volatile_acidity'])
    citric_acid = float(request.form['citric_acid'])
    residual_sugar = float(request.form['residual_sugar'])
    chlorides = float(request.form['chlorides'])
    free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
    total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
    density = float(request.form['density'])
    pH = float(request.form['pH'])
    sulfates = float(request.form['sulfates'])
    alcohol = float(request.form['alcohol'])

    input_features = np.array([fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,
                              sulfates,alcohol ])

    prediction = model.predict(np.array([input_features]))

    return render_template('index.html', input_features=input_features, prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)