

from ast import main


def clock_wise(matrix):
    """Recibe una matriz y la rota en sentido horario"""
    if not matrix:
        return matrix
    return list(zip(*matrix[::-1]))

print(clock_wise([[1,2,3],[4,5,6],[7,8,9]]))

def counter_clock_wise(matrix):
    """Recibe una matriz y la rota en sentido antihorario"""
    if not matrix:
        return matrix
    return list(zip(*matrix))[::-1]

print(counter_clock_wise([[1,2,3],[4,5,6],[7,8,9]]))

if __name__=="__main__":
    main()