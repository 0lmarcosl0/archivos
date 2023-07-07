#no ay sitema de anti poner signo en otro

fila1 = ["   ","   ","   "]
fila2 = ["   ","   ","   "]
fila3 = ["   ","   ","   "]
cor = 0
turno = 1
print("Ta_te_ti")
jugador1 = input("Símbolo del jugador 1: ")
jugador2 = input("Símbolo del jugador 2: ")
ganador = False

while True:
    if turno == 1:
        print(f"Turno del jugador {turno} : {jugador1}")
        print("         1     2     3")
        print(f"a : {fila1}")
        print(f"b : {fila2}")
        print(f"c : {fila3}")
        cor_num = input("N_Dime la fila: ")
        cor_letra = input("L_Dime cuál: ")
        cor_num = int(cor_num)
        cor = cor_num - 1
        if cor_num == cor_num and cor_letra == "a":
            fila1.pop(cor)
            fila1.insert(cor, jugador1)
        elif cor_num == cor_num and cor_letra == "b":
            fila2.pop(cor)
            fila2.insert(cor, jugador1)
        elif cor_num == cor_num and cor_letra == "c":
            fila3.pop(cor)
            fila3.insert(cor, jugador1)
        
        if fila1 == [jugador1, jugador1, jugador1] or fila2 == [jugador1, jugador1, jugador1] or fila3 == [jugador1, jugador1, jugador1]:
            print(f"Ganador: Jugador 1")
            ganador = True
            break
        
        turno = 2
    else:
        print(f"Turno del jugador {turno} : {jugador2}")
        print("         1     2     3")
        print(f"a : {fila1}")
        print(f"b : {fila2}")
        print(f"c : {fila3}")
        cor_num = input("N_Dime la fila: ")
        cor_letra = input("L_Dime cuál: ")
        cor_num = int(cor_num)
        cor = cor_num - 1
        
        if cor_num == cor_num and cor_letra == "a":
            fila1.pop(cor)
            fila1.insert(cor, jugador2)
        elif cor_num == cor_num and cor_letra == "b":
            fila2.pop(cor)
            fila2.insert(cor, jugador2)
        elif cor_num == cor_num and cor_letra == "c":
            fila3.pop(cor)
            fila3.insert(cor, jugador2)
        
        if fila1 == [jugador2, jugador2, jugador2] or fila2 == [jugador2, jugador2, jugador2] or fila3 == [jugador2, jugador2, jugador2]:
            print(f"Ganador: Jugador 2")
            ganador = True
            break
        
        turno = 1

if not ganador:
    print("Empate")