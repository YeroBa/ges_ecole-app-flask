from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskges_ecole import db
from flaskges_ecole.models import Classe, Eleve, classe_eleves
from flaskges_ecole.classes.forms import ClasseForm, SearchNomClassSelectForm, UpdateClasseForm

classes = Blueprint('classes', __name__)

@classes.route('/classe/new', methods=['POST', 'GET'])
@login_required
def new_classe():
    form = ClasseForm()
    if form.validate_on_submit():
       classes = Classe(nom_classe=form.nom_classe.data)
       db.session.add(classes)
       db.session.commit()
       flash('Your classe has been created !','success')
       return redirect(url_for('classes.new_classe'))

    clas = Classe.query.all()
    return render_template('parametres/new_classe.html', form=form, title='New Classe', clas=clas)

@classes.route('/classe/<int:classe_id>/update', methods=['POST', 'GET'])
def update_classe(classe_id):
    classe = Classe.query.get_or_404(classe_id)
    form = UpdateClasseForm()
    if form.validate_on_submit():
       classe.nom_classe = form.nom_classe.data
       db.session.commit()
       flash('Your classe has been updated !', 'success')
       return redirect(url_for('classes.new_classe'))
    elif request.method == 'GET':
      form.nom_classe.data = classe.nom_classe

    return render_template('parametres/show_classe.html', classe=classe, title='Show Classe',form=form)



@classes.route('/classe/<int:classe_id>/delete', methods=['POST'])
@login_required
def delete_classe(classe_id):
    classe = Classe.query.get_or_404(classe_id)
    db.session.delete(classe)
    db.session.commit()
    flash('Your classe has been deleted !', 'success')
    return redirect(url_for('classes.new_classe'))

@classes.route('/search/name_classe/liste_eleve', methods=['GET', 'POST'])
@login_required
def search_name_classe():
    form = SearchNomClassSelectForm()
    if form.validate_on_submit():
        nom_classe=form.nom_classe.data
        classes = Classe.query.join(classe_eleves).\
                               join(Eleve).\
                               filter(
                                 (classe_eleves.c.classe_id == Classe.id)
                               & (classe_eleves.c.eleve_id == Eleve.id)
                                ).filter(Classe.nom_classe == nom_classe).all()
        if classes:
          return render_template('eleves/show_liste_evele_inscrit.html', nom_classe=nom_classe, classes=classes)
        else:
          flash('Oups ! Pas d\'eleve inscrit dans cette classe', 'danger')

    classes = Classe.query.all()
    return render_template('parametres/search_name_classe.html', form=form, title='Search Name Classe', classes=classes, legend='Search Name Classe')
