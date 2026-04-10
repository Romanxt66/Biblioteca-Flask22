from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from app.models.etiqueta import Etiqueta
from app import db

bp = Blueprint('etiqueta', __name__, url_prefix='/Etiqueta')

@bp.route('/')
@login_required
def index():
    data = Etiqueta.query.all()
    return render_template('etiqueta/index.html', data=data)

@bp.route('/ver/<int:id>')
@login_required
def ver(id):
    etiqueta = Etiqueta.query.get_or_404(id)
    return render_template('etiqueta/ver.html', etiqueta=etiqueta)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        nueva = Etiqueta(
            nombre=request.form['nombre'],
            slug=request.form['slug']
        )
        db.session.add(nueva)
        db.session.commit()
        return redirect(url_for('etiqueta.index'))
    return render_template('etiqueta/add.html')

@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    etiqueta = Etiqueta.query.get_or_404(id)
    db.session.delete(etiqueta)
    db.session.commit()
    return redirect(url_for('etiqueta.index'))

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    etiqueta = Etiqueta.query.get_or_404(id)
    if request.method == 'POST':
        etiqueta.nombre = request.form['nombre']
        etiqueta.slug   = request.form['slug']
        db.session.commit()
        return redirect(url_for('etiqueta.index'))
    return render_template('etiqueta/edit.html', etiqueta=etiqueta)