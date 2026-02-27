class Agente_aspiradora():
    def aspiradora(self, estado, ubicacion):
        self.estado = estado
        self.ubicacion = ubicacion
        
    def actuar(self):
         if(self.estado == 'sucio'):
             print("Aspiradora en funcionamiento Camcia el estado a limpio")
             self.estado = "limpio"
         elif (self.ubicacion == "B"):
             print("Aspiradora cambiando a la ubicacion A")
             self.ubicacion = "A"
         else:
              print("Aspiradora Cambiando de ubicacon a B")
              self.ubicacion = "B"
              


aspiradora = Agente_aspiradora()
aspiradora.aspiradora("sucio", "A")
lista = ["sucio", "limpio", "sucio", "limpio", "sucio", "limpio", "sucio", "limpio", "sucio", "limpio", "limpio"]

for estado in lista:
    aspiradora.estado = estado
    print("El estado es ", estado)
    aspiradora.actuar()

