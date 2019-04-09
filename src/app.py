from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import robot as robot
import argparse
from threading import Timer
import time
from config import TIME_INTERVAL
from mac_addresses import MAC_ADDRESSES

global ts, robot

# TODO: wiele robotów, losowanie numerka, kolor robota, wywalić serwer jak coś nie działa

global ROBOTS
ROBOTS = []


def check_robot(interval):
    Timer(interval, check_robot, [interval]).start()
    global ts, robot
    print(time.time() - ts)

    for robot in ROBOTS:
        if robot.is_time_exceeded():
            robot.stop()

    if time.time() - ts > interval:
        robot.stop()


parser = argparse.ArgumentParser(description='Robot server')
parser.add_argument('--port', '-p', type=int,
                    help='Port to run flask server', required=False, default=5000)

args = parser.parse_args()

robot = robot.Robot(MAC_ADDRESSES[0][0], MAC_ADDRESSES[0][1])

ts = time.time()
check_robot(TIME_INTERVAL)

APP = Flask(__name__)
CORS(APP)


@APP.route('/control_robot')
@cross_origin()
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
    return jsonify(color=robot.color)


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=args.port)
