#!/usr/bin/env pybricks-micropython
#TODO: terminati run-ul unu, facet-il sa mearga perfect
#TODO: apucativa de run-ul 2
#**************************IMPORTS**************************
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

#**************************ROBOTUL**************************
#!bratDr (+) ridicare
#!bratSt (-) lasa in jos

#definim caramida si display-ul
zap=EV3Brick()
zapdisplay = EV3Brick()

#definim motoarele si senzorii
st = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
dr = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
bratSt = Motor(Port.A)
bratDr = Motor(Port.D)
#senzorCuloareDr = ColorSensor(Port.S1)
senzorCuloareSt = ColorSensor(Port.S2)
senzorApasare = TouchSensor(Port.S3)
senzorGyro = GyroSensor(Port.S4)
senzorUltra = UltrasonicSensor(Port.S1)

#**************************OBIECTELE**************************

#DRIVE BASE-UL SI SETARILE OBIECTELOR
zap1 = DriveBase(st, dr, 50, 105)
zap2 = DriveBase(st, dr, 50, 105)
zap3 = DriveBase(st, dr, 50, 105)
zap4 = DriveBase(st, dr, 50, 105)
zap5 = DriveBase(st, dr, 50, 105)
zap6 = DriveBase(st, dr, 50, 105)
zap7 = DriveBase(st, dr, 50, 105)
zap8 = DriveBase(st, dr, 50, 105)

zap1.settings(800, 500, 300, 300)
zap2.settings(1000, 1000, 300, 300)
zap3.settings(800, 500, 300, 300)
zap4.settings(800, 500, 300, 300)
zap5.settings(800, 500, 300, 300)
zap6.settings(800, 500, 300, 300)
zap7.settings(800, 500, 300, 300)
zap8.settings(800, 500, 300, 300)



st.stop()
dr.stop()

#CREEM COEFICIENTELE DE EROARE
#!Daca nu sti pentru ce sunt coefincientele intraba-l pe Vlad

global coefd1
global coeft1
global coefd2
global coeft2
global coefd3
global coeft3
global coefd4
global coeft4
global coefd5
global coeft5
global coefd6
global coeft6
global coefd7
global coeft7
global coefd8
global coeft8

coefd1 = 1
coeft1 = 1
coefd2 = 1
coeft2 = 1
coefd3 = 1
coeft3 = 1
coefd4 = 1
coeft4 = 1
coefd5 = 1
coeft5 = 1
coefd6 = 1
coeft6 = 1
coefd7 = 1
coeft7 = 1
coefd8 = 1
coeft8 = 1

#**************************THREAD SENZORI**************************
#definim STOPWATCH
x = 1
watch = StopWatch()
data = DataLog('run', 'time', 'angle', 'distance')

def sensor_thread():
    while True:
    #citeste datele de la gyro
        angle = senzorGyro.angle()
        time = watch.time()
        run = x
        distance = senzorUltra.distance()
        data.log(run, time/1000, angle, distance/10)
        wait(100)





#**************************THREAD BRATE**************************
varBrat1 = 0
varBrat2 = 0

def brat01_thread():
    global varBrat1
    while True:

        sem.acquire()
        if varBrat1 != 0:
            sem.release()
            bratDr.run_time(varBrat1, 1000)
            varBrat1 = 0
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

#PROGRAMUL PRINCIPAL PENTRU THREAD-URI
sem = _thread.allocate_lock()
_thread.start_new_thread(brat01_thread,())
_thread.start_new_thread(brat02_thread,())

sem.acquire()
varBrat1 = 0
varBrat2 = 0
sem.release()

#**************************RUNS**************************
def run01():
    zap1.straight(coefd1*40)
    bratDr.run_time(500,180)
    zap1.turn(coeft1*-50)
    zap1.straight(coefd1*190)
    zap1.turn(coeft1*-60)
    zap1.straight(coefd1*80)
    #se ridica primul om
    bratDr.run_time(400,500)
    zap1.straight(coefd1*-20)
    zap1.turn(coeft1*76)
    zap1.straight(coefd1*-100)
    bratDr.run_time(-400,500)
    zap1.straight(coefd1*180)
    #se ridica al doilea om
    bratDr.run_time(200,1000)
    zap1.turn(coeft1*10)
    zap1.straight(coefd1*50)
    zap1.turn(coeft1*-10)
    zap1.straight(coefd1*180)
    zap1.straight(coefd1*-6)
    #actionam motorul pentru cocos
    bratSt.run_time(-1000,2000)
    zap1.straight(coefd1*-400)

    bratDr.stop()
    bratSt.stop()

def run02():
    zap2.straight(-400)
    time.sleep(0.2)
    zap2.straight(400)


def run03():
    zap3.straight(coefd1*500)
    zap3.turn(coeft1*37)
    zap3.straight(coefd1*240) 
    zap3.turn(coeft1*-55)
    zap3.straight(coefd1*100)

    bratDr.stop()
    bratSt.stop()

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

#**************************URMARIRE LINIE**************************

def urmarireLinie1(degrees):
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


#**************************DISPLAY**************************
#FUNCTIA DE AFISARE
zapdisplay.screen.draw_text(80, 50, str(x), Color.BLACK, None) 
zap.speaker.beep() 

def update_screen(x):
    zapdisplay.screen.clear()
    zapdisplay.screen.draw_text(80, 50, str(x), Color.BLACK, None)

touch=0

#**************************DISPLAY**************************

while True:
    #verificare apasare butoane
    if Button.UP in zapdisplay.buttons.pressed() and x < 8:
        x = x+1
        update_screen(x)
        wait(700)

    elif Button.DOWN in zapdisplay.buttons.pressed() and x > 1:
        x = x-1
        update_screen(x)
        wait(700)

    if int(x)==1 and senzorApasare.pressed() :
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run01()
            touch = 0
            _thread.start_new_thread(sensor_thread())
    if int(x)==2 and senzorApasare.pressed():
        wait(200)
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run02()
            touch = 0
            _thread.start_new_thread(sensor_thread())
    if int(x)==3 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run03()
            touch = 0
            _thread.start_new_thread(sensor_thread())
    if int(x)==4 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run04()
            touch = 0
            _thread.start_new_thread(sensor_thread())
    if int(x)==5 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run05(5000)
            touch = 0
            _thread.start_new_thread(sensor_thread())
    if int(x)==6 and senzorApasare.pressed():
        touch = 1   
        if senzorApasare.pressed() and touch==1:
            run06()
            touch = 0
            _thread.start_new_thread(sensor_thread())
    if int(x)==7 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run07()
            touch = 0
            _thread.start_new_thread(sensor_thread())
    if int(x)==8 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run08()
            touch = 0
            _thread.start_new_thread(sensor_thread())

dr.stop()
st.stop()
