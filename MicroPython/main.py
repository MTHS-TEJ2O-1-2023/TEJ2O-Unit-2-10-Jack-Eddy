"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *
import neopixel

# cleanup
np = neopixel.NeoPixel(pin16, 4)
np[0] = (0, 0, 0)
np[1] = (0, 0, 0)
np[2] = (0, 0, 0)
np[3] = (0, 0, 0)
np.show()

while True:
    # light level is <= 51
    if input.light_level() <= 51:
        np[0] = (0, 0, 0)
        np[1] = (0, 0, 0)
        np[2] = (0, 0, 0)
        np[3] = (0, 0, 0)
        np.show()
    # light level is > 52
    if input.light_level() > 52:
        np[0] = (0, 255, 0)
        np[1] = (0, 0, 0)
        np[2] = (0, 0, 0)
        np[3] = (0, 0, 0)
        np.show()
    # light level is > 104
    if input.light_level() > 104:
        np[0] = (0, 255, 0)
        np[1] = (0, 255, 0)
        np[2] = (0, 0, 0)
        np[3] = (0, 0, 0)
        np.show()
    # light level is > 156
    if input.light_level() > 156:
        np[0] = (0, 255, 0)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 0, 0)
        np.show()
    # light level is > 208
    if input.light_level() > 208:
        np[0] = (0, 255, 0)
        np[1] = (0, 255, 0)
        np[2] = (0, 255, 0)
        np[3] = (0, 255, 0)
        np.show()
