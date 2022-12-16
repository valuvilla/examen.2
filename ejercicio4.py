from ast import main


def luck_check(str):
    lista = list(str)
    numeros1=[]
    numeros2=[]
    for i in range(len(lista)):
        if len(lista)%2 ==0:
            primeros=lista[:len(lista)//2]
            ultimos=lista[len(lista)//2:]
        else:
            lista_1=lista.pop(len(lista)//2)
            primeros=lista_1[:len(lista)//2]
            ultimos=lista_1[len(lista)//2:]
    for i in primeros:
            numeros1.append(int(i))
    for i in ultimos:
            numeros2.append(int(i))

    return sum(numeros1) == sum(numeros2)
    

            
#Probamos el codigo
print(luck_check(input("Introduce un número alto: ")))

if __name__ == '__main__':
    main()