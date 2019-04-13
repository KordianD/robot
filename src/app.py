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
    global ts, ROBOTS
    print(time.time() - ts)

    for robot in ROBOTS:
        if robot.is_time_exceeded():
            robot.stop()


parser = argparse.ArgumentParser(description='Robot server')
parser.add_argument('--port', '-p', type=int,
                    help='Port to run flask server', required=False, default=5000)

args = parser.parse_args()

for i, (mac, color) in enumerate(MAC_ADDRESSES):
    ROBOTS.append(robot.Robot(mac, color))

ts = time.time()
check_robot(TIME_INTERVAL)
old_id = 0

APP = Flask(__name__)
CORS(APP)


@APP.route('/control_robot')
@cross_origin()
def control_robot():
    global ts
    ts = time.time()
    direction = request.args.get('direction', 0)
    mousedown = request.args.get('mousedown', 0)
    user_age = request.args.get('user_age', 0)
    user_id = request.args.get('user_id', 0)
    for robot in ROBOTS:
        if user_id == robot.user_id:
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
            return jsonify(color=robot.color, endgame=0)
        elif user_id == old_id:
            return jsonify(color=robot.color, endgame=1)
    # if above didn't return, new user:
    oldest_robot = min(ROBOTS, key=lambda x: x.age())
    old_id = oldest_robot.user_id
    oldest_robot.user_id = user_id
    return jsonify(color=robot.color, endgame=0)


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=args.port)
