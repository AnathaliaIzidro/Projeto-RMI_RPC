from flask import Flask, request, jsonify
import Pyro4

app = Flask(__name__)

# Conecte-se ao servidor Pyro4
server = Pyro4.Proxy("PYRO:resta_um_server@localhost:9090")

@app.route('/move-piece', methods=['POST'])
def move_piece():
    from_row = request.json['from_row']
    from_col = request.json['from_col']
    to_row = request.json['to_row']
    to_col = request.json['to_col']
    server.move_piece(from_row, from_col, to_row, to_col)
    return jsonify({'message': 'Peça movida com sucesso!'})

@app.route('/get-game-state', methods=['GET'])
def get_game_state():
    game_state = server.get_game_state()
    return jsonify({'game_state': game_state})

@app.route('/send-message', methods=['POST'])
def send_message():
    message = request.json['message']
    player = request.json['player']
    server.send_message(message, player)
    return jsonify({'message': 'Mensagem enviada com sucesso!'})

@app.route('/get-messages', methods=['GET'])
def get_messages():
    messages = server.get_messages()
    return jsonify({'messages': messages})

if __name__ == '__main__':
    app.run(debug=True)