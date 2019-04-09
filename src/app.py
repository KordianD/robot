from flask import Flask, render_template, request
from flask_cors import CORS
import robot as robot
import argparse
from threading import Timer
import time
from src.config import TIME_INTERVAL

global ts, robot


# TODO: wiele robotów, losowanie numerka, kolor robota, wywalić serwer jak coś nie działa


def check_robot(interval):
    Timer(interval, check_robot, [interval]).start()
    global ts, robot
    print(time.time() - ts)

    if time.time() - ts > interval:
        robot.stop()


parser = argparse.ArgumentParser(description='Robot server.')
parser.add_argument('--port', '-p', type=int,
                    help='Port to run flask server', required=False, default=5000)
parser.add_argument('--mac', '-m', type=str,
                    help='Bluetooth mac address of robot', required=False, default="00:07:80:80:10:C9")

args = parser.parse_args()
robot = robot.Robot()
robot.socket.connect((args.mac, 1))
ts = time.time()
check_robot(TIME_INTERVAL)

APP = Flask(__name__)
CORS(APP)


@APP.route('/control_robot')
def control_robot():
    global ts
    ts = time.time()
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
def index():
    return render_template('index.html')


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=args.port)
