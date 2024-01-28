#!/usr/bin/env pybricks-micropython
#*********IMPORTS*********
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

#*********ROBOTUL*********
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
senzorCuloareDr = ColorSensor(Port.S1)
senzorCuloareSt = ColorSensor(Port.S2)
senzorApasare = TouchSensor(Port.S3)
senzorGiro = GyroSensor(Port.S4)

#*********OBIECTELE*********

#DRIVE BASE-UL SI SETARILE OBIECTELOR
zap1 = DriveBase(st, dr, 49.5, 103)
zap2 = DriveBase(st, dr, 49.5, 103)
zap3 = DriveBase(st, dr, 49.5, 103)
zap4 = DriveBase(st, dr, 49.5, 103)
zap5 = DriveBase(st, dr, 49.5, 103)
zap6 = DriveBase(st, dr, 49.5, 103)
zap7 = DriveBase(st, dr, 49.5, 103)
zap8 = DriveBase(st, dr, 49.5, 103)
zap9 = DriveBase(st, dr, 49.5, 103)
zap10 = DriveBase(st, dr, 49.5, 103)
zap11 = DriveBase(st, dr, 49.5, 103)
zap12 = DriveBase(st, dr, 49.5, 103)

zap1.settings(800, 800, 300, 300)
zap2.settings(1000, 500, 300, 300)
zap3.settings(800, 1000, 800, 800)
zap4.settings(800, 500, 300, 300)
zap5.settings(800, 500, 300, 300)
zap6.settings(800, 500, 300, 150)
zap7.settings(1000, 500, 800, 800)
zap8.settings(800, 500, 200, 200)
zap9.settings(1000, 1000, 800, 800)
zap10.settings(800, 500, 300, 300)
zap11.settings(1000, 500, 800, 800)
zap12.settings(800, 500, 200, 200)

st.stop()
dr.stop()

#*********COEFICIENTE DE EROARE*********

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
global coefd9
global coeft9
global coefd10
global coeft10
global coefd11
global coeft11
global coefd12
global coeft12

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
coefd9 = 1
coeft9 = 1
coefd10 = 1
coeft10 = 1
coefd11 = 1
coeft11 = 1
coefd12 = 1
coeft12 = 1

#*********THREAD-URI*********

global angles_zap1
global bratSt_speed
global bratSt_angles
global bratDr_speed
global bratDr_angles
global extra


# Create a shared lock
global_lock = _thread.allocate_lock()
zap1_lock = _thread.allocate_lock()
bratDr_lock = _thread.allocate_lock()
def thread_zap1(angles_zap1):
    with global_lock:
        zap1.straight(coefd1 * angles_zap1)

def thread_bratSt(bratSt_speed, bratSt_angles, extra):
    with global_lock:
        bratSt.run_angle(bratSt_speed, bratSt_angles, extra)

def thread_bratDr(bratDr_speed, bratDr_angles):
    with global_lock:
        bratDr.run_time(bratDr_speed, bratDr_angles)


    
#*********URMARIRE LINIE*********

def urmarireLinie1(degrees):
    while st.angle() < degrees:
        zap1.straight(coefd1*-25)
        zapdisplay.screen.clear()
        zapdisplay.screen.draw_text(80, 50, str(st.angle()), Color.BLACK, None)
        if senzorCuloareSt.color() == Color.BLACK:
            zap1.turn(10)
        if senzorCuloareSt.color() == Color.WHITE:
            zap1.turn(-10)

#*********RUNS*********
def run01():
    #MIXER
    zap1.straight(coefd1 * 230)
    zap1.turn(coeft1 * 45)
    zap1.straight(coefd1 * 240)
    _thread.start_new_thread(thread_bratDr, (1000, 1200))
    _thread.start_new_thread(thread_zap1, (20,))
    bratDr.run_time(1000, 1200)
    zap1.straight(coefd1 * 1)  
    zap1.turn(coeft1 * 45)
    zap1.straight(coefd1 * -100)
    zap1.turn(coeft1 * -45)
    zap1.straight(coefd1 * -400)

def run02():
    #DRAGON
    zap3.straight(coefd3*-380)
    zap3.straight(coefd3*50)
    zap3.turn(coeft3*60)
    zap3.straight(coefd3*300)

def run03(repetari):
    #TEATRU
    # mergem la teatru
    zap3.straight(coeft3*-660)
    zap3.turn(coeft3*-35)
    # face misiunea
    for i in range(repetari):
        zap3.straight(coeft2*-30)
        zap3.straight(coeft2*30)
    zap3.turn(coeft3*40)
    zap3.straight(coeft3*660)

def run04():
    #SINA BAZA ROSIE
    bratSt.run_time(1000, 300)
    zap4.straight(coefd4*470)
    bratSt.run_time(-500, 500)
    zap4.straight(coefd4*-200)
    zap4.reset()
    while zap4.distance() < 200:
        zap4.drive(45, 200)
    zap4.straight(5)
    '''
    zap4.turn(coeft4*-90)
    zap4.straight(coefd4*100)
    zap4.turn(coeft4*-45)
    zap4.straight(coefd4*100)
    '''

def run05():
    #SCH BAZA SI LINIE SPATE
    zap1.straight(coefd1 * 260)
    zap1.turn(coeft1*90)
    zap1.straight(coefd1 * 640)
    zap1.turn(coeft1 * -90)
    zap1.straight(coefd1 * 270)
    zap1.turn(coeft1*10)
    #diagonala
    zap1.straight(coefd1 * 100)
    zap1.turn(coeft1*-10)
    zap1.straight(coefd1 * 80)
    #actionam bratul ca sa facem MOV
    bratSt.run_angle(-1000, 1050)
    #dam cu spatele dupa MOV
    zap1.straight(coefd1*-90)
    #ne intoarcem spre lalea
    zap1.turn(coeft1*-90)
    #facem diagonala pentru a face laleaua
    zap1.straight(coefd1*-160)
    zap1.turn(coeft1*-30)
    #facem diagonala ca sa ne apropiem
    zap1.straight(coefd1*-220)
    zap1.turn(coeft1*30)
    #mergem cu spatele sa facem laleaua
    zap1.straight(coefd1*-440)
    zap1.turn(coeft1*-120)
    zap1.straight(coefd1*60)
    zap1.turn(coeft1*-110)
    #facem TAO
    bratSt.run_angle(-1000, 500)
    zap1.straight(coefd1*170)
    bratSt.run_angle(1000, 1400)
    bratDr.run_angle(-1000, 300)
    #catre baza albastraaaaaaaaaa LETSGOOOOOO MEOW MEOW
    zap1.straight(coefd1*-180)
    zap1.turn(coeft1*100)
    zap1.straight(coefd1*900)

    '''_thread.start_new_thread(thread_zap1, (100,))
    _thread.start_new_thread(thread_bratSt, (1000, 360))
    _thread.start_new_thread(thread_bratDr, (1000, 360))
    _thread.start_new_thread(thread_zap1, (100,))'''

def run06():
    #TURN
    #mergem spre tao
    zap6.straight(coefd6*-450)
    #diagonala
    zap6.turn(coeft6*-45)
    zap6.straight(coefd6*-290)
    #ne intoarcem paralel cu turnul
    zap6.turn(coeft6*-50)
    #mergem pana in fata turnului paralel
    zap6.straight(coefd6*-680)
    #ne intoarcem spre muzeu
    zap6.turn(coeft6*90)
    #lasam tot in muzeu
    zap6.straight(coefd6*-70)
    #mergem in turn
    zap6.straight(coefd6*70)
    zap6.turn(20)
    zap6.straight(coefd6*100)
    zap6.turn(-20)
    zap6.straight(coefd6*60)
    #facem turnul
    bratSt.run_time(-1000, 4600)
    #ne indepartam de turn
    bratSt.run_time(1000, 1000)
    zap6.straight(coefd6*-90)
    zap6.turn(coeft6*-100)
    zap6.straight(coefd6*640)
    zap6.turn(coeft6*75)
    zap6.straight(coefd6*700)

def run07():
    #SINA
    zap7.straight(coeft2*-400)
    zap7.straight(coeft2*400)

def run09():
    #GAINA/COCOS
    #diagonala
    zap9.straight(coefd9*130)
    #ne intoarcem spre cocos
    zap9.turn(coeft9*-45)
    #mergem in cocos
    zap9.straight(coefd9*330)
    zap9.turn(coeft9*-15)
    #actionam bratul pentru cocos
    bratSt.run_time(1000, 2050)
    zap9.straight(coefd9*30)
    #facem un unghi ca sa facem imprimanta
    zap9.turn(coeft9*-10)
    #ne intoarcem in baza
    zap9.straight(coefd9*-600)

def run12():
    #LANSAT OAMENI
    zap2.turn(coeft2*-20)
    bratSt.run_time(1000, 1400)
    bratSt.run_time(-1000, 1400)
    zap2.straight(coeft2*20)
    zap2.turn(coeft2*-55)
    zap2.straight(coeft2*-90)
    wait(1000)
    bratSt.run_time(900, 1500)
    bratSt.run_time(-900, 1500)
    zap2.turn(coeft2*-30)
    bratSt.run_time(900, 1400)
    bratSt.run_time(-900, 1400)

def run13():
    bratSt.run_time(1300, 900)

#*********BRAT OAMENII*********

def miscaBrat(cm):
    bratSt.run_time(1000, cm**2.2)

#*********DISPLAY*********
#FUNCTIA DE AFISARE
x = 4
zapdisplay.screen.draw_text(80, 50, str(x), Color.BLACK, None) 
zap.speaker.beep() 

def update_screen(x):
    zapdisplay.screen.clear()
    zapdisplay.screen.draw_text(80, 50, str(x), Color.BLACK, None)

touch=0

#*********DISPLAY*********

while True:
    #verificare apasare butoane
    if Button.UP in zapdisplay.buttons.pressed() and x < 13:
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
    if int(x)==2 and senzorApasare.pressed():
        wait(200)
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run02()
            touch = 0
    if int(x)==3 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run03(1)
            touch = 0   
    if int(x)==4 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run04()
            touch = 0
    if int(x)==5 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run05()
            touch = 0
    if int(x)==6 and senzorApasare.pressed():
        touch = 1   
        if senzorApasare.pressed() and touch==1:
            run06()
            touch = 0
    if int(x)==7 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run07()
            touch = 0
    if int(x)==8 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run08()
            touch = 0
    if int(x)==9 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run09()
            touch = 0
    if int(x)==10 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run10()
            touch = 0
    if int(x)==11 and senzorApasare.pressed():
        touch = 1   
        if senzorApasare.pressed() and touch==1:
            run11()
            touch = 0
    if int(x)==12 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run12()
            touch = 0
    if int(x)==13 and senzorApasare.pressed():
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run13()
            touch = 0

    if Button.LEFT in zapdisplay.buttons.pressed():
        _thread.start_new_thread(thread_bratSt, (500, 120, Stop.COAST))
        _thread.start_new_thread(thread_bratDr, (500, 120, Stop.COAST))
        wait(500)

    if Button.RIGHT in zapdisplay.buttons.pressed():
        bratSt.run_angle(200, 100)
        wait(200)

dr.stop()
st.stop()
