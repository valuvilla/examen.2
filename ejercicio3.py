
from ast import main
import sys

def Fibonnacci(n):
    sys.set_int_max_str_digits(2000000)
    if n<0:
        print("Error: El número debe ser positivo")
    else:
        a,b=0,1
        for i in range(n):
            a,b=b,a+b
    return "Número de Fibonacci de {} es {}".format(n,a)

print(Fibonnacci(int(input("Introduce un número: "))))
        
if __name__ == '__main__':
    main()