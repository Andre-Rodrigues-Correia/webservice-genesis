import xml.etree.ElementTree as ET

def parse_xml(data):
    try:
        tree = ET.ElementTree(ET.fromstring(data))
        root = tree.getroot()
        nome = root.find('nome').text
        data_nascimento = root.find('data_nascimento').text
        sexo = root.find('sexo').text
        visitas = [visita.text for visita in root.findall('visitas/visita')]

        return {
            'nome': nome,
            'data_nascimento': data_nascimento,
            'sexo': sexo,
            'visitas': visitas
        }
    except ET.ParseError as e:
        raise ValueError(f"Erro ao processar o XML: {e}")
