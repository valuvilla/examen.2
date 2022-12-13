
def Fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(2))
        
