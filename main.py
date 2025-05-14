import sys
from commands.creates import generate_graph, generate_user_graph

def print_graph(graph, graph_type):
    if graph_type == 'matrix':
        n = len(graph)
        print("  | ", ' '.join(str(i+1) for i in range(n)))
        print("--+" + "-" * (2 * n))
        for i, row in enumerate(graph):
            print(f"{i+1} | ", ' '.join(str(val) for val in row))
    else:
        for i, neighbors in enumerate(graph):
            print(f"{i+1}>", ' '.join(str(n+1) for n in neighbors))

def get_saturation():
    saturation = None
    while not saturation or saturation < 0 and saturation > 100:
        saturation = float(input("saturation (0-100)> "))
    return saturation / 100

def help():
    print('''Komendy:
    print - wyświetla graf (lista sąsiedztwa)
    exit - kończy program
    help - wyświetla pomoc''')

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ["--generate", "--user-provided", "-g", "-u"]:
        print("Użycie: python program.py --generate/-g lub --user-provided/-u")
        return

    try:

        graph_type = input("type> ")

        if graph_type not in ["matrix", "list", "table"]:
            print("Niepoprawny typ grafu. Wybierz 'matrix', 'list' lub 'table'.")
            return

        n = int(input("nodes> "))
        graph=[]

        if sys.argv[1] in ["--generate", "-g"]:
            saturation = get_saturation()
            graph = generate_graph(n, graph_type, saturation)
            
        elif sys.argv[1] in ["--user-provided", "-u"]:
            saturation = get_saturation()
            graph = generate_user_graph(n, graph_type, saturation)
        
        print("Graph created successfully.")

        while True:
            command = input("action> ").strip().lower()
            if command == "print":
                print_graph(graph, graph_type)
            elif command == "exit":
                print("Exiting program.")
                break
            elif command == "help":
                help()

    except KeyboardInterrupt:
        print("\nExiting program...")
    except EOFError:
        print("\nExiting program...")

if __name__ == "__main__":
    main()
