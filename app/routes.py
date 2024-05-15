import json

from flask import request, jsonify, current_app
from .models import Paciente, Visita, db
from .utils import parse_xml


def parse_data(data):
    if request.content_type == 'application/xml':
        return parse_xml(data)
    return json.loads(data)


@current_app.route('/pacientes', methods=['POST'])
def add_paciente():
    try:
        data = parse_data(request.data)
        nome = data['nome']
        data_nascimento = data['data_nascimento']
        sexo = data['sexo']
        visitas = data['visitas']

        paciente = Paciente(nome=nome, data_nascimento=data_nascimento, sexo=sexo)
        db.session.add(paciente)
        db.session.commit()

        for visita in visitas:
            nova_visita = Visita(data_visita=visita, paciente_id=paciente.id)
            db.session.add(nova_visita)
        db.session.commit()

        response = jsonify({'message': 'Paciente e visitas cadastrados com sucesso!'})
        response.status_code = 201
        return response

    except Exception as e:
        current_app.logger.error(f"Erro ao processar a solicitação: {e}")
        response = jsonify({'error': 'Erro ao processar a solicitação'})
        response.status_code = 500
        return response
