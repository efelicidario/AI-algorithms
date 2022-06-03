
############################################################################

# Edmund Felicidario
# Lab 9 - Mamdani Inference in Python
# CMPS 3560 - Artificial Intelligence
# 29 March 2022

############################################################################

# Appendix A. Solution to Problem Setup
# Water. Has three linguistic values operating on the same domain,
# which is a function of the liters of water to bring on the hike: 
bottle = [ (0.0, 0.2), (0.5, 0.5), (1.0, 1.0), (0.5, 1.5), (0.0, 2.0) ]
none = [ (1.0, 0), (0.75, 0.1), (0.50, 0.2), (0.25, 0.3), (0.0, 0.4) ]
alot = [ (0.0, 1.00), (0.25, 1.25), (0.5, 1.50), (0.75, 1.75), (1.0, 2.00) ]

# Temperature. Has two linguistic values operating on the same
# domain, which is a function of the temperature: Moderate and Hot.
moderate = [ (0.0, 52), (0.5, 61), (1.0, 69), (0.5, 75), (0.0, 80) ]
hot = [ (0.0, 85), (0.5, 86), (1.0, 114), (0.5, 95), (0.0, 85) ]

# Distance. Has three linguistic values operating on the same domain,
# which is a function of the distance to travel: Short, Medium, Long.
short = [ (1.0, 0.0), (0.8, 0.3), (0.7, 0.5), (0.5, 0.7), (0.0, 1.0) ]
medium = [ (0.0, 0.4), (0.5, 0.7), (1.0, 1.0), (0.5, 1.3), (0.0, 1.6) ]
long = [ (0.0, 0.25), (0.5, 1.0), (0.7, 2.0), (0.8, 5.5), (1.0, 10.0) ]


# Appendix B. Membership function
def membership(inputValue, fuzzySet):
    closestValue = 1000000
    updatedValue = fuzzySet[0][0]
    
    for p in fuzzySet:
        fuzzyValue, crisp = p
        
        if crisp == inputValue:
            return fuzzyValue
        
        distance = abs(crisp - inputValue)
        if distance < closestValue:
            closestValue = distance
            updatedValue = fuzzyValue
    return updatedValue

# Inverse membership function
def inverseMembership(inputValue, fuzzySet):
    closestValue = 1000000
    updatedValue = fuzzySet[0][1]
    
    for p in fuzzySet:
        fuzzyValue, crisp = p
        
        if fuzzyValue == inputValue:
            return crisp
        
        distance = abs(fuzzyValue - inputValue)
        if distance < closestValue:
            closestValue = distance
            updatedValue = crisp
    return updatedValue


# Test case
# Temperature
T = 80
# Distance
L = 2

# Rule 1
rule1ant = membership( T, none )
rule1cons = inverseMembership( rule1ant, none )

# Rule 2
rule2ant = min( membership(T,moderate), membership(L,medium) )
rule2cons = inverseMembership( rule2ant, bottle )

# Rule 3
rule3ant = max( membership(T,hot), membership(L,long) )
rule3cons = inverseMembership( rule3ant, alot )

numerator = 0 # Numerator of Eq. 4.18
denominator = 0 # Denominator of Eq. 4.18
# For x from 0 to 2 in steps of 0.1: # This is x = a to b in Eq. 4.18
for x in range(0, 3):
    # Evaluate the summation of Equation 4.18
    u = rule1ant * membership(x,none) + rule2ant * membership(x,bottle) + rule3ant * membership(x,alot)
    numerator = numerator + u * x
    denominator = denominator + u
Recommendation = numerator / denominator


print(Recommendation)