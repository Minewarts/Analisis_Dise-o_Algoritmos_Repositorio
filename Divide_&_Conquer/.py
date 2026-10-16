from typing import List
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
'''def Count(array:List[int],target:int)->int:
    i = 0
    j = len(array)
    flag = False
    while True:
        if not flag:
            mid = (j+i)//2
            if i == j:
                if i >= len(array) or array[i] != target:
                    return 0
                flag = True
                r_i = i 
                i = 0
                j = len(array) - 1 
                continue
            if array[mid] >= target:
                j = mid
            elif array[mid] < target:
                i = mid+1

        else:
            mid = (j+i)//2 + 1
            if i == j:
                return j - r_i + 1        
            if array[mid] <= target:
                i = mid
            elif array[mid] > target:
                j = mid-1
    


print(Count([1, 2, 3, 4, 5, 5, 5, 5, 5, 6], 5))
'''

##Merge Sort

'''def MergeSort(array:List[int])->List[int]:
    if len(array) == 0:
        return []
    if len(array) == 1:
        return array
    mid = len(array)//2
    a_left = MergeSort(array[:mid])
    a_right = MergeSort(array[mid:])
    p_left = 0 
    p_right = 0
    r_array = []

    if a_left[-1] <= a_right[0]:
        return a_left+a_right
    while p_right < len(a_right) and p_left<len(a_left):
        
        if a_left[p_left] <= a_right[p_right]: 
            r_array.append(a_left[p_left])
            p_left += 1

        else: 
            r_array.append(a_right[p_right])
            p_right += 1
    
    r_array.extend(a_left[p_left:])
    r_array.extend(a_right[p_right:]) 
    
    return r_array

print(MergeSort([8,9,4,8,6]))'''


#N/2 --- n+1
'''Dado un número entero positivo n, se pueden aplicar las siguientes operaciones:

Si n es par, reemplázalo por n / 2.
Si n es impar, reemplázalo por n + 1 o n - 1.
Tu tarea consiste en retornar el número mínimo de operaciones necesarias para que n se convierta en 1.'''


'''def n_op(n:int)->int:
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + n_op(n//2)
    else:
        return min(1+n_op(n-1),1+n_op(n+1))

print(n_op(7))
'''
    
#count pero con los dos ultimos valores

'''def Count(array:List[int],target:int,k:int)->List[int]:
    i = 0
    j = len(array)
    flag = False
    while True:
        if not flag:
            mid = (j+i)//2
            if i == j:
                if i >= len(array) or array[i] != target:
                    return []
                flag = True
                r_i = i 
                i = 0
                j = len(array) - 1 
                continue
            if array[mid] >= target:
                j = mid
            elif array[mid] < target:
                i = mid+1

        else:
            mid = (j+i)//2 + 1
            if i == j:
                if k > (j-r_i)+1:
                    raise ValueError('No hay suficientes ocurrencias')
                return array[j-k+1:j+1]
                     
            if array[mid] <= target:
                i = mid
            elif array[mid] > target:
                j = mid-1

print(Count([3, 5, 7, 7, 7, 7, 9, 11, 11],7,6))'''

'''def find_less_dif(array:List[int], curr_dif:int= float("inf"), curr_index:int= None,i:int = 0,j:int = None)->int:
    
    if j is None:
        j = len(array) - 1

    if i > j:
        return curr_index
    
    if curr_dif is None:
        curr_dif = float("inf")

    mid = (i+j)//2
    dif = array[mid] - mid 
     
    if dif == 0:
        return mid
    if abs(dif) <= curr_dif:
        curr_index = mid
        curr_dif = abs(dif)

    if dif > 0:
        j = mid-1     
    if dif < 0:
        i = mid+1

    min = find_less_dif(array, curr_dif, curr_index, i, j)
    return min
    
print(find_less_dif([-10, -5, -1, 4, 6, 9]))
'''


#maximo array con que este dentro del limite de la suma
def max_array_limit_sum(array:List[int], limit_array:List[int])->List[int]:
    array.sort()
    r_array = []
    acc = 0
    acc_array = []
    for i in array:
        acc+=i
        acc_array.append(acc)

    for j in limit_array:
        left = 0
        right = len(acc_array) - 1
        max = float("-inf")
        while True:
            if left>right:
                break
            mid = (left+right)//2
            if acc_array[mid] == j:
                max = mid
                break
            if acc_array[mid] > j:
                right = mid-1 
            if acc_array[mid] < j:
                left = mid+1 
            if  mid > max and acc_array[mid] < j:
                max = mid 


        r_array.append(max+1)

    return r_array

print(max_array_limit_sum([4,5,2,1],[3,10,21]))
