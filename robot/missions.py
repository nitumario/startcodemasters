#!/usr/bin/env pybricks-micropython

#************IMPORTS************

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
from setup import Robot

#************DECLARAM ROBOTII************

zap1 = Robot(56,117.5)
zap2 = Robot(56,117.5)
zap3 = Robot(56,117.5)
zap4 = Robot(56,117.5)
zap5 = Robot(56,117.5)

#************RUN-URILE************

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
    zap2.d.straight(320)
    zap2.d.turn(-39)
    zap2.d.straight(330)
    zap2.d.turn(85)
    zap2.d.straight(190)
    zap2.d.turn(-15)
    straight_thread(30, lock0)
    bratSt.run_angle(200, 300)
    wait(500)
    bratDr.d.run_angle(500, 700)
    zap2.d.straight(-100)
    zap2.d.turn(110)
    zap2.d.straight(450)

def run03():
    zap3.d.straight(-350)
    zap3.d.straight(350)

def run04():
    bratDr.run_angle(-100, 10)
    zap4.straight(1500)
    zap4.turn(155)
    bratDr.run_angle(100, 200)

def run05():
    zap5.settings(700, 700, 100, 100)

    zap5.d.straight(-110)

    zap5.d.stop()
    senzorGiro.reset_angle(0)
    while(senzorGiro.angle()<90):
        st.run(100)
        dr.run(-100)
    dr.stop()
    st.stop()

    zap5.d.straight(-410)
    zap5.d.turn(-65)
    zap5.d.straight(-610)
    zap5.d.turn(-32)
    zap5.d.straight(190)
    bratSt.run_angle(-500, 1950)
    zap5.d.straight(-50)
    zap5.d.turn(60)
    zap5.d.straight(230)
    zap5.d.turn(-60)
    zap5.d.straight(-200)
    wait(500)
    zap5.d.straight(130)
    zap5.d.turn(70)
    zap5.d.straight(-380)
    zap5.d.turn(50)
    zap5.d.straight(-400)
    zap5.d.turn(40)
    zap5.d.straight(-700)
