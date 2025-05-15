import sys
from commands.graph_creation import generate_graph, generate_user_graph
from commands.topologic_sorts import sort_graph
import commands.searching as searching

def print_graph(graph, graph_type):
    print(f"Graph type: {graph_type}")
    if graph_type == 'matrix':
        n = len(graph)
        print("  | ", ' '.join(str(i+1) for i in range(n)))
        print("--+" + "-" * (2 * n))
        for i, row in enumerate(graph):
            print(f"{i+1} | ", ' '.join(str(val) for val in row))
    elif graph_type == 'list':
        for i, neighbors in enumerate(graph):
            print(f"{i+1}>", ' '.join(str(n+1) for n in neighbors))
    elif graph_type == 'table':
        if not graph:
            print("Graph is empty.")
        for edge in graph:
            print(f"{edge[0]+1} {edge[1]+1}")

def get_saturation():
    saturation = None
    while not saturation or saturation < 0 or saturation > 100:
        try:
            saturation = float(input("saturation (0-100)> "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            saturation = None
    return saturation / 100

def help():
    print('''Komendy:
    print - wyświetla graf (lista sąsiedztwa)
    exit - kończy program
    help - wyświetla pomoc''')

def is_valid_argument():
    return len(sys.argv) >= 2 and sys.argv[1] in ["--generate", "--user-provided", "-g", "-u"]

def main():
    try:
        if not is_valid_argument():
            print("Usage: python program.py --generate/-g lub --user-provided/-u")
            return
        
        graph=[]
        graph_type = input("type> ")
        if not sys.stdin.isatty(): print(graph_type)
        if graph_type not in ["matrix", "list", "table"]:
            print("Invalid graph type. Please choose from 'matrix', 'list', or 'table'.")
            return

        while True:
            try:
                n = int(input("nodes> "))
                if not sys.stdin.isatty(): print(n)
                if n <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Wpisz poprawną liczbę wierzchołków.")
            
        if sys.argv[1] in ["--generate", "-g"]:
            saturation = get_saturation()
            graph = generate_graph(n, graph_type, saturation)
        elif sys.argv[1] in ["--user-provided", "-u"]:
            graph = generate_user_graph(n, graph_type)
        
        if graph is None:
            print("Could not create graph. Please check your input.")
            return
        
        print("Graph created successfully.")

        while True:
            command = input("action> ").strip().lower()
            if not sys.stdin.isatty(): print(command)
            if command == "print":
                print_graph(graph, graph_type)

            elif command == "help":
                help()

            elif command in ["bfs", "breath-first search"]:
                if graph_type == "matrix":
                    searching.bfs(graph, 0, searching.get_neighbors_matrix)
                elif graph_type == "list":
                    searching.bfs(graph, 0, searching.get_neighbors_list)
                elif graph_type == "table":
                    searching.bfs(graph, 0, searching.get_neighbors_table)

            elif command in ["dfs", "depth-first search"]:
                if graph_type == "matrix":
                    searching.dfs(graph, 0, searching.get_neighbors_matrix)
                elif graph_type == "list":
                    searching.dfs(graph, 0, searching.get_neighbors_list)
                elif graph_type == "table":
                    searching.dfs(graph, 0, searching.get_neighbors_table)

            elif command == "find":
                u = int(input("from> ")) #starting node
                v = int(input("to> ")) #ending node
                if searching.edge_exists(graph, graph_type, u, v):
                    print(f"True: edge ({u},{v}) exists in the Graph!")
                else:
                    print(f"False: edge ({u},{v}) does not exist in the Graph!")

            elif command == "sort":
                sort_graph(graph, graph_type, n)

            elif command == "exit":
                print("Exiting program...")
                break

            else:
                print("Wrong command. Type 'help' for a list of commands.")

    except KeyboardInterrupt:
        print("\nExiting program...")
    except EOFError:
        print("\nExiting program...")

if __name__ == "__main__":
    main()
