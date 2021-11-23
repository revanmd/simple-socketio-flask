from flask import Flask
from flask_socketio import SocketIO
import random 
import time
from threading import Thread

app = Flask(__name__)
app.config['SECRET_KEY'] = 'RrEimeG}2A~9vWE'
socketio = SocketIO(app,cors_allowed_origins="*")

@socketio.on('connect')
def connecting():
    print('user_connected')

@socketio.on('disconnect')
def disconnecting():
    print('user_disconnected')

@app.route('/insert_data')
def handler_data():
	socketio.emit('broadcast_channel_a','dari channel a',broadcast=True)
	socketio.emit('broadcast_channel_b','dari channel b',broadcast=True)
	return "data berhasil ditambahkan"


if __name__ == '__main__':
	socketio.run(app)
