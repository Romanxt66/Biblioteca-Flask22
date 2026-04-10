from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.users import User
from werkzeug.security import check_password_hash

bp = Blueprint('auth', __name__)

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        emailUser    = request.form['emailUser']
        passwordUser = request.form['passwordUser']

        user = User.query.filter_by(emailUser=emailUser).first()

        if user and check_password_hash(user.passwordUser, passwordUser):
            login_user(user)
            flash("Login exitoso!", "success")
            if user.perfil is None:
                return redirect(url_for('perfil.crear_mio'))
            return redirect(url_for('perfil.mi_perfil'))
        
        flash('Correo o contraseña incorrectos.', 'danger')
    
    if current_user.is_authenticated:
        return redirect(url_for('perfil.mi_perfil'))
    return render_template("login.html")

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('auth.login'))