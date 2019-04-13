import socket
from config import DEFAULT_VELOCITY
from config import TIME_INTERVAL
import time


class Robot:

    def __init__(self, mac: str, color: str):
        self.socket = socket.socket(
            socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

        self.socket.connect((mac, 1))
        self.last_update = time.time()
        self.color = color
        self.new_user_time = time.time()
        self.user_age = 15
        self.user_id = 0

    def send_speed_command(self, left, right):
        cmd = '[={},{}]'.format(left, right)
        self.socket.send(bytes(cmd, 'UTF-8'))
        self.last_update = time.time()
        print(cmd)

    def forward(self):
        self.send_speed_command(self.velocity(), self.velocity())

    def reverse(self):
        self.send_speed_command(-self.velocity(), -self.velocity())

    def left(self):
        self.send_speed_command(0, math.ceil(self.velocity()/2))

    def right(self):
        self.send_speed_command(math.ceil(self.velocity()/2), 0)

    def stop(self):
        self.send_speed_command(0, 0)

    def is_time_exceeded(self):
        return (time.time() - self.last_update) > TIME_INTERVAL

    def robot_age(self):
        return (time.time() - self.new_user_time)

    def velocity(self):
        if user_age < 10:
            return math.ceil(DEFAULT_VELOCITY/2)
        elif user_age > 20:
            return DEFAULT_VELOCITY
        else
        return math.ceil(user_age / 20 * DEFAULT_VELOCITY)
