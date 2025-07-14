import heldKarp
import time
import tsplib95

def printMatrix(matrix,n):
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end='\t')
        print()
def tspLibLoader(problem: str):
    tspProblem = tsplib95.parse(problem)
    n = tspProblem.dimension

    dists = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dists[i][j] = dists[j][i] = tspProblem.get_weight(start=i+1,end=j+1)
            pass

    return dists


def testFunction(tspFileString):
    dists = tspLibLoader(tspFileString)

    start = time.perf_counter()
    answer = heldKarp.held_karp(dists)
    end = time.perf_counter()

    return {
        "cost":answer[0],
        "duration": end - start,
        "tour": answer[1]
    } 

    
#print(testFunction("eil20.tsp"))