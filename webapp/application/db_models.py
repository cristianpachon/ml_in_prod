from datetime import datetime
from application import db

class HouseInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(100), unique = True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    house_description = db.Column(db.JSON)
    def __repr__(self):
        return 'RawFeatures({}, {})'.format(self.id, self.house_description)

class RawFeatures(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    raw_features = db.Column(db.JSON)

    def __repr__(self):
        return 'RawFeatures({}, {})'.format(self.id, self.raw_features)