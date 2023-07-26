from datetime import date
from random import randint
import time
#Escriba una función redondear() que permita redondear un número
#decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
#entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
#anterior (3)

#inicio = time.time()
#def redondear(n):
#  if n >= 0:
#    return int(n + 0.5)
#  else:
#    return int(n - 0.5)
#numero = float(input("Dime un numero decimal: "))
#num = redondear(numero)
#print(f"El numero redondeado es  {num}")
#final = time.time()
#print(f"El time de ejecucion es {final - inicio} segundos")

#Coloque el módulo del ejercicio anterior dentro de un paquete. En un
#módulo que esté fuera de ese paquete, cree una función de suma de
#decimales que redondee el resultado haciendo uso de la funció
#redondear() del paquete recién creado

#inicio = time.time()
#def redondear(n1,n2):
#    num1 = 0
#    num2 = 0
#    if n1 >= 0:
#        num1 = int(n1 + 0.5)
#    else:
#        num1 = int(n1 - 0.5)
#    if n2 >= 0:
#        num2 = int(n2+ 0.5)
#    else:
#        num2 = int(n2 - 0.5)
#    return (num1 + num2)
#numero1 = float(input("Dime un numero decimal: "))
#numero2 = float(input("Dime otro numero decimal: "))
#print(redondear(numero1,numero2))
#final = time.time()
#print(f"El time de ejecucion es {final - inicio} segundos")

#Usando el módulo datetime, escribe un programa que muestre la fecha
#y hora actuales del sistema

#inicio = time.time()
#print(date.today())
#final = time.time()
#print(f"El time de ejecucion es {final - inicio} segundos")

 #Escriba un programa que devuelva un número par al azar entre 2 y 10
#(pista: para comprobar si se pueden generar todos los números, pruebe
#ejecutar el programa dentro de un ciclo infinito)

#inicio = time.time()
#algo = "algo"
#print("Esrcriba |s| para salir")
#while algo != " ":
#    algo = input("Dime algo: ")
#    print(randint(2,10))
#    if algo == "s":
#    	final = time.time()
#    	print(f"El time de ejecucion es {final - inicio} segundos")
#    	break

#Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
#para la adivinación o para buscar consejo. Su mecanismo es muy simple:
#ante una pregunta del usuario, la bola responde con una de 8 posibles
#respuestas:
#- Es seguro que sí
#- Las chances son buenas
#- Puedes contar con ello
#- Pregúntame de nuevo más tarde
#- Concéntrate y pregunta de nuevo
#- No veo con claridad, intenta de nuevo
#- Mi respuesta es no
#- Mis fuentes me dicen que no
#Escriba una función en Python para simular la bola mágica

#def bola_magica():
#    inicio = time.time()
#    print("Bola Magica")
#    print("Para terminar escriba : |salir| ")
#    while True:
#        salir = input("Cual es tu pregunta: ")
#        suerte = randint(1,8)
#        if salir == "salir":
#            final = time.time()
#            print(f"El time de ejecucion es {final - inicio} segundos")
#            break
#        if suerte == 1:
#            print("Mi respuesta es no")
#        elif suerte == 2:
#            print("Mis fuentes me dicen que no")
#        elif suerte == 3:
#            print("Es seguro que sí")
#        elif suerte == 4:
#            print("Puedes contar con ello")
#        elif suerte == 5:
#            print("Pregúntame de nuevo más tarde")
#        elif suerte == 6:
#            print("Las chances son buenas")
#        elif suerte == 7:
#            print("Concéntrate y pregunta de nuevo")
#        elif suerte == 8:
#            print("No veo con claridad, intenta de nuevo")
#bola_magica()

#Encuentre el tiempo de ejecución de los programas de los ejercicios
#anteriores (pista: use el módulo time)

#inicio = time.time()
#print("Time")
#final = time.time()
#print(f"El time de ejecucion es {final - inicio} segundos")
