from app import db
from datetime import datetime, timezone

publicacion_etiqueta = db.Table('publicacion_etiqueta',
    db.Column('publicacion_id', db.Integer, db.ForeignKey('publicacion.id'), primary_key=True),
    db.Column('etiqueta_id',    db.Integer, db.ForeignKey('etiqueta.id'),    primary_key=True)
)

class Publicacion(db.Model):
    __tablename__ = 'publicacion'
    id         = db.Column(db.Integer, primary_key=True)
    titulo     = db.Column(db.String(200), nullable=False)
    contenido  = db.Column(db.Text)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario    = db.relationship('User', backref=db.backref('publicaciones', lazy='dynamic'))
    etiquetas  = db.relationship('Etiqueta', secondary=publicacion_etiqueta, backref=db.backref('publicaciones', lazy='dynamic'))