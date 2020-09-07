import pytest
from model.get_prediction import get_prediction
import numpy as np

def test_model():
    features = {'median_age' : 12}
    
    try:
        predicted_value = get_prediction(features)
    except:
        predicted_value = 0
    
    real_value = 191392.54
    diff = abs(predicted_value - real_value)
    assert diff < 1e-6