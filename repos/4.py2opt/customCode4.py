from py2opt.solver import Solver
import tsplib95
import time

def tspLibLoader(problem: str):
    tspProblem = tsplib95.parse(problem)
    n = tspProblem.dimension

    dists = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            dists[i][j] = dists[j][i] = tspProblem.get_weight(start=i+1,end=j+1)
            pass

    return [n,dists]

def generateBasicRoute(n):
    dists = []
    for i in range(n):
        dists.append(i)
    return dists



def testFunction(tspFileString,initialRoute,improvement_threshold=0.01):

    dists = tspLibLoader(tspFileString)
    solver =Solver(dists[1],initialRoute)

    start = time.perf_counter()
    solver.two_opt(improvement_threshold=improvement_threshold)
    end = time.perf_counter()
    

    return {
       "cost":solver.best_distance,
        "duration": end - start,
        "tour": solver.best_route
    } 

#initialRoute = generateBasicRoute(20)
#print(testFunction("eil20.tsp",initialRoute))