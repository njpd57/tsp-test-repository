"""
Paper GTSPH. 07/07/25

    Martín Antonio Gómez Navarro 
    Nicolás Joaquín Palacios Díaz 
    
    Docente:
        Gustavo Gatica

    Ingeniería Civil Informática
    Universidad Nacional Andrés Bello
    Julio 2025

"""

import sys
import os
from datetime import datetime
import utils.tspUtils as tspUtils

#Brute Foce | B&B DFS | Simulated Annealing
#https://github.com/Kacper-Sleziak/Travelling_Salesman_Problem
sys.path.append("../repos/1.Travelling_Salesman_Problem")
from customCode1 import testFunctionBruteForce as bruteForce
from customCode1 import testFunctionBranchAndBound as branchAndBound
from customCode1 import testFunctionSimulatedAnnealing as simulatedAnnealing

# HeldKarp
#https://github.com/carl-olin/held-karp
sys.path.append("../repos/2.held-karp")
from customCode2 import testFunction as heldKarp

# Nearest Neighbor
#https://github.com/m3hdi-i/tsp-with-nn
sys.path.append("../repos/3.tsp-with-nn")
from customCode3 import testFunction as nearestNeighbour

# 2OPT
#https://github.com/pdrm83/py2opt
sys.path.append("../repos/4.py2opt")
from customCode4 import testFunction as twoOpt

# Genetic Algorithm
#https://github.com/hassanzadehmahdi/Traveling-Salesman-Problem-using-Genetic-Algorithm
sys.path.append("../repos/5.Traveling-Salesman-Problem-using-Genetic-Algorithm")
from customCode5 import testFunction as geneticAlgorithm 

# Tabu Search
#https://github.com/Xavier-MaYiMing/Tabu-Search
sys.path.append("../repos/6.Tabu-Search")
from customCode6 import testFunction as tabuSearch

#Ant Colony System |Max-Min Ant System Elitist Ant System
#https://github.com/Josephbakulikira/Traveling-Salesman-Algorithm
sys.path.append("../repos/7.Traveling-Salesman-Algorithm")
from customCode7 import testFunction as AntSystem 

#GSPH Frontera
#https://github.com/incfDevuser/gsph_toolkit
sys.path.append("../repos/8.GSPH")
from customCode8 import testFunction as GSPH 


# Main Parameters
OUTPUT_FOLDER = "output"
RESULTS_FILE = "results.csv"
TABLE_FILE = "comparation.csv"

# Lista de archivos TSP a probar
TSP_FILE_PATH = "input/"
#TSP_FILE_LIST = ["eil10.tsp","eil20.tsp","eil51.tsp","berlin52.tsp", "eil76.tsp","bier127.tsp","a280.tsp"]
#20 instancias
TSP_FILE_LIST = [
    "a280.tsp",
    "berlin52.tsp",
    "bier127.tsp",
    "ch130.tsp",
    "ch150.tsp",
    "d198.tsp",
    "eil51.tsp",    
    "eil76.tsp",
    "eil101.tsp",
    "gil262.tsp",
    "kroA100.tsp",
    "kroB100.tsp",
    "kroC100.tsp",
    "kroD100.tsp",
    "kroE100.tsp",
    "kroA150.tsp",
    "kroB150.tsp",
    "kroA200.tsp",    
    "kroB200.tsp",
    "lin105.tsp",
    "lin318.tsp",
    "linhp318.tsp",
    "pr76.tsp",
    "pr107.tsp",
    "pr124.tsp",
    "pr136.tsp",
    "pr144.tsp",
    #"pr152.tsp",
    #"pr226.tsp",
    #"pr264.tsp",
    #"pr299.tsp",
    #"pr439.tsp",
    #"pr1002.tsp",

]

TSPLIB_BKS=[
    2579,
    7542,
    118282,
    6110,
    6528,
    15780,
    426,
    538,
    629,
    2378,
    21282,
    22141,
    20749,
    21294,
    22068,
    26524,
    26130,
    29368,
    29437,
    14379,
    42029,
    41345,
    108159,
    44303,
    59030,
    96772,
    58537,
    73682,
    58537,
    49135,
    48191,
    107217,
    259045
]

def runGSPH():
    TABLE_HEADERS = "Instancia;Repositorio;Distancia;BKS;GAPBKS;TiempoEjecución\n"
    currTime = datetime.now()
    table = open(f"comparation_table_GSPH_{currTime.second}.csv","w")

    table.write(TABLE_HEADERS)
    instanceIndex = 0
    for tsp in TSP_FILE_LIST:
        problem_path = os.path.join(TSP_FILE_PATH, tsp)
        instance_name = tsp.upper().split(".")[0]
        instance_bks = TSPLIB_BKS[instanceIndex]
        instanceIndex += 1
        with open(problem_path) as file:
            problem_str = file.read()

            print(instance_name,instance_bks)
            results = GSPH(problem_str)
            tspUtils.generateOutput(instance_name,"gsph_fc",results,OUTPUT_FOLDER,RESULTS_FILE)
            cost = results.get("cost")
            gapbks = tspUtils.getGapBKS(instance_bks,cost)
            table.write(f"{instance_name};GSPH_FC;{cost};{instance_bks};{gapbks};{results.get("duration")}\n")
            print(f"\t\t{cost}")       

    table.close()

def runTest(_seed=1):
    functionList = [lambda x:bruteForce(x),
                    lambda x:branchAndBound(x),
                    lambda x:heldKarp(x),
                    lambda x:nearestNeighbour(x,_seed),
                    #-------------------------------------------#
                    #Estas son de mejora, y se aplicarán al final
                    #lambda x:twoOpt(x),
                    #lambda x:simulatedAnnealing(x,AGES=10),
                    #-------------------------------------------#
                    lambda x:geneticAlgorithm(x,POPULATION_SIZE=1000),
                    lambda x:tabuSearch(x),
                    lambda x:AntSystem(x),
                    lambda x:AntSystem(x,mode='Elitist'),
                    lambda x:AntSystem(x,mode='MaxMin'),
                    lambda x:GSPH(x)
                    ]
    repoNames = [
            "BruteForce",
            "BranchAndBound",
            "HeldKarp",
            "NearestNeighbour",
            #"2-OPT",
            #"SimulatedAnnealing",
            "GeneticAlgorithm",
            "TabuSearch",
            "AntSystem1",
            "AntSystem2",
            "AntSystem3",
            "GsphFC",
            ]

    TABLE_HEADERS = "Instancia;Repositorio;Distancia;BKS;GAPBKS;TiempoEjecución\n"
    currTime = datetime.now()
    table = open(f"comparation_table_{currTime.second}.csv","w")

    table.write(TABLE_HEADERS)
    instanceIndex = 0
    for tsp in TSP_FILE_LIST:
        problem_path = os.path.join(TSP_FILE_PATH, tsp)
        instance_name = tsp.upper().split(".")[0]
        instance_bks = TSPLIB_BKS[instanceIndex]
        instanceIndex += 1

        with open(problem_path) as file:
            problem_str = file.read()

            index = 0
            print()
            print(instance_name,instance_bks)
            best_route = []
            best_len = sys.maxsize
            
            for function in functionList:
                
                #Prevenir métodos exactos.
                if(index < 3):
                    if('10' in instance_name):
                        pass
                    elif('20' in instance_name):
                        if(index == 0 or index == 1):
                            index += 1
                            continue
                    else:
                        index += 1
                        continue                        
                print(f"{repoNames[index]} -", end='')

                results = function(problem_str)
                tspUtils.generateOutput(instance_name,repoNames[index],results,OUTPUT_FOLDER,RESULTS_FILE)

                cost = results.get("cost")
                tour = results.get("tour")
                gapbks = tspUtils.getGapBKS(instance_bks,cost)
                table.write(f"{instance_name};{repoNames[index]};{cost};{instance_bks};{gapbks};{results.get("duration")}\n")
                print(f"\t\t{cost}")

                if(cost < best_len):
                    best_len = cost
                    best_route = tour
                index += 1

            #Ahora aplicaremos 2 opt y SA
            results = twoOpt(problem_str,best_route,improvement_threshold=1e-4)
            tspUtils.generateOutput(instance_name,"2-OPT",results,OUTPUT_FOLDER,RESULTS_FILE)
            gapbks = tspUtils.getGapBKS(instance_bks,results.get("cost"))
            print(f"2OPT - ", end='')
            cost = results.get("cost")
            table.write(f"{instance_name};2-OPT;{cost};{instance_bks};{gapbks};{results.get("duration")}\n")
            print(f"\t\t{int(best_len)}-{results.get("cost")}")

            #SA
            results = simulatedAnnealing(problem_str,AGES=50,INITIAL_ROUTE=best_route,INITIAL_LEN=best_len)
            tspUtils.generateOutput(instance_name,"SimulatedAnnealing",results,OUTPUT_FOLDER,RESULTS_FILE)
            gapbks = tspUtils.getGapBKS(instance_bks,results.get("cost"))
            print(f"SimulatedAnnealing - \t", end='')
            cost = results.get("cost")
            table.write(f"{instance_name};SimulatedAnnealing;{cost};{instance_bks};{gapbks};{results.get("duration")}\n")
            print(f"\t\t{int(best_len)}- {results.get("cost")}")

    table.close()

if __name__ == "__main__":
 runTest()