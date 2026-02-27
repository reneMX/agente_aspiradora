class AgenteAspiradoraReactivo:
    def percibir(self, ubicacion, estado):
        self.ubicacion = ubicacion
        self.estado = estado

    def decidir_accion(self):
        if self.estado == "sucia":
            return "aspirar"
        elif self.ubicacion == "A":
            return "mover_der"
        else:
            return "mover_izq"


class AgenteAspiradoraModelo:
    def __init__(self):
        #Difinicion del constructor 
        #Modelo
        self.modelo = {
            "A": "desconocido",
            "B": "desconocido"
        }
        self.ubicacion_actual = None

    #Actualiza el estado de acuerdo a al persepcion 
    def actualizar_estado(self, percepcion):
        """
        percepcion: (ubicacion, estado)
        estado ∈ {"sucia", "limpia"}
        """
        ubicacion, estado = percepcion
        
        # Actualizar ubicación actual
        self.ubicacion_actual = ubicacion
        
        # Actualizar modelo interno
        self.modelo[ubicacion] = estado

    def decidir_accion(self, percepcion):
        """
        Retorna la acción a realizar:
        {"aspirar", "mover_izq", "mover_der", "nada"}
        """
        self.actualizar_estado(percepcion)
        ubicacion, estado = percepcion

        # Regla 1: Si está sucia, aspirar
        if estado == "sucia":
            #Aqui el agente no se auto actualiza, es el entorno
            #self.modelo[ubicacion] = "limpia"  # Actualizar modelo después de aspirar
            return "aspirar"

        # Regla 2: Si ambas están limpias, detenerse
        if self.modelo["A"] == "limpia" and self.modelo["B"] == "limpia":
            return "apagar"

        # Regla 3: Moverse hacia la otra ubicación
        if ubicacion == "A":
            return "mover_der"
        else:
            return "mover_izq"


# -----------------------------

# Simulación del entorno
# -----------------------------

def simular(agente, entorno_inicial, ubicacion_inicial, descripcion, ciclos):
    entorno = dict(entorno_inicial) #Obtenemos los valores iniciales del entorno
    ubicacion = ubicacion_inicial
    
    
    print("\n" + "=" * 55)
    print(f"  {descripcion}")
    print("=" * 55)
    print(f"  Estado inicial → A: {entorno['A']} | B: {entorno['B']}")
    print("-" * 55)
    
    for paso in range(1, ciclos + 1):
        percepcion = (ubicacion, entorno[ubicacion])
        
        #CASO AGENTE REACTIVO
        if isinstance(agente, AgenteAspiradoraReactivo): #Validamos si es REactivo
            agente.percibir(ubicacion, entorno[ubicacion])
            accion = agente.decidir_accion()
        else:
            accion = agente.decidir_accion(percepcion)
        
        print(f"Paso {paso}")
        print(f"Percepción: {percepcion}")
        print(f"Acción: {accion}")
        print("-" * 40)
        
        #CASO AGENTE MODELO
        if isinstance(agente, AgenteAspiradoraModelo):
            print(f"  Modelo interno: {agente.modelo}")
        print(f"  Entorno       : A={entorno['A']} | B={entorno['B']}")
        print("-" * 55)
        
        if accion == "aspirar":
            entorno[ubicacion] = "limpia"
        elif accion == "mover_der":
            ubicacion = "B"
        elif accion == "mover_izq":
            ubicacion = "A"
        elif accion == "apagar":            
            print("Todo está limpio. Agente detenido.")
            break


# CASOS DE PRUEBA

if __name__ =="__main__":
    simular(agente=AgenteAspiradoraReactivo(), entorno_inicial={"A":"sucia", "B":"sucia"}, ubicacion_inicial = "A", descripcion="AGENTE REACTIVO - A y B Sucias", ciclos=10 )
    simular(agente=AgenteAspiradoraModelo(), entorno_inicial={"A":"sucia", "B":"sucia"}, ubicacion_inicial = "A", descripcion="AGENTE MODELO - A y B Sucias", ciclos=10 )
    simular(agente=AgenteAspiradoraReactivo(), entorno_inicial={"A":"limpia", "B":"sucia"}, ubicacion_inicial = "A", descripcion="AGENTE MODELO - B Sucia" , ciclos=10)
    
    