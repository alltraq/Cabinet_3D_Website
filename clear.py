import socketio
import time

DELAY = 1

sio = socketio.Client()
# sio.connect('http://localhost:5000')
sio.connect('http://10.10.55.74:5000')

print("Connected to server")

sio.emit('clear_boxes', {})
time.sleep(DELAY)
