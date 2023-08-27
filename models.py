from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Response(db.Model):
    __tablename__ = 'responses'
    _id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    resp1 = db.Column(db.Integer)
    resp2 = db.Column(db.Integer)
    resp3 = db.Column(db.Integer)
    resp4 = db.Column(db.Integer)
    resp5 = db.Column(db.Integer)

    def __init__(self, resp1, resp2, resp3, resp4, resp5):
        self.resp1 = resp1
        self.resp2 = resp2
        self.resp3 = resp3
        self.resp4 = resp4
        self.resp5 = resp5

    def __repr__(self):
        return f'{self.resp1}, {self.resp2}, {self.resp3}, {self.resp4}, {self.resp5}'