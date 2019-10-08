from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskges_ecole import db
from flaskges_ecole.models import Eleve, Classe
from flaskges_ecole.eleves.forms import EleveForm

eleves = Blueprint('eleves', __name__)

@eleves.route('/eleve/new', methods=['POST', 'GET'])
@login_required
def new_eleve():
    form = EleveForm()
    if form.validate_on_submit():
       eleve = Eleve(prenom_eleve=form.prenom_eleve.data, nom_eleve=form.nom_eleve.data, sexe=form.sexe.data, user=current_user)
       classe = Classe.query.filter_by(id=form.id_nom_classe.data).first()
       classe.eleves.append(eleve)
       db.session.add(classe)
       db.session.commit()
       flash(' Inscription reussi avec success !','success')
       return redirect(url_for('main.dashbord'))
    classes = Classe.query.all()
    return render_template('eleves/new_eleve.html', form=form, legend='New Eleve', title='New Eleve', classes=classes)








