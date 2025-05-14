import sys

def create(node_number, saturation):
    print("create_func")

def create_user(node_number):
    print("create_user_func")

def print_graph(graph):
    print("print_graph_func")

def help():
    print('''Komendy:
    print - wyświetla graf (lista sąsiedztwa)
    exit - kończy program
    help - wyświetla pomoc''')

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ["--generate", "--user-provided", "-g", "-u"]:
        print("Użycie: python program.py --generate/-g lub --user-provided/-u")
        return

    n = int(input("nodes> "))
    graph=[]

    if sys.argv[1] in ["--generate", "-g"]:
        saturation = None

        while saturation not in range(0,101):
            saturation = int(input("saturation (0-100)> "))
        saturation = int(saturation) / 100

        graph = create(n, saturation)
    elif sys.argv[1] in ["--user-provided", "-u"]:
        graph = create_user(n)

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
