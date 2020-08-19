import joblib

filepath = './data/linear_regression.joblib'

features_names = {'median_age'}

model = joblib.load(filepath)
