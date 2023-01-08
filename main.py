import RPi.GPIO as GPIO
from time import sleep
import time
from moteur import Mot
from deplacements import *
#from gpiozero import Servo
from ultrasson import CaptUltrasson
from cartographier import cartographier, affichage
import plotly.express as px
from servo import Servo

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
#servo = Servo(2)
servo = Servo(2)
servo.mid()

# test1mot(motg,motd)

# Capteur Ultrasson
capt = CaptUltrasson(26,19)
# print(capt.distance())

# arret_obstacle(0,motg,motd,capt)
carte = cartographier(0.2,0.015,(400,500),servo,capt)
#print(carte)
# affichage(carte)
#arret_obstacle(0,motg,motd,capt)
#sleep(1)

GPIO.cleanup()

fig = px.imshow(carte)
fig.show()

