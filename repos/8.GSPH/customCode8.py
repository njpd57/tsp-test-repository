import gsph
import tsplib95
import time

def getCityFromTSPLIB(problem: tsplib95.models.StandardProblem):
    nodeSize = problem.dimension
    cities = []
    for i in range(nodeSize):
        nodei = problem.node_coords[i+1]
        cities.append((nodei[0], nodei[1]))

    return cities



def testFunction(tspFileString,
                 MAX_ITER_LOCAL = 800,
                 EPS_FRONTIER = 5):
    problem = tsplib95.parse(tspFileString)
    nodes = getCityFromTSPLIB(problem)

    start   = time.perf_counter()
    routes, _, total_length, _, _ = gsph.gsph_fc(nodes,MAX_ITER_LOCAL=MAX_ITER_LOCAL,EPS_FRONTIER=EPS_FRONTIER)
    end     = time.perf_counter()

    tour = gsph.recoverTour(routes,problem)
    #FALTA CERRAR EL CICLO
    #total_length+=problem.get_weight(tour[0],tour[-1])

    return {
       "cost":  total_length,
        "duration": end - start,
        "tour": tour,
    }