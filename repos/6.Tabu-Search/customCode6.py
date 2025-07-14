import tsplib95
import TS
import random
import time
def tspLibLoader(problem: str):
    tspProblem = tsplib95.parse(problem)

    #For this repo i need to get only de x and y values.
    x = []
    y = []

    for i in range(1,tspProblem.dimension+1):
        node =tspProblem.node_coords[i]
        x.append(node[0])
        y.append(node[1])

    return [x,y]

def testFunction(tspFileString,iterations=30,seed=0):
    random.seed(seed)
    x,y = tspLibLoader(tspFileString)

    start = time.perf_counter()
    result = TS.cleanMain(x,y,iterations)    
    end = time.perf_counter()
    
    return {
       "cost":result['best length'],
        "duration": end - start,
        "tour": result['best path'],
        "convergence": result['convergence iteration']
    }