import csv
from distutils.log import error
import math
from random import random
from random import seed
from copy import deepcopy

seed(random())
file = 'lab-es-data.csv'
alpha = 0.1

def boxMuller():
    # Start with two uniformly dist. random nums
    u1 = random()
    u2 = random()
    r = math.sqrt( -2 * math.log(u1) )
    theta = 2 * math.pi * u2
    X = r * math.cos(theta)
    Y = r * math.sin(theta)
    return X # Bad practice???

class Individual:
    def __init__( self, m ):
        self.coeff = [ 2 * random() - 1 for i in 
        range(m) ]
        self.n = m # Degree of polynomial
        self.setFitness()
        
    def setFitness( self ):
        global data
        self.fitness = 0
        for p in data:
            x = p[0] # -75
            yd = p[1] # Desired
            # y = ax^3 + bx^2 + cx + d
            # y = dx^0 + cx^1 + bx^2 + ax^3
            # yo = coeffi * x ^ i
            y = 0
            for i in range(self.n):
                y += self.coeff[i] * x ** i # ghat
            self.fitness += ( y - yd ) ** 2
            
    def mutate( self ):
        global alpha # Hack
        for i in range( self.n ):
            self.coeff[i] += alpha * boxMuller()
        self.setFitness()

with open(file, newline='') as csvfile:
    data = []
    for row in csv.reader( csvfile, delimiter=',' ):
        # Need to typecast
        castRow = [ float(row[i]) for i in range( len(row)) ]
        data.append( castRow )

parent = Individual(4)
for iterations in range(10000):
    offspring = deepcopy(parent)
    offspring.mutate()
    if offspring.fitness < parent.fitness:
        print( "In iteration", str(iterations), "..." )
        parent = offspring
        print( "... parent replaced, new fitness value is ", 
        str(offspring.fitness), "..." )
        print( "Equation is: ", str(offspring.coeff[3]), "x^3 + ", 
        str(offspring.coeff[2]), "x^2 + ", str(offspring.coeff[1]), "x + ", 
        str(offspring.coeff[0]) )