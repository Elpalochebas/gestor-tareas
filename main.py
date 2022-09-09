from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import db

from models import Tarea

app = Flask(__name__)


@app.route('/')
def home():
    tareas_db = db.session.query(Tarea).all()

    for tarea in tareas_db:
        tarea.date_format()

    categorias = db.session.execute('SELECT DISTINCT categoria FROM tarea')

    return render_template('index.html', lista_tareas=tareas_db, lista_categorias=categorias)


@app.route('/crear-tarea', methods=['POST'])
def crear():
    tarea = Tarea(  contenido=request.form['contenido_tarea'],
                    hecha=False,
                    categoria=request.form['categoria_tarea'],
                    fecha_creacion=datetime.now(),
                    fecha_entrega=datetime.strptime(request.form['fecha_tarea'], '%Y-%m-%dT%H:%M'))

    try: 
        db.session.add(tarea)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    return redirect(url_for('home'))

@app.route('/update-tarea/<id>', methods=['POST'])
def actualizar(id):
    db.session.query(Tarea).filter_by(id=int(id)).update(dict(
        contenido=request.form['contenido_tarea'], 
        categoria=request.form['categoria_tarea'],
        fecha_entrega=datetime.strptime(request.form['fecha_tarea'], '%Y-%m-%dT%H:%M')))
    try: 
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    return redirect(url_for('home'))


@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    db.session.query(Tarea).filter_by(id=int(id)).delete()
    try: 
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    return redirect(url_for('home'))


@app.route('/tarea-hecha/<id>')
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    tarea.hecha = not (tarea.hecha)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
    return redirect(url_for('home'))


if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)
