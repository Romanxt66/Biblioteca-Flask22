from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models.perfil import Perfil
from app.models.publicacion import Publicacion
from app import db

bp = Blueprint('perfil', __name__, url_prefix='/Perfil')

@bp.route('/mi-perfil')
@login_required
def mi_perfil():
    perfil = Perfil.query.filter_by(usuario_id=current_user.idUser).first()
    if perfil is None:
        return redirect(url_for('perfil.crear_mio'))
    publicaciones = Publicacion.query.filter_by(usuario_id=current_user.idUser).all()
    return render_template('perfil/mi_perfil.html', perfil=perfil, publicaciones=publicaciones)

@bp.route('/crear', methods=['GET', 'POST'])
@login_required
def crear_mio():
    if Perfil.query.filter_by(usuario_id=current_user.idUser).first():
        return redirect(url_for('perfil.mi_perfil'))
    if request.method == 'POST':
        nuevo = Perfil(
            bio=request.form['bio'],

            usuario_id=current_user.idUser
        )
        db.session.add(nuevo)
        db.session.commit()
        flash('Perfil creado exitosamente.', 'success')
        return redirect(url_for('perfil.mi_perfil'))
    return render_template('perfil/crear.html')

@bp.route('/editar-mio', methods=['GET', 'POST'])
@login_required
def editar_mio():
    perfil = Perfil.query.filter_by(usuario_id=current_user.idUser).first_or_404()
    if request.method == 'POST':
        perfil.bio         = request.form['bio']
        
        db.session.commit()
        flash('Perfil actualizado.', 'success')
        return redirect(url_for('perfil.mi_perfil'))
    return render_template('perfil/editar.html', perfil=perfil)

@bp.route('/')
@login_required
def index():
    data = Perfil.query.all()
    return render_template('perfil/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nuevo = Perfil(
            bio=request.form['bio'],
            
            usuario_id=request.form['usuario_id']
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('perfil.index'))
    return render_template('perfil/add.html')

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    perfil = Perfil.query.get_or_404(id)
    if request.method == 'POST':
        perfil.bio         = request.form['bio']
        
        db.session.commit()
        return redirect(url_for('perfil.index'))
    publicaciones = Publicacion.query.filter_by(usuario_id=perfil.usuario_id).all()
    return render_template('perfil/edit.html', perfil=perfil, publicaciones=publicaciones)

@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    perfil = Perfil.query.get_or_404(id)
    db.session.delete(perfil)
    db.session.commit()
    return redirect(url_for('perfil.index'))

@bp.route('/ver-publicaciones/<int:id>')
@login_required
def ver_publicaciones(id):
    perfil = Perfil.query.get_or_404(id)
    publicaciones = Publicacion.query.filter_by(usuario_id=perfil.usuario_id).all()
    return render_template('perfil/ver_publicaciones.html', perfil=perfil, publicaciones=publicaciones)    