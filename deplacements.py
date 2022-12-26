import RPi.GPIO as GPIO
from time import sleep
from moteur import Mot

def test1mot(motg,motd):

    motd.vitesse(100)
    motg.vitesse(100)

    motd.avancer()
    motg.avancer()

    sleep(2)

    motd.vitesse(50)
    motg.vitesse(50)

    motd.avancer()
    motg.avancer()

    sleep(2)

    motd.reculer()
    motg.reculer()

    sleep(2)

    motd.vitesse(0)
    motg.vitesse(0)

    sleep(1)

def test1servo(servo):
    servo.min()
    sleep(1)
    servo.max()
    sleep(1)
    servo.mid()
    sleep(1)
    
def arret_obstacle(dt,motg,motd,capt):
    sleep(dt)
    motd.vitesse(50)
    motg.vitesse(50)
    motd.avancer()
    motg.avancer()
    while True:
        if capt.distance() < 20:
            motd.vitesse(0)
            motg.vitesse(0)
            break
        sleep(0.1)
    