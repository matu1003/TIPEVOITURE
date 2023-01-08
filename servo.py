import RPi.GPIO as GPIO
from time import sleep
import pigpio

class Servo:
    def __init__(self,pin):
        self.pin = pin
        self.pwm = pigpio.pi()
        self.pwm.set_mode(pin, pigpio.OUTPUT)
        self.pwm.set_PWM_frequency(pin,50)
    
    def mid(self):
        self.pwm.set_servo_pulsewidth(self.pin,1500)
    
    def set(self,angle):
        self.pwm.set_servo_pulsewidth(self.pin,1500 + 1000 * angle)
