
############################################################################

# Edmund Felicidario
# Lab 8 - Monotonic Inference
# CMPS 3560 - Artificial Intelligence
# 22 March 2022

############################################################################

# Task 1 - Problem Setup

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

############################################################################

# Task 2 - Implementing Fuzzy Membership

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

print("If distance on the walk is long, then the water bottle is none.")
print(inverseMembership(membership(13, short), none))
print(inverseMembership(membership(75, hot), bottle))
print("")
