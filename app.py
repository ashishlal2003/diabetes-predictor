import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

# Starting the WebApp Development
app = Flask(__name__)

# Loading the pickle file
clmodel = pickle.load(open('clmodel.pkl', 'rb'))

# Making routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    
    # Convert dictionary to NumPy array
    input_data = np.array(list(data.values()))
    
    # Perform any necessary preprocessing on the input_data
    
    try:
        output = clmodel.predict(input_data.reshape(1, -1))
        predicted_value = int(output[0])  # Convert to int
        
        return jsonify({'predicted_value': predicted_value})
    except Exception as e:
        error_message = str(e)
        app.logger.error(error_message)
        return jsonify({'error': 'Prediction failed', 'error_message': error_message})

if __name__ == "__main__":
    app.run(debug=True)
