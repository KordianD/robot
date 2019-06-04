import socket
import serial
from config import DEFAULT_VELOCITY
from config import TIME_INTERVAL
import time
import math
import os


class Robot:

    def __init__(self, mac: str, color: str, com: str):
        if os.name == 'posix':
            self.socket = socket.socket(
                socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            print("Input 1234 code in system bluetooth window")
            self.socket.connect((mac, 1))
        else:
            self.serial = serial.Serial(com)
        self.last_update = time.time()
        self.color = color
        self.user_time = time.time()
        self.user_age = 15
        self.user_id = 0

    def send_speed_command(self, left, right):
        cmd = '[={},{}]'.format(left, right)
        if os.name == 'posix':
            self.socket.send(bytes(cmd, 'UTF-8'))
        else:
            self.serial.write(bytes(cmd, 'UTF-8'))
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

    def age(self):
        return (time.time() - self.user_time)

    def velocity(self):
        if self.user_age < 10:
            return math.ceil(DEFAULT_VELOCITY/2)
        elif self.user_age > 20:
            return DEFAULT_VELOCITY
        else:
            return math.ceil(self.user_age / 20 * DEFAULT_VELOCITY)
