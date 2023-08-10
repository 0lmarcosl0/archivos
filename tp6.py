import Tp6_4 as Archivo

#Escribir una clase llamada Rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área
#class triangulo():
#    def __init__(self,base,altura):
#        self.base = base
#        self.altura = altura
#    def area(self):
#        return (self.base * self.altura) / 2

#base = int(input("Dime la base del triangulo: "))
#altura = int(input("Dime la altura del triangulo: "))

#Triangulo = triangulo(base,altura)
#print(Triangulo.area())

#Modelar una clase Mate que describa el funcionamiente de la conocida bebida tradicional argentina. La clase debe contener..

#class mate():
#  def __init__(self,cebado,estado=False,max_cebada=10):
#    self.cebado=cebado
#    self.estado=estado
#    self.max_cebada=max_cebada
#  def llenar_mate(self):
#    if self.cebado > self.max_cebada and self.estado==False:
#      print("¡Cuidado! ¡Te quemaste!")
#      self.estado=True
#    else:
#      print("Se cebo")
#      self.estado=True
#  def beber_mate(self):
#    if self.estado==False:
#      print("¡El mate está vacío!")
#    elif self.cebado<0:
#      print("“Advertencia: el mate está lavado.”")
#    else:
#      print("Bebido")
#      print("-1")
#      print(self.cebado)
#      self.cebado -= 1
     
#mate = mate(cebado=3,max_cebada=4)

#Botella y Sacacorchos...

#class Corcho:
#     def __init__(self, Bodega):
#         self.Bodega=Bodega
#    
#     def __str__(self):
#         return self.Bodega

#class Botella:
#     def __init__(self, Corcho:Corcho):
#         self.CorchoDeBotella=Corcho

#class Sacacorcho:
#     def __init__(self):
#         self.CorchoSacacorcho=None
#    
#     def Destapar(self,Botella:Botella):
#         if self.CorchoSacacorcho==None:
#             if Botella.CorchoDeBotella!=None:
#                 self.CorchoSacacorcho=Botella.CorchoDeBotella
#                 Botella.CorchoDeBotella=None
#                 print("Botella destapada")
#             else:
#                 print("La botella ya esta destapada")
#         else:
#             print("El sacacorchos ya tiene un corcho, primero hay que limpiarlo")
#            
#     def Limpiar(self):
#         if self.CorchoSacacorcho==None:
#             print("El sacacorchos ya esta limpio")
#         else:
#             self.CorchoSacacorcho=None
#             print("Sacacorcho limpiado")
#no mio

#class Restaurante():
#  def __init__(self,restaurante_nombre,tipo_de_comida):
#    estado = False
#    self.restaurante_nombre=restaurante_nombre
#    self.tipo_de_comida=tipo_de_comida
#    self.estado = estado
#  
#  def describir_restaurante(self):
#    print(f"El restaurante se llama {self.restaurante_nombre} el tipo de comida es {self.tipo_de_comida} ")
#  def Abrir_Restaurante(self):
#    if self.estado!=True:
#      print("Restaurante Abierto")
#    else:
#      print("Ya esta abierto")
#class Heladeria(Restaurante):
#  def __init__(self,sabores:tuple,restaurante_nombre,tipo_de_comida):
#    estado = False
#    self.sabores=sabores
#    self.restaurante_nombre=restaurante_nombre
#    self.tipo_de_comida=tipo_de_comida
#    self.estado=estado
#  def sabor_heladeria(self):
#    print(f"La lista de sabore es {self.sabores}")

#negocio = Heladeria(("choco","fruti"),"Casa","Helados")

#negocio.sabor_heladeria()

#Escribir una clase Personaje que contenga los atributos vida, posicion y velocidad, y los métodos recibir_ataque, que
#reduzca la vida según una cantidad recibida y lance una excepción si la vida pasa a ser menor o igual que cero, y mover
#que reciba una dirección y se mueva en esa dirección la cantidad indicada por velocidad...

#class Persona():
#  def __init__(self,vida,posicion,velocidad):
#    self.vida=vida
#    self.posicion=posicion
#    self.velocidad=velocidad
#  def recibir_ataque(self):

#la consgina es confusa y no entiendo

#Usuarios: Cree una clase Usuario. Cree también dos atributos nombre y apellido, así como otros atributos que típicamente
#se guardan en un perfil de usuario. Escriba un método describir_usuario() que muestre un resumen de la información del
#usuario. Escriba otro método saludar_usuario() que muestre un saludo personalizado al usuario.
#Cree varias instancias que representen distintos usuarios y llame ambos métodos para cada uno

#class Usuario():
#  def __init__(self,Nombre,Apellido,ID):
#    self.Nombre=Nombre
#    self.Apellido=Apellido
#    self.ID=ID
#  def describir_usuario(self):
#    print(f"Nombre:{self.Nombre}\nApellido:{self.Apellido}\nID:{self.ID}")
#  def saludo_usuario(self):
#    print(f"Hola! {self.Nombre} ,te recuerda que debes 100 €.\n ")
    
#usuario1 = Usuario("Omar","Martínez",29473028)
#usuario2 = Usuario("Jose","García",84739003)
#usuario3 = Usuario("Franco","Peréz",48026679)

#usuario1.describir_usuario()
#usuario1.saludo_usuario()
#usuario2.describir_usuario()
#usuario2.saludo_usuario()
#usuario3.describir_usuario()
#usuario3.saludo_usuario()

#Admin: Un administrador es un tipo de usuario con privilegios especiales. Cree una clase Admin que herede de la clase
#Usuario del ejercicio anterior y agréguele un atributo privilegios que almacene una lista de strings tales como puede
#postear en el foro”, “puede borrar un post”, “puede banear usuario”, etc. Escriba un método mostrar_privilegios() que
#muestre el conjunto de privilegios del administrador, cree una instancia de la clase y llame al método

#class Admi(Usuario):
#  def __init__(self,Nombre,Apellido,ID):
#    privilegios=["Puede postear en el foro","puede borrar un post","puede banear un usuario","puede desbanear un usuario"]
#    self.Nombre=Nombre
#    self.Apellido=Apellido
#    self.ID=ID
#    self.privilegios=privilegios
#  def mostrar_privilegios(self):
#    print(f"Tus privilegios {self.Nombre} como admi son {self.privilegios}.")

#admi1 = Admi("Tomas","Rodríguez",93740099)
#admi1.mostrar_privilegios()

#Privilegios: Escriba una clase Privilegios. La clase debería tener un atributo, privilegios, que almacene una lista de strings
#con los privilegios de manera similar a la del ejercicio 7. Mueva el método mostrar_privilegios() de ese ejercicio a esta
#clase, y haga que una instancia de esta clase sea un atributo de la clase Admin. Cree una nueva instancia de Admin y use
#el método para mostrar privilegios

#sin ganas

#Restaurante importado: Escriba un programa que esté en otro archivo que la clase Restaurante del ejercicio 4, e impórtela
#al módulo actual. Cree una instancia de Restaurante y llame a alguno de sus métodos para asegurarse que la importación funciono


tienda = Archivo.Restaurante("La cocina","Carnes")
tienda.Abrir_Restaurante()