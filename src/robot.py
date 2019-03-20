def sendSpeedCommand(left, right):
    cmd = '[={},{}]'.format(left, right)
    # TODO: send over serial bluetooth (rfcomm)
    print(cmd)
    #
    return


def forward():
    sendSpeedCommand(40, 40)
    return


def left():
    sendSpeedCommand(10, 30)
    return


def right():
    sendSpeedCommand(30, 10)
    return


def stop():
    sendSpeedCommand(0, 0)
    return
