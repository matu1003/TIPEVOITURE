import RPi.GPIO as GPIO
from time import sleep
import time
from moteur import Mot
from deplacements import *
from gpiozero import Servo
from ultrasson import CaptUltrasson

GPIO.setmode(GPIO.BCM)

'''
18:ENB
23 et 24: moteur gauche
21:ENA
16 et 20: moteur droit
2 Servo
26 Trig Ultrasson
19 Echo Ultrasson
'''
# Moteurs
motd = Mot(20,16,21)
motg = Mot(23,24,18)

# Servo
servo = Servo(2)

# test1mot(motg,motd)
# test1servo(servo)

# Capteur Ultrasson
capt = CaptUltrasson(26,19)
# print(capt.distance())

arret_obstacle(0,motg,motd,capt)

GPIO.cleanup()

