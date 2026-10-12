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

def MergeSort(array:List[int])->List[int]:
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

print(MergeSort([8,9,4,8,6]))

    

        

     