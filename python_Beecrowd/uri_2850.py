try:
    while True:
        txt = input()
        if txt.lower() == "esquerda":
            print("ingles")
        if txt.lower() == "direita":
            print("frances")
        if txt.lower() == "nenhuma":
            print("portugues")
        if txt.lower() == "as duas":
            print("caiu")
except EOFError:
    pass