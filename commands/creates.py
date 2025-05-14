from math import floor
from random import randint
import sys

def create(node_number, type, saturation):
    graph=[]
    edge_number = floor(node_number*saturation)

    if type == "matrix":
        for i in range(0, node_number):
            graph.append([])
            for j in range(0,node_number):
                graph[i].append(0)
        for i in range(edge_number):
            while True:
                a = randint(0, node_number-1)
                b = randint(0, node_number-1)
                if a<b and graph[a][b] == 0:
                    graph[a][b] = 1
                    break

    elif type=="list":
       pass

    elif type=="table":
        pass

    return graph

def create_user(node_number, type):
    graph=[]

    if type == "matrix":
        for i in range(0, node_number):
            graph.append([])
            for j in range(0,node_number):
                graph[i].append(0)
        pass

    elif type=="list":
       pass

    elif type=="table":
        pass

    return graph
