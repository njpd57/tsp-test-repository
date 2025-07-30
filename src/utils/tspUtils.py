from datetime import datetime
import os
import tsplib95
import sys
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
TSP_LIB_BKS_FILE = "input/bks.txt"
TSPLIB_BKS  = []





def getUltimateFunctionList(selection,POPULATION_SIZE=1000,SEED=1,includeExacts=False,initial_route=[],improvement_threshold=0.01):
    print(selection)
    ULTIMATE_FUNCTION_LIST = {
        1: lambda x:bruteForce(x),
        2: lambda x:branchAndBound(x),
        3: lambda x:heldKarp(x),
        4: lambda x:nearestNeighbour(x,SEED),
        5: lambda x:geneticAlgorithm(x,POPULATION_SIZE),
        6: lambda x:tabuSearch(x),
        7: lambda x:AntSystem(x),
        8: lambda x:AntSystem(x,mode="Elitist"),
        9: lambda x:AntSystem(x,mode="MaxMin"),
        10: lambda x:GSPH(x),
        11: lambda x:twoOpt(x,initialRoute=initial_route,improvement_threshold=improvement_threshold),
        12: lambda x:simulatedAnnealing(x,initial_route)
    }

    return [ULTIMATE_FUNCTION_LIST[i] for i in selection if i in ULTIMATE_FUNCTION_LIST]


def generateFunctionList(selected_algorithms=[0],POPULATION_SIZE=1000,SEED=1,includeExacts=False,includeGSPH=False):
    functionList = []

    if(includeExacts):
        function.append({"name": "BruteForce", "function": lambda x:bruteForce(x)})
        function.append({"name": "BranchAndBound", "function": lambda x:branchAndBound(x)})
        function.append({"name": "HeldKarp", "function": lambda x:heldKarp(x)})
            
    functionList.append({"name": "NearestNeighbour", "function": lambda x:nearestNeighbour(x,SEED)})
    functionList.append({"name": "GeneticAlgorithm", "function": lambda x:geneticAlgorithm(x,POPULATION_SIZE)})
    functionList.append({"name": "TabuSearch", "function": lambda x:tabuSearch(x)})
    functionList.append({"name": "AntSystem", "function": lambda x:AntSystem(x)})
    functionList.append({"name": "AntSystemElitist", "function": lambda x:AntSystem(x,mode="Elitist")})
    functionList.append({"name": "AntSystemMaxMin", "function": lambda x:AntSystem(x,mode="MaxMin")})

    if(includeGSPH):
        functionList.append({"name": "GsphFC", "function": lambda x:GSPH(x)})
    
    return functionList

def loadBKS() -> dict:
    with open(TSP_LIB_BKS_FILE,"r") as file:
        lines = file.read()
        data = lines.split("\n")
        
        bks = {}
        for instance in data:
            name, optimal = instance.split(":")
            name = name.strip()
            optimal = int(optimal.strip())
            bks[name.upper()]=optimal
    return bks
        

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


def runTest(tspFile,seed,POPULATION_SIZE=500,includeExacts = False):
    functionList = generateFunctionList(SEED=seed,POPULATION_SIZE=POPULATION_SIZE,includeExacts=includeExacts)
    currTime = datetime.now()

    table = open(f"comparation_table_{currTime.day}_{currTime.minute}.csv","w")
    table.write(TABLE_HEADERS)
    instanceIndex = 0

    problem_path = os.path.join(tspFile)
    #instance_bks = TSPLIB_BKS[instanceIndex]
    instanceIndex += 1

    bksDict = loadBKS()

    with open(problem_path) as file:
        problem_str = file.read()
        problem  = tsplib95.parse(problem_str)

        index = 0

        instance_name = problem.name.upper()
        instance_bks = bksDict[instance_name]

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


def runTest(selectedTspFiles,selectedAlgorithms):

    functionList =getUltimateFunctionList(selection=selectedAlgorithms)

    print(functionList)
    

    resultados = {
        "Fuerza Bruta - 565428"
    }
    return(resultados)
    pass
    #Tiene que retornar una lista de resultados7