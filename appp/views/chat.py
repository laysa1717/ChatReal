from flask import render_template 
from flask_socketio import emit, Namespace
from appp.models.chat import Message, ChatRoom

chat_room = ChatRoom()

class ChatNamespace(Namespace):
    def on_connect(self):
        emit('message', {'message': 'Bem-vindo ao chat em tempo real!'})
    
    def on_send_message(self, data):
        message = Message('Usuário', data['message'])
        chat_room.add_message(message)
        emit('message', {'message': f'Usuário: {data["message"]}'}, broadcast=True)

def configure_chat_socket(socketio):
    socketio.on_namespace(ChatNamespace('/chat'))

def configure_chat_routes(app):
    @app.route('/')
    def index():
        messages = chat_room.get_messages()
        return render_template('chat.html', messages=messages)