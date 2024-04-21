def comprobacionCamino(estado,frontera)->bool:
    for i in frontera:
        #print(estado,i)
        if estado == i:
            #print("falso")
            return False
   
    #print("verdadero")
    return True #Si no se encuentra el estado en la frontera, se retorna verdadero

def creandoHijos(estado,frontera,f):
    while True:

        if estado[0] < 4 and estado[1] < 3 and comprobacionCamino([4,3],f):
            frontera.append([4,3])
            #print,frontera)
        elif estado[0] < 4 and comprobacionCamino([4,estado[1]],f):
            frontera.append([4,estado[1]])
            
        elif estado[1] < 3 and comprobacionCamino([estado[0],3],f):
            frontera.append([estado[0],3])

        elif estado[0]+estado[1]>=3 and comprobacionCamino([estado[0]-(3-estado[1]),3],f):
            frontera.append([estado[0]-(3-estado[1]),3])

        elif estado[0]+estado[1]<3 and comprobacionCamino([0,estado[0]+estado[1]],f):
            frontera.append([0,estado[0]+estado[1]])

        elif estado[0]+estado[1]>=4 and comprobacionCamino([4,estado[1]-(4-estado[0])],f):
            frontera.append([4,estado[1]-(4-estado[0])])

        elif estado[0]+estado[1]<4 and comprobacionCamino([estado[0]+estado[1],0],f): 
            frontera.append([estado[0]+estado[1],0])

        elif estado[0]>0 and comprobacionCamino([0,estado[1]],f):
            frontera.append([0,estado[1]])

        elif estado[1]>0 and comprobacionCamino([estado[0],0],f):
            frontera.append([estado[0],0])
        else: 
            return frontera

def estadoObjetivo(estado):
    if estado == [2,0]:
        return True
    return False

def main():
    # Intentar acceder a un índice en el arreglo vacío causará un IndexError
    #x es la jarra de 4 litros
    #y es la jarra de 3 litros
    estado = [0,0]  # Estado inicial de las jarras, ambas están vacías,(x,y),frontera = []  # Este arreglo guardará el,frontera que se siguió para llegar a la solución, los caminos son duplas (x,y) donde x es el número de litros en la jarra de 4 litros y y es el número de litros en la jarra de 3 litros
    camino = []
    f = []

    f.append(estado)
    camino.append(estado)
    while camino != []:

        if estadoObjetivo(estado):
            print("Se llegó al estado objetivo")
            print(camino)
            break
        else:
            for i in creandoHijos(estado,camino,f):#no entiendo porque no se actualiza el valor de camino, se pasa por referencia
                f.append(i)

            print(f)
            print("iteracion")
            camino.pop(0)
            estado = camino[0]
            print(camino)
            #print(estado)
            #print(estado[0])
            #print(estado[1])    

if __name__ == "__main__":
    main()


