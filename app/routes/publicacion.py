from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from app.models.publicacion import Publicacion
from app.models.etiqueta import Etiqueta
from app import db

bp = Blueprint('publicacion', __name__, url_prefix='/Publicacion')

@bp.route('/')
@login_required
def index():
    data = Publicacion.query.all()
    return render_template('publicacion/index.html', data=data)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nueva = Publicacion(
            titulo=request.form['titulo'],
            contenido=request.form['contenido'],
            usuario_id=current_user.idUser
        )
        etiquetas = Etiqueta.query.filter(Etiqueta.id.in_(request.form.getlist('etiquetas'))).all()
        nueva.etiquetas = etiquetas
        db.session.add(nueva)
        db.session.commit()
        return redirect(url_for('perfil.mi_perfil'))
    etiquetas = Etiqueta.query.all()
    return render_template('publicacion/add.html', etiquetas=etiquetas)

@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    pub = Publicacion.query.get_or_404(id)
    db.session.delete(pub)
    db.session.commit()
    return redirect(url_for('perfil.mi_perfil'))

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    pub = Publicacion.query.get_or_404(id)
    if request.method == 'POST':
        pub.titulo    = request.form['titulo']
        pub.contenido = request.form['contenido']
        etiquetas = Etiqueta.query.filter(Etiqueta.id.in_(request.form.getlist('etiquetas'))).all()
        pub.etiquetas = etiquetas
        db.session.commit()
        return redirect(url_for('publicacion.index'))
    etiquetas = Etiqueta.query.all()
    return render_template('publicacion/edit.html', pub=pub, etiquetas=etiquetas)   
     
@bp.route('/ver-etiquetas/<int:id>')
@login_required
def ver_etiquetas(id):
    pub = Publicacion.query.get_or_404(id)
    return render_template('publicacion/ver_etiquetas.html', pub=pub)    