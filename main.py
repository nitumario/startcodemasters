#!/usr/bin/env pybricks-micropython
#*IMPORTS***
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

#*ROBOTUL***
#!bratDr (+) ridicare
#!bratSt (-) lasa in jos

#definim caramida si display-ul
zap=EV3Brick()
zapdisplay = EV3Brick()
speaker = EV3Brick()

#definim motoarele si senzorii
st = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
dr = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
bratSt = Motor(Port.A)
bratDr = Motor(Port.D)
senzorCuloareDr = ColorSensor(Port.S1)
senzorCuloareSt = ColorSensor(Port.S2)
senzorApasare = TouchSensor(Port.S3)
senzorGiro = GyroSensor(Port.S4)

#*OBIECTELE***

#DRIVE BASE-UL SI SETARILE OBIECTELOR

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


zap2.settings(1000, 500, 300, 300)
zap3.settings(800, 1000, 800, 800)
zap4.settings(800, 500, 300, 300)
zap5.settings(800, 500, 300, 300)
zap6.settings(800, 500, 300, 150)
zap7.settings(1000, 500, 800, 800)
zap8.settings(800, 300, 100, 100)
zap9.settings(1000, 1000, 800, 800)
zap10.settings(1000, 500, 300, 300)
zap11.settings(1000, 500, 800, 800)
zap12.settings(800, 500, 200, 200)

st.stop()
dr.stop()

#*COEFICIENTE DE EROARE***

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

#*THREAD-URI***

global angles_zap1
global bratSt_speed
global bratSt_angles
global bratDr_speed
global bratDr_angles
global extra
global coeftT
coeftT = 1
zapT = DriveBase(st, dr, 49.5, 103)
zapT.settings(400, 400, 300, 300)
global_lock = _thread.allocate_lock()
def thread_zap1(angles_zap1):
    with global_lock:
        zapT.straight(coefd1 * angles_zap1)

def thread_bratSt(bratSt_speed, bratSt_angles, extra):
    with global_lock:
        bratSt.run_angle(bratSt_speed, bratSt_angles, extra)

def thread_bratDr(bratDr_speed, bratDr_angles):
    with global_lock:
        bratDr.run_time(bratDr_speed, bratDr_angles)


    
#*URMARIRE LINIE***

def urmarireLinie1(degrees):
    while st.angle() < degrees:
        zap1.straight(coefd1*-25)
        zapdisplay.screen.clear()
        zapdisplay.screen.draw_text(80, 50, str(st.angle()), Color.BLACK, None)
        if senzorCuloareSt.color() == Color.BLACK:
            zap1.turn(10)
        if senzorCuloareSt.color() == Color.WHITE:
            zap1.turn(-10)

#*GYRO FUNCTIONS***

def gyrogoto(scop, viteza):
    while senzorGiro.angle() < scop:
        st.run(viteza)
        dr.run(-viteza)
        print(senzorGiro.angle())
        if scop-senzorGiro.angle() > 10:
            print("a iesit1")
            break
        elif scop-senzorGiro.angle() < 10:
            print("a iesit2")
            break
    st.hold()
    dr.hold()

    if scop-senzorGiro.angle() > 10:
        print("a iesit3")
        zapT.turn(coeftT*scop-senzorGiro.angle())
        zapT.stop()
    elif scop-senzorGiro.angle() < 10:
        print("a iesit4")

        zapT.turn(coeftT*scop-senzorGiro.angle())
        zapT.stop()


    while senzorGiro.angle() > scop:
        st.run(-viteza)
        dr.run(viteza)
        print(senzorGiro.angle())
    st.hold()
    dr.hold()


def gyroSpeedLog(TBR):
    #TBR vine de la Time Between Reads si este in ms
    watch = StopWatch()
    data = DataLog('time', 'speed')
    while True:
        time=watch.time()
        speed=senzorGiro.speed()
        print(speed)
        data.log(time, speed)
        wait(TBR)

def gyroTurn(degree):
    senzorGiro.reset_angle(0)
    
    while True:
        current_angle = senzorGiro.angle()
        print(current_angle)
        if current_angle + 10 <= degree:
            zap1.turn(10)
        elif current_angle == degree:
            break
        else:
            zap1.turn(1)

#*SENZOR CULOARE***
StR = 0
DrR = 0

def gasireRgb(StR, DrR):
    if StR == 1 and DrR == 0:
        print(senzorCuloareSt.rgb())
        wait(100)
    elif StR == 0 and DrR == 1:
        print(senzorCuloareDr.rgb())
        wait(100)

def gasireCuloare(StC, DrC):
    if StC == 1 and DrC == 0:
        print(senzorCuloareSt.color())
        wait(100)
    elif StC == 0 and DrC == 1:
        print(senzorCuloareDr.color())
        wait(100)

def gasireLuminaAmbient(StA, DrA):
    if StA == 1 and DrA == 0:
        print(senzorCuloareSt.ambient())
        wait(100)
    elif StA == 0 and DrA == 1:
        print(senzorCuloareDr.ambient())
        wait(100)

def gasireRefractie(StRe, DrRe):
    if StRe == 1 and DrRe == 0:
        print(senzorCuloareSt.reflection())
        wait(100)
    elif StRe == 0 and DrRe == 1:
        print(senzorCuloareDr.reflection())
        wait(100)

def oprireRgb(StR, DrR, r, g, b):
    st.reset_angle(0)
    rgbul = [r, g, b]
    while True:
        if StR == 1 and DrR == 0:
            while senzorCuloareSt.rgb()!=rgbul:
                st.run(300)
                dr.run(300)
            st.hold()
            dr.hold()
        while StR == 0 and DrR == 1:
            while senzorCuloareDr.rgb()!=rgbul:
                st.run(300)
                dr.run(300)
            st.hold()
            dr.hold()
        break

def oprireCuloare(StC, DrC, unghiRoata, culoare):
    st.reset_angle(0)
    while True:
        if StC == 1 and DrC == 0:
            while senzorCuloareSt.color()!=culoare and st.angle()<unghiRoata:
                st.run(300)
                dr.run(300)
            st.hold()
            dr.hold()
        elif StC == 0 and DrC == 1:
            while senzorCuloareDr.color()!=culoare and st.angle()<unghiRoata:
                st.run(300)
                dr.run(300)
            st.hold()
            dr.hold()
        break

def oprireLuminaAmbient(StA, DrA, unghiRoata, luminaAmbient):
    st.reset_angle(0)
    while True:
        if StC == 1 and DrC == 0:
            while senzorCuloareSt.ambient()!=luminaAmbient and st.angle()<unghiRoata:
                st.run(300)
                dr.run(300)
            st.hold()
            dr.hold()
        elif StC == 0 and DrC == 1:
            while senzorCuloareDr.ambient()!=luminaAmbient and st.angle()<unghiRoata:
                st.run(300)
                dr.run(300)
            st.hold()
            dr.hold()
        break

def oprireRefractie(StRe, DrRe, unghiRoata, refractie):
    st.reset_angle(0)
    while True:
        if StC == 1 and DrC == 0:
            while senzorCuloareSt.reflection()!=refractie and st.angle()<unghiRoata:
                st.run(300)
                dr.run(300)
            st.hold()
            dr.hold()
        elif StC == 0 and DrC == 1:
            while senzorCuloareDr.reflection()!=refractie and st.angle()<unghiRoata:
                st.run(300)
                dr.run(300)
            st.hold()
            dr.hold()
        break

#*BRAT OAMENII***

def miscaBrat(cm):
    bratSt.run_time(1000, cm**2.2)

#*PID***
def pidLinie(gradR):
    st.reset_angle(0)
    uEroare = 0
    integral = 0

    while st.angle() < gradR:
        eroare = senzorCuloareDr.reflection() - 50
        pFix = eroare*0.5

        integral = integral + eroare
        iFix = integral *0.01

        derivat = eroare-uEroare
        uEroare = eroare
        dFix = derivat*4

        zap1.drive(10, pFix+iFix+dFix)


bratSt.stop()
bratDr.stop()

def run01(): #oameni si imprimanta baza dreapta

    zap1 = DriveBase(st, dr, 56, 117.5)
    zap1.settings(1000, 1000, 100, 100)

    #luat 2 oameni
    bratDr.run_time(500, 700)
    zap1.straight(230)
    zap1.turn(-70)
    zap1.straight(20)
    zap1.turn(-50)
    bratDr.run_time(-150, 1300)
    zap1.turn(50)
    zap1.straight(-200)

    wait(4000)

    #cocos si imprimanta
    zap1.straight(160)
    zap1.turn(-40)

    zap1.straight(320)
    bratSt.run_angle(1000, 600)
    bratDr.run_time(500, 900)

    zap1.straight(-450)

    bratSt.stop()
    bratDr.stop()


def run02():
    zap2.straight(320)
    zap2.turn(-39)
    zap2.straight(330)
    zap2.turn(85)
    zap2.straight(190)
    zap2.turn(-15)
    bratSt.run_angle(200, 300)
    _thread.start_new_thread(thread_zap1,(40,))
    bratDr.run_angle(500, 700)
    zap2.straight(-100)
    zap2.turn(110)
    zap2.straight(450)

def run03():
    zap3.straight(-350)
    zap3.straight(350)

def run04():
    bratDr.run_angle(-100, 10)
    zap4.straight(1500)
    zap4.turn(155)
    bratDr.run_angle(100, 200)


def run05():
    #zap5 = DriveBase(st, dr, 56, 117.5)
    zap5.settings(700, 700, 100, 100)

    zap5.straight(-110)

    zap5.stop()
    senzorGiro.reset_angle(0)
    while(senzorGiro.angle()<90):
        st.run(100)
        dr.run(-100)
    dr.stop()
    st.stop()

    zap5.straight(-410)
    zap5.turn(-65)
    zap5.straight(-610)
    zap5.turn(-32)
    zap5.straight(190)
    bratSt.run_angle(-500, 1950)
    zap5.straight(-50)
    zap5.turn(60)
    zap5.straight(230)
    zap5.turn(-60)
    zap5.straight(-200)
    wait(500)
    zap5.straight(130)
    zap5.turn(70)
    zap5.straight(-380)
    zap5.turn(50)
    zap5.straight(-400)
    zap5.turn(40)
    zap5.straight(-700)
    

    















#*DISPLAY***
#FUNCTIA DE AFISARE
x = 5
zapdisplay.screen.draw_text(80, 50, str(x), Color.BLACK, None) 
zap.speaker.beep() 

def update_screen(x):
    zapdisplay.screen.clear()
    zapdisplay.screen.draw_text(80, 50, str(x), Color.BLACK, None)

touch=0

#*DISPLAY***
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
            run03()
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