#1)Escriba una función que muestre todos los números primos entre 1 y un número n que es
#ingresado por parámetro

#def n_primo(n):
#    limite = n + 1
#    primos = []
#    if n >= 2:
#        primos.append(2)
#    for num in range(3, limite, 2):
#        es_primo = True
#        for i in range(2, int(num ** 0.5) + 1):
#            if num % i == 0:
#                es_primo = False
#                break
#        if es_primo:
#            primos.append(num)
#    print(primos)

#print("Primos")
#n = int(input("Ingrese un número: "))

#n_primo(n)

#2)_Escriba una función que le pida al usuario ingresar condimentos para un sándwich, hasta 
#que el usuario ingrese ‘salir’. Cada vez que se ingrese un condimento, muestre un mensaje 
#avisando que ya se agregó el condimento al sándwich. Escriba versiones diferentes del 
#programa de acuerdo a estos criterios: 
#• Use un test condicional en el ciclo while para detener la ejecución. 
#• Use un test condicional dentro del ciclo para decidir si continuar la ejecución.

#print("Dime tu condimentos para el sandwhic , pon salir para terminar")
#condimentos = []
#con = "algo"
#while con  != "salir":
#	con = input("Dime : ")
#	if con != "salir":
#		condimentos.append(con)
#print(f"Tu sandwich tiene: {condimentos}")

#print("Dime tu condimentos para el sandwhic , pon salir para terminar")
#condimentos = []
#con = "algo"
#while True:
#	con = input("Dime : ")
#	if con != "salir":
#		condimentos.append(con)
#	else:
#		break
#print(f"Tu sandwich tiene: {condimentos}")

#3) A) Remera: Escriba una función “hacer_remera()” que tome como parámetros un 
#tamaño y el mensaje que debería ir impreso en la remera. La función debe mostrar un mensaje 
#describiendo el tamaño de la remera y el mensaje impreso en ella. Llame la función una vez 
#usando argumentos por posición. Llámela una segunda vez usando argumentos por clave. 
#B) Remeras Grandes: Modifique la “funcion hacer_remera()” para que el tamaño por 
#defecto sea ‘L’ y el mensaje, ‘Me gusta Python’. Haga un par de remeras, la primera con los 
#valores por defecto, y la segunda con valores diferentes.

#A
#def hacer_remera(tamaño, impresion=""):
#    print(f"Tu remera tiene un tamaño de {tamaño} y lo que tiene impreso es {impresion}")
#    return impresion

#print("Remera")
#tam = input("Dime el tamaño: ")
#imp = input("Dime lo que tenga impreso: ")
#hacer_remera(tam, impresion=imp)

#B
#def hacer_remera(tamaño, impresion=""):
#    tam = "L"
#    imp= "Me Gusta Python"
#    print(f"Tu remera tiene un tamaño de {tam} y lo que tiene impreso es {imp}")
#        
#    print(f"Tu remera tiene un tamaño de {tamaño} y lo que tiene impreso es {impresion}")
#    return impresion

#print("Remera")
#tam = input("Dime el tamaño: ")
#imp = input("Dime lo que tenga impreso: ")
#hacer_remera(tam, impresion=imp)

#Serie de Fibonacci: Escriba una función fibonacci(n) que devuelva los n primeros numeros 
#de la serie de Fibonacci. En esta serie, los primeros dos números son 0 y 1, y cada sucesivo 
#número es la suma de los dos números inmediatamente anteriores (ejemplo: 0,1,1,2,3,5,8, …).

#def fibonacci(n):
#    num = [0, 1] 
#    if n <= 2:
#        return num[:n]
#    while len(num) < n:
#        numero = num[-1] + num[-2]
#        num.append(numero) 
#    print(num)
#n = int(input("Dime un numero: "))
#fibonacci(n)