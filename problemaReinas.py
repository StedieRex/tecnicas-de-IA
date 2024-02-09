# tablero = [0, 0, 0, 0, 0, 0, 0, 0] es
# reina = 0
# escribiendo normal
# def funcionSucesor(tablero):
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    def __repr__(self):
        return str(self.data)
    def __eq__(self, other):
        return self.data == other.data

def comprobacionCamino(estado:list,iu:int,reina:int): # iu = indiceUltimaReinaColocada
    """
    Esta función toma un estado y un camino

    Parámetros:
    estado (Nodo): Estado actual
    camino (Lista): Lista de estados

    Devuelve:
    bool: True si el estado es válido, False si no
    """
    # ciclo por cada reina
        # ciclo por cada reina
            # reina choca con alguna otra reina
                # no es válido
            # reina no choca con ninguna otra reina
                # es válido
    for e in estado: # e = reina
        i=estado.index(e) # i = indice
        if e == 0:
            continue
        if (i+1-e)==(iu+1-reina) or (i+1+e)==(iu+1+reina):
            return False
        
    return True
        
def sucesor(estado: tuple, pv:bool) -> list:
    reinasDesocupadas = [2,3,4,5,6,7,8]
    for i in estado:
        if i in reinasDesocupadas:
            reinasDesocupadas.remove(i)
    """
    Esta función toma un estado

    Parámetros:
    estado (Nodo): Estado inicial

    Devuelve:
    sucesores (Lista): lista de sucesores prometedores
    """
    sucesores = []
    # ciclo por cada reina
        # reina choca con alguna otra reina
            # no se agrega a la lista de sucesores
        # reina no choca con ninguna otra reina
            # se agrega a la lista de sucesores
    if pv:
        sucesores.append((1,0,0,0,0,0,0,0))
        sucesores.append((0,1,0,0,0,0,0,0))
        sucesores.append((0,0,1,0,0,0,0,0))
        sucesores.append((0,0,0,1,0,0,0,0))
        sucesores.append((0,0,0,0,1,0,0,0))
        sucesores.append((0,0,0,0,0,1,0,0))
        sucesores.append((0,0,0,0,0,0,1,0))
        sucesores.append((0,0,0,0,0,0,0,1))
    else:
        for i in range(len(estado)):
            if estado[i] == 0:
                for j in reinasDesocupadas:
                    sucesor = list(estado)
                    sucesor[i] = j
                    if comprobacionCamino(estado,i,j):
                        sucesores.append(tuple(sucesor))    
                break

    return sucesores

def objetivo(estado: tuple) -> bool:
    return True

def estadoObjetivo(estado):
    """
    Esta función toma un estado

    Parámetros:
    estado (Nodo): Estado actual

    Devuelve:
    bool: True si el estado es el objetivo, False si no
    """
    contador = 0
    for e in estado:
        if e == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False
def depth_first(initial_state: tuple) -> list:
    visited = []
    stack = []
    stack.append(initial_state)
    primeraVez = True
    #while len(stack) > 0:
    while stack != []:
        visited = stack[-1]
        if estadoObjetivo(visited):
            print(f"Se llegó al estado objetivo {visited}")
            return visited
        else:
            successors = sucesor(visited,primeraVez) # los prometedores sucesores
            print(f"-Sucesores: {successors}")
            for i in successors:
                stack.append(i)
            print(f"-Stack: {stack}")
            #eliminar el elemento visited
            stack.remove(visited)
            primeraVez = False

def main():
    reina = 1
    initial_state = (0,0,0,0,0,0,0,0)
    #print(initial_state)
    #print(sucesor(initial_state,False))
    #print(estadoObjetivo((1,2,3,4,5,6,7,0)))
    print(depth_first(initial_state))

if __name__ == "__main__":
    main()