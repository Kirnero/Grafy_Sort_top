from math import floor
from random import randint
import sys

def generate_graph(node_number, graph_type, saturation):
    graph=[]
    edge_number = floor(node_number*(node_number-1)*saturation/2)

    if graph_type == "matrix": # Macierz sąsiedztwa
        for i in range(0, node_number):
            graph.append([])
            for j in range(0,node_number):
                graph[i].append(0)
        for i in range(edge_number):
            while True:
                a = randint(0, node_number - 1)
                b = randint(0, node_number - 1)
                if a<b and graph[a][b] == 0:
                    graph[a][b] = 1
                    break

    elif graph_type=="list": # Lista następników
        for i in range(node_number):
            graph.append([])

        for i in range(edge_number):
            while True:
                a = randint(0, node_number - 1)
                b = randint(0, node_number - 1)
                if a < b and b not in graph[a]:
                    graph[a].append(b)
                    break

    elif graph_type=="table": # Tabela krawędzi
        for i in range(edge_number):
            while True:
                a = randint(0, node_number - 1)
                b = randint(0, node_number - 1)
                if a < b and [a,b] not in graph:
                    graph.append([a,b])
                    break

    return graph

def generate_user_graph(node_number, graph_type):
    graph=[]

    if graph_type == "matrix": # Macierz sąsiedztwa
        for i in range(0, node_number):
            graph.append([])
            for j in range(0,node_number):
                graph[i].append(0)

        for i in range(node_number):
            line = input(f"{i+1}> ")
            if not sys.stdin.isatty(): print(line)
            line = line.split()
            
            for j in range(len(line)):
                try:
                    x = int(line[j])
                except ValueError:
                    print(f"Invalid input: '{line[j]}' is not a number")
                    return None
                if i+1 == x:
                    print("Can't add self-loop")
                    continue

                if x > node_number or x < 1:
                    print("Invalid node number")
                    return None

                graph[i][x-1] = 1

    elif graph_type=="list": # Lista następników
       for i in range(node_number):
            graph.append([])

       for i in range(node_number):
            line = input(f"{i+1}> ")
            if not sys.stdin.isatty(): print(line)
            line = line.split()
            
            for j in range(len(line)):
                try:
                    x = int(line[j])
                except ValueError:
                    print(f"Invalid input: '{line[j]}' is not a number")
                    return None
                if i+1 == x:
                    print("Can't add self-loop")
                    continue

                if x > node_number or x < 1:
                    print("Invalid node number")
                    return None

                graph[i].append(x-1)

    elif graph_type=="table": # Tabela krawędzi
        for i in range(node_number):
            line = input(f"{i+1}> ")
            if not sys.stdin.isatty(): print(line)
            line = line.split()
            for j in range(len(line)):
                try:
                    x = int(line[j])
                except ValueError:
                    print(f"Invalid input: '{line[j]}' is not a number")
                    return None
                if i+1 == x:
                    print("Can't add self-loop")
                    continue

                if x > node_number or x < 1:
                    print("Invalid node number")
                    return None

                graph.append([i,x-1])

    return graph
