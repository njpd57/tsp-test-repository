from datetime import datetime
import os
import sys
import tsplib
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
TABLE_HEADERS = "Instancia;Repositorio;Distancia;BKS;GAPBKS;TiempoEjecución\n"

# Lista de archivos TSP a probar
TSP_FILE_PATH = "input/"
TSPLIB_BKS  = []

def generateFunctionList(POPULATION_SIZE=1000,SEED=1):
    return [
        {"name": "BruteForce", "function": lambda x:bruteForce(x)},
        {"name": "BranchAndBound", "function": lambda x:branchAndBound(x)},
        {"name": "HeldKarp", "function": lambda x:heldKarp(x)},
        {"name": "NearestNeighbour", "function": lambda x:nearestNeighbour(x,SEED)},
        {"name": "GeneticAlgorithm", "function": lambda x:geneticAlgorithm(x,POPULATION_SIZE)},
        {"name": "TabuSearch", "function": lambda x:tabuSearch(x)},
        {"name": "AntSystem", "function": lambda x:AntSystem(x)},
        {"name": "AntSystemElitist", "function": lambda x:AntSystem(x,mode="Elitist")},
        {"name": "AntSystemMaxMin", "function": lambda x:AntSystem(x,mode="MaxMin")},
        {"name": "GsphFC", "function": lambda x:GSPH(x)}
    ]


def generateOutput(INSTANCE_NAME,REPO_NAME,RESULTS,OUTPUT_FOLDER="output",RESULTS_FILE="results.csv"):
    currTime = datetime.now()
    year = currTime.year
    month = currTime.month
    day = currTime.day
    hour = currTime.hour
    minute = currTime.minute
    second = currTime.second

    title = f"{INSTANCE_NAME}_{REPO_NAME}_{year}_{month}_{day}_{hour}_{minute}_{second}"

    outputPath = os.path.join(OUTPUT_FOLDER,title)
    os.mkdir(outputPath)

    results_string = f"distance;duration;path\n{RESULTS.get('cost')};{RESULTS.get('duration')};{RESULTS.get('tour')}\n"
    results_path = os.path.join(outputPath,RESULTS_FILE)
    with open(results_path,'w') as file:
        file.write(results_string)
    
def getGapBKS(bks,br):
    return ((br - bks)/bks) * 100


def runTest(tspFile,seed,POPULATION_SIZE=500):
    functionList = generateFunctionList(seed,POPULATION_SIZE)
    currTime = datetime.now()

    table = open(f"comparation_table_{currTime.day}_{currTime.minute}.csv","w")
    table.write(TABLE_HEADERS)
    instanceIndex = 0

    problem_path = os.path.join(TSP_FILE_PATH, tspFile)
    instance_name = tspFile.upper().split(".")[0]
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
            print(f"{function["name"]} -", end='')

            results = function["function"](problem_str)
            generateOutput(instance_name,function["name"],results,OUTPUT_FOLDER,RESULTS_FILE)

            cost = results.get("cost")
            tour = results.get("tour")
            gapbks = getGapBKS(instance_bks,cost)
            table.write(f"{instance_name};{function["name"]};{cost};{instance_bks};{gapbks};{results.get("duration")}\n")
            print(f"\t\t{cost}")

            if(cost < best_len):
                best_len = cost
                best_route = tour
            index += 1

        #Ahora aplicaremos 2 opt y SA
        results = twoOpt(problem_str,best_route,improvement_threshold=1e-4)
        generateOutput(instance_name,"2-OPT",results,OUTPUT_FOLDER,RESULTS_FILE)
        gapbks = getGapBKS(instance_bks,results.get("cost"))
        print(f"2OPT - ", end='')
        cost = results.get("cost")
        table.write(f"{instance_name};2-OPT;{cost};{instance_bks};{gapbks};{results.get("duration")}\n")
        print(f"\t\t{int(best_len)}-{results.get("cost")}")

        #SA
        results = simulatedAnnealing(problem_str,AGES=50,INITIAL_ROUTE=best_route,INITIAL_LEN=best_len)
        generateOutput(instance_name,"SimulatedAnnealing",results,OUTPUT_FOLDER,RESULTS_FILE)
        gapbks = getGapBKS(instance_bks,results.get("cost"))
        print(f"SimulatedAnnealing - \t", end='')
        cost = results.get("cost")
        table.write(f"{instance_name};SimulatedAnnealing;{cost};{instance_bks};{gapbks};{results.get("duration")}\n")
        print(f"\t\t{int(best_len)}- {results.get("cost")}")

    table.close()

def runAllTest(tspFile,seed):
    pass

def runTestWithFunction(seed):
    pass