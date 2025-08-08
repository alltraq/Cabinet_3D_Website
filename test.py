import socketio
import time

DELAY = 1

sio = socketio.Client()
sio.connect('http://localhost:5000')

print("Connected to server")

sio.emit('clear_boxes', {})

time.sleep(DELAY)

# Move box 101 to shelf 3
sio.emit('box_update', {'box_id': '13102', 'shelf': 3})

time.sleep(DELAY)

# Move box 101 to shelf 5
sio.emit('box_update', {'box_id': '101', 'shelf': 5})

time.sleep(DELAY)

# Remove box 101
sio.emit('box_update', {'box_id': '101', 'shelf': 6})

time.sleep(DELAY)

# Remove box 101
sio.emit('box_update', {'box_id': '101', 'shelf': 0})

time.sleep(DELAY)

# Remove box 101
sio.emit('box_update', {'box_id': '13102', 'shelf': 0})

time.sleep(DELAY)

for i in range(1, 7):
    sio.emit('box_update', {'box_id': '13102', 'shelf': i})
    time.sleep(DELAY)

