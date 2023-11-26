#!/usr/bin/env pybricks-micropython

#! Nu modificati importurile ca ne ducem dracu sau sa modificati orice alt ceva infara de runuri
#! version: 0.3
#***************************IMPORTS***************************
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

#***************************VALUES***************************

# Create variables
zap=EV3Brick()

viteza = 350 #viteza
vitneg = -viteza #viteza negativa
vitezafin = 400 #viteza final
acceleratie=200
vitmax=1000
zapdisplay = EV3Brick()

# definim motoarele si senzorii
st = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
dr = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
bratSt = Motor(Port.A)
bratDr = Motor(Port.D)
touch_sensor = TouchSensor(Port.S3)
left_sensor = ColorSensor(Port.S2)
right_sensor = ColorSensor(Port.S1)
#gyro = GyroSensor(Port.S3)

# cream drivebase-ul
zap1 = DriveBase(st, dr, 50, 105)
global coefd1
global coeft1
coefd1 = 1
coeft1 = 1
zap1.settings(800, 500, 300, 300)
st.stop()
dr.stop()
global varBrat
varBrat = 0
sem = _thread.allocate_lock()
zap.speaker.beep() 

#***************************THREAD BRATE***************************

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
            bratSt.run_time(varBrat2, 1000)
            varBrat2 = 0
        else:
            sem.release()
            time.sleep(0.1) 



_thread.start_new_thread(brat01_thread,())
_thread.start_new_thread(brat02_thread,())

sem.acquire()
varBrat2 = 0
varBrat = 0
sem.release()

#***************************RUNS***************************
def run01():
    bratDr.run_time(500,180)
    zap1.straight(coefd1*40)
    zap1.turn(coeft1*-50)
    zap1.straight(coefd1*190)
    
    zap1.turn(coeft1*-60)
    zap1.straight(coefd1*60)
    bratDr.run_time(700,500)
    zap1.turn(coeft1*72)
    zap1.straight(coefd1*-60)
    #zap1.straight(coefd1*120)
    #bratDr.run_time(450, 600)
    #zap1.straight(coefd1*60)
    #zap1.turn(coeft1*-10)
    #zap1.straight(coefd1*70)

    #bratSt.run_time(-1000, 6000)


    #zap1.straight(coefd1*200)
    #zap1.turn(coeft1*-23)
    #zap1.straight(coefd1*40)
    #zap1.turn(coeft1*30)
    #zap1.straight(coefd1*50)
    #zap1.turn(coeft1*-7)
    #bratDr.run_time(450, 550)
    #zap1.straight(coefd1*200)

    bratDr.stop()
    bratSt.stop()

def run02():
    zap1.straight(coefd1*500)
    zap1.turn(coeft1*37)
    zap1.straight(coefd1*240) 
    zap1.turn(coeft1*-55)
    zap1.straight(coefd1*100)


    bratDr.stop()
    bratSt.stop()
    
def run03():
    zap1.straight(-400)
    time.sleep(0.2)
    zap1.straight(400)


def run05(degrees):
    st.reset_angle(0)
    while st.angle() < degrees:
        zap1.straight(coefd1*50)
        time.sleep(0.1)
        zapdisplay.screen.clear()
        zapdisplay.screen.draw_text(80, 50, str(st.angle()), Color.BLACK, None)
        if left_sensor.color() == Color.WHITE:
            zap1.turn(10)
        if left_sensor.color() == Color.BLACK:
            zap1.turn(-10)


#bratDr (-) ridicare
#bratSt (+) ridicare

def run06():
    #ridica bratele
    bratDr.run_time(-400, 550)
    bratSt.run_time(400, 550)
    #merge cu spatele pana in fata sinei
    zap1.straight(coefd1*470)
    #coboara ambele brate
    bratDr.run_time(450, 570)
    bratSt.run_time(-400, 550)
    #merge in fata cu directia spre baza
    zap1.straight(coefd1*-110)
    #urca brat stanga
    bratSt.run_time(400, 550)
    #se intoarce 45 de grade
    zap1.turn(coeft1*-45)
    #o ia cu fata cu directia spre baza
    zap1.straight(coefd1*-100)
    #se intoarce pe directia 0
    zap1.turn(coeft1*-45)
    #megre inainte ca sa lase camera in locul ei
    zap1.straight(coefd1*150)
    #ridica bratul
    bratDr.run_time(-400 ,550)
    #merge in baza
    zap1.straight(coefd1*400)
    bratDr.stop()
    bratSt.stop()


#***************************Display***************************

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
            run05(5000)
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
dr.stop()
st.stop()
