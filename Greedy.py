import random
import math

class Comuna:
    def __init__(self,id,costo,vecinos,uso):
        self.id = id
        self.costo = costo
        self.vecinos = vecinos
        self.uso = uso   

def cargarDatos():
    comunas = [Comuna(2,1,[4,5],0)]
    comunas.append(Comuna(3,1.5,[5,27,29],0))
    comunas.append(Comuna(4,1.2,[2,25,26,28],0))
    comunas.append(Comuna(5,2,[2,3,28,29],0))
    comunas.append(Comuna(6,3,[7,9,15,24,27],0))
    comunas.append(Comuna(7,2,[6,8,9,10,15],0))
    comunas.append(Comuna(8,1,[7,10],0))
    comunas.append(Comuna(9,1,[6,7],0))
    comunas.append(Comuna(10,3,[7,8,15,33],0))
    comunas.append(Comuna(11,4,[12,16,17,24,25],0))
    comunas.append(Comuna(12,3,[11,13,15],0))
    comunas.append(Comuna(13,3,[12,15,17,33,35],0))
    comunas.append(Comuna(14,2,[16,17,30,31,37],0))
    comunas.append(Comuna(15,2.5,[6,7,10,12,13],0))
    comunas.append(Comuna(16,1.5,[11,14,17,30],0))
    comunas.append(Comuna(17,2,[11,13,14,16,33,35],0))
    comunas.append(Comuna(18,2,[20,34],0))
    comunas.append(Comuna(19,3,[21,22,34],0))
    comunas.append(Comuna(20,2,[18,21,34],0))
    comunas.append(Comuna(21,2,[19,20,34],0))
    comunas.append(Comuna(22,3,[19,23],0))
    comunas.append(Comuna(23,2,[22],0))
    comunas.append(Comuna(24,3,[6,11,15,25,26,27,28],0))
    comunas.append(Comuna(25,3,[11,24,26],0))
    comunas.append(Comuna(26,1,[4,24,25,28],0))
    comunas.append(Comuna(27,2.5,[3,6,28,29],0))
    comunas.append(Comuna(28,2,[4,5,24,26,27,29],0))
    comunas.append(Comuna(29,3.5,[3,5,27,28],0))
    comunas.append(Comuna(30,2,[14,16,31,34,36,37],0))
    comunas.append(Comuna(31,1.5,[14,35,38],0))
    comunas.append(Comuna(33,2,[10,13,15,17,35],0))
    comunas.append(Comuna(34,3,[18,19,20,21,30,36],0))
    comunas.append(Comuna(35,3.5,[17,31,33],0))
    comunas.append(Comuna(36,2,[30,34,38],0))
    comunas.append(Comuna(37,2.5,[14,30],0))
    comunas.append(Comuna(38,1.5,[30,31,36],0))
    return comunas

def algorythm(universe,subSets,costs):

    #set used to save the selected subsets
    selected =set()
    #set that represent the elements that are not used yet
    notUsed = subSets

    while notUsed:
        bestsubset = None
        bestRatio = 0
        for Set in subSets:
            
            
        

#universe: 2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38
#subsets: [4,5],[5,27,29],[2,25,26,28],[2,3,28,29],[7,9,15,24,27],[6,8,9,10,15],[7,10],[6,7],[7,8,15,33],[12,16,17,24,25],[11,13,15],[12,15,17,33,35],[16,17,30,31,37],[6,7,10,12,13],[11,14,17,30],[11,13,14,16,33,35],[20,34],[21,22,34],[18,21,34],[19,20,34],[19,23],[22],[6,11,15,25,26,27,28],[11,24,26],[4,24,25,28],[3,6,28,29],[4,5,24,26,27,29],[3,5,27,28],[14,16,31,34,36,37],[14,35,38],[10,13,15,17,35],[18,19,20,21,30,36],[17,31,33],[30,34,38],[14,30],[30,31,36]
#costs: 1,1.5,1.2,2,3,2,1,1,3,4,3,3,2,2.5,1.5,2,2,3,2,2,3,2,3,3,1,2.5,2,3.5,2,1.5,2,3,3.5,2,2.5,1.5


#id de cada comuna
universe = set(2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,33,34,35,36,37,38)
#subsets del universo
subSets = set([4,5],[5,27,29],[2,25,26,28],[2,3,28,29],[7,9,15,24,27],[6,8,9,10,15],[7,10],[6,7],[7,8,15,33],[12,16,17,24,25],[11,13,15],[12,15,17,33,35],[16,17,30,31,37],[6,7,10,12,13],[11,14,17,30],[11,13,14,16,33,35],[20,34],[21,22,34],[18,21,34],[19,20,34],[19,23],[22],[6,11,15,25,26,27,28],[11,24,26],[4,24,25,28],[3,6,28,29],[4,5,24,26,27,29],[3,5,27,28],[14,16,31,34,36,37],[14,35,38],[10,13,15,17,35],[18,19,20,21,30,36],[17,31,33],[30,34,38],[14,30],[30,31,36])
#costos¿
costs = set(1,1.5,1.2,2,3,2,1,1,3,4,3,3,2,2.5,1.5,2,2,3,2,2,3,2,3,3,1,2.5,2,3.5,2,1.5,2,3,3.5,2,2.5,1.5)

print(algorythm(universe,subSets,costs))

    
    

    
    
    


#comunas = cargarDatos()
#print(len(universe))
#print(len(comunas))