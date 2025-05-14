

def sort_graph(graph, graph_type):
    if graph_type == "matrix":
        topological_sort_matrix(graph)
    elif graph_type == "list":
        topological_sort_list(graph)
    elif graph_type == "table":
        topological_sort_table(graph)
    else:
        print("Invalid graph type.")
        return

def topological_sort_matrix(graph):
    pass

def topological_sort_list(graph):
    pass

def topological_sort_table(graph):
    pass