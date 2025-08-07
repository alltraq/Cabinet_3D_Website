from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Shelf state: shelf number (1-6) -> list of box IDs
shelf_state = {i: [] for i in range(1, 7)}

@app.route('/')
def index():
    return render_template('index.html', shelves=shelf_state)

@socketio.on('box_update')
def handle_box_update(data):
    box_id = data['box_id']
    shelf = data['shelf']  # 1 to 6, or 0 if removed completely

    # Remove the box from all shelves
    for shelf_boxes in shelf_state.values():
        if box_id in shelf_boxes:
            shelf_boxes.remove(box_id)

    # If shelf > 0, add box to that shelf
    if 1 <= shelf <= 6:
        shelf_state[shelf].append(box_id)

    emit('update_shelves', shelf_state, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
