# Cabinet 3D Website

This project is a real-time web application for tracking and managing boxes on shelves, built with Flask and Flask-SocketIO.

## Features
- Visual representation of a cabinet with 6 shelves
- Real-time updates of box positions across all connected clients
- Move boxes between shelves or remove them entirely
- Clear all boxes from all shelves

## How It Works
- The backend maintains the state of each shelf and the boxes on it
- The frontend displays the shelves and boxes, updating instantly when changes occur
- Communication between frontend and backend is handled via WebSockets (Socket.IO)
- Runs with Gunicorn + Gevent

## Getting Started

### Prerequisites
- Python 3.7+
- pip

### Installation
1. Clone this repository:
   ```sh
   git clone <repo-url>
   cd Cabinet_3D_Website
   ```
2. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Linux/Mac
   ```
3. Install dependencies:
   ```sh
   pip install flask flask-socketio gunicorn gevent gevent-websocket
   ```

### Debugging the Application
1. Start the server:
   ```sh
   python app.py
   ```
2. Open your browser and go to `http://localhost:5000`

### Testing
- Run the test script to simulate box movements:
  ```sh
  python test.py
  ```

## Project Structure
```
app.py           # Main Flask application
static/          # Static files (images, CSS, etc.)
templates/       # HTML templates
  index.html     # Main UI
  ...
test.py          # Test client for simulating box events
```

## Start the webserver
``` bash
$ source .venv/bin/activate
$ gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 -b 0.0.0.0:5000 app:app  
orker -w 1 -b 0.0.0.0:5000 app:app
```

## 🔁 Optional: Auto-start on boot with systemd
Create a service:

```bash
Copy
sudo nano /etc/systemd/system/shelftracker.service
Paste this:

ini
Copy
[Unit]
Description=Cabinet Shelf Tracker
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/cabinet_shelf_tracker
ExecStart=/usr/local/bin/gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 app:app
Restart=always

[Install]
WantedBy=multi-user.target
```
Enable it:

```bash
Copy
sudo systemctl daemon-reexec
sudo systemctl enable shelftracker
sudo systemctl start shelftracker
```
