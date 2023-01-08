import numpy as np
import math
import matplotlib.pyplot as plt
import time

def polaireEnCartesien(r,a) :  ##Tout est dans le titre
    return r*np.sin(a), r*np.cos(a)


def angleBizarreEnRadians(a):
    '''[-1,1] -> [-pi/4,pi/4]'''
    return np.pi/2 * a
    
    
def modifierCarte(carte,coordonnees) : ## carte c'est un matrice, et les coordonnees sont cartesiennes
    x,y = coordonnees
    dim = np.shape(carte)
    xMax, yMax = dim[1]//2, dim[0]
    if x >= -xMax and x <= xMax and y<= yMax :
        carte[math.floor(y),math.floor(x)+xMax] = 1

## dim = [quelconque, pair]

def cartographier(imax,ipas,dim,servo,capt) :  ## on donne des dim, et il cree un tableau des alentours Ensuite il met 1 a chaque fois qu'il y a un obstacle
    carte = np.zeros((dim[0],dim[1]))
    for x in range(dim[1]) :                                                      
        for y in range(1,dim[0]):                                                   
           if np.arctan(abs((x-(dim[1]/2))/y)) >= angleBizarreEnRadians(imax) :  
                carte[y,x] = .5
    angle = -imax
    servo.set(angle)
    time.sleep(0.2)
    while angle <= imax:
        time.sleep(0.1)
        servo.set(angle)
        modifierCarte(carte,polaireEnCartesien(capt.distance(), angleBizarreEnRadians(angle)))
        angle += ipas
       
    return carte 

def affichage(carte) :
    dim = np.shape(carte)
    X = []
    Y = []
    for x in range(dim[1]) :
        for y in range(dim[0]) :
            if carte[y,x] == 1 :
                X.append(dim[1]-x-1)
                Y.append(y)
    plt.plot(Y,X)
    plt.axis([0,dim[0],0,dim[1]])
    plt.show()
