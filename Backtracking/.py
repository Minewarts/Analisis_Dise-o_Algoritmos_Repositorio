from typing import List
matriz = [
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
    

print (Caminos(matriz, c1, c2, k))