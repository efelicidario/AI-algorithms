#Genetic Algorithms
from random import random
from random import seed
import math

seed(random())

def select( pop, fitness ):
    # Select a fit individual???
    # Convert each fitness to a prob
    probs = [ fitness[i] / sum(fitness) for i in range(len(fitness)) ]
    # For each indiviual, select based on rand()???
    for i in range(0,len(pop)):
        if random() <= probs[i]:
            return pop[i]
    return pop[0] # ???

def crossover( candidate1, candidate2, M ):
    offspring1 = candidate1[0:int(M/2):M] + candidate2[int(M/2):M]
    offspring2 = candidate2[0:int(M/2):M] + candidate1[int(M/2):M]
    return offspring1, offspring2

def mutate( indiv, pM ):
    ## CHANGE
    if random() <= pM:
        index = math.floor( len(indiv) * random() )
        # Generate a random index
        if indiv[index] == 0:
            indiv[index] = 1
        else:
            indiv[index] = 0

# 11111 11111 11111 11111 fitness 20
# 01010 11111 00000 00000 fitness 6

#generation p, totally random
M = 10 # Genome length
N = 8 # Size of the *initial* generation
O = 100 # Iterations
pC = 0.8 # Some random chance / 100%!
pM = 0.05

# Ternary operator in Python
# VALUE_IF_TRUE of EXPR else VALUE_IF_FALSE
p = []
for j in range(N):
    p.append( [ 1 if random() > 0.5 else 0 for i in range(M) ] )

#Simulation (set number of iterations?)
for j in range(O):
    #geneartion pPlusOne to null
    pPlusOne = []
    # Calculate the fitness for each indiv. in p
    fitness = []
    for k in range(0, len(p)): # For each indiv. ...
        fitness.append( sum( p[k] ) )
    #for each indiv. candidate1 in p:
    for candidate1 in p:
        if random() <= pC:
            # candidate1 elected to crossover
            candidate2 = select( p, fitness )
            offspring1, offspring2 = crossover( candidate1, candidate2, M )
            mutate( offspring1, pM )
            mutate( offspring2, pM )
            pPlusOne.append( offspring1 )
            pPlusOne.append( offspring2 )
    p = pPlusOne
    print( "Geneartion ", j )
    print( fitness )