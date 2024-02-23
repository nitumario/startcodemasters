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
        self.coefd = 1
        self.coeft = 1

    lock0 =_thread.allocate_lock()
    lock1 = _thread.allocate_lock()
    lock2 = _thread.allocate_lock()
    lock3 = _thread.allocate_lock()

    def straight_threadSET(self, angles,lock):
        with lock:
            self.d.straight(self.coefd * angles)

    def run_by_time_threadSET(self,speed,time,motor,lock):
        with lock:
            motor.run_time(speed, time)

    def run_by_angle_threadSET(self,speed,angle,motor,lock):
        with lock:
            motor.run_angle(speed, angle)
    global threadstop
    threadstop = False
    def thread_start(self):
        threadstop = False
    def thread_stop(self):
        threadstop = True

    def straight_thread(self, angles, lock):
        if not threadstop:
            _thread.start_new_thread(self.straight_threadSET, (angles,lock))

    def run_by_time_thread(self, speed,time,motor, lock):
        if not threadstop:
            _thread.start_new_thread(self.run_by_time_threadSET, (speed,time,motor,lock))

    def run_by_angle_thread(self, speed,angle,motor, lock):
        if not threadstop:
            _thread.start_new_thread(self.run_by_angle_threadSET, (speed,angle,motor,lock))

    
            

    def datalog(self, data_logger):
        if self.RecordOn is True: data_logger=True

        if data_logger is True:
            self.datalog.log(self.timer.time(), self.d.distance(),self.senzorGiro.angle(), self.senzorCuloareSt.reflection(),self.senzorCuloareDr.reflection(), \
                            self.bratSt.speed(), self.bratDr.speed(), self.st.speed(), self.dr.speed())
        else:
            pass
        
    def gyrogoto(self, scop, viteza, abandon_timer = 4000):
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