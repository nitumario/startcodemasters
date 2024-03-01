
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
import numpy as np
import matplotlib.pyplot as plt

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
    threadstop = False
    def thread_start(self):
        self.threadstop = False
    def thread_stop(self):
        self.threadstop = True

    def straight_threadSET(self, angles: int, lock) -> None:
        with lock:
            self.d.self.straight(self.coefd * angles)

    def run_by_time_threadSET(self, speed: int, time, motor, lock) -> None:
        with lock:
            motor.run_time(speed, time)

    def run_by_angle_threadSET(self, speed: int, angle: int, motor, lock) -> None:
        with lock:
            motor.run_angle(speed, angle)

    def straight_thread(self, angles, lock) -> None:
        if not self.threadstop:
            _thread.self.start_new_thread(self.self.straight_threadSET, (angles,lock))

    def run_by_time_thread(self, speed, time, motor, lock) -> None:
        if not self.threadstop:
            _thread.self.start_new_thread(self.run_by_time_threadSET, (speed,time,motor,lock))

    def run_by_angle_thread(self, speed, angle, motor, lock) -> None:
        if not self.threadstop:
            _thread.self.start_new_thread(self.run_by_angle_threadSET, (speed,angle,motor,lock))

    def datalog(self, data_logger) -> None:
        if self.RecordOn is True: data_logger=True

        if data_logger is True:
            self.datalog.log(self.timer.time(), self.d.diself.stance(),self.senzorGiro.angle(), self.senzorCuloareSt.reflection(),self.senzorCuloareDr.reflection(), \
                            self.bratSt.speed(), self.bratDr.speed(), self.st.speed(), self.dr.speed())
        else:
            pass
        
    #************GYRO FUNCTIONS************

    def gyrogoto(self, scop, viteza: int, abandon_timer=4000, spin=1) -> None:
        self.d.stop()
        timer = StopWatch()
        if spin == 1:
            while timer.time() < abandon_timer:
                print("timp", timer.time())
                while self.senzorGiro.angle() < scop:
                    self.st.run(viteza)
                    self.dr.run(-viteza)
                    print(self.senzorGiro.angle())
                    if timer.time() >= abandon_timer:
                        print("Abandoning due to timeout")
                        self.st.hold()
                        self.dr.hold()
                        return
                self.st.hold()
                self.dr.hold()
                if scop - self.senzorGiro.angle() > 10:
                    print("a iesit1")
                    self.d.turn(self.coeft * (scop - self.senzorGiro.angle()))
                    break
                elif scop - self.senzorGiro.angle() < -10:
                    print("a iesit2")
                    self.d.turn(self.coeft * (scop - self.senzorGiro.angle()))
                    break
                self.st.hold()
                self.dr.hold()
                if scop - self.senzorGiro.angle() > 10:
                    print("a iesit3")
                    self.d.turn(self.coeft * (scop - self.senzorGiro.angle()))
                    self.stop()
                elif scop - self.senzorGiro.angle() < -10:
                    print("a iesit4")
                    self.d.turn(self.coeft * (scop - self.senzorGiro.angle()))
                    self.stop()
                while self.senzorGiro.angle() > scop:
                    self.st.run(-viteza)
                    self.dr.run(viteza)
                    print(self.senzorGiro.angle())
                    if timer.time() >= abandon_timer:
                        print("Abandoning due to timeout")
                        self.st.hold()
                        self.dr.hold()
                        return
                self.st.hold()
                self.dr.hold()
            




    #************COLOUR FUNCTIONS************



    #************EXPERIMENTAL************
    def selfDrive_log(self, name):
        datalog_file = DataLog("distance", "gyro_angle", name=name, timestamp=False, extension=".csv", append=False)
        distances = []
        gyro_angles = []
        while True:
            dis = self.d.distance()
            gyro_angle = self.senzorGiro.angle()
            datalog_file.log(dis, gyro_angle)
            distances.append(dis)
            gyro_angles.append(gyro_angle)
            
            plt.scatter(distances, gyro_angles, color='blue', label='Data')
            
            z = np.polyfit(distances, gyro_angles, deg=5)  
            p = np.poly1d(z)
            plt.plot(distances, p(distances), color='red', label='Trendline')
            
            plt.xlabel('Distance')
            plt.ylabel('Gyro Angle')
            plt.legend()
            plt.show()

    def self_drive(self, begin, stop, speed, kp, t1 = 0, t2 = 0, t3 = 0, t4 = 0, t5 = 0, t6 = 0, t7 = 0,):
        while True:
            x = self.d.distance() + 0
            formula_unghi = t1 + t2 * x + t3 * x ** 2 + t4 * x ** 3 + t5 * x ** 4 + t6 * x ** 5 + t7 * x ** 6
            if x <= begin or x >= stop:
                unghi_dorit = 0
            else:
                unghi_dorit = formula_unghi
            unghi_gyro = self.senzorGiro.angle()
            eroare = unghi_dorit - unghi_gyro
            corectie = kp * eroare
            self.d.drive(speed, corectie)
            if self.d.distance() >= stop:
                break            
    
