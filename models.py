from app import db
from datetime import datetime

class users(db.Model):
    usr_id = db.Column(db.Integer, primary_key=True)
    usr_email = db.Column(db.String(100), nullable = False)

    def __init__(self, id, email):
        self.usr_id = id
        self.usr_email = email