from math import floor
from random import randint
import sys

def generate_graph(node_number, graph_type, saturation):
    graph=[]
    edge_number = floor(node_number*saturation)

    if graph_type == "matrix":
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

    elif graph_type=="list":
       pass

    elif graph_type=="table":
        pass

    return graph

def generate_user_graph(node_number, graph_type):
    graph=[]

    if graph_type == "matrix":
        for i in range(0, node_number):
            graph.append([])
            for j in range(0,node_number):
                graph[i].append(0)
        pass

    elif graph_type=="list":
       pass

    elif graph_type=="table":
        pass

    return graph
