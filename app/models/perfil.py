from app import db
from datetime import datetime, timezone

class Perfil(db.Model):
    __tablename__ = 'perfil'
    id          = db.Column(db.Integer, primary_key=True)
    bio         = db.Column(db.Text)
    usuario_id  = db.Column(db.Integer, db.ForeignKey('usuario.id'), unique=True, nullable=False)
    usuario     = db.relationship('User', backref=db.backref('perfil', uselist=False))