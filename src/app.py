from flask import Flask, render_template, request
from flask_cors import CORS
import robot as robot
import socket
import argparse

parser = argparse.ArgumentParser(description='Robot server.')
parser.add_argument('--port', '-p', type=int,
                    help='Port to run flask server', required=False, default=5000)
parser.add_argument('--mac', '-m', type=str,
                    help='Bluetooth mac address of robot', required=False, default="00:07:80:80:10:C9")
args = parser.parse_args()
APP = Flask(__name__)
CORS(APP)

robot = robot.Robot()
#robot.socket.connect((args.mac, 1))


@APP.route('/control_robot')
def control_robot():
    direction = request.args.get('direction', 0)
    mousedown = request.args.get('mousedown', 0)
    if mousedown == '1':
        print('button pressed:', direction)

        if direction == 'up':
            robot.forward()
        elif direction == 'left':
            robot.left()
        elif direction == 'right':
            robot.right()
        else:
            robot.reverse()
    else:
        robot.stop()
    return "nothing"


@APP.route("/test")
def test():
    return render_template('index_test.html')


@APP.route("/")
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=args.port)
