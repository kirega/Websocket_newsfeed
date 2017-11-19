from flask import Flask,render_template
from flask_socketio import SocketIO, send
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret' #For encyption
socketio = SocketIO(app)




@socketio.on('message')   #listen to a particular event i.e message event.
def WorkMessage(msg):   #function gets called when theres a message
	print('Post:'+ msg)
	send(msg, broadcast= True) #sends messages to everyone connected on server in realtime
@app.route('/')
def index():
	return render_template('index.html')





if __name__ == '__main__':
	socketio.run(app)