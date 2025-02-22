from flask import Flask, request, jsonify
from .model import Model
import json


app = Flask(__name__)
model = Model(app.root_path + "/../models/random_forest_pipeline.pkl")


@app.route('/predict', methods=['POST'])
def predict():
    x = []

    # Read line by line from request stream
    for line in request.stream:
        try:
            # Decode and parse each line
            json_line = json.loads(line.decode('utf-8'))
            print(json_line)
            x.append(model.parse_item(json_line))
        except json.JSONDecodeError:
            return jsonify({
                'status': 'error',
                'message': 'Invalid JSON format'
            }), 400

    return jsonify({'predictions': model.predict(x)})
