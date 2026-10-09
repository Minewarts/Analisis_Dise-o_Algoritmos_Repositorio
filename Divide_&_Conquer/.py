from typing import List
## leet code aceptance  - code Forces divide and conquered
'''def n_medios(array:List[int], target:int, i:int = 0 , j :int =None)->bool:
    print(j)
    if len(array) == 0: 
        return False
    if array[len(array)//2]!= target and j == None:
        return False
    if j == None:
        j = len(array)//2

    mid = (j+i)//2

    if i == j:
        if i >= len(array)//2:
            return False
        if array[i+len(array)//2] == target:
            return True
        return False

    if array[mid] < target:
        i = mid+1
    if array[mid] == target:
        j=mid
    
    if n_medios(array,target, i,j):
        return True

    return False

print(n_medios([0,0,0,1,1,2],1))'''


##contar cuantos valores hay de un numero en un array ordenado de menor a mayor
