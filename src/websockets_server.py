from flask import Flask
from flask_uwsgi_websocket import GeventWebSocket

# Run:
# uwsgi --master --http :8080 --http-websockets --gevent 100 --wsgi websockets_server:app
# from src directory

# HTTP server
app = Flask(__name__)
websocket = GeventWebSocket(app)
connected = set()

@app.route('/')
def index():
    return "clients connected: {}".format(len(connected))

@websocket.route('/echo')
def echo(ws):
    connected.add(ws)
    try:
        while True:
            ws.send("")
    finally:
        connected.remove(ws)

if __name__ == '__main__':
    app.run(gevent=100)
