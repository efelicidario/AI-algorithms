###############################################
# Edmund Felicidario
# Simple Propositional Logic Backward Chaining
# CMPS 3560 - Artificial Intelligence
# 1 March 2022
###############################################

def BC( KB, DB, goal ):
    if goal in DB:
        return True
    else:
        for p in KB: # p = (["b"], "b")
            ante, cons = p
            # ante = ["b"]
            # cons = "c"
            if goal == cons: # This rule is the subgoal
                proven = 0
                
                for q in ante: # ante = ["b", "d"]
                    if BC( KB, DB, q ):
                        proven += 1
                        
                if proven == len(ante):
                    return True
                    
        return False

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
DB = [ "" ]
goal = ""

print("")
print( BC(KB, DB, goal) )
print("")
