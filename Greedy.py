import time
import os
def algorythm(universe,subSets,costs):

    #set used to save the selected subsets
    selected = [[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]]
    #sets that represent the elements that are not used yet
    notUsed = universe
    subSetsCopy = subSets
    costCopy = costs
    
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
            cost = costCopy[i]
            costRatio = cost / len(subSets)
            
            if costRatio > bestRatio:
                for x in subSetsCopy[i]:
                    if x in notUsed:
                        bestSubset = subSetsCopy[i]
                        bestRatio = costRatio
                        bestPos = i
                    else:
                        break
        #save the best subset of the iteration
        selected[bestPos]=[1,bestSubset]
        #selected.append(bestSubset[0])
        #add the cost of the subset to the total
        totalCost += costs[bestPos]
        print("best subset: ",bestSubset)
        print("cost of the subset: $",costs[bestPos])
        print("total cost rn: $",totalCost)
        print()
        time.sleep(1)
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

#universe: 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38
#subsets: [4,5],[5,27,29],[2,25,26,28],[2,3,28,29],[7,9,15,24,27],[6,8,9,10,15],[7,10],[6,7],[7,8,15,33],[12,16,17,24,25],[11,13,15],[12,15,17,33,35],[16,17,30,31,37],[6,7,10,12,13],[11,14,17,30],[11,13,14,16,33,35],[20,34],[21,22,34],[18,21,34],[19,20,34],[19,23],[22],[6,11,15,25,26,27,28],[11,24,26],[4,24,25,28],[3,6,28,29],[4,5,24,26,27,29],[3,5,27,28],[14,16,31,34,36,37],[14,35,38],[10,13,15,17,35],[18,19,20,21,30,36],[17,31,33],[30,34,38],[14,30],[30,31,36]
#costs: 1,1.5,1.2,2,3,2,1,1,3,4,3,3,2,2.5,1.5,2,2,3,2,2,3,2,3,3,1,2.5,2,3.5,2,1.5,2,3,3.5,2,2.5,1.5

#id de cada comuna
universe = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38]
#subsets del universo
subSets = [[2,4,5],[3,5,27,29],[4,2,25,26,28],[5,2,3,28,29],[6,7,9,15,24,27],[7,6,8,9,10,15],[8,7,10],[9,6,7],[10,7,8,15,33],
           [11,12,15,16,17,24,25],[12,11,13,15],[13,12,15,17,33],[14,16,17,30,31,37],[15,6,7,10,11,12,13,24,33],[16,11,14,17,30],[17,11,13,14,16,33,35],
           [18,20,34],[19,21,22,34],[20,18,21,34],[21,19,20,34],[22,19,23],[23,22],[24,6,11,15,25,26,28],[25,4,11,24,26],[26,4,24,25,28],[27,3,6,28,29],[28,4,5,24,26,27,29],[29,3,5,27,28],[30,14,16,34,36,37,38],[31,14,35,38],
           [33,10,13,15,17,35],[34,18,19,20,21,30,36],[35,17,31,33],[36,30,34,38],[37,14,30],[38,30,31,36]]
'''
subSets = [{2,4,5},{3,5,27,29},{4,2,25,26,28},{5,2,3,28,29},{6,7,9,15,24,27},{7,6,8,9,10,15},{8,7,10},{9,6,7},{10,7,8,15,33},
           {11,12,15,16,17,24,25},{12,11,13,15},{13,12,15,17,33},{14,16,17,30,31,37},{15,6,7,10,11,12,13,24,33},{16,11,14,17,30},{17,11,13,14,16,33,35},
           {18,20,34},{19,21,22,34},{20,18,21,34},{21,19,20,34},{22,19,23},{23,22},{24,6,11,15,25,26,28},{25,4,11,24,26},{26,4,24,25,28},{27,3,6,28,29},{28,4,5,24,26,27,29},{29,3,5,27,28},{30,14,16,34,36,37,38},{31,14,35,38},
           {33,10,13,15,17,35},{34,18,19,20,21,30,36},{35,17,31,33},{36,30,34,38},{37,14,30},{38,30,31,36}]
'''
#[{4,5},{5,27,29},{2,25,26,28},{2,3,28,29},{7,9,15,24,27},{6,8,9,10,15},{7,10},{6,7},{7,8,15,33},{12,16,17,24,25},{11,13,15},{12,15,17,33,35},{16,17,30,31,37},{6,7,10,12,13},{11,14,17,30},{11,13,14,16,33,35},{20,34},{21,22,34},{18,21,34},{19,20,34},{19,23},{22},{6,11,15,25,26,27,28},{11,24,26},{4,24,25,28},{3,6,28,29},{4,5,24,26,27,29},{3,5,27,28},{14,16,31,34,36,37},{14,35,38},{10,13,15,17,35},{18,19,20,21,30,36},{17,31,33},{30,34,38},{14,30},{30,31,36}]
#costos
costs = [1,1.5,1.2,2,3,2,1,1,3,4,3,3,2,2.5,1.5,2,2,3,2,2,3,2,3,3,1,2.5,2,3.5,2,1.5,2,3,3.5,2,2.5,1.5]
#dictionary of costs
'''
costs = {(0): 1,(1):1.5,(2): 1.2,(3):2, 4:3, 5:2, 6:1, 7:1, 8:3,
         9:4, 10:3, 11:3, 12:2, 13:2.5, 14:1.5, 15:2,
         16:2,17:3,18:2,19:2,20:3,21:2,22:3,23:3,
         24:1,25:2.5,26:2,27:3.5,28:2,29:1.5,
         30:2,31:3,32:3.5,33:2,34:2.5,35:1.5}
'''
'''
costs = {frozenset({2,4,5}): 1,frozenset({3,5,27,29}):1.5,frozenset({4,2,25,26,28}): 1.2,frozenset({5,2,3,28,29}):2,frozenset({6,7,9,15,24,27}):3,frozenset({7,6,8,9,10,15}):2,frozenset({8,7,10}):1,frozenset({9,6,7}):1,frozenset({10,7,8,15,33}):3,
         frozenset({11,12,15,16,17,24,25}):4,frozenset({12,11,13,15}):3,frozenset({13,12,15,17,33}):3,frozenset({14,16,17,30,31,37}):2,frozenset({15,6,7,10,11,12,13,24,33}):2.5,frozenset({16,11,14,17,30}):1.5,frozenset({17,11,13,14,16,33,35}):2,
         frozenset({18,20,34}):2,frozenset({19,21,22,34}):3,frozenset({20,18,21,34}):2,frozenset({21,19,20,34}):2,frozenset({22,19,23}):3,frozenset({23,22}):2,frozenset({24,6,11,15,25,26,28}):3,frozenset({25,4,11,24,26}):3,
         frozenset({26,4,24,25,28}):1,frozenset({27,3,6,28,29}):2.5,frozenset({28,4,5,24,26,27,29}):2,frozenset({29,3,5,27,28}):3.5,frozenset({30,14,16,34,36,37,38}):2,frozenset({31,14,35,38}):1.5,
         frozenset({33,10,13,15,17,35}):2,frozenset({34,18,19,20,21,30,36}):3,frozenset({35,17,31,33}):3.5,frozenset({36,30,34,38}):2,frozenset({37,14,30}):2.5,frozenset({38,30,31,36}):1.5}
'''
'''
{frozenset({4,5}): 1,frozenset({5,27,29}):1.5,frozenset({2,25,26,28}): 1.2,frozenset({2,3,28,29}):2,frozenset({7,9,15,24,27}):3,frozenset({6,8,9,10,15}):2,frozenset({7,10}):1,frozenset({6,7}):1,frozenset({7,8,15,33}):3,frozenset({12,16,17,24,25}):4,frozenset({11,13,15}):3,frozenset({12,15,17,33,35}):3
 ,frozenset({16,17,30,31,37}):2,frozenset({6,7,10,12,13}):2.5,frozenset({11,14,17,30}):1.5,frozenset({11,13,14,16,33,35}):2,frozenset({20,34}):2,frozenset({21,22,34}):3
 ,frozenset({18,21,34}):2,frozenset({19,20,34}):2,frozenset({19,23}):3,frozenset({22}):2,frozenset({6,11,15,25,26,27,28}):3,frozenset({11,24,26}):3,frozenset({4,24,25,28}):1,frozenset({3,6,28,29}):2.5,frozenset({4,5,24,26,27,29}):2,frozenset({3,5,27,28}):3.5,frozenset({14,16,31,34,36,37}):2
 ,frozenset({14,35,38}):1.5,frozenset({10,13,15,17,35}):2,frozenset({18,19,20,21,30,36}):3,frozenset({17,31,33}):3.5,frozenset({30,34,38}):2,frozenset({14,30}):2.5,frozenset({30,31,36}):1.5}
'''
bestSets= (algorythm(universe,subSets,costs))

#os.system('cls')

print("Best places \n",bestSets)
#comunas = cargarDatos()
#print(len(universe))
#print(len(comunas))