from flask import Flask
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['groupname']
    join_room(room)
    print(f"{username} has joined {room}.")
    emit('receive_message', {
        'usermessage': f"{username} has joined the chat.",
        'username': username,
        'groupname': room,
    }, to=room)

@socketio.on('send_message')
def handle_message(data):
    print(f'data in flask handle_message is {data}')
    print(f'data flask handle_message is sending to is {data['groupname']}')
    emit('receive_message', data, to=data['groupname'])



@socketio.on('connect')
def handle_connect():
    print("Client connected!")


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5001)

