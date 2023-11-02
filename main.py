#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import utime
import time
import _thread

# Create variables
zap=EV3Brick()

viteza = 350 #viteza
vitneg = -viteza #viteza negativa
vitezafin = 400 #viteza final
acceleratie=200
vitmax=1000

zapdisplay = EV3Brick()
# definim motoarele si senzorii
st = Motor(Port.B)
dr = Motor(Port.C)
bratDr = Motor(Port.A)
bratSt = Motor(Port.D)
touch_sensor = TouchSensor(Port.S3)
#left_sensor = ColorSensor(Port.S1)
#right_sensor = ColorSensor(Port.S2)
#gyro = GyroSensor(Port.S3)

# cream drivebase-ul
zap1 = DriveBase(st, dr, 62, 135)
global coedf1
coefd1 = 1
zap1.settings(1000, 1000, 1000, 1000)


global varBrat
varBrat = 0
sem = _thread.allocate_lock()

#power point(6.16 sec)
def run01():
    zap1.straight(coefd1*-300)
    zap1.turn(-70)
    bratSt.run_time(800, 300)
    zap1.straight(coefd1*-400)

def brat01_thread():
    global varBrat
    while True:

        sem.acquire()
        if varBrat != 0:
            sem.release()
            bratDr.run_time(varBrat, 1000)
            varBrat = 0
        else:
            sem.release()
            time.sleep(0.1) 


def brat02_thread():
    global varBrat2
    while True:

        sem.acquire()
        if varBrat2 != 0:
            sem.release()
            bratSt.run_time(varBrat2, 500)
            varBrat2 = 0
        else:
            sem.release()
            time.sleep(0.1) 



_thread.start_new_thread(brat01_thread,())
_thread.start_new_thread(brat02_thread,())

sem.acquire()
varBrat = 1
varBrat2 = 1
sem.release()

x = 1
zapdisplay.screen.draw_text(80, 50, str(x), Color.BLACK, None)

# afisare run pe ecran
def update_screen(x):
    zapdisplay.screen.clear()
    zapdisplay.screen.draw_text(80, 50, str(x), Color.BLACK, None)

touch=0

# main
while True:
    # verificare apasare butoane
    if Button.UP in zapdisplay.buttons.pressed() and x < 8:
        x = x+1
        update_screen(x)
        wait(700)

    elif Button.DOWN in zapdisplay.buttons.pressed() and x > 1:
        x = x-1
        update_screen(x)
        wait(700)


    if int(x)==1 and touch_sensor.pressed() :
        touch = 1
        if touch_sensor.pressed() and touch==1:
            run01()
            touch = 0
    if int(x)==2 and touch_sensor.pressed():
        wait(200)
        touch = 1
        if touch_sensor.pressed() and touch==1:
            run02()
            touch = 0
    if int(x)==3 and touch_sensor.pressed():
        touch = 1
        if touch_sensor.pressed() and touch==1:
            run03()
            touch = 0   
    if int(x)==4 and touch_sensor.pressed():
        touch = 1
        if touch_sensor.pressed() and touch==1:
            run04()
            touch = 0
    if int(x)==5 and touch_sensor.pressed():
        touch = 1
        if touch_sensor.pressed() and touch==1:
            run05()
            touch = 0
    if int(x)==6 and touch_sensor.pressed():
        touch = 1
        if touch_sensor.pressed() and touch==1:
            run06()
            touch = 0
    if int(x)==7 and touch_sensor.pressed():
        touch = 1
        if touch_sensor.pressed() and touch==1:
            run07()
            touch = 0
    if int(x)==8 and touch_sensor.pressed():
        touch = 1
        if touch_sensor.pressed() and touch==1:
            run08()
            touch = 0