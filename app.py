from flask import Flask
from flask_socketio import SocketIO
from appp.views.chat import configure_chat_routes, configure_chat_socket

app = Flask(__name__, template_folder='appp/templates', static_folder='appp/static')
app.config['SECRET_KEY'] = 'laysa'
socketio = SocketIO(app)

configure_chat_routes(app)
configure_chat_socket(socketio)

if __name__ == '__main__':
    socketio.run(app, debug=True)