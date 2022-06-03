import csv
import math
from random import random
from random import seed
# File name to load
file = 'iris_full_vector.csv'
seed(1)
# Open the file
with open(file, newline='') as csvfile:
    # Initialize data to a list of empty objects
    data = []
    # For each row in the file ...
    for row in csv.reader( csvfile, delimiter=',' ):
        # ...append the whole row as an object. 'row' is a 5 length vector.
        data.append(row)

nh = 4
no = 2

wh1 = [random() for i in range (nh)]
wh2 = [random() for i in range (nh)]
wo1 = [random() for i in range(no)]
wo2 = [random() for i in range(no)]
wo3 = [random() for i in range(no)]
thetah1 = random()
thetah2 = random()
thetao1 = random()
thetao2 = random()
thetao3 = random()


def feedForward( x, w, theta ):
    X = 0
    for i in range(0, len(w)):
        X = X + w[i] * float(x[i])
    X = X - theta # no changes
    # Activation function
    y = 1 / ( 1 + math.exp( -X ) ) #TODO
    return y

def errorCorrection( yd, y, x, w, theta ):
    
    delta = y * ( 1 - y ) * ( yd - y )
    
    for i in range(0, len(w)):
        w[i] = w[i] + alpha * float(x[i]) * delta
    theta = theta - alpha * delta
    
    return delta

# Backpropagation
def backProp( yd, y, x, w, theta, deltas, weights ):
    e = 0
    for i in range(0, len(deltas)):
        e = e + weights[i] * deltas[i]
        
    delta = y * ( 1 - y ) * e #??? Approximate with delta and W values
    
    for i in range(0, len(w)):
        w[i] = w[i] + alpha * float(x[i]) * delta
    theta = theta - alpha * delta
    
    return delta

alpha = 0.1

print( " ***** Starting epoch ***** " )
for epoch in range(0, 100):
    loss = 0 # number of correct classifications
    print( "***** This is epoch ", epoch )
    
    for sample in data:
        x = sample[:4]
        ydo1 = float(sample[4])
        ydo2 = float(sample[5])
        ydo3 = float(sample[6])
        
        # Feed Forward
        # H1
        yh1 = feedForward( x, wh1, thetah1 )
        # H2
        yh2 = feedForward( x, wh2, thetah2 )
        # 01
        outputHidden = ( yh1, yh2 )
        yo1 = feedForward( outputHidden, wo1, thetao1 )
        # 02
        yo2 = feedForward( outputHidden, wo2, thetao2 )
        # 03
        yo3 = feedForward( outputHidden, wo3, thetao3 )
        
        # ???
        lossSample = math.sqrt( (ydo1 - yo1)**2 + (ydo2 - yo2)**2 + (ydo3 - yo3)**2 )
        loss = loss + lossSample
        
        ### Backpropagation ###
        delta01 = errorCorrection( ydo1, yo1, outputHidden, wo1, thetao1 ) # error correction is for output
        delta02 = errorCorrection( ydo2, yo2, outputHidden, wo2, thetao2 ) # error correction is for output
        delta03 = errorCorrection( ydo3, yo3, outputHidden, wo3, thetao3 ) # error correction is for output
        deltaOutput = ( delta01, delta02, delta03 )
        
        deltaH1 = backProp( yh1, yh1, x, wh1, thetah1, deltaOutput, (wo1[0], wo2[0], wo3[0]) )
        deltaH2 = backProp( yh2, yh2, x, wh2, thetah2, deltaOutput, (wo1[1], wo2[1], wo3[1]) )
   
        print( "This sample's output is: " )
        print( (ydo1, ydo2, ydo3) )
        print( "The output of the network is: " )
        print( (yo1, yo2, yo3) )
        
    print( "The loss for this epoch is: ", loss )