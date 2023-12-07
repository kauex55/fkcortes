from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    if request.method == 'POST':
        # Lógica para agendar horário
        data = request.form['data']
        horario = request.form['horario']
        # ... processamento do agendamento ...
        return jsonify({'message': 'Horário agendado com sucesso!'})

    return render_template('agendar.html')

if __name__ == '__main__':
    app.run(debug=True)
