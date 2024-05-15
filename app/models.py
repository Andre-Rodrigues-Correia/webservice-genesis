from . import db


class Paciente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    sexo = db.Column(db.String(10), nullable=False)
    visitas = db.relationship('Visita', backref='paciente', lazy=True)


class Visita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_visita = db.Column(db.String(10), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('paciente.id'), nullable=False)
