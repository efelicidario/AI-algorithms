###############################################
# Edmund Felicidario
# Propositional Logic Forward Chaining: A better approach
# CMPS 3560 - Artificial Intelligence
# 22 February 2022
###############################################


# Function def starts here
def PLFC( KB, DB, q ):

    count = [] # A null list
    for i in KB:
        ante, cons = i
        count.append(len(ante))
        
    inferred = []
        

    while DB: # While there is stuff in DB
        p = DB.pop(0)
        if p == q: # If this is the goal
            return True # ... quit and return true
        if p not in inferred:
            # inferred[p] <- true
            inferred.append( p ) # ... assert it
            for c in range(0,len(KB)): # For each rule
                ante, cons = KB[c]
                if p in ante:
                    # decrement count[c]
                    count[c] -= 1
                    # if count[c] is zero
                    if count[c] == 0:
                        # Otherwise push the consequent into DB
                        DB.append( cons )
    return False

KB = ( (["a"],"b"), (["b"],"a"), (["b"], "d") )
DB = [ "a", "e" ]
goal = "a"

print("")
print( PLFC(KB,DB,goal) )
