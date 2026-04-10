from app import db
from flask_login import UserMixin    
from datetime import datetime, timezone



class User(db.Model, UserMixin):
    __tablename__ = 'usuario'
    idUser       = db.Column('id',         db.Integer, primary_key=True)
    nameUser     = db.Column('nombre',     db.String(100), nullable=False)
    emailUser    = db.Column('email',      db.String(150), unique=True, nullable=False)
    passwordUser = db.Column('password',   db.String(120), nullable=False)
    creado_en    = db.Column(db.DateTime,  default=lambda: datetime.now(timezone.utc))

    # loansUser         = db.relationship("Loan", back_populates="user", lazy='dynamic')
    # computerLoansUser = db.relationship('ComputerLoan', back_populates='user', lazy='dynamic')

    def get_id(self):
        return str(self.idUser)

    def to_dict(self):
        return {
            "idUser":    self.idUser,
            "nameUser":  self.nameUser,
            "emailUser": self.emailUser,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def validate_registration(nameUser, emailUser, passwordUser):
        errors = []

        if not nameUser or not nameUser.strip():
            errors.append("El nombre es obligatorio")

        if not emailUser or not emailUser.strip():
            errors.append("El email es obligatorio")
        elif User.query.filter_by(emailUser=emailUser).first():
            errors.append("El email ya está registrado")

        if not passwordUser:
            errors.append("La contraseña es obligatoria")
        elif len(passwordUser) < 6:
            errors.append("La contraseña debe tener al menos 6 caracteres")

        return errors