class Restaurante():
  def __init__(self,restaurante_nombre,tipo_de_comida):
    estado = False
    self.restaurante_nombre=restaurante_nombre
    self.tipo_de_comida=tipo_de_comida
    self.estado = estado
  
  def describir_restaurante(self):
    print(f"El restaurante se llama {self.restaurante_nombre} el tipo de comida es {self.tipo_de_comida} ")
  def Abrir_Restaurante(self):
    if self.estado!=True:
      print("Restaurante Abierto")
    else:
      print("Ya esta abierto")