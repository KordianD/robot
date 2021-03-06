from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import robot as robot
import argparse
from threading import Timer
import time
from config import TIME_INTERVAL
from mac_addresses import MAC_ADDRESSES

global ts, robot

global ROBOTS
ROBOTS = []


def check_robot(interval):
    Timer(interval, check_robot, [interval]).start()
    global ts, ROBOTS
    # print(time.time() - ts)

    for robot in ROBOTS:
        if robot.is_time_exceeded():
            robot.stop()


parser = argparse.ArgumentParser(description='Robot server')
parser.add_argument('--port', '-p', type=int,
                    help='Port to run flask server', required=False, default=5000)

args = parser.parse_args()

for i, (mac, color, com) in enumerate(MAC_ADDRESSES):
    try:
        ROBOTS.append(robot.Robot(mac, color, com))
    except:
        print(f"WARNING: Couldn't add {color} robot")

ts = time.time()
check_robot(TIME_INTERVAL)
old_id = 0

APP = Flask(__name__)
CORS(APP)


@APP.route('/control_robot')
def control_robot():
    global ts, old_id
    ts = time.time()
    direction = request.args.get('direction', 0)
    mousedown = request.args.get('mousedown', 0)
    user_age = int(request.args.get('user_age', 0))
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
    oldest_robot = max(ROBOTS, key=lambda x: x.age())
    old_id = oldest_robot.user_id
    oldest_robot.user_id = user_id
    oldest_robot.user_age = user_age
    oldest_robot.user_time = time.time()
    print("new user: {}, {}, assigned {}".format(
        user_id, user_age, robot.color))
    return jsonify(color=robot.color, endgame=0)


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=args.port)
