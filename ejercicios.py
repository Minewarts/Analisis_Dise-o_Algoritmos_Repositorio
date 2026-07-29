from typing import List
'''tenemos un conjunto ce C comidas y de B Bebidas'''

comidas = ["c1","c2","c3","c4"]
bebidas = ["b1","b2","b3"]

def combinaciones(comidas:List[str], bebidas:List[str])->List[List[str]]:#O(B*C)
    combinaciones_lista : List[List[str]] = [] #O(1)
    for i in comidas:#O(C)
        for j in bebidas:#O(B)
            #Cuando importa el orden del "for", hablamos de permutacion, cuando no importa hablamos de una combiancion
            combinaciones_lista.append([i,j]) #append: O(1) --> creacion de tupla (numero elementos), O(2): O(3) = O(1)
            #combinaciones_lista.append(f"{i},{j}") #append: O(1) --> Creacion str es el 
    return combinaciones_lista  #O(1)
            

combinaciones_lis = combinaciones(comidas, bebidas)

print(combinaciones_lis)


#----------------------------------------------------------------------------------------------------------------------------------------#
'''generar contraseña de tamaño 4 que contenga cualquier cantidad de vocales o digitos y repetir'''

vocales = "aeiou"
dig = "01234"
digitos= vocales + dig

def generar_contraseñas(digitos: str) -> List[str]:
    contraseñas : List[str] = []
    for i in digitos:
        #digitos = digitos[i:]
        for j in digitos:
            for k in digitos:
                for l in digitos:
                    if i != j and i!= k and j!=k and k!= l and j!=l and i!=l:
                        contraseñas.append(f"{i}{j}{k}{l}")
    return contraseñas

contraseñas = generar_contraseñas(digitos)
print(contraseñas)