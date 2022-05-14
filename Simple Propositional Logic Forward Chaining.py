###############################################
# Edmund Felicidario
# Simple Propositional Logic Forward Chaining
# CMPS 3560 - Artificial Intelligence
# 8 February 2022
###############################################

# Knowledge Base
KB = [ 
      (["papers"],"verbal"), (["manuals"],"verbal"), (["documents"],"verbal"), (["textbooks"],"verbal"), 
      (["pictures"],"visual"), (["illustrations"],"visual"), (["photographs"],"visual"), (["diagrams"],"visual"), 
      (["machines"],"physical object"), (["buildings"],"physical object"), (["tools"],"physical object"), 
      (["numbers"],"symbolic"), (["formulas"],"symbolic"), (["computer programs"],"symbolic"),
      (["lecturing"],"oral"), (["advising"],"oral"), (["counselling"],"oral"),
      (["building"],"hands-on"), (["repairing"],"hands-on"), (["troubleshooting"],"hands-on"), ([""],""),
      (["writing"],"documented"), (["typing"],"documented"), (["drawing"],"documented"),
      (["evaluating"],"analytical"), (["reasoning"],"analytical"), (["investigating"],"analytical"),
      (["physical object", "hands-on", "required"],"workshop"),
      (["symbolic", "analytical", "required"], "lecture-tutorial"),
      (["visual", "documented", "not required"], "videocasette"), 
      (["visual", "oral", "required"], "lecture-tutorial"), 
      (["verbal", "analytical", "required"], "lecture-tutorial"), 
      (["verbal", "oral", "required"], "role-play exercises") 
      ]

# Database
DB = [] # A set of facts

print("")
print( "What is the environment? " )
p = input( "Enter: " )
DB.append(p)

print("")
print( "What is the job? " )
p = input( "Enter: " )
DB.append(p)

print("")
print( "Required or not required: " )
p = input( "Enter: " )
DB.append(p)

count = 1 # Number of times we've iterated over the whole rule set
changes = True

while changes:
    changes = False # Set the flag that there have been no changes to false
    
    
#    print( "Starting Iteration " + str(count))
    
    for p in KB: # For each rule in the set of rules...
        antecedent, consequent = p
        
#        print( "Consdier a rule where: " )
#        print( antecedent )
#        print( "implies: " )
#        print ( consequent )
        
        # Determine if all literals in antecedent are also in KB
        satisfied = True # Flag for entire premise being satisfied
        for q in antecedent:
            # q will be a string
            # KB is a list of strings
            if q not in DB:
                satisfied = False # Flag as false, all clauses must be inferred
                
        # If it passes the above, then antecedent is satisfied
        # ...and consequent should be entailed
        if satisfied and consequent not in DB:
            DB.append( consequent )
            changes = True
#            print( "Antecedent is in DB, consequent is implied, DB is now: ")
#            print(DB)
#        elif satisfied and consequent not in DB:
#            print( "Consequent is implied, but was already in DB" )
#        else:
#            print( "Consequent is not implied" )
            
    count = count + 1
    
print( "" )
print( "DB: ", DB )
print( "Based on the Medium, the answer is: ", )
print( DB[len(DB) - 1] )
print( "" )