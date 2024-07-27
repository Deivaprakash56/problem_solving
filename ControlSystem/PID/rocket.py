import numpy as np 
import matplotlib
import turtle
import time

# GLOBAL PARAMS
TIMER = 0
SETPOINT = 10
SIM_TIME = 10
INITIAL_X = 0
INITIAL_Y = -100
MASS = 1 # Kg
MAX_THRUST = 15 #Newtons
g = -9.81 # Gravitational constant
V_i = 0 #initial velocity
Y_i = 0 #initial height
#---------------

#----PID GAINS----
KP = 0.36
KI = 40
KD = 0.0008099999999999997
antiWindup = True
#------------------

class Simulation(object):
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.setup(1280, 900)
        self.marker = turtle.Turtle()
        self.marker.penup()
        self.marker.left(90)
        self.marker.goto(15, SETPOINT)
        self.marker.color('red')
        self.sim = True
        self.timer = 0
        self.poses = np.array([])
        self.times = np.array([])
        self.kpe = np.array([])
        self.kde = np.array([])
        self.kie = np.array([])
        self.thrst = np.array([])

    def cycle(self):
        while(self.sim):
            if self.timer > SIM_TIME:
                self.sim = False

class Rocket(object):
    def __init__(self):
        global Rocket
        self.Rocket = turtle.Turtle()
        self.Rocket.shape('Square')
        self.Rocket.color('black')
        self.Rocket.goto(INITIAL_X, INITIAL_Y)
        self.Rocket.speed(0)

def main():
    sim = Simulation()
    sim.cycle()
    
main()