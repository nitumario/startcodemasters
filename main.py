#!/usr/bin/env pybricks-micropython
#IMPORTS****
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

#ROBOTUL****
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

#OBIECTELE****

#DRIVE BASE-UL SI SETARILE OBIECTELOR
zapT = DriveBase(st, dr, 49.5, 103)
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

zapT.settings(400, 400, 300, 300)
zap1.settings(800, 800, 300, 300)
zap2.settings(1000, 500, 300, 300)
zap3.settings(800, 1000, 800, 800)
zap4.settings(800, 500, 300, 300)
zap5.settings(800, 500, 300, 300)
zap6.settings(800, 500, 300, 150)
zap7.settings(1000, 500, 300, 300)
zap8.settings(800, 500, 200, 200)
zap9.settings(1000, 1000, 800, 800)
zap10.settings(1000, 500, 300, 300)
zap11.settings(1000, 500, 800, 800)
zap12.settings(800, 500, 200, 200)

st.stop()
dr.stop()

#COEFICIENTE DE EROARE****

#CREEM COEFICIENTELE DE EROARE
#!Daca nu sti pentru ce sunt coeficientele intraba-l pe Vlad

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
global coeft7
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
global coeftT
coeftT = 1

#THREAD-URI****

global angles_zap1
global bratSt_speed
global bratSt_angles
global bratDr_speed
global bratDr_angles
global extra

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

#URMARIRE LINIE****

def urmarireLinie1(degrees):
    while st.angle() < degrees:
        zap5.straight(coefd5*10)
        zapdisplay.screen.clear()
        zapdisplay.screen.draw_text(80, 50, str(st.angle()), Color.BLACK, None)
        if senzorCuloareSt.color() == Color.BLACK:
            zap5.turn(10)
        if senzorCuloareSt.color() == Color.WHITE:
            zap5.turn(-10)

def urmarireLinie2(grade2):
    alb = 3
    negru = 40
    medieL = (alb+negru)/2
    pGain = 2
    while st.angle() < grade2:
        deviatie = senzorCuloareDr.reflection() - medieL
        rotireL = pGain * deviatie
        print(rotireL)
        zap1.drive(100, rotireL)

def urmarireLinie3(grade3):
    while st.angle() < grade3:
        if gasireCuloare(0, 1) == Color.BLACK:
            zap1.turn(10)
        elif gasireCuloare(0, 1) == Color.WHITE:
            zap1.turn(-10)
        else:
            zap1.straight(10)

#GYRO FUNCTIONS****

def gyroSpeedLog(TBR):
    #TBR vine de la Time Between Reads si este in ms
    watch = StopWatch()
    #data = DataLog('time', 'speed')
    while True:
        time=watch.time()
        speed=senzorGiro.speed()
        print(speed)
        #data.log(time, speed)
        wait(TBR)

global heading
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
#SENZOR CULOARE****

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

#BRAT OAMENII****

def miscaBrat(cm):
    bratSt.run_time(1000, cm**2.2)

#PID****
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

        zap13.drive(10, pFix+iFix+dFix)

#RUNS****
def run01():
    #MIXER - linia 5
    zap1.straight(coefd1 * 210)
    zap1.turn(coeft1 * 45)
    zap1.straight(coefd1 * 250)
    _thread.start_new_thread(thread_bratDr, (1000, 1200))
    _thread.start_new_thread(thread_zap1, (coefd1*30,))
    bratDr.run_time(1000, 1200)
    zap1.straight(coefd1 * 1) #linia asta nu face nimic dar reseteaza threadurile 
    zap1.turn(coeft1 * 45)
    zap1.straight(coefd1 * -100)
    zap1.turn(coeft1 * -45)
    zap1.straight(coefd1 * -400)

    bratDr.stop()
    bratSt.stop()

def run02(repetari):
    #mergem spre dragon
    zap2.straight(coefd2 * -250)
    #ne intoarcem opus dragonului
    zap2.turn(coeft2 * -35)
    #diagonala dragon
    zap2.straight(coefd2 * -150)
    #face dragonul
    zap2.turn(coeft2 * 45)
    #inapoi in baza
    zap2.straight(coefd2 * 325)
    wait(1500)
    # face misiunea
    zap2.straight(-580 * coefd2)
    zap2.turn(45 * coeft2)
    zap2.straight(-120  * coefd2)
    zap2.turn(-95 * coeft2)
    zap2.stop()
    """dr.reset_angle(0)
    while dr.angle() < 220:
        dr.run(500) 
    dr.hold()"""
    for i in range(repetari):
        zap3.straight(coefd2*-60)
        zap3.straight(coefd2*60)
    zap2.turn(90)
    '''
    zap3.straight(coeft2*-140)
    zap2.turn(-90)
    zap3.straight(coeft2*-100)
    zap3.turn(coeft3*20)
    zap4.reset()
    while zap4.distance() < 700:
        zap4.drive(500, 10)
    zap4.straight(coefd4*10)
    zap4.stop()
    zap4.reset()
    '''
    zap2.straight(coefd2*600)

    bratDr.stop()
    bratSt.stop()

def run03():
    #DUCEM OAMENII - pe directia zonei de lasat oameni din fata dinozaurului
    zap3.straight(coefd3*-430)
    zap3.straight(coefd3*430)

def run04():
    #SINA - la extrema cu spatele
    bratSt.run_time(-700, 500)
    #zap4.drive(150, 0)
    zap4.straight(coefd4*460)
    zap4.stop()
    bratSt.run_time(300, 900)
    zap4.straight(coefd4*-200)
    zap4.reset()
    while zap4.distance() < 100:
        zap4.drive(100 * coefd4, -60)
    zap4.straight(coefd4*10)
    zap4.stop()
    zap4.reset()
    bratSt.run_time(-700, 500)
    zap4.reset()
    while zap4.distance() > -200:
        zap4.drive(-1000 * coefd4, 20)
    zap4.straight(coefd4*-100)
    zap4.stop()    
    zap4.reset()

    bratDr.stop()
    bratSt.stop()

def run05():
    #SCH BAZA SI MISIUNI SPATE - linia 1 cu distantier pe spate
    senzorGiro.reset_angle(0)
    zap5.straight(coefd5*130)
    #ne intoarcem spre turn
    zap5.turn(coeft5*-95)
    #mergem langa turn
    zap5.straight(coefd5*-650)
    #ne intoarcem spre MOV
    zap5.stop()
    gyrogoto(-177, 80)
    #facem mov
    zap5.straight(coefd5*-550)
    zap5.stop()
    senzorGiro.reset_angle(0)
    #dam cu spatele dupa MOV
    zap5.straight(coefd5*90)
    #ne intoarcem spre lalea
    zap5.turn(coeft5*65)
    #facem diagonala pentru a face laleaua
    zap5.straight(coefd5*-260)
    zap5.turn(coefd5*25)
    #facem laleaua
    zap5.straight(coefd5*-600)
    print(senzorGiro.angle())
    zap5.stop()
    #ne indreptam pe directia 90
    gyrogoto(90, 100)
    zap5.straight(coefd5*100)
    zap5.turn(coeft5*55)
    zap5.straight(coeft5*-800)

    #codul pentru a face si tao


def run06():
    senzorGiro.reset_angle(0)
    print(senzorGiro.angle())
    #TURN
    #mergem spre tao
    zap7.straight(coefd7*-450)
    print(senzorGiro.angle())
    #diagonala
    zap7.turn(coeft7*-45)
    print(senzorGiro.angle())
    zap7.straight(coefd7*-270)
    print(senzorGiro.angle())
    #ne intoarcem paralel cu turnul
    zap7.turn(coeft7*-50)
    print(senzorGiro.angle())
    #mergem pana in fata turnului paralel
    zap7.straight(coefd7*-670)
    print(senzorGiro.angle())
    #ne intoarcem spre muzeu
    zap7.stop()
    gyrogoto(0, 100)
    print(senzorGiro.angle())
    #lasam tot in muzeu
    zap7.straight(coefd7*-100)
    zap7.stop()
    senzorGiro.reset_angle(0)
    zap7.straight(coefd7*50)
    zap7.turn(coeft7*25)
    zap7.straight(coefd7*120)
    zap7.turn(coeft7*-25)
    zap7.straight(coefd7*80)
    bratSt.run_time(-1000, 4600)
    bratSt.run_time(1000, 1000)
    zap7.straight(coefd7*-90)
    zap7.turn(coeft7*-100)
    zap7.straight(coefd7*640)
    zap7.turn(coeft7*75)
    zap7.straight(coefd7*700)
    
    bratDr.stop()
    bratSt.stop()

def run07():
    #SINA
    zap8.straight(coefd8*-400)
    zap8.straight(coefd8*400)

    bratDr.stop()
    bratSt.stop()

def run08():
    #luam specialistii de langa sina si cocos
    zap9.straight(coefd9*30)
    #semi-cerc
    zap9.reset()
    while zap9.distance() < 250:
        zap9.drive(100 * coefd9, -25)
    #iesim din while
    zap9.straight(coefd9*5)
    zap9.stop()
    zap9.reset()

    
    zap9.turn(-160 * coeft9)
    zap9.straight(coefd9*400)
    bratDr.stop()
    bratSt.stop()

def run09():
    senzorGiro.reset_angle(0)
    #!GAINA/COCOS
    #diagonala
    zap10.straight(coefd10*170)
    #ne intoarcem spre cocos
    zap10.stop()
    gyrogoto(-45, 100)
    #mergem in cocos
    zap10.straight(coefd10*350)
    zap10.stop()
    gyrogoto(-45, 100)
    #actionam bratul pentru cocos
    zap10.straight(coefd10*20)
    bratSt.run_time(1000, 2120)
    #facem un unghi ca sa facem imprimanta
    zap10.turn(coeft10*-10)
    #ne intoarcem in baza
    zap10.straight(coefd10*-600)

    bratDr.stop()
    bratSt.stop()

def run10():
    #LANSAT OAMENI
    zap11.turn(coeft11*-20)
    bratSt.run_time(1000, 1400)
    bratSt.run_time(-1000, 1400)
    zap11.straight(coeft11*20)
    zap11.turn(coeft11*-55)
    zap11.straight(coefd11*-90)
    wait(1000)
    bratSt.run_time(900, 1500)
    bratSt.run_time(-900, 1500)
    zap11.turn(coeft11*-30)
    bratSt.run_time(900, 1400)
    bratSt.run_time(-900, 1400)

    bratDr.stop()
    bratSt.stop()

def run11():
    senzorGiro.reset_angle(0)
    gyrogoto(90, 100)
    gyrogoto(-90, 100)
    gyrogoto(0, 100)
#BRAT OAMENII****
'''
def miscaBrat():
    bratSt.run_time(700, 500)
    zap10.straight(coefd10*-200)
    zap10.reset()
    while zap10.distance() < 250:
        zap10.drive(100, -50)
    zap10.straight(coefd10*10)
    zap10.stop()    
    zap10.reset()
    bratSt.run_time(-700, 500)
    zap10.reset()
    while zap10.distance() > -300:
        zap10.drive(-100, 20)
    zap10.straight(coefd10*-100)
    zap10.stop()
    zap10.reset()
'''

#DISPLAY****
#FUNCTIA DE AFISARE
x = 1
zapdisplay.screen.draw_text(80, 50, str(x), Color.BLACK, None) 
zap.speaker.beep() 

def update_screen(x):
    zapdisplay.screen.clear()
    zapdisplay.screen.draw_text(80, 50, str(x), Color.BLACK, None)

touch=0

#DISPLAY****
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
        touch = 1
        if senzorApasare.pressed() and touch==1:
            run02(1)
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