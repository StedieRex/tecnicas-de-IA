# tablero = [0, 0, 0, 0, 0, 0, 0, 0] es
# reina = 0
# escribiendo normal
# def funcionSucesor(tablero):

def sucesor(estado: tuple) -> list:
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

    return sucesores

def objetivo(estado: tuple) -> bool:
    return True

def comprobacionCamino(estado,camino):
    pass

def estadoObjetivo(estado):
    pass

def depth_first(initial_state: tuple) -> list:
    visited = []
    stack = []
    stack.append(initial_state)
    while len(stack) > 0:
        visited = stack[-1]
        if estadoObjetivo(visited):
            print(f"Se llegó al estado objetivo {visited}")
            return visited
        else:
            successors = sucesor(visited) # los prometedores sucesores
            stack.push(successors)

def main():
    initial_state = (0,0,0,0,0,0,0,0)
    print(initial_state)

if __name__ == "__main__":
    main()