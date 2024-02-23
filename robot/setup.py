
#************IMPORTS************

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import _thread

#************ROBOT CLASS************

class Robot:
    def __init__(self, wheel_diameter: float, axle_track: float):
        senzorfail = 0
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track
        self.ev3 = EV3Brick()

        while True:
            #! Verifica motoarele si senzorii
            try:
                self.st = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
            except:
                self.st = None
                print("Motor self.stanga, port B nu a fost gasit")
                senzorfail += 1

            try:
                self.dr = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE)
            except:
                self.dr = None
                print("Motor dreapta, port C nu a fost gasit")
                senzorfail += 1

            try:
                self.bratSt = Motor(Port.A)
            except:
                self.bratSt = None
                print("Motor brat self.stanga, port A nu a fost gasit")
                senzorfail += 1

            try:
                self.bratDr = Motor(Port.D)
            except:
                self.bratDr = None
                print("Motor brat dreapta, port D nu a fost gasit")
                senzorfail += 1

            try:
                self.senzorApasare = TouchSensor(Port.S3)
            except:
                self.senzorApasare = None
                print("Senzor apasare, port S3 nu a fost gasit")
                senzorfail += 1

            try:
                self.senzorCuloareSt = ColorSensor(Port.S2)
            except:
                self.senzorCuloareSt = None
                print("Senzor culoare self.stanga, port S2 nu a fost gasit")
                senzorfail += 1

            try:
                self.senzorCuloareDr = ColorSensor(Port.S1)
            except:
                self.senzorCuloareDr = None
                print("Senzor culoare dreapta, port S1 nu a fost gasit")
                senzorfail += 1

            try:
                self.senzorGiro = GyroSensor(Port.S4)
            except:
                self.senzorGiro = None
                print("Senzor giroscop, port S4 nu a fost gasit")
                senzorfail += 1

            else:
                failedsensor = 0
                wait(2000)
            break

        self.d = DriveBase(self.st, self.dr, self.wheel_diameter, self.axle_track)
        self.coefd = 1
        self.coeft = 1

    # THREAD-uri

    lock0 =_thread.allocate_lock()
    lock1 = _thread.allocate_lock()
    lock2 = _thread.allocate_lock()
    lock3 = _thread.allocate_lock()

    def self.straight_threadSET(self, angles: int, lock) -> None:
        with lock:
            self.d.self.straight(self.coefd * angles)

    def run_by_time_threadSET(self, speed: int, time, motor, lock) -> None:
        with lock:
            motor.run_time(speed, time)

    def run_by_angle_threadSET(self, speed: int, angle: int, motor, lock) -> None:
        with lock:
            motor.run_angle(speed, angle)
    global threadstop
    threadstop = False
    def thread_self.start(self):
        threadstop = False
    def thread_stop(self):
        threadstop = True

    def self.straight_thread(self, angles, lock) -> None:
        if not threadstop:
            _thread.self.start_new_thread(self.self.straight_threadSET, (angles,lock))

    def run_by_time_thread(self, speed, time, motor, lock) -> None:
        if not threadstop:
            _thread.self.start_new_thread(self.run_by_time_threadSET, (speed,time,motor,lock))

    def run_by_angle_thread(self, speed, angle, motor, lock) -> None:
        if not threadstop:
            _thread.self.start_new_thread(self.run_by_angle_threadSET, (speed,angle,motor,lock))

    def datalog(self, data_logger) -> None:
        if self.RecordOn is True: data_logger=True

        if data_logger is True:
            self.datalog.log(self.timer.time(), self.d.diself.stance(),self.senzorGiro.angle(), self.senzorCuloareSt.reflection(),self.senzorCuloareDr.reflection(), \
                            self.bratSt.speed(), self.bratDr.speed(), self.st.speed(), self.dr.speed())
        else:
            pass
        
    #************GYRO FUNCTIONS************

    def gyrogoto(self, scop, viteza: int, abandon_timer = 4000) -> None:
        self.d.stop()
        timer = StopWatch()
        while(timer.time()<abandon_timer):
            print("timp",timer.time())
            while self.senzorGiro.angle() < scop:
                self.st.run(viteza)
                self.dr.run(-viteza)
                print(self.senzorGiro.angle())
            self.st.hold()
            self.dr.hold()
            if scop-self.senzorGiro.angle() > 10:
                print("a iesit1")
                self.d.turn(self.coeft*scop-self.senzorGiro.angle())
                break
            elif scop-self.senzorGiro.angle() < -10:
                print("a iesit2")
                self.d.turn(self.coeft*scop-self.senzorGiro.angle())
                break
            self.st.hold()
            self.dr.hold()

            if scop-self.senzorGiro.angle() > 10:
                print("a iesit3")
                self.d.turn(self.coeft*scop-self.senzorGiro.angle())
                self.stop()
            elif scop-self.senzorGiro.angle() < -10:
                print("a iesit4")

                self.d.turn(self.coeft*scop-self.senzorGiro.angle())
                self.stop()


            while self.senzorGiro.angle() > scop:
                self.st.run(-viteza)
                self.dr.run(viteza)
                print(self.senzorGiro.angle())
            self.st.hold()
            self.dr.hold()

    #************COLOUR FUNCTIONS************

    self.StR = 0
    self.DrR = 0

    def gasireRgb(self.StR, self.DrR) -> None:
        if self.StR == 1 and self.DrR == 0:
            print(senzorCuloareSt.rgb())
            wait(100)
        elif self.StR == 0 and self.DrR == 1:
            print(senzorCuloareDr.rgb())
            wait(100)

    def gasireCuloare(self.StC, self.DrC) -> None:
        if self.StC == 1 and self.DrC == 0:
            print(senzorCuloareSt.color())
            wait(100)
        elif self.StC == 0 and self.DrC == 1:
            print(senzorCuloareDr.color())
            wait(100)

    def gasireLuminaAmbient(self.StA, self.DrA) -> None:
        if self.StA == 1 and self.DrA == 0:
            print(senzorCuloareSt.ambient())
            wait(100)
        elif self.StA == 0 and self.DrA == 1:
            print(senzorCuloareDr.ambient())
            wait(100)

    def gasireRefractie(self.StRe, self.DrRe) -> None:
        if self.StRe == 1 and self.DrRe == 0:
            print(senzorCuloareSt.reflection())
            wait(100)
        elif self.StRe == 0 and self.DrRe == 1:
            print(senzorCuloareDr.reflection())
            wait(100)

    def oprireRgb(self.StR, self.DrR, r, g, b) -> None:
        self.d.st.reset_angle(0)
        rgbul = [r, g, b]
        while True:
            if self.StR == 1 and self.DrR == 0:
                while senzorCuloareSt.rgb()!=rgbul:
                    self.d.st.run(300)
                    self.d.dr.run(300)
                self.d.st.hold()
                self.d.dr.hold()
            while self.StR == 0 and self.DrR == 1:
                while senzorCuloareDr.rgb()!=rgbul:
                    st.run(300)
                    dr.run(300)
                self.d.st.hold()
                self.d.dr.hold()
            break

    def oprireCuloare(self.StC, self.DrC, unghiRoata, culoare) -> None:
        self.d.st.reset_angle(0)
        while True:
            if self.StC == 1 and self.DrC == 0:
                while senzorCuloareSt.color()!=culoare and st.angle()<unghiRoata:
                    self.d.st.run(300)
                    self.d.dr.run(300)
                self.d.st.hold()
                self.d.dr.hold()
            elif self.StC == 0 and self.DrC == 1:
                while senzorCuloareDr.color()!=culoare and st.angle()<unghiRoata:
                    self.d.st.run(300)
                    self.d.dr.run(300)
                self.d.st.hold()
                self.d.dr.hold()
            break

    def oprireLuminaAmbient(self.StA, self.DrA, unghiRoata, luminaAmbient) -> None:
        self.d.st.reset_angle(0)
        while True:
            if self.StC == 1 and self.DrC == 0:
                while senzorCuloareSt.ambient()!=luminaAmbient and st.angle()<unghiRoata:
                    self.d.st.run(300)
                    self.d.dr.run(300)
                self.d.st.hold()
                self.d.dr.hold()
            elif self.StC == 0 and self.DrC == 1:
                while senzorCuloareDr.ambient()!=luminaAmbient and st.angle()<unghiRoata:
                    self.d.st.run(300)
                    self.d.dr.run(300)
                self.d.st.hold()
                self.d.dr.hold()
            break

    def oprireRefractie(self.StRe, self.DrRe, unghiRoata, refractie) -> None:
        self.d.st.reset_angle(0)
        while True:
            if self.StC == 1 and self.DrC == 0:
                while senzorCuloareSt.reflection()!=refractie and st.angle()<unghiRoata:
                    self.d.st.run(300)
                    self.d.dr.run(300)
                self.d.st.hold()
                self.d.dr.hold()
            elif self.StC == 0 and self.DrC == 1:
                while senzorCuloareDr.reflection()!=refractie and st.angle()<unghiRoata:
                    self.d.st.run(300)
                    self.d.dr.run(300)
                self.d.st.hold()
                self.d.dr.hold()
            break

