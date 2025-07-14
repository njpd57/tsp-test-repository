import tsplib95
import BruteForce
import Branch_and_Bound
import SimulatedAnnealing
import time
import numpy as np

def tspLibLoader(problem: str):
    tspProblem = tsplib95.parse(problem)
    n = tspProblem.dimension

    dists = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dists[i][j] = dists[j][i] = tspProblem.get_weight(start=i+1,end=j+1)
            pass

    return [n,dists]



def timer():
    i = 0
    while True:
        time.sleep(1)
        print(f"{i} Segundos.")
        i+=1



def testFunctionBruteForce(tspFileString):
    dists = tspLibLoader(tspFileString)

    start = time.perf_counter()
    result = BruteForce.brute_force(dists[1],dists[0])
    end = time.perf_counter()

    return {
       "cost":int(result[0]),
        "duration": end - start,
        "tour": result[1]
    } 

def testFunctionBranchAndBound(tspFileString):
    dists = tspLibLoader(tspFileString)

    matrix = np.array(dists[1],dtype='int16')

    start = time.perf_counter()
    result = Branch_and_Bound.main_loop(matrix,dists[0])
    end = time.perf_counter()

    return {
      "cost":int(result[0]),
        "duration": end - start,
        "tour": result[1]
    } 


def testFunctionSimulatedAnnealing(tspFileString,
                                   INITIAL_ROUTE = [],
                                    INITIAL_LEN = -1,
                                   AGES=50,
                                   COOLING_FACTOR = 0.90,
                                   START_TEMPERATURE = 1000,
                                   #END_TEMPERATURE = 10**-5,
                                   END_TEMPERATURE = 0.1
                                   ):
    dists = tspLibLoader(tspFileString)

    matrix = np.array(dists[1],dtype='int16')

    start = time.perf_counter()
    result = SimulatedAnnealing.mainFunction(matrix,dists[0],
                                             AGES=AGES,
                                             A=COOLING_FACTOR,
                                             END_TEMPERATURE=END_TEMPERATURE,
                                             T0=START_TEMPERATURE,
                                             INITIAL_ROUTE=INITIAL_ROUTE,
                                             INITIAL_LEN=INITIAL_LEN)
    end = time.perf_counter()

    return {
      "cost":int(result[0]),
        "duration": end - start,
        "tour": result[1]
    }
