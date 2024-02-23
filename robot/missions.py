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
def run01(): #oameni si imprimanta baza dreapta
    #luat 2 oameni
    zap1.bratDr.run_time(500, 700)
    zap1.d.straight(230)
    zap1.d.turn(-70)
    zap1.d.straight(20)
    zap1.d.turn(-50)
    zap1.bratDr.run_time(-150, 1300)
    zap1.d.turn(50)
    zap1.d.straight(-200)


def run02():
    zap1.run_by_angle_thread(500, 360, zap1.bratSt, zap1.lock0)
    zap1.run_by_angle_thread(500,360,zap1.bratDr, zap1.lock1)
    wait(1000)
    zap1.thread_stop()
    EV3Brick().speaker.beep(100, 500)
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