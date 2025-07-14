import tsplib95
import time
import tsp as repoTSP

def getCityFromTSPLIB(problem: tsplib95.models.StandardProblem):
    nodeSize = problem.dimension
    cities = []
    for i in range(nodeSize):
        nodei = problem.node_coords[i+1]
        cities.append([i+1,float(nodei[0]),float(nodei[1])])
    return cities

def testFunction(tspFileString,
                POPULATION_SIZE = 2000, 
                TOURNAMENT_SELECTION_SIZE = 4,
                MUTATION_RATE = 0.1,
                CROSSOVER_RATE = 0.9,
                TARGET = 450.0):
    problem = tsplib95.parse(tspFileString)

    
    cities = getCityFromTSPLIB(problem)
    
    

    firstpopu,firstfitest = repoTSP.selectPopulation(cities,POPULATION_SIZE)
    start = time.perf_counter()
    answer, genNumber = repoTSP.geneticAlgorithm(
        firstpopu,
        len(cities),
        TOURNAMENT_SELECTION_SIZE,
        MUTATION_RATE,
        CROSSOVER_RATE,
        TARGET,
    )
    end = time.perf_counter()
    tour = []
    for i in answer[1]:
        tour.append(i[0])

    return {
        "cost":answer[0],
        "duration": end - start,
        "tour": tour
        } 
