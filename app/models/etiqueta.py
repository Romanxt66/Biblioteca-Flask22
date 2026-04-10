from app import db

class Etiqueta(db.Model):
    __tablename__ = 'etiqueta'
    id     = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    slug   = db.Column(db.String(50), nullable=False)