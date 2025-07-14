import sys
from copy import copy

#Cleaning
#print("To start program choose testing file: ")
#file_name = input()
#print(f"You are using file '{file_name}' ")
#print(" ")
#matrix, OPT, numbers_of_cities = create_matrix(file_name)

def find_very_first_best_path(matrix,numbers_of_cities):
    first_best_len = 0
    first_best_path = [0]

    minimum = sys.maxsize
    next_city = 0
    # find shortest way from city with 0 index
    for i in range(matrix[0].size):
        if i != 0:
            if matrix[0][i] < minimum:
                minimum = matrix[0][i]
                next_city = i

    first_best_len += minimum
    first_best_path.append(next_city)

    # when first best_path == numbers_of_cities we have all route
    while len(first_best_path) != numbers_of_cities:
        city_to_research = next_city
        minimum = sys.maxsize

        for i in range(matrix[city_to_research].size):
            if i not in first_best_path and i != 0:
                if matrix[city_to_research][i] < minimum:
                    minimum = matrix[city_to_research][i]
                    next_city = i

        first_best_len += minimum
        first_best_path.append(next_city)

    last_city = next_city
    first_best_path.append(0)
    first_best_len += matrix[last_city][0]

    return first_best_path, first_best_len


def bound(vertex,matrix,numbers_of_cities):
    # Get cost from cities that are in path
    bound = value(vertex,matrix)

    cities_still_to_search = []

    # finding cities that we are still not in path
    for i in range(numbers_of_cities):
        if i not in vertex:
            cities_still_to_search.append(i)

    # adding city from vertex (last city in path) that dont have path to next city
    cities_still_to_search.append(vertex[-1])

    # finding minimal cost of traveling to every city that we have to travel to
    for city in cities_still_to_search:
        minimum = sys.maxsize
        for i in range(matrix[city].size):
            if i not in vertex or i == 0:
                if matrix[city][i] < minimum and i != city:
                    minimum = matrix[city][i]
        bound += minimum

    return bound


def value(vertex,matrix):
    value = 0

    for i in range(len(vertex)):
        v = i
        u = i + 1

        if u < len(vertex):
            city_1 = vertex[v]
            city_2 = vertex[u]
            value += matrix[city_1][city_2]

    return value


def main_loop(matrix,numbers_of_cities):
    best_path, best_len = find_very_first_best_path(matrix,numbers_of_cities)
    root = [0]
    priority_queue = [root]


    while priority_queue:
        researching_vertex = priority_queue[-1]
        priority_queue.pop()

        cities_not_in_vertex = []

        for i in range(numbers_of_cities):
            if i not in researching_vertex:
                cities_not_in_vertex.append(i)

        # Adding kids to queue
        if cities_not_in_vertex:
            for city in cities_not_in_vertex:
                new_vertex = copy(researching_vertex)
                new_vertex.append(city)
                if bound(new_vertex,matrix,numbers_of_cities) < best_len:
                    priority_queue.append(new_vertex)

        # Counting final value of node
        else:
            new_vertex = copy(researching_vertex)
            new_vertex.append(0)
            final_len = value(new_vertex,matrix)
            final_path = new_vertex

            if final_len < best_len:
                best_len = final_len
                best_path = final_path

    return [
        best_len,
        best_path
    ]

#main_loop()
