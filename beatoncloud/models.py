from beatoncloud import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def is_active(self):
        # 이 사용자가 활성 상태인지 여부를 반환
        return self.active


class InterestInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classic = db.Column(db.Boolean, default=False)
    jazz = db.Column(db.Boolean, default=False)
    pop = db.Column(db.Boolean, default=False)
    ballade = db.Column(db.Boolean, default=False)
    hiphop = db.Column(db.Boolean, default=False)
    reggae = db.Column(db.Boolean, default=False)
    trot = db.Column(db.Boolean, default=False)
    electronic = db.Column(db.Boolean, default=False)
    rock = db.Column(db.Boolean, default=False)
    rnb = db.Column(db.Boolean, default=False)
