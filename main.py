import sys
from commands.creates import create, create_user

def print_graph(graph, representation_type):
    if representation_type == 'matrix':
        n = len(graph)
        print("  | ", ' '.join(str(i+1) for i in range(n)))
        print("--+" + "-" * (2 * n))
        for i, row in enumerate(graph):
            print(f"{i+1} | ", ' '.join(str(val) for val in row))
    else:
        for i, neighbors in enumerate(graph):
            print(f"{i+1}>", ' '.join(str(n+1) for n in neighbors))
    
def help():
    print('''Komendy:
    print - wyświetla graf (lista sąsiedztwa)
    exit - kończy program
    help - wyświetla pomoc''')

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ["--generate", "--user-provided", "-g", "-u"]:
        print("Użycie: python program.py --generate/-g lub --user-provided/-u")
        return

    gtype = input("Type> ")
    n = int(input("nodes> "))
    graph=[]

    if sys.argv[1] in ["--generate", "-g"]:
        saturation = None

        while saturation < 0 and saturation > 100:
            saturation = float(input("saturation (0-100)> "))
        saturation /= 100

        graph = create(n, gtype, saturation)
    elif sys.argv[1] in ["--user-provided", "-u"]:
        graph = create_user(n, gtype)

    while True:
        command = input("> ").strip().lower()
        if command == "print":
            print_graph(graph)
        elif command == "exit":
            print("Exiting program.")
            break
        elif command == "help":
            help()

if __name__ == "__main__":
    main()
