def send_speed_command(left, right):
    cmd = '[={},{}]'.format(left, right)
    # TODO: send over serial bluetooth (rfcomm)
    print(cmd)
    #


def forward():
    send_speed_command(40, 40)


def left():
    send_speed_command(10, 30)


def right():
    send_speed_command(30, 10)


def stop():
    send_speed_command(0, 0)
