import tsp_with_nn
import time
import tsplib95
from random import seed as randSeed

def printMatrix(matrix,n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end='\t')
        print()

def tspLibLoader(problem: str):
    tspProblem = tsplib95.parse(problem)
    n = tspProblem.dimension
    dists = [[0] * n for _ in range(n)]
    for i, u in enumerate(tspProblem.get_nodes()):
        for j, v in enumerate(tspProblem.get_nodes()):
            if i != j:
                dists[i][j] = tspProblem.get_weight(u, v)

    return [n,dists]

def testFunction(tspFileString,seed):
    randSeed(seed)
    dists = tspLibLoader(tspFileString)

    start = time.perf_counter()
    answer = tsp_with_nn.nearestNeighbour(dists[0],dists[1])
    end = time.perf_counter()


    return {
       "cost":answer[0],
        "duration": end - start,
        "tour": answer[1]
    } 