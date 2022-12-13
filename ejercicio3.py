
from ast import main


def Fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        for i in range(2, n+1):
            return Fibonacci(n-1) + Fibonacci(n-2)
    

print(Fibonacci(10))
        
if __name__ == '__main__':
    main()