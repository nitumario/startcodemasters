from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import _thread
from setup import Robot

zap1 = Robot(56,117.5)
zap1.d.settings(1000,1000,100,100)
def run01():
    zap1.bratDr.run_time(500, 700)
    zap1.d.straight(230)
    zap1.d.turn(-70)
    zap1.d.straight(20)
    zap1.d.turn(-50)
    zap1.bratDr.run_time(-150, 1300)
    zap1.d.turn(50)
    zap1.d.straight(-200)

    wait(4000)

    zap1.d.straight(160)
    zap1.d.turn(-40)

    zap1.d.straight(320)
    zap1.bratSt.run_angle(1000, 600)
    zap1.bratDr.run_time(500, 900)

    zap1.d.straight(-450)

    zap1.bratSt.stop()
    zap1.bratDr.stop()



def run02():
    zap1.senzorGiro.reset_angle
    zap1.d.straight(300)
    zap1.gyrogoto(360, 100)

def run03():
    pass

def run04():
    pass

def run05():
    pass

def run06():
    pass

def run07():
    pass

def run08():
    pass
