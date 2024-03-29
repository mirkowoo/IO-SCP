import os

from simulatedAnnealing import simulatedAnnealing

#universe id's
universe = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38]
#universe subsets
subSets = [[2,4,5],[3,5,27,29],[4,2,25,26,28],[5,2,3,28,29],[6,7,9,15,24,27],[7,6,8,9,10,15],[8,7,10],[9,6,7],[10,7,8,15,33],
           [11,12,15,16,17,24,25],[12,11,13,15],[13,12,15,17,33],[14,16,17,30,31,37],[15,6,7,10,11,12,13,24,33],[16,11,14,17,30],[17,11,13,14,16,33,35],
           [18,20,34],[19,21,22,34],[20,18,21,34],[21,19,20,34],[22,19,23],[23,22],[24,6,11,15,25,26,28],[25,4,11,24,26],[26,4,24,25,28],[27,3,6,28,29],[28,4,5,24,26,27,29],[29,3,5,27,28],[30,14,16,34,36,37,38],[31,14,35,38],
           [33,10,13,15,17,35],[34,18,19,20,21,30,36],[35,17,31,33],[36,30,34,38],[37,14,30],[38,30,31,36]]
#a dictionary of subsets based on array pos
dictionarySubSets = {0: [2,4,5],1: [3,5,27,29],2: [4,2,25,26,28],3:[5,2,3,28,29],4:[6,7,9,15,24,27],5:[7,6,8,9,10,15],6:[8,7,10],7:[9,6,7],8:[10,7,8,15,33],
           9: [11,12,15,16,17,24,25],10: [12,11,13,15],11:[13,12,15,17,33],12: [14,16,17,30,31,37],13: [15,6,7,10,11,12,13,24,33],14: [16,11,14,17,30],15: [17,11,13,14,16,33,35],
           16: [18,20,34],17: [19,21,22,34],18: [20,18,21,34],19: [21,19,20,34],20: [22,19,23],21: [23,22],22: [24,6,11,15,25,26,28],23: [25,4,11,24,26],24: [26,4,24,25,28],25: [27,3,6,28,29],26: [28,4,5,24,26,27,29],27: [29,3,5,27,28],28: [30,14,16,34,36,37,38],29: [31,14,35,38],
           30: [33,10,13,15,17,35],31: [34,18,19,20,21,30,36],32: [35,17,31,33],33:[36,30,34,38],34:[37,14,30],36:[38,30,31,36]}
#costs array for every universe object
costs = [1,1.5,1.2,2,3,2,1,1,3,4,3,3,2,2.5,1.5,2,2,3,2,2,3,2,3,3,1,2.5,2,3.5,2,1.5,2,3,3.5,2,2.5,1.5]


os.system('cls')

simulatedAnnealing(universe,subSets,costs,dictionarySubSets)




