from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)

# Configurar o CORS
CORS(app)

#configurar especificamente para domínio
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})


# Configuração do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://schandon:admin123@localhost:5432/medilab-test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Definição do Modelo de Dados
class Pacientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    numAcesso = db.Column(db.String(20), nullable=True)
    visita = db.Column(db.String(50), nullable=True)
    patientID = db.Column(db.String(20), nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    modalidade = db.Column(db.String(2), nullable=False)
    tipoExame = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.String(20), nullable=False)
    estado = db.Column(db.String(1), nullable=False)
    medsol = db.Column(db.String(100), nullable=True)
    laudo = db.Column(db.String(1), nullable=True)
    sexo = db.Column(db.String(1), nullable=True)
    especial = db.Column(db.String(1), nullable=True)
    urgente = db.Column(db.String(1), nullable=True)
    restaurado = db.Column(db.String(1), nullable=False)

# Cria as tabelas no banco de dados
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET"])
def home():
    return "API Medilab Inicializada! (●'◡'●)"

# Rota para obter todos os pacientes
@app.route('/pacientes', methods=['GET'])
def obter_pacientes():
    pacientes = Pacientes.query.all()
    resultado = [
        {
            'id': p.id,
            'nome': p.nome,
            'numAcesso': p.numAcesso,
            'visita': p.visita,
            'patientID': p.patientID,
            'data': p.data.isoformat(),
            'modalidade': p.modalidade,
            'tipoExame': p.tipoExame,
            'numero': p.numero,
            'estado': p.estado,
            'medsol': p.medsol,
            'laudo': p.laudo,
            'sexo': p.sexo,
            'especial': p.especial,
            'urgente': p.urgente,
            'restaurado': p.restaurado,
        }
        for p in pacientes
    ]
    return jsonify(resultado)

# Rota para obter um paciente por ID
@app.route('/pacientes/<int:id>', methods=['GET'])
def obter_paciente_por_id(id):
    paciente = Pacientes.query.get(id)
    if paciente:
        resultado = {
            'id': paciente.id,
            'nome': paciente.nome,
            'numAcesso': paciente.numAcesso,
            'visita': paciente.visita,
            'patientID': paciente.patientID,
            'data': paciente.data.isoformat(),
            'modalidade': paciente.modalidade,
            'tipoExame': paciente.tipoExame,
            'numero': paciente.numero,
            'estado': paciente.estado,
            'medsol': paciente.medsol,
            'laudo': paciente.laudo,
            'sexo': paciente.sexo,
            'especial': paciente.especial,
            'urgente': paciente.urgente,
            'restaurado': paciente.restaurado,
        }
        return jsonify(resultado)
    else:
        return jsonify({'erro': 'paciente não encontrado'}), 404
    
#Criando um paciente    
@app.route('/paciente', methods=['POST'])
def criar_paciente():
    paciente_data = request.get_json()
    
    # # Verifica se todos os campos obrigatórios estão presentes
    # if not all(k in paciente_data for k in ('nome', 'patientID', 'modalidade', 'tipoExame', 'numero', 'estado', 'restaurado')):
    #     return jsonify({'erro': 'Campos obrigatórios ausentes'}), 400
    
    # Cria um novo paciente
    paciente = Pacientes(
        nome=paciente_data.get('nome'),
        numAcesso=paciente_data.get('numAcesso'),
        visita=paciente_data.get('visita'),
        patientID=paciente_data.get('patientID'),
        data=datetime.strptime(paciente_data.get('data'), '%Y-%m-%d') if paciente_data.get('data') else datetime.utcnow(),
        modalidade=paciente_data.get('modalidade'),
        tipoExame=paciente_data.get('tipoExame'),
        numero=paciente_data.get('numero'),
        estado=paciente_data.get('estado'),
        medsol=paciente_data.get('medsol'),
        laudo=paciente_data.get('laudo'),
        sexo=paciente_data.get('sexo'),
        especial=paciente_data.get('especial'),
        urgente=paciente_data.get('urgente'),
        restaurado=paciente_data.get('restaurado'),
    )
    
    # Adiciona e comita a nova entrada ao banco de dados
    db.session.add(paciente)
    db.session.commit()

    # Converte o objeto paciente para um dicionário e retorna
    paciente_dict = {
        'id': paciente.id,
        'nome': paciente.nome,
        'numAcesso': paciente.numAcesso,
        'visita': paciente.visita,
        'patientID': paciente.patientID,
        'data': paciente.data.isoformat(),
        'modalidade': paciente.modalidade,
        'tipoExame': paciente.tipoExame,
        'numero': paciente.numero,
        'estado': paciente.estado,
        'medsol': paciente.medsol,
        'laudo': paciente.laudo,
        'sexo': paciente.sexo,
        'especial': paciente.especial,
        'urgente': paciente.urgente,
        'restaurado': paciente.restaurado,
    }

    return jsonify(paciente_dict), 201



# Rota para criar um novo paciente
@app.route('/pacientes', methods=['POST'])
def criar_pacientes():
    novos_pacientes = request.get_json()
    pacientes_adicionados = []
    for paciente_data in novos_pacientes:
        paciente = Pacientes(
            nome=paciente_data.get('nome'),
            numAcesso=paciente_data.get('numAcesso'),
            visita=paciente_data.get('visita'),
            patientID=paciente_data.get('patientID'),
            data=datetime.strptime(paciente_data.get('data'), '%Y-%m-%d') if paciente_data.get('data') else datetime.utcnow(),
            modalidade=paciente_data.get('modalidade'),
            tipoExame=paciente_data.get('tipoExame'),
            numero=paciente_data.get('numero'),
            estado=paciente_data.get('estado'),
            medsol=paciente_data.get('medsol'),
            laudo=paciente_data.get('laudo'),
            sexo=paciente_data.get('sexo'),
            especial=paciente_data.get('especial'),
            urgente=paciente_data.get('urgente'),
            restaurado=paciente_data.get('restaurado'),
        )
        db.session.add(paciente)
        pacientes_adicionados.append(paciente_data)
    db.session.commit()
    return jsonify(pacientes_adicionados), 201

# Rota para atualizar um paciente existente
@app.route('/pacientes/<int:id>', methods=['PUT'])
def atualizar_paciente(id):
    paciente_atualizado = request.get_json()
    paciente = Pacientes.query.get(id)
    if paciente:
        paciente.nome = paciente_atualizado.get('nome', paciente.nome)
        paciente.numAcesso = paciente_atualizado.get('numAcesso', paciente.numAcesso)
        paciente.visita = paciente_atualizado.get('visita', paciente.visita)
        paciente.patientID = paciente_atualizado.get('patientID', paciente.patientID)
        paciente.data = datetime.strptime(paciente_atualizado.get('data'), '%Y-%m-%d') if paciente_atualizado.get('data') else paciente.data
        paciente.modalidade = paciente_atualizado.get('modalidade', paciente.modalidade)
        paciente.tipoExame = paciente_atualizado.get('tipoExame', paciente.tipoExame)
        paciente.numero = paciente_atualizado.get('numero', paciente.numero)
        paciente.estado = paciente_atualizado.get('estado', paciente.estado)
        paciente.medsol = paciente_atualizado.get('medsol', paciente.medsol)
        paciente.laudo = paciente_atualizado.get('laudo', paciente.laudo)
        paciente.sexo = paciente_atualizado.get('sexo', paciente.sexo)
        paciente.especial = paciente_atualizado.get('especial', paciente.especial)
        paciente.urgente = paciente_atualizado.get('urgente', paciente.urgente)
        paciente.restaurado = paciente_atualizado.get('restaurado', paciente.restaurado)

        db.session.commit()
        return jsonify({
            'id': paciente.id,
            'nome': paciente.nome,
            'numAcesso': paciente.numAcesso,
            'visita': paciente.visita,
            'patientID': paciente.patientID,
            'data': paciente.data.isoformat(),
            'modalidade': paciente.modalidade,
            'tipoExame': paciente.tipoExame,
            'numero': paciente.numero,
            'estado': paciente.estado,
            'medsol': paciente.medsol,
            'laudo': paciente.laudo,
            'sexo': paciente.sexo,
            'especial': paciente.especial,
            'urgente': paciente.urgente,
            'restaurado': paciente.restaurado,
        })
    else:
        return jsonify({'erro': 'paciente não encontrado'}), 404

# Rota para deletar um paciente
@app.route('/pacientes/<int:id>', methods=['DELETE'])
def deletar_paciente(id):
    paciente = Pacientes.query.get(id)
    if paciente:
        db.session.delete(paciente)
        db.session.commit()
        return '', 204
    else:
        return jsonify({'erro': 'paciente não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
