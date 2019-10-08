from datetime import datetime
from itsdangerous import JSONWebSignatureSerializer as Serializer
from flaskges_ecole import db, login_manager, app
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
  password = db.Column(db.String(60), nullable=False)
  eleves = db.relationship('Eleve', backref='user', lazy=True)

  def get_reset_token(self):
    s = Serializer(app.config['SECRET_KEY'])
    return s.dumps({'user_id': self.id}).decode('utf-8')

  @staticmethod
  def verify_reset_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
      user_id = s.loads(token)['user_id']
    except:
      return None

    return User.query.get(user_id)

  def __repr__(self):
   return f"User('{self.username}', '{self.email}', '{self.image_file}')"

classe_eleves = db.Table('classe_eleves',
    db.Column('classe_id', db.Integer, db.ForeignKey('classe.id'), primary_key=True),
    db.Column('eleve_id', db.Integer, db.ForeignKey('eleve.id'), primary_key=True),
    db.Column('date_inscrit', db.DateTime, nullable=False, default=datetime.utcnow)

)

class Classe(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nom_classe = db.Column(db.String(50), unique=True, nullable=False)
  eleves = db.relationship('Eleve', secondary=classe_eleves, back_populates='classes', cascade="all", lazy='dynamic')

  def __repr__(self):
    return f"Classe('{self.nom_classe}')"

class Eleve(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  prenom_eleve = db.Column(db.String(255), nullable=False)
  nom_eleve = db.Column(db.String(100), nullable=False)
  sexe = db.Column(db.String(50), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  classes = db.relationship('Classe', secondary=classe_eleves, back_populates='eleves',  lazy='joined')

  def __repr__(self):
    return f"Eleve('{self.prenom_eleve}', '{self.nom_eleve}', '{self.sexe}')"




