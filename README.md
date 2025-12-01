# Pruebas de Algoritmos para el Problema del Viajante (TSP) usando TSPLIB

Este repositorio contiene un conjunto de scripts y utilidades para realizar pruebas comparativas de diferentes algoritmos de resolución del Problema del Viajante (TSP), utilizando instancias estándar de la biblioteca TSPLIB.

## Objetivo

El objetivo principal es evaluar y comparar el desempeño de diversos algoritmos exactos y metaheurísticos sobre instancias TSP reales, facilitando la experimentación y el análisis de resultados.

## Características

- Soporte para múltiples algoritmos: fuerza bruta, branch & bound, Held-Karp, vecino más cercano, 2-OPT, recocido simulado, algoritmos genéticos, búsqueda tabú, colonia de hormigas, y GSPH.
- Lectura y procesamiento de archivos `.tsp` del formato TSPLIB.
- Generación automática de reportes y tablas comparativas de resultados.
- Fácil integración de nuevos algoritmos o instancias.

## Estructura del repositorio

- `src/`: Scripts principales para la ejecución de pruebas.
- `repos/`: Implementaciones de los distintos algoritmos.
- `input/`: Instancias TSP en formato TSPLIB.
- `output/`: Resultados y reportes generados.

## Requisitos

- Python 3.x
- Paquetes: `tsplib95`, `numpy`, y otros especificados en los scripts de cada algoritmo.

## Ejecución

1. Coloca los archivos `.tsp` de TSPLIB en la carpeta `input/`.
2. Agrega los archivos a la lista inicial TSP_FILE_LIST.
2. Ejecuta el script principal:
   ```bash
   python src/main.py
   ```
3. Los resultados se guardarán en la carpeta `output/` y en archivos CSV comparativos.

## Algoritmos Seleccionados
A continuación se listan los algoritmos recopilados de los repositorios de GitHub para este proyecto.

1. Exhaustive Search
2. Branch & Bound
3. Simulated Annealing
4. Nearest Neighbour
5. Held Karp
6. 2-opt
7. Genetic Algorithm
8. Tabu Search
9. GSPH
10. 

## Repositorios Seleccionados

A continuación, se listan los repositorios de GitHub seleccionados para este proyecto los cuales contienen la implementación de los diez algoritmos:

1. [@p13i Traveling-Salesperson-Problem](https://github.com/p13i/Traveling-Salesperson-Problem) [A] [Exhaustive Search, Branch & Bound, Simmulated Annhealing] 
2. [@carl-olin held-karp](https://github.com/carl-olin/held-karp) [B] [Held-Karp]
3. [@m3hdi- tsp-with-nn](https://github.com/m3hdi-i/tsp-with-nn) [C] [Nearest Neighbour]
4. [@pdrm83 py2opt](https://github.com/pdrm83/py2opt) [D]
5. [@hassanzadehmahdi Traveling-Salesman-Problem-Using-Genetic-Algorithm](https://github.com/hassanzadehmahdi/Traveling-Salesman-Problem-using-Genetic-Algorithm)[E]
6. [@Xavier-MaYiMing Tabu-Search](https://github.com/Xavier-MaYiMing/Tabu-Search)[F] [Tabu Search]
7. [@Josephbakulikira Traveling-Salesman-Algorithm](https://github.com/Josephbakulikira/Traveling-Salesman-Algorithm)[G] 
8. [@incfDevuser gsph-toolkit](https://github.com/incfDevuser/gsph_toolkit)[H] [GSPH]

## Créditos

Desarrollado por:
- Martín Antonio Gómez Navarro
- Nicolás Joaquín Palacios Díaz

Docente: Gustavo Gatica  
Ingeniería Civil Informática  
Universidad Nacional Andrés Bello  
Julio 2025