

def sort_graph(graph, graph_type, node_number):
    initialize_sort = input("Sort type (kahn/tarjan)> ")
    while initialize_sort.lower() not in ["kahn", "tarjan"]:
        initialize_sort = input("Sort type (kahn/tarjan)> ")
        if initialize_sort.lower() not in ["kahn", "tarjan"]:
            print("Invalid sort type. Choose 'kahn' or 'tarjan'.")
    if initialize_sort.lower() == "kahn":
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
            print(candidates)
            if graph[i][1] in candidates:
                candidates.remove(graph[i][1])
        return candidates[0]
    return -1


def kahn_sort(graph, graph_type, node_number):
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

        print("Current sorted nodes:", ' '.join(map(str, [x + 1 for x in sorted_nodes])))
    print("Sorted nodes:", ' '.join(map(str, [x + 1 for x in sorted_nodes])))
                
            

def tarjan_sort(graph, graph_type, node_number):
    pass