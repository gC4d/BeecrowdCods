from this import d


try:
    while True:
        d = input()
        s = input()
        if s in d:
            print("Resistente")
        else:
            print("Nao resistente")
except EOFError:
    pass