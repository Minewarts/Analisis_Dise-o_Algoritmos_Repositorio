#se aplica especialmente cuando hay subproblema solapados, nos genera el mismo sub_arbol
#-Memoization - Top Down - espacial O(2n) - temporal
#-Tabulation - Bottom Up - O(n) - 

import sys
from typing import Dict, List, Tuple

'''def fibonacci(n:int , count:int = 0, memo:Dict[int:int] = {0:0,1:1})->int:

    if n in memo:
        return memo[n], count
    else:
        lfibo, count = fibonacci(n-1, count+1,memo)
        rfibo, count = fibonacci(n-2, count+1, memo)
        memo[n] = lfibo + rfibo
        return memo[n], count
sys.setrecursionlimit(8000)
print(fibonacci(800))
'''
'''def fibonacci_tab(n:int):
    c1 = 0
    c2 = 1
    for i in range(2, n+1):
        fibo = c1+c2
        c1 = c2
        c2 = fibo
    return fibo

print(fibonacci_tab(5))'''

'''def coinchange(target:int, coins:List[int], memo:Dict[int:bool] = {}, acc:int = 0, count:int = 0)->Tuple[bool, int]:
    if target==0:
        return False,count
    if acc in memo:
        if memo[acc] == True:
            return True,count
        else:
            return False,count
        

    if acc == target:
        return True,count
    if acc > target:
        memo[acc] = False
        return memo[acc],count

    for i in coins:

        r,count = coinchange(target, coins, memo, acc+i, count) 
        if r:
            memo[acc+i] = True
            count += 1
            return True,count


    memo[acc] = False
    return memo[acc],count

print(coinchange(9,[4,2,5,1]))'''

#Montañas

'''def mountains(array:List[int])->int:
    izq,der = 0,len(array)-1
    while True:
        mid = (izq+der)//2
        if array[mid]> array[mid-1] and array[mid]> array[mid+1]:
            return mid
        if array[mid]> array[mid+1]:
            der = mid-1
        if array[mid]> array[mid-1]:
            izq = mid+1'''
    

'''arr = [1, 2, 3, 1]
arr = [1, 2, 1, 3, 5, 6, 4]
print(mountains(arr))
'''

'''def finding_target_moved(array:List[int], target:int)->int:
    der,izq = len(array)-1, 0
    while True:
        mid = (der+izq)//2
        if izq > der:
            return -1
        if target == array[mid]:
            return mid

        if target > array[mid]:
            izq = mid+1

        if target <= array[der] and target < array[mid]:
            izq = mid+1

        if target > array[izq] and target < array[mid]:
            der = mid-1

print(finding_target_moved([4, 5, 6, 7, 0, 1, 2], 0))'''


#Ejercicio Escalas, se pueden subir de 1 a 3 escalas, de cuants manera se pueden subir, n escalas

'''def escalar(target:int):
    #memo = [0,1,2,4]
    c1 = 1
    c2 = 2
    c3 = 4
    for _ in range(3,target):

        r = c1 + c2 + c3
        c1 = c2
        c2 = c3
        c3 = r
    return r

print(escalar(5))
'''
        
'''def escalar(array:List[int])->int:
    c1,c2,c3 = array[0],array[1],array[2]
    r = 0
    for i in range(3,len(array)):
        r =  min(c1,c2,c3) + array[i]
        c1 = c2
        c2 = c3
        c3 = r
    return r

print(escalar([5,1,2,4,1]))
'''
def escalar(array:List[int],memo:Dict{int:int} =,count:int = 0):        
        

