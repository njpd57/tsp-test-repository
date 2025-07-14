import tsplib95
import time
from point import Point
from antColony import AntColony

def tsplib_to_points(problem):
    # Devuelve una lista de Point en el orden de los nodos
    return [Point(*problem.node_coords[i+1]) for i in range(problem.dimension)]

def testFunction(tspFileString, mode='ACS', colony_size=5, steps=50):
    problem = tsplib95.parse(tspFileString)
    points = tsplib_to_points(problem)
    if not points:
        raise ValueError("No nodes found in TSP instance.")
    # El nombre del modo debe ser 'ACS', 'ELITIST', 'MAX-MIN'
    if mode == 'Elitist':
        variation = 'ELITIST'
    elif mode == 'MaxMin' or mode == 'Max-Min':
        variation = 'MAX-MIN'
    else:
        variation = 'ACS'
    aco = AntColony(variation=variation, size=colony_size, max_iterations=steps, nodes=points)
    start = time.perf_counter()
    for i in range(steps):
        aco.Simulate(i)
    end = time.perf_counter()
    # El mejor tour es aco.best_tour (índices), la mejor distancia es aco.best_distance
    return {
        "cost": aco.best_distance,

        "duration": end - start,
        "tour": aco.best_tour
    } 
def main():
    # Leer el archivo TSP desde la ruta especificada
    tsp_file_path = "input/berlin52.tsp"
    
    # Leer el archivo TSP
    problem = tsplib95.parse(tsp_file_path)
    points = tsplib_to_points(problem)
    aco = AntColony(variation='ACS', size=5, max_iterations=50, nodes=points)
    for i in range(50):
        aco.Simulate(i)
    print(aco.best_distance)

if __name__ == "__main__":
    main()

