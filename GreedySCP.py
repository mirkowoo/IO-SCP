import time


def setCoveringProblem(universe,subSets,costs):

    #set used to save the selected subsets
    selected = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    #sets that represent the elements that are not used yet
    notUsed = universe.copy()
    subSetsCopy = subSets.copy()
    costCopy = costs.copy()
    
    #value to store the total cost
    totalCost = 0
    
    #veryfies if notUsed is empty or not, so the cycle can run until then
    while notUsed:
        #variables definition
        bestSubset = None
        bestRatio = -0.1
        bestPos = -1
        print("largo notUsed: ",len(notUsed))
        print(notUsed)
        for i in range(len(subSetsCopy)):
            #print(subSetsCopy[i])
            localCost = costCopy[i]
            costRatio = localCost/ len(subSets)
            
            if costRatio > bestRatio:
                for x in subSetsCopy[i]:
                    if x in notUsed:
                        bestSubset = subSetsCopy[i]
                        bestRatio = costRatio
                        bestPos = i
                    else:
                        break
        #save the best subset of the iteration
        selected[bestPos]=1
        #selected.append(bestSubset[0])
        #add the cost of the subset to the total
        totalCost += costs[bestPos]
        '''
        print("best subset: ",bestSubset)
        print("cost of the subset: $",costs[bestPos])
        print("total cost rn: $",totalCost)
        print()
        time.sleep(1)
        '''
        #removing the values from te arrays to disregard them in the next iterations
        for i in range(len(bestSubset)):
            for x in notUsed:
                if(x == bestSubset[i]):
                    notUsed.remove(bestSubset[i])
                    break

            for x in range(len(subSetsCopy)):
                if(subSetsCopy[x][0] == bestSubset[0]):
                    subSetsCopy.pop(x)
                    costCopy.pop(x)
                    break
    return selected