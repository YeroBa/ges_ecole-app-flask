from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError
from flaskges_ecole.models import Classe

class ClasseForm(FlaskForm):

  nom_classe = StringField('Nom Classe', validators=[DataRequired(), Length(min=4, max=15)])

  submit = SubmitField('Valider')

  def validate_nom_classe(self, nom_classe):

    classe = Classe.query.filter_by(nom_classe=nom_classe.data).first()

    if classe:
        raise ValidationError('That nom classe is taken. Pleaz choose a different one')

class SearchNomClassSelectForm(FlaskForm):

  nom_classe = StringField('Nom Classe', validators=[DataRequired()])

  submit = SubmitField('Send Search')

class UpdateClasseForm(FlaskForm):

  nom_classe = StringField('nom_classe', validators=[DataRequired()])

  submit = SubmitField('Update')


