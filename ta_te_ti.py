#TA_TE_TI
def gano(fila1, fila2, fila3, sym):
    if fila1 == [sym, sym, sym] or fila2 == [sym, sym, sym] or fila3 == [sym, sym, sym]:
        return True
    elif fila1[0] == sym and fila2[0] == sym and fila3[0] == sym or fila1[1] == sym and fila2[1] == sym and fila3[1] == sym or fila1[2] == sym and fila2[2] == sym and fila3[2] == sym:
        return True
    elif fila1[0] == sym and fila2[1] == sym and fila3[2] == sym or fila1[2] == sym and fila2[1] == sym and fila3[0] == sym:
        return True
    else:
        return False
fila1 = ["   ","   ","   "]
fila2 = ["   ","   ","   "]
fila3 = ["   ","   ","   "]
cor = 0
turno = 1
print("Ta_te_ti")
jugador1 = input("Símbolo del jugador 1: ")
jugador2 = input("Símbolo del jugador 2: ")
ganador = False
fin = 0
while fin != 9:
    if turno == 1:
        print(f"Turno del jugador {turno} : {jugador1}")
        print("         1     2     3")
        print(f"a : {fila1}")
        print(f"b : {fila2}")
        print(f"c : {fila3}")
        cor_num = input("N_Dime la fila: ")
        while cor_num != "1" and cor_num != "2" and cor_num != "3":
            					print("ERROR")
            					cor_num = input("N_Dime la fila: ")
        cor_letra = input("L_Dime cuál: ")
        while cor_letra != "a" and cor_letra != "b" and cor_letra != "c":
                  print("ERROR")
                  cor_letra = input("L_Dime cuál: ")
        cor_num = int(cor_num)
        cor = cor_num - 1
        if cor_letra == "a":
            fila1.pop(cor)
            fila1.insert(cor, jugador1)
        elif cor_letra == "b":
            fila2.pop(cor)
            fila2.insert(cor, jugador1)
        elif cor_letra == "c":
            fila3.pop(cor)
            fila3.insert(cor, jugador1)        
        if gano(fila1,fila2,fila3,jugador1):
            print(f"Ganador: Jugador 1")
            ganador = True
            print(fila1)
            print(fila2)
            print(fila3)
            break
        fin += 1
        turno = 2
    else:
        print(f"Turno del jugador {turno} : {jugador2}")
        print("         1     2     3")
        print(f"a : {fila1}")
        print(f"b : {fila2}")
        print(f"c : {fila3}")
        cor_num = input("N_Dime la fila: ")
        while cor_num != "1" and cor_num != "2" and cor_num != "3":
            					print("ERROR")
            					cor_num = input("N_Dime la fila: ")
        cor_letra = input("L_Dime cuál: ")
        while cor_letra != "a" and cor_letra != "b" and cor_letra != "c":
                  print("ERROR")
                  cor_letra = input("L_Dime cuál: ")
        cor_num = int(cor_num)
        cor = cor_num - 1        
        if cor_letra == "a":
            fila1.pop(cor)
            fila1.insert(cor, jugador2)
        elif cor_letra == "b":
            fila2.pop(cor)
            fila2.insert(cor, jugador2)
        elif cor_letra == "c":
            fila3.pop(cor)
            fila3.insert(cor, jugador2)                
        if gano(fila1,fila2,fila3,jugador2):
            print(f"Ganador: Jugador 2")
            ganador = True
            print(fila1)
            print(fila2)
            print(fila3)
            break
        fin += 1
        turno = 1
if not ganador:
    print("Empate")