from ast import main
from string import ascii_letters

def trabajo(cadena):
    if len(cadena) > 1 and cadena[0] == '#':
        letra=cadena.split("#")[1:]
        palabra=letra[0]
        if  len(letra) == 1:
            if palabra[0] in ascii_letters:
                    return [palabra]
            else:
                    return "Error"
        else:
                return []
    elif cadena[-1] == "#":
             return [] 
    else:
        return [cadena]

#Probamos el codigo
print(trabajo(input("Introduce una cadena: ")))

if __name__ == '_main_':
    main()

