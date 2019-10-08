from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class EleveForm(FlaskForm):

  prenom_eleve = StringField('Prenom', validators=[DataRequired()])
  nom_eleve = StringField('Nom', validators=[DataRequired()])
  sexe = StringField('Sexe', validators=[DataRequired()])
  id_nom_classe = StringField('Nom Classe', validators=[DataRequired()])
  submit = SubmitField('Valider')



