import sys
import os
import glob
import questionary
from utils import tspUtils
# 1. Detectar archivos .tsp
def listar_archivos_tsp(directorio="input"):
    return glob.glob(os.path.join(directorio, "*.tsp"))

# 2. Definir algoritmos disponibles
ALGORITMOS = {
    "Fuerza bruta": 1,
    "Branch And Bound": 2,
    "Held Karp (Programación Dinamica)" : 3,
    "Vecino Más Cercano": 4,
    "Algoritmo Genético": 5,
    "Búsqueda Tabú": 6,
    #"Simulated Annealing": 3,
    "Ant Colony Optimization": 7,
    "Ant Colony Elitist": 8,
    "Ant Colony Max-Min": 9,
    "GSPH-FC":10
}
# 3. Definir algoritmos de mejora disponibles
ALGORITMOS_MEJORA = {
    "2-opt": 11,
    "Simulated Annealing": 12 
}


def seleccionar_archivos_tsp(archivos):
    return questionary.checkbox(
        "Selecciona los archivos .tsp a utilizar:",
        choices=archivos
    ).ask()

def seleccionar_algoritmos():
    return questionary.checkbox(
        "Selecciona los algoritmos a ejecutar:",
        choices=ALGORITMOS
    ).ask()

def utilizar_algoritmos_mejora():
    return questionary.confirm(
        "¿Desea utilizar algoritmos de optimización?"
    ).ask()

def seleccionar_resultados_optimizar(RESULTADOS):
    return questionary.checkbox(
        "Selecciona los resultados a optimizar:",
        choices=RESULTADOS
    ).ask()

def seleccionar_algoritmos_optimizacion():
    return questionary.checkbox(
        "Selecciona los algoritmos a ejecutar:",
        choices=list(ALGORITMOS_MEJORA.keys())
    ).ask()

def exportar_resultados():
    return questionary.confirm(
        "¿Desea exportar resultados?"
    ).ask()

#Agregar posibilidad de cambiar parámetros de funciones específicas!!!!,,
def main():
    archivos_tsp = listar_archivos_tsp()
    if not archivos_tsp:
        print("No se encontraron archivos .tsp en el directorio.")
        return

    selectedTspFiles = seleccionar_archivos_tsp(archivos_tsp)
    selectedAlgorithms = seleccionar_algoritmos()

    resultados_iniciales = tspUtils.runTestFirstPart(selectedTspFiles=selectedTspFiles,selectedAlgorithms=selectedAlgorithms)
    if utilizar_algoritmos_mejora():
        resultados_a_mejorar = seleccionar_resultados_optimizar(resultados_iniciales)
        resultados_a_mejorar = [{'name':i,'tour': resultados_iniciales[i][0], 'tsp': resultados_iniciales[i][1]} for i in resultados_a_mejorar if i in resultados_iniciales]
        print(resultados_a_mejorar)
        algoritmos_mejora = seleccionar_algoritmos_optimizacion()

        resultados_optimizados = tspUtils.runTestSecondPart(resultados_a_mejorar,algoritmos_mejora)

    if exportar_resultados():
        pass
    
if __name__ == "__main__":
    main()
