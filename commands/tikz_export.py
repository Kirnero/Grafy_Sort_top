import math

def export_graph_tikz(graph, graph_type):
    n = get_node_count(graph, graph_type)
    angle_step = 360 / n
    radius = 3

    positions = {
        i: (radius * math.cos(math.radians(i * angle_step)),
            radius * math.sin(math.radians(i * angle_step)))
        for i in range(n)
    }

    tikz = ["\\begin{tikzpicture}[->,>=stealth,shorten >=1pt,auto,node distance=2cm,thick,main node/.style={circle,draw}]"]

    for i in range(n):
        x, y = positions[i]
        tikz.append(f"\\node[main node] (N{i}) at ({x:.2f},{y:.2f}) {{{i+1}}};")

    if graph_type == "matrix":
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1:
                    tikz.append(f"\\draw[->] (N{i}) to (N{j});")

    elif graph_type == "list":
        for i in range(n):
            for j in graph[i]:
                tikz.append(f"\\draw[->] (N{i}) to (N{j});")

    elif graph_type == "table":
        for edge in graph:
            a, b = edge
            tikz.append(f"\\draw[->] (N{a}) to (N{b});")

    tikz.append("\\end{tikzpicture}")
    return '\n'.join(tikz)

def get_node_count(graph, graph_type):
    if graph_type == "matrix" or graph_type == "list":
        return len(graph)
    elif graph_type == "table":
        max_node = 0
        for a, b in graph:
            max_node = max(max_node, a, b)
        return max_node + 1
