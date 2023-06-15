import time
import os
import math
import random

import numpy as np
from GreedySCP import setCoveringProblem
#function that calculates the cost of the given solution
def costCalculation(s,costs):
    cost = 0
    print(len(costs),' , ',len(s))
    for i in range(len(s)):
        if s[i] == 1:
          cost += costs[i]
    return cost

#ending criteria function (rn the program stops at "20 degrees", but can be changed for further improvement)
def endingCriteria(t):
    if t <= 20:
        return True
    else:
        return False

#function to verify a given solution      
def verifySolution(s,subSets,dictionarySubSets):
  
  notUsed = subSets
  
  for i in range(len(s)):
    for x in notUsed:
      if s[i] == 1:
        notUsed.remove([dictionarySubSets[x][0]])
        
  if not notUsed:   
    return False
  return False
  
#this function realizes the bitflip movement 
def bitflip(s,subSets,cost,dictionarySubSets):
  sCopy = s.copy()
  bestCost = 0
  initialCost = costCalculation(s)
  while bestCost < initialCost:
    
    for i in range(len(sCopy)):
      if sCopy[i] == 1: sCopy[i] = 0
      else: sCopy[i] = 1
      
      if verifySolution(sCopy) == True:
        bestCost = costCalculation(sCopy,cost)
        
          
  return sCopy

def bestSolution(s,sMas):
    if (s[0] > sMas[0]):
      return s
    else:
      return sMas

#This is the cooling function for the variable 't', it is subject to changes for testing and optimization purposes.
def exponentialCooling(t,iteracion):
    coolingRate = 0.4
    return t * (coolingRate ** iteracion)

#simulated annealing function
def simulatedAnnealing(universe,subSets,costs,dictionarySubSets):
    x = time.time()
    print("largo universo:",len(universe),"y largo costos: ",len(costs),"largo suSets: ",len(subSets))
    s = sMas = setCoveringProblem(universe,subSets,costs)
    print("largo universo:",len(universe),"y largo costos: ",len(costs),"largo suSets: ",len(subSets))
    bestCost = costCalculation(s,costs)
    print("Initial solution:")
    print(s)
    print("Cost: $",bestCost)
    #Temperature values (can change to further improvement)
    tO = 1000 
    t = 1000
    
    iteration = 0
    while not endingCriteria(t):
        #siguiente vecino
        for i in range(len(universe)):
            sSiguiente = bitflip(s,subSets,costs,dictionarySubSets)
            difS = s[0] - sSiguiente[0]

            if difS < 0:
                s = sSiguiente
            else:
                #función de aceptación por probabilidad
                p = math.e ** -difS/t
                if random.randrange(0,1) < p:
                    s = sSiguiente
            sMas = bestSolution(s,sMas)
            iteracion+= 1
            t = exponentialCooling(t,iteracion)
    return sMas

os.system('cls')