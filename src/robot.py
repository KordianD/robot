import socket
from src.config import DEFAULT_VELOCITY


class Robot:

    def __init__(self):
        self.socket = socket.socket(
            socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    def send_speed_command(self, left, right):
        cmd = '[={},{}]'.format(left, right)
        self.socket.send(bytes(cmd, 'UTF-8'))
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
