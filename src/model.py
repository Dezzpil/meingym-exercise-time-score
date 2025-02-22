import joblib


class Model:
    def __init__(self, model_path):
        self.pipeline = joblib.load(model_path)

    def parse_item(self, data_item):
        x_val = []
        for i in self.pipeline.feature_names_in_:
            if i in data_item:
                x_val.append(data_item[i])
        if len(x_val) != len(self.pipeline.feature_names_in_):
            raise TypeError('data mismatch model features')
        return x_val

    def parse_data(self, data):
        x = []
        for data_item in data:
            x.append(self.parse_item(data_item))
        return x

    def predict(self, x):
        predictions = self.pipeline.predict(x)
        return predictions.tolist()
