import socketio
import time

sio = socketio.Client()
sio.connect('http://localhost:5000')

# Move box 101 to shelf 3
sio.emit('box_update', {'box_id': '13102', 'shelf': 3})

time.sleep(3)

# Move box 101 to shelf 5
sio.emit('box_update', {'box_id': '1012', 'shelf': 5})

time.sleep(3)

# Remove box 101
sio.emit('box_update', {'box_id': '101', 'shelf': 1})
