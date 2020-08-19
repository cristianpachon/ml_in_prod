from model import model
from model import features_names
import numpy as np

def transform_features(raw_features):
    features = ['median_age']
    list_features = [raw_features[feature] for feature in features_names]
    print(np.array(list_features).reshape(-1, 1))
    return np.array(list_features).reshape(-1, 1)


def get_prediction(features):
    features_transformed = transform_features(features)
    print(features_transformed)
    return model.predict(features_transformed)
