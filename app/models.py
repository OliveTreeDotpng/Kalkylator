from app import db
from flask_login import UserMixin
from app import login_manager

@login_manager.user_loader
# Laddar användaren från databasen baserat på användar-ID.
def load_user(user_id):
    return User.query.get(int(user_id))

# UserMixin: Flask-Login klass för användarautentisering.
# User: Modell för användare med användarnamn, lösenord och sparade beräkningar.
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    # backref="owner": Skapar en relation mellan användare och beräkningar.
    # lazy=True: Laddar beräkningar för användaren vid behov.
    calculation = db.relationship("Calculation", backref="owner", lazy=True)

class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    expression = db.Column(db.String(100), nullable=False)
    result = db.Column(db.String(100), nullable=False)

