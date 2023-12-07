from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Exemplo de dados (substitua isso por seu mecanismo de armazenamento real)
agendamentos = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', agendamentos=agendamentos)

@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    if request.method == 'POST':
        # Lógica para agendar horário
        data = request.form['data']
        horario = request.form['horario']
        novo_agendamento = {'data': data, 'horario': horario}
        agendamentos.append(novo_agendamento)
        return jsonify({'message': 'Horário agendado com sucesso!'})

    return render_template('agendar.html')

@app.route('/agendamentos/<int:agendamento_id>', methods=['DELETE', 'PUT'])
def gerenciar_agendamento(agendamento_id):
    if request.method == 'DELETE':
        if 0 <= agendamento_id < len(agendamentos):
            del agendamentos[agendamento_id]
            return jsonify({'message': 'Agendamento excluído com sucesso!'})
        else:
            return jsonify({'error': 'ID de agendamento inválido'}), 404

    elif request.method == 'PUT':
        # Lógica para atualizar agendamento
        if 0 <= agendamento_id < len(agendamentos):
            data = request.form['data']
            horario = request.form['horario']
            agendamentos[agendamento_id]['data'] = data
            agendamentos[agendamento_id]['horario'] = horario
            return jsonify({'message': 'Agendamento atualizado com sucesso!'})
        else:
            return jsonify({'error': 'ID de agendamento inválido'}), 404

if __name__ == '__main__':
    app.run(debug=True)