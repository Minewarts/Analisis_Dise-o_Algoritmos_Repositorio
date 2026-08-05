from typing import List,Set
'''tenemos un conjunto ce C comidas y de B Bebidas'''

'''comidas = ["c1","c2","c3","c4"]
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

print(combinaciones_lis)'''


#----------------------------------------------------------------------------------------------------------------------------------------#
'''generar contraseña de tamaño 4 que contenga cualquier cantidad de vocales o digitos y repetir'''

"""vocales = "aeiou"
dig = "01234"
digitos= vocales + dig #O(l+d)

def generar_contraseñas(digitos: str) -> List[str]:
    contraseñas : List[str] = [] ##O(l+d)
    for i in digitos:
        #digitos = digitos[i:]
        for j in digitos:
            for k in digitos:
                for l in digitos:
                    '''if i != j and i!= k and j!=k and k!= l and j!=l and i!=l:
                        contraseñas.append(f"{i}{j}{k}{l}")'''
                    current_password : Set[str] = {i,j,k,l} ## Aplicamos conjuntos que no permite que se se inserten valores iguales ##O(1)
                    if len(current_password) == 4:
                        current_password : str = i+j+k+l ##O(1)
                        contraseñas.append(current_password) ##O1
    return contraseñas

    ##Temporal: O(n**4)
    ##Espacioal: =(n!)

contraseñas = generar_contraseñas(digitos)
print(len(contraseñas))"""

#----------------------------------------------------------------------------------------------------------------------------------------#
''' Cantidad parejas que pueden sumar 75 sin reflejos'''
'''L=[4,5,6,2,357,245,71,345,7,8,256,9]
T=75

def number_pairs(l : List[int], t : int)-> int:
    pairs:List[List[int]] = []
    for i in l:
        for j in l:
            if (i + j == t) and ([i,j] not in pairs and [j,i] not in pairs):
                pairs.append([i,j])

    return len(pairs)

print(number_pairs(L, T))'''
#----------------------------------------------------------------------------------------------------------------------------------------#
'''cuantas veces s2 esta alamcenado en s1 R=3 '''

'''s1 = "asdfasdfeasdasdf"
s2 = "df"

def count_in_str(string_1:str, string_in:str)->int:
    count = 0
    for i in range (len(string_1)):

        if string_1[i:i+len(string_in)] == string_in :
            count+=1 

    return count

print(count_in_str(s1, s2))'''
#----------------------------------------------------------------------------------------------------------------------------------------#
'''Dado un arreglo de enteros, calcular la suma maxima de  un subarreglo contiguo'''
"""x = [3,-4,5,7,-7,9] 
def sum_max_cont(l:List[float])->float:
    sum_max = float("-inf")
    for i in range (len(l)):


    return suma_max





    
print(sum_max_cont(x))"""
#----------------------------------------------------------------------------------------------------------------------------------------#
"""Permutaciones"""
s1= "easlñop"

def permutaciones(text:str)->List[str]:
    permutaciones=[]
    for i, value_i in enumerate(text):

        for j, value_j in enumerate(text):
            if i == j:
                pass
            else:
                for k, value_k in enumerate(text):
                    if k == j or k ==i:
                        pass 
                    else: 
                        permutaciones.append(f'{value_i}{value_j}{value_k}')

    return permutaciones

print(permutaciones(s1))