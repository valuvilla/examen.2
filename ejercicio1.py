from ast import main
from string import ascii_letters

def trabajo(cadena):
    if cadena[0] == "#" and cadena[1] != "#":
            letra=cadena.split("#")[1:][-1]
            if letra[0] in ascii_letters:
                return [letra]
            else:
                return "Error"
    elif cadena[0] == "#" and cadena[-1] == "#":
            return [] 
    else:
         return [cadena]

#Probamos el codigo
print(trabajo("##"))

if __name__ == '_main_':
    main()

