import csv
from random import random
from random import seed

# File name to load
file = 'iris.csv'
seed(1)

# Open the file
with open(file, newline='') as csvfile:
    # Initialize data to a list of empty objects
    data = []
    # For each row in the file ...
    for row in csv.reader( csvfile, delimiter=',' ):
        # ...append the whole row as an object. 'row' is a 5 length vector.
        data.append(row)
        
# Pop the header row
data.pop(0) 

class Neuron:
    def __init__( self, n ):
        self.w = [random() for i in range(n)] # weight vector
        # w = [ 0, 0, 0, 0 ]
        self.theta = random()
        self.n = n

    def feedForward( self, x ):
        self.X = 0
        for i in range(0, 4):
            self.X = self.X + self.w[i] * float(x[i])
        self.X = self.X - self.theta
        #Activation function
        if self.X >= 0:
            self.y = 1
        else:
            self.y = -1 # I'm using step bc I didnt replace the -1s
            
    def errorCorrection( self, yd, x ):
        global alpha
        self.e = yd - self.y 
        if self.e != 0:
            for i in range( 0, self.n ):
                self.w[i] = self.w[i] + alpha * float(x[i]) * self.e
            self.theta = self.theta - alpha * self.e
            return False
        return True

alpha = 0.01
a = Neuron(4)

for epoch in range(0, 1):
    print( "***** This is epoch ", epoch )
    count = 0 # number of correct classifications
    for sample in data:
        x = sample[:4]
        yd = float(sample[4])
        a.feedForward( x )
        if a.errorCorrection( yd, x ):
            count = count + 1
    print( "The number correct for this epoch is ", count/150 )
    print( "" )