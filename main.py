from datetime import datetime

def getTime():
    now = datetime.now()
    return now.day, now.hour, now.minute, now.second


def timeInS(day, hour, minute, second, debug=False):
    speed = 5 if debug else 2 # to speed up the color change
    return speed * second + minute * 60 + hour * 60 * 60 + day * 24 * 60 * 60

def StoHex(seconds):
    seconds%=(16*16)**3
    # explanation of following line:
    # get rid of the 0x prefix using [2:]
    #.zfill(6) pads 0s to the front of the string until it is 6 characters long
    return hex(seconds)[2:].zfill(6)


def hexToRGB(hex):
    return int(hex[0:2], 16), int(hex[2:4], 16), int(hex[4:6], 16)

import matplotlib
import time

# for i in range(5):
#     # wait for 1 second
#     time.sleep(1)
#     print(hexToRGB(StoHex(timeInS(*getTime()))))

import matplotlib.pyplot as plt
import numpy as np
# plot color in matplotlib
for i in range(100):
    rgb = hexToRGB(StoHex(timeInS(*getTime(), debug=True)))
    col = np.array(rgb).reshape(1, 1, 3)
    plt.imshow(col)
    plt.title(f"{col} is time, i={i}")
    plt.show(block=False)
    plt.pause(1)
    plt.close()
