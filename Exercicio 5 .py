from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Inicializa o banco de dados
def init_db():
    conn = sqlite3.connect('barbearia.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS agendamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            email TEXT,
            cabeleireiro TEXT,
            tipo_corte TEXT,
            data TEXT,
            hora TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# Rota simples para teste
@app.route('/')
def home():
    return 'API de agendamento da barbearia ativa!'

# Rota para agendamento via JSON
@app.route('/agendar', methods=['POST'])
def agendar():
    data = request.get_json()

    campos_necessarios = ['nome', 'email', 'cabeleireiro', 'tipo_corte', 'data', 'hora']
    if not all(campo in data for campo in campos_necessarios):
        return jsonify({'erro': 'Dados incompletos.'}), 400

    try:
        conn = sqlite3.connect('barbearia.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO agendamentos (nome, email, cabeleireiro, tipo_corte, data, hora)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            data['nome'],
            data['email'],
            data['cabeleireiro'],
            data['tipo_corte'],
            data['data'],
            data['hora']
        ))
        conn.commit()
        conn.close()
        return jsonify({'mensagem': 'Agendamento realizado com sucesso.'}), 201

    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
