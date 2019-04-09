import socket
from src.config import DEFAULT_VELOCITY
from src.config import TIME_INTERVAL
import time


class Robot:

    def __init__(self, mac: str):
        self.socket = socket.socket(
            socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

        self.socket.connect((mac, 1))
        self.last_update = time.time()

    def send_speed_command(self, left, right):
        cmd = '[={},{}]'.format(left, right)
        self.socket.send(bytes(cmd, 'UTF-8'))
        self.last_update = time.time()
        print(cmd)

    def forward(self):
        self.send_speed_command(DEFAULT_VELOCITY, DEFAULT_VELOCITY)

    def reverse(self):
        self.send_speed_command(-DEFAULT_VELOCITY, -DEFAULT_VELOCITY)

    def left(self):
        self.send_speed_command(0, DEFAULT_VELOCITY)

    def right(self):
        self.send_speed_command(DEFAULT_VELOCITY, 0)

    def stop(self):
        self.send_speed_command(0, 0)

    def is_time_exceeded(self):
        return (time.time() - self.last_update) > TIME_INTERVAL
