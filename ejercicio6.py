from ast import main
import numpy as np

def definir_matriz():
    n=int(input("Ingrese la dimension de la matriz: "))
    p=int(int("Generar matriz aleatoria (1) o ingresarla manualmente (2): "))
    if p==1:
        lim=int(input("Ingrese el limite superior de los numeros aleatorios: "))
        matrix=np.random.randint(lim+1,size=(n,n))
    elif p==2:
        matrix=np.array([[int(input()) for i in range(n)] for j in range(n)])
    else:
        print("Opcion invalida")
    return matrix


def sentido_horario(matrix):
    if not matrix:
        return matrix
    return list(zip(*matrix[::-1]))

#print(sentido_horario([[1,2,3],[4,5,6],[7,8,9]]))

def sentido_antihorario(matrix):
    if not matrix:
        return matrix
    return list(zip(*matrix))[::-1]

#print(sentido_antihorario([[1,2,3],[4,5,6],[7,8,9]]))
def definir_sentido():
    sentido=int(input("Ingrese el sentido de la rotacion: 1 para sentido horario, 2 para sentido antihorario: "))
    if sentido==1:
        return sentido_horario
    elif sentido==2:
        return sentido_antihorario
    else:
        print("Opcion invalida")
        return None

print(definir_sentido())


if __name__=="__main__":
    main()