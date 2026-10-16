#se aplica especialmente cuando hay subproblema solapados, nos genera el mismo sub_arbol
#-Memoization - Top Down - espacial O(2n) - temporal
#-Tabulation - Bottom Up

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

def coinchange(target:int, coins:List[int], memo:Dict[int:bool] = {}, acc:int = 0, count:int = 0)->Tuple[bool, int]:
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

print(coinchange(9,[4,2,5,1]))

            
        

    