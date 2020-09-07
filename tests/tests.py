import pytest
from model import model
import numpy as np

def test_model():
    features = np.array([12]).reshape(-1, 1)
    
    try:
        predicted_value = model.predict(features)
    except:
        predicted_value = None

    real_value = 191392.543992269
    diff = abs(predicted_value - real_value)
    assert diff < 1e-6