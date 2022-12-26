import RPi.GPIO as GPIO
import time

class CaptUltrasson:
    def __init__(self,trig,echo):
        GPIO.setup(trig,GPIO.OUT)
        GPIO.setup(echo,GPIO.IN)
        self.trig = trig
        self.echo = echo
    
    def distance(self):
        # Envoi signal
        GPIO.output(self.trig, True)
     
        # Desactiver signal apres cours temps
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
     
        StartTime = time.time()
        StopTime = time.time()
     
        # Temps depart
        while GPIO.input(self.echo) == 0:
            StartTime = time.time()
     
        while GPIO.input(self.echo) == 1:
            StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2
     
        return distance
