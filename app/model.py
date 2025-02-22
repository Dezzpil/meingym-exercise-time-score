import joblib
import pandas as pd

class Model:
    def __init__(self, model_path):
        self.pipeline = joblib.load(model_path)

    def predict(self, input_data):
        # Convert input data to DataFrame
        input_df = pd.DataFrame(input_data)
        # Make predictions
        predictions = self.pipeline.predict(input_df)
        return predictions.tolist()
