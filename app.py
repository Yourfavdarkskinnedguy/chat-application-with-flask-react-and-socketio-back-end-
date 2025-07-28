from flask import Flask, session
from flask_socketio import SocketIO, emit, join_room
from server import generate_prompt
import random

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
    #print(f'data in flask handle_message is {data}')
    
    emit('receive_message', data, to=data['groupname'])


@socketio.on('send_botmsg')
def handle_bot_msg(data):
    username= data.get('username')
    usermessage= data.get('usermessage')
    groupname= data.get('groupname')
    timeHHmm= data.get('timeHHmm')

    result= generate_prompt(username, usermessage)
    print(f'result message passed to generate prompt is {result}')
    if result is None:
        random_name=random.choice(['Selat', 'maddison', 'James', 'John', 'Michael scoffield', 'Sholademi Daniel', 'Ayomikun', 'Samuel', 'Esther', 'Sarah'])
        random_message= random. choice(['Hello Gents', 'Hi everyone', 'What is the smallest planet in our solar system? Mercury,'
                                        'What has to be broken before you can use it?', 'Which continent is known as the “Dark Continent”?',
                                        'I speak without a mouth and hear without ears. What am I?', 'Who wrote “Romeo and Juliet”?', 'What do you call fake spaghetti? An impasta.',
                                        'Why was the math book sad? It had too many problems.', 'Why did the bicycle fall over? Because it was two-tired.', 'Who painted the Mona Lisa?'])
        botmsg_tosend= {'username':random_name, 'groupname':groupname,
                    'usermessage': random_message, 'timeHHmm': timeHHmm}
        emit('receive_message', botmsg_tosend, to=groupname)
        #return name, message
    else:
        name=result['name']
        message=result['message']
        botmsg_tosend= {'username':name, 'groupname':groupname,
                        'usermessage': message, 'timeHHmm': timeHHmm}
        print(f'botmsg_tosend in handle botmsg is {botmsg_tosend}')
        emit('receive_message', botmsg_tosend, to=groupname)

@socketio.on('connect')
def handle_connect():
    print("Client connected!")






if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5001)

