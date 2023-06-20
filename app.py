import pickle
from flask import Flask, request, render_template
import pandas as pd
from waitress import serve

# Starting the WebApp Development
app = Flask(__name__)

# Loading the pickle file
clmodel = pickle.load(open('clmodel.pkl', 'rb'))

# Making routes
@app.route('/')
def home():
    return render_template('home.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    data = {
        'Pregnancies': [float(request.form['Pregnancies'])],
        'Glucose': [float(request.form['Glucose'])],
        'BloodPressure': [float(request.form['BloodPressure'])],
        'SkinThickness': [float(request.form['SkinThickness'])],
        'Insulin': [float(request.form['Insulin'])],
        'BMI': [float(request.form['BMI'])],
        'DiabetesPedigreeFunction': [float(request.form['DiabetesPedigreeFunction'])],
        'Age': [float(request.form['Age'])]
    }

    try:
        input_data = pd.DataFrame(data)
        output = clmodel.predict(input_data)
        predicted_value = int(output[0])
        prediction_text = ""
        if predicted_value == 1:
            prediction_text = 'You have diabetes.'
        else:
            prediction_text = 'You do not have diabetes.'
        return render_template('home.html', prediction_text=prediction_text)
    except Exception as e:
        error_message = str(e)
        app.logger.error(error_message)
        prediction_text = 'Prediction failed: {}'.format(error_message)
        return render_template('home.html', prediction_text=prediction_text)

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=5000)
