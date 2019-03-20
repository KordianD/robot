from flask import Flask, render_template, request

APP = Flask(__name__)


@APP.route('/control_robot')
def control_robot():
    dir = request.args.get('dir', 0)
    mousedown = request.args.get('mousedown', 0)
    print("direction is %, mouse up/down %", dir, mousedown)  # debug print
    return "nothing"


@APP.route("/")
def hello():
    return render_template('index.html')


if __name__ == "__main__":
    APP.run(host='0.0.0.0', debug=True)
