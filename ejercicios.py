from typing import List,Set,Dict
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
'''Dado un arreglo de enteros, calcular la suma maxima de un subarreglo contiguo'''
'''x = [3,-4,5,7,-7,9] 
def sum_max_cont(l:List[float])->float:
    sum_max = float("-inf")
    for i in range (len(l)):
        for j in range (i+1, i+4):
            if j <= len(l):
                print(f'Current: {l[i:j]}')
                sum_current =sum(l[i:j])
                if  sum_current >= sum_max:
                    print(f'suma maxima previa : {sum_max} ,suma maxima actual :{sum_current}')
                    sum_max = sum_current

    return sum_max
    
print(sum_max_cont(x))'''
#----------------------------------------------------------------------------------------------------------------------------------------#
"""Permutaciones"""
#s1= "easl" 



'''def obtener_permutaciones(texto:str)->List[str]:
    if len(texto) <= 1:
        return [texto]
    
    lista_permutaciones = []
    niveles = [""]
    while(niveles):
        current = niveles.pop(0)

        if len(current) == len(texto):
            lista_permutaciones.append(current)
            continue

        for char in texto:
            
            if char in current:
                continue
            niveles.append(current+char)

    return lista_permutaciones

def permutaciones_recursivas(texto:str, current:str="", permutaciones: List[str]=[])->List[str]:
    if len(current) == len(texto):
        permutaciones.append(current)
        return permutaciones

    for char in texto:
        if char not in current:
            permutaciones_recursivas(texto, current+char, permutaciones)
    
    return permutaciones

print(obtener_permutaciones(s1))
print(permutaciones_recursivas(s1))'''
#----------------------------------------------------------------------------------------------------------------------------------------#
"""matriz = [[2,1,1,1,1],[0,1,0,1,1], [0,0,1,1,1],[0,0,1,1,1],[1,0,1,1,1]]

def tamaño_submatriz(matriz:List[List[int]])->int:
    max_n:int = 0
    for i in range (len(matriz)-1):
        for j in range (len(matriz)-1):
            n=i
            m=j
            if matriz[i][j] == 1:
                flag=False
                n+=1
                m+=1
                sub_matriz= [fila[j:m] for fila in matriz[i:n]]

                for k in range(len(sub_matriz)-1):
                    for h in range(len(sub_matriz)-1):
                        if sub_matriz[k][h] != 1:
                            break
                        if len(sub_matriz) == k+1 and len(sub_matriz) == h+1:
                            if max_n< k+1:
                                max_n = k+1
                                flag = True
                                break
                    if flag:
                        break


                    if sub_matriz[k][h] != 1:
                        break

    return max_n"""


"""def max_submatrix(matriz:List[List[int]])->int:
    max_n:int = 0
    for m in range(len(matriz)):
        for n in range(len(matriz)):
            flag = False
            for k in range (1,len(matriz)):
                for i in range (m, m+k):
                    for j in range (n, n+k):
                        if (i+len(matriz) and j<len(matriz)):
                            if(matriz[i][j] != 1):
                                flag = True
                                break
                        if flag:
                            break
                    if flag:
                        break
                if flag:
                    break"""


#----------------------------------------------------------------------------------------------------------------------------------------#
"""promedio valores: dada una lista de enteros devolver la sublista de tamaño k con mejor promedio de valores"""

"""list=[4,2,7,4,9,22]
k = 2

def mejor_promedio(list:List[int], k:int)->List[int]:
    max_prom= float("-inf")
    max_lista= []
    for i in range (len(list)-1): #O(n) 
        if i <= len(list)-(k) :
            sublista=list[i:i+k] #O(n)
            print(sublista)
            if max_prom<= sum(sublista)/k: #O(n)
                max_lista = sublista

    return max_lista


print(mejor_promedio(list,k))"""

#----------------------------------------------------------------------------------------------------------------------------------------#
# """conjuunto de n objetos, maximo valor bajo capacidad"""# 

w=[2,3,4,5] #peso
v=[3,4,5,6] #valor

def subconjunto_max_valor(peso:List[int], valor:List[int], W:int )-> List[int]:
    suma_max=float("-inf")
    peso_valor = [[peso[i],valor[i],i] for i in range(len(peso))]
    combinaciones = []
    comb_aux = [[l] for l in peso_valor]
    while comb_aux: 
        current = comb_aux.pop(0)
        combinaciones.append(current)

        ultimo_elemento = current[-1]
        ultimo_i = ultimo_elemento[2]

        for j in range(ultimo_i+1,len(peso_valor)):
            if ([peso_valor[j],current] not in comb_aux) and (peso_valor[j] != current) : 
                comb_aux.append(current + [peso_valor[j]])

    for k in combinaciones: 
        peso_t = sum( m[0] for m in k )
        valor_t = sum( n[1] for n in k )
        if valor_t >= suma_max and peso_t <= W:
            suma_max = valor_t
            comb_max = k

    return comb_max

print (subconjunto_max_valor(w,v,5))


##----------------------------------------------------------------------------------------------------------------------------------------#

'''Tripleta Con suma objetivo

Dado un arreglo de n enteros y un valor X, determine si existen tres elementos distintos cuya suma sea exactamente X'''

'''array = [4,5,6,7,8,]
objetive = 22

def objetive_trio(list:List[int], objetive: int)->List[int]:
    for i in list:
        for j in list:
            for k in list:
                if sum([i,j,k])==objetive and i!=j and j != k and i!=k:
                    return [i,j,k]
    return 'no hay tripleta que sume la cantidad objetivo'

print(objetive_trio(array, objetive))
'''

#----------------------------------------------------------------------------------------------------------------------------------------#


'''inp='110101'

def count_combination(st:str)->int: 
    n = len(st)
    count = 0 
    r = []
    for i in range(n-4):
        for j in range (i+1, n-3): 
            for k in range(j+1, n-2):
                for l in range(k+1, n-1):
                    for m in range(l+1, n):
                        boo : bool= True
                        if st[i] == st[j]:
                            boo=False
                        if st[j] == st[k]:
                            boo=False
                        if st[k] == st[l]:
                            boo=False
                        if st[l] == st[m]:
                            boo=False
                        if boo:
                            count+=1
                            r.append([st[i],st[j],st[k],st[l],st[m]])

    return count,r

print (count_combination(inp))'''
                    


        


