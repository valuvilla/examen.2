from ast import main
import numpy as np

def definir_matriz():
    n=int(input("Ingrese la dimension de la matriz: "))    
    p=int(input("Generar matriz aleatoria (1) o ingresarla manualmente (2): "))
    if p==1:
        lim=int(input("Ingrese el limite superior de los numeros aleatorios: "))
        matrix=np.random.randint(lim+1,size=(n,n))
    elif p==2:
         matrix=np.array([[int(input()) for i in range(n)] for j in range(n)])
    else:
        print("Opcion invalida")
    print("La matriz original es: ",matrix)
    return matrix

def sentido_horario(matrix):
    return np.rot90(matrix)[::-1]


def sentido_antihorario(matrix):
    return np.rot90(matrix)

def definir_sentido():
    sentido=int(input("Ingrese el sentido de la rotacion: 1 para sentido horario, 2 para sentido antihorario: "))
    if sentido==1:
        matrix=definir_matriz()
        matrix_nueva=sentido_horario(matrix)   
    elif sentido==2:
        matrix=definir_matriz()
        matrix_nueva=sentido_antihorario(matrix)
    else:
        print("Opcion invalida")
    return "la matriz rotada es: ",matrix_nueva

print(definir_sentido())


if __name__=="__main__":
    main()