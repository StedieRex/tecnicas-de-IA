def comprobacionCamino(estado:list,iu:int,reina:int): # iu = indiceUltimaReinaColocada
    """
    Esta función toma un estado y un camino

    Parámetros:
    estado (Nodo): Estado actual

    estos 2 parametros son las coordenadas de la reina que se acaba de colocar
    iu (int): indice de la ultima reina colocada
    reina (int): reina a colocar

    Devuelve:
    bool: True si la reina no se enfrenta en diagonal, False si no
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
        if (i+1-e)==(iu+1-reina) or (i+1+e)==(iu+1+reina):# se le suma 1 a los indices para que no empiecen en 0
            return False
        
    return True
        
def sucesor(estado: tuple, pv:bool) -> list:
    """
    Esta función toma un estado

    Parámetros:
    estado (Nodo): Estado inicial

    Devuelve:
    sucesores (Lista): lista de sucesores prometedores
    """
    #se usa un vector para saber que reinas están desocupadas, o las columnas que no tienen reina
    reinasDesocupadas = [2,3,4,5,6,7,8]
    for i in estado:
        if i in reinasDesocupadas:
            reinasDesocupadas.remove(i)

    sucesores = []
    if pv: #en caso de ser la primera iteraicon se mueve por filas la primera reina, pv = primeraVez
        for i in range(len(estado)):
            sucesor = list(estado)
            sucesor[i] = 1
            #print(f"-Sucesor: {sucesor}")
            sucesores.append(tuple(sucesor))
    else: #ya que pasamos el primer vector se empieza a mover por columnas
        for i in range(len(estado)):
            if estado[i] == 0:
                for j in reinasDesocupadas:
                    sucesor = list(estado)
                    sucesor[i] = j
                    if comprobacionCamino(estado,i,j):
                        sucesores.append(tuple(sucesor))    
                break

    return sucesores

def objetivo(estado):
    """
    Esta función toma un estado

    Parámetros:
    estado (Nodo): Estado actual

    Devuelve:
    bool: True si el estado es el objetivo, False si no
    """
    #solo se cuenta el numero de ceros que tiene el estado, si no hay ceros es que ya se llegó al estado objetivo
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
        if objetivo(visited):
            #print(f"Se llegó al estado objetivo {visited}")
            return visited
        else:
            successors = sucesor(visited,primeraVez) # los prometedores sucesores
            #print(f"-Sucesores: {successors}")
            mostrarLiFo.config(state="normal")
            mostrarLiFo.insert(tk.INSERT, f"-Sucesores: {successors}\n")
            for i in successors:
                stack.append(i)
            #print(f"-Stack: {stack}")
            mostrarLiFo.insert(tk.INSERT, f"-Stack: {stack}\n")
            mostrarLiFo.config(state="disabled")
            #eliminar el elemento visited
            
            stack.remove(visited)
            primeraVez = False

def main():

    initial_state = (0,0,0,0,0,0,0,0)
    cajaEstadoini.config(state="normal")
    cajaEstadoini.insert(tk.END, initial_state)
    cajaEstadoini.config(state="disabled")
    print(depth_first(initial_state))

if __name__ == "__main__":
    #aqui se implementa la interfaz gráfica
    import tkinter as tk
    from tkinter import messagebox
    from tkinter import scrolledtext
    def main():

        initial_state = (0,0,0,0,0,0,0,0)
        #print(initial_state)
        #print(sucesor(initial_state,False))
        #print(estadoObjetivo((1,2,3,4,5,6,7,0)))
        messagebox.showinfo("Solución",depth_first(initial_state))

    root = tk.Tk()
    root.title("Problema de las 8 reinas")
    root.geometry("825x460")
    #bloquear tamaño de la ventana
    root.resizable(0,0)
    
    button = tk.Button(root, text="Iniciar", command=main)
    button.place(x=20,y=3)

    # Crear un Frame que contendrá la caja de texto y la barra de desplazamiento
    frame_contenedor = tk.Frame(root)
    frame_contenedor.pack()
    frame_contenedor.config(width=55, height=10)
    frame_contenedor.place(x=19,y=32)

    # Crear una caja de texto con barras de desplazamiento vertical
    mostrarLiFo = scrolledtext.ScrolledText(frame_contenedor, height=25, width=97, state="disabled", wrap=tk.NONE)
    mostrarLiFo.pack(side="left", fill="both", expand=True)

    # Crear una barra de desplazamiento horizontal
    scrollbar_horizontal = tk.Scrollbar(frame_contenedor, orient=tk.HORIZONTAL, command=mostrarLiFo.xview)
    scrollbar_horizontal.place(x=0, y=388, relwidth=.98, height=20)

    # Configurar la caja de texto para desplazarse horizontalmente
    mostrarLiFo.config(xscrollcommand=scrollbar_horizontal.set)

    cajaEstadoini= tk.Text(root, height=1, width=25, state="disabled")#caja para numero de grupos 
    cajaEstadoini.place(x=180,y=3)

    initial_state = (0,0,0,0,0,0,0,0)
    cajaEstadoini.config(state="normal")
    cajaEstadoini.insert(tk.END, f"{initial_state}")
    cajaEstadoini.config(state="disabled")

    labelEstadoIni = tk.Label(root, text="Estado inicial:")
    labelEstadoIni.place(x=100,y=3)

    root.mainloop()
    