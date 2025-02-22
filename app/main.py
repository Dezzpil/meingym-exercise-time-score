from flask import Flask, request, jsonify
from .model import Model

app = Flask(__name__)

# Load the model
model = Model("models/random_forest_pipeline.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request
    input_data = request.json
    # Make predictions
    predictions = model.predict(input_data)
    # Return predictions as JSON
    return jsonify({'predictions': predictions})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
