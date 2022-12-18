
from ast import main
import sys

def Fibonnacci(n):
    private_cache={}
    if n in private_cache:
        return private_cache[n]
    elif n<0:
        raise ValueError("Error: El número debe ser positivo")
    elif n==0 or n==1:
        return "Número de Fibonacci de {} es {}".format(n,n)
    else:
        private_cache[n]=Fibonnacci(n-1)+Fibonnacci(n-2)
        return private_cache[n]

print(Fibonnacci(int(input("Introduce un número: "))))
        
if __name__ == '__main__':
    main()