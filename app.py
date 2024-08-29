from flask import Flask, request, render_template
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pickle
from ucimlrepo import fetch_ucirepo 

app = Flask(__name__)

# Fetch and prepare data
wine_quality = fetch_ucirepo(id=186)  
x = wine_quality.data.features 
y = wine_quality.data.targets 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input features
        features = [
            float(request.form['fixed_acidity']),
            float(request.form['volatile_acidity']),
            float(request.form['citric_acid']),
            float(request.form['residual_sugar']),
            float(request.form['chlorides']),
            float(request.form['free_sulfur_dioxide']),
            float(request.form['total_sulfur_dioxide']),
            float(request.form['density']),
            float(request.form['pH']),
            float(request.form['sulfates']),
            float(request.form['alcohol'])
        ]

        # Make a prediction
        prediction = model.predict(np.array([features]))
        return render_template('index.html', prediction=prediction[0])

    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
