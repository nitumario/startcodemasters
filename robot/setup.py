from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
import _thread

class Robot:
    def __init__(self, wheel_diameter, axle_track, ):
        senzorfail = 0
        self.wheel_diameter = wheel_diameter
        self.axle_track = axle_track
        self.ev3 = EV3Brick()
        self.display = EV3Brick()
        self.timer = StopWatch()
        self.speaker = EV3Brick
        self.record = False

        self.datalog = self.datalog = DataLog('time', 'distance', 'gyroangle', 'lcolor','rcolor', "llspd",'rlspd',"lmspd","rmspd",name="log_robot", timestamp= False, extension = 'csv', append=True)

        while True:
            try:
                self.st = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
            except:
                self.st = None
                print("Motor stanga, port B nu a fost gasit")
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
                print("Motor brat stanga, port A nu a fost gasit")
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
                print("Senzor culoare stanga, port S2 nu a fost gasit")
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
        
    def multithreading():
        

    def datalog(self, data_logger):
        if self.RecordOn is True: data_logger=True

        if data_logger is True:
            self.datalog.log(self.timer.time(), self.d.distance(),self.senzorGiro.angle(), self.senzorCuloareSt.reflection(),self.senzorCuloareDr.reflection(), \
                            self.bratSt.speed(), self.bratDr.speed(), self.st.speed(), self.dr.speed())
        else:
            pass