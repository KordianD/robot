import socket


class Robot:

    def __init__(self):
        self.socket = socket.socket(
            socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

    def send_speed_command(self, left, right):
        cmd = '[={},{}]'.format(left, right)
        print(cmd)

    def forward(self):
        self.send_speed_command(400, 400)

    def reverse(self):
        self.send_speed_command(-400, -400)

    def left(self):
        self.send_speed_command(0, 100)

    def right(self):
        self.send_speed_command(100, 0)

    def stop(self):
        self.send_speed_command(0, 0)
