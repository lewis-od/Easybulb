from flask import Flask
from easybulb import Easybulb
import flask
import math
import socket
import sys

if len(sys.argv) != 2:
    raise Exception("Please provide the IP address of your Easybulb hub")
ip_addr = sys.argv[1] # IP address validation handled by Easybulb class

app = Flask(__name__)
lights = Easybulb(ip_addr)
print("Easybulb initialised with ip: {}".format(ip_addr))

@app.route('/on')
def on():
    lights.on()
    return flask.jsonify(result='ok')

@app.route('/off')
def off():
    lights.off()
    return flask.jsonify(result='ok')

@app.route('/white')
def white():
    lights.white()
    return flask.jsonify(result='ok')

@app.route('/colour/<int:col>')
def colour(col):
    if col < 0 or col > 255:
        return flask.jsonify(result='error',
            error='colour must be between 0 and 255')
    lights.colour(col)
    return flask.jsonify(result='ok')

@app.route('/brightness/<int:percent>')
def brightness(percent):
    if percent < 0 or percent > 100:
        return flask.jsonify(result='error',
            error='brightness must be between 0 and 100%')
    raw_brightness = math.floor((percent / 100.0) * 59.0)
    raw_brightness = int(raw_brightness)
    if raw_brightness <= 1:
        raw_brightness = 2
    lights.brightness(raw_brightness)
    return flask.jsonify(result='ok', brightness=percent, raw_brightness=raw_brightness)

if __name__ == '__main__':
    app.run(debug=True)
