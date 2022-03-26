import numpy as np

##WORK IN PROGRESS

"""
#Compute the overlap with the current input for each column
for c in columns:
    overlap(c) = 0
    for s in connectedSynapses(c):
        overlap(c) = overlap(c) + input(t, s.sourceInput)
        overlap(c) = overlap(c) * boost(c)

#Compute the winning columns after inhibition
for c in columns:
    minLocalActivity = kthScore(neighbors(c), numActiveColumnsPerInhArea)
    if overlap(c) > stimulusThreshold and overlap(c) >= minLocalActivity:
        activeColumns(t).append(c)

#Update synapse permanences and internal variables
for c in activeColumns(t):
    for s in potentialSynapses(c):
        if active(s):
            s.permanence += synPermActiveInc
            s.permanence = min(1.0, s.permanence)
        else:
            s.permanence = synPermInactiveDec
            s.permanence = max(0.0, s.permanence)
for c in columns:
    activeDutyCycle(c) = updateActiveDutyCycle(c)
    activeDutyCycleNeighbors = mean(activeDutyCycle(neighbors(c))
    boost(c) = boostFunction(activeDutyCycle(c), activeDutyCycleNeighbors)
    overlapDutyCycle(c) = updateOverlapDutyCycle(c)
    if overlapDutyCycle(c) < minDutyCycle(c):
        increasePermanences(c, 0.1*connectedPerm)
inhibitionRadius = averageReceptiveFieldSize()  
              
"""