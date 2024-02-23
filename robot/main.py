#!/usr/bin/env pybricks-micropython
#*IMPORTS***
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
from missions import run01, run02, run03, run04, run05, run06, run07, run08
from setup import Robot

ev3 = EV3Brick()
x = 1
ev3.screen.draw_text(80, 50, str(x), Color.BLACK, None) 
ev3.speaker.beep()
senzorApasare = TouchSensor(Port.S3)
runs = [run01, run02, run03, run04, run05, run06, run07, run08]

def update_screen(x):
    ev3.screen.clear()
    ev3.screen.draw_text(80, 50, str(x), Color.BLACK, None)

touch = 0
while True:
    if Button.UP in ev3.buttons.pressed():
        x += 1
        update_screen(x)
        wait(700)
    elif Button.DOWN in ev3.buttons.pressed():
        x -= 1
        update_screen(x)
        wait(700)
    elif senzorApasare.pressed():
        run = runs[x - 1]
        run()   