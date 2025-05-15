import copy
import sys

def sort_graph(graph, graph_type, node_number):
    selected_sort = None

    while True:
        selected_sort = input("Sort type (kahn/tarjan)> ")
        if not sys.stdin.isatty(): print(selected_sort)

        if selected_sort.lower() not in ["kahn", "tarjan"]:
            print("Invalid sort type. Choose 'kahn' or 'tarjan'.")
        else:
            break
    
    if selected_sort.lower() == "kahn":
        kahn_sort(graph[:], graph_type, node_number)
    else:
        tarjan_sort(graph[:], graph_type, node_number)

def node_without_incoming_edges(graph, graph_type, node_number):
    if graph_type == "matrix":
        for i in range(len(graph)):
            if graph[i][i] == -1: continue
            line = True
            for j in range(len(graph)):
                if graph[j][i] == 1:
                    line = False
                    break
            if line: return i

    elif graph_type == "list":
        candidates=[]
        for i in range(node_number):
            if graph[i]!=(-1): candidates.append(i)
        for i in range(len(graph)):
            if graph[i] == -1: continue
            for j in range(len(graph[i])):
                if graph[i][j] in candidates:
                    candidates.remove(graph[i][j])
                    print(candidates)
        return candidates[0]

    elif graph_type == "table":
        candidates=[]
        for i in range(len(graph)):
            candidate = graph[i][1]
            if candidate not in candidates and candidate != -1: candidates.append(graph[i][1])
            candidate = graph[i][0]
            if candidate not in candidates and candidate != -1: candidates.append(graph[i][0])
        for i in range(len(graph)):
            if -1 in graph[i]: continue
            #print(candidates)
            if graph[i][1] in candidates:
                candidates.remove(graph[i][1])
        return candidates[0]
    return -1


def kahn_sort(graph, graph_type, node_number):

    graph = copy.deepcopy(graph)

    sorted_nodes = []
    while len(sorted_nodes) < node_number:
        node = node_without_incoming_edges(graph, graph_type, node_number)
        if node == -1:
            print("Graph is cyclic!")
            return
        sorted_nodes.append(node)

        #Remove node from graph
        if graph_type == "matrix":
            for i in range(len(graph)):
                graph[i][node] = 0
                graph[node][i] = 0
            graph[node][node]=-1

        elif graph_type == "list":
            for i in range(len(graph)):
                if graph[i] == -1: continue
                if node in graph[i]:
                    graph[i].remove(node)
            graph[node] = -1

        elif graph_type == "table":
            for i in range(len(graph)):
                if graph[i][0] == node:
                    graph[i][0] = -1
                if graph[i][1] == node:
                    graph[i][1] = -1

        #Removing done

        #print("Current sorted nodes:", ' '.join(map(str, [x + 1 for x in sorted_nodes])))
    print("Sorted nodes:", ' '.join(map(str, [x + 1 for x in sorted_nodes])))
                
            
def tarjan_sort(graph, graph_type, node_number):
    visited_temp = [False] * node_number
    visited_perm = [False] * node_number
    result = []

    def visit(n):
        if visited_perm[n]:
            return
        if visited_temp[n]:
            print("Graph is cyclic!")
            raise Exception("Cycle detected")

        visited_temp[n] = True

        neighbors = []
        if graph_type == "matrix":
            for i in range(node_number):
                if graph[n][i] == 1:
                    neighbors.append(i)

        elif graph_type == "list":
            neighbors = graph[n][:]

        elif graph_type == "table":
            for edge in graph:
                if edge[0] == n:
                    neighbors.append(edge[1])

        for m in neighbors:
            visit(m)

        visited_temp[n] = False
        visited_perm[n] = True
        result.insert(0, n)
        #print("Current sorted nodes:", ' '.join(map(str, [x + 1 for x in result])))

    
    for node in range(node_number):
        if not visited_perm[node]:
            visit(node)
    print("Sorted nodes:", ' '.join(map(str, [x + 1 for x in result])))
