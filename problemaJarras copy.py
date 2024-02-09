def comprobacionCamino(estado,camino):
    for i in camino:
        if estado == i:
            print("falso")
            return False
   
    print("verdadero")
    return True

def estadoObjetivo(estado):
    if estado == [2,0]:
        return True
    return False

#x es la jarra de 4 litros
#y es la jarra de 3 litros
estado = [0,0]  # Estado inicial de las jarras, ambas están vacías,(x,y)
camino = [(0,0)]  # Este arreglo guardará el camino que se siguió para llegar a la solución, los caminos son duplas (x,y) donde x es el número de litros en la jarra de 4 litros y y es el número de litros en la jarra de 3 litros

# Intentar acceder a un índice en el arreglo vacío causará un IndexError
try:
    # mientras 
    #print(camino)
    while estado != [2,0]:
        camino
        if estado[0] < 4 and estado[1] < 3 and comprobacionCamino([4,3],camino):
            estado[0] = 4
            estado[1] = 3
            camino.append(estado)
            #print(camino)
        elif estado[0] < 4 and comprobacionCamino([4,estado[1]],camino):
            estado[0] = 4
            camino.append(estado)
            
        elif estado[1] < 3 and comprobacionCamino([estado[0],3],camino):
            estado[1] = 3
            camino.append(estado)

        elif estado[0]+estado[1]>=3 and comprobacionCamino([estado[0]-(3-estado[1]),3],camino):
            estado = [estado[0]-(3-estado[1]),3]
            camino.append(estado)

        elif estado[0]+estado[1]<3 and comprobacionCamino([0,estado[0]+estado[1]],camino):
            estado = [0,estado[0]+estado[1]]
            camino.append(estado)

        elif estado[0]+estado[1]>=4 and comprobacionCamino([4,estado[1]-(4-estado[0])],camino):
            estado = [4,estado[1]-(4-estado[0])]
            camino.append(estado)

        elif estado[0]+estado[1]<4 and comprobacionCamino([estado[0]+estado[1],0],camino):
            estado = [estado[0]+estado[1],0]
            camino.append(estado)

        elif estado[0]>0 and comprobacionCamino([0,estado[1]],camino):
            estado = [0,estado[1]]
            camino.append(estado)

        elif estado[1]>0 and comprobacionCamino([estado[0],0],camino):
            estado = [estado[0],0]
            camino.append(estado)

        if estadoObjetivo(estado):
            print("Se llegó al estado objetivo")
            print(camino)
            break

except IndexError as e:
    print(f"Error: {e}")
