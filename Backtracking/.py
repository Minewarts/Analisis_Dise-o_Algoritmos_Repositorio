from typing import List
'''matriz = [
          [2,0,0,2],
          [1,2,0,0],
          [1,0,5,0],
          [5,4,5,2]
          ]
c1 = [1,0]
c2 = [2,2]
k = 8

def Caminos(matriz : List[List[int]], c1 : List[int], c2 : List[int], k : int, i : int = None , j : int = None, sum_act:int = 0,
            camino : List[List[int]] = None, caminos : List [List[List[int]]] = None) -> List [List[List[int]]]:

    if camino is None : camino = []
    if caminos is None: caminos = []
    if i is None and j is None:
        i=c1[0]
        j=c1[1]

    sum_act = sum_act + matriz[i][j] 

    if sum_act > k:
        return caminos

    if [i,j] in camino:
        return caminos
    
    if [i,j] == c2:
        camino.append([i,j])
        caminos.append(camino.copy())
        camino.pop()
        return caminos

    
    if i < len(matriz)-1: 
        camino.append([i,j])
        Caminos(matriz,c1,c2,k,i+1,j,sum_act, camino, caminos)
        camino.pop()
    if i > 0: 
        camino.append([i,j])
        Caminos(matriz,c1,c2,k,i-1,j,sum_act, camino, caminos)
        camino.pop()
    if j < len(matriz[0])-1: 
        camino.append([i,j])
        Caminos(matriz,c1,c2,k,i,j+1,sum_act, camino, caminos)
        camino.pop()
    if j > 0: 
        camino.append([i,j])
        Caminos(matriz,c1,c2,k,i,j-1,sum_act, camino, caminos)
        camino.pop()

    return caminos
    

print (Caminos(matriz, c1, c2, k))'''


#-------------------------------------------------------------------------------------------------#

#permutaciones

'''nums = [1,2,3]

def generar_permutaciones(array:List[int],  permutaciones: List[List[int]] = [],current: List[int] = [], visited : List[int] = [])->List[List[int]]:
    if sorted(current) in permutaciones: 
        return permutaciones
    else:
        permutaciones.append(current.copy())
    
    
    if len(current) >= len(array):
        return permutaciones

    for i in range(len(array)):
        if i in visited:
            continue
        current.append(array[i])
        generar_permutaciones(array, permutaciones, current, visited+[i])
        current.pop()

    return permutaciones

print(generar_permutaciones(nums))'''

#-------------------------------------------------------------------------------------------------#

'''candidatos = [8,2,3,6,7]
k = 7 
def combinaciones_suma (array : List[int], target : int, current : List[int] = [], current_s : int = 0 , resultado : List[List[int]]= [])-> List[List[int]]:
    if len(current) > len(array):
        return resultado
    if current_s == target and sorted(current) not in resultado:
        resultado.append(current.copy())
    
    for i in range(len(array)):
        if array[i] > target:
            continue
        current.append(array[i])
        combinaciones_suma(array,target, current, current_s +array[i], resultado)
        current.pop()

    return resultado

print(combinaciones_suma(candidatos,k))'''

#-------------------------------------------------------------------------------------------------#

#Encontrar palabras en una matriz

board = [['A','B','C','E'], 
         ['S','F','C','S'], 
         ['A','D','E','E']]
word = "ABCCED"

def finding_word(word: str, matriz: List[List[str]], current:str = '', i:int = None, j:int = None, index:int = 0, visited:List[List[int]] = None):
    if visited is None:
        visited = []

    if current == word:
        return True

    if index >= len(word):
        return False

    if (matriz[i][j] != word[index]) and current != '':
        return False

    if [i,j] in visited:
        return False
    
    if matriz[i][j] is word[index]:
        current+=matriz[i][j]
        index+=1
        visited.append([i,j])
    
    if i < len(matriz)-1:
        respuesta = finding_word(word, matriz, current, i+1, j, index, visited)
        if respuesta:
            visited.pop()
            return True
            
        

    if j < len(matriz[i])-1:
        respuesta = finding_word(word, matriz, current, i, j+1, index, visited)
        if respuesta:
            visited.pop()
            return True

    if i  > 0: 
        respuesta = finding_word(word, matriz, current, i-1, j, index, visited)
        if respuesta:
            visited.pop()
            return True

    if j  > 0: 
        respuesta = finding_word(word, matriz, current, i, j-1, index, visited)
        if respuesta:
            visited.pop()
            return True
        
    visited.pop()
    return False

def buscar_en_matriz(word: str, board: List[List[str]]) -> bool:
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                if finding_word(word, board, current='', i=i, j=j, index=0, visited=None):
                    return True
    return False

print(buscar_en_matriz(word,board))