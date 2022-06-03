###############################################
# Edmund Felicidario
# Certainty Factors
# CMPS 3560 - Artificial Intelligence
# 22 March 2022
###############################################


def isInDB( literal, DB ):
    for p in DB:
        lit, cf = p
        if lit == literal:
            return True
    
def getCF( literal, DB ):
    for p in DB:
        lit, cf = p
        if lit == literal:
            return cf

DB = [ ("A", 1.00), 
      ("B", 0.70), 
      ("C", 0.75), 
      ("D", 0.80), 
      ("E", 0.50), 
      ("M", -1.0) ] # ... [-1,1]
KB = [ (("Y", "D"), "Z", 0.7), 
      (("A", "B", "E"), "Y", 0.95), 
      (("A"), "X", 1.0), 
      (("C"), "L", 1.0), 
      (("L", "M"), "N", 1.0) ]

count = 1 # Number of times we've iterated over the whole rule set
changes = True

while changes:
    changes = False # Set the flag that there have been no changes to false
    
    print( "Starting iteration " + str(count))
    
    for p in KB: # For each rule in the set of rules...
        antecedent, consequent, cf = p
        
        print( "Consdier a rule where: " )
        print( antecedent )
        print( "implies: " )
        print( consequent )
        print( " with CF" )
        print( cf )
        
        # Determine if all literals in antecedent are also in KB
        satisfied = True # Flag for entire premise being satisfied
        for q in antecedent: # A and B -> C ... ["A", "B"]
            # q will be a string
            # KB is a list of strings
            if not isInDB(q, DB):
                satisfied = False # Flag as false, all clauses must be inferred
                
        # If it passes the above, then antecedent is satisfied
        # ...and consequent should be entailed
        if satisfied and not isInDB( consequent, DB): # TODO
            tmp = 10000
            for r in antecedent:
                if getCF(r, DB) < tmp:
                    tmp = getCF(r, DB)
            DB.append( (consequent, cf*tmp) )
            print ( DB )
            changes = True
            print( "Antecedent is in DB, consequent is implied, DB is now: ")
            print(DB)
        elif satisfied and isInDB( consequent, DB ):
            print( "Consequent is implied, but was already in DB" )
        else:
            print( "Consequent is not implied" )
            
    count = count + 1
    
print( "No more changes. DB is: " )
print(DB)