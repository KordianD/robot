from flask import Flask, render_template, request
import robot as robot

APP = Flask(__name__)


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
            robot.stop()
    else:
        robot.stop()
    return "nothing"


@APP.route("/")
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    APP.run(host='0.0.0.0', debug=True)
