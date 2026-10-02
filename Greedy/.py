from typing import List
import heapq as hq

#                                  Ejercicio 1
#--------------------------------------------------------------------------------#
'''
boleto_1 = [2,4,2,1]
boleto_2 = [0,1,3,5]
boleto_3 = [3,7,5,4]

def combinaciones_menor_or_mayor(lista: List[int])->bool:
    mitad_1 = lista[:len(lista)//2]
    mitad_2 = lista[len(lista)//2:]
    mitad_1 = sorted(mitad_1)
    mitad_2 = sorted(mitad_2)

    my = False
    mn = False
    for i in range(len(mitad_1)):
        if mitad_1 [i] > mitad_2[i]:
            my = True
        if mitad_1 [i] < mitad_2[i]:
            mn = True

        if my and mn:
            return False

    return True

print(combinaciones_menor_or_mayor(boleto_1))
print(combinaciones_menor_or_mayor(boleto_2))
print(combinaciones_menor_or_mayor(boleto_3))
'''

#                                  Ejercicio 2
#--------------------------------------------------------------------------------#
'''s1="RLRRLLRLRL"
s2="RLLLLRRRLR"
s3="LLLLRRRR"
s4="RLRRRLLRLL"


def sub_cadenas_balanceadas(string:str)->int:
    i = 0
    count_R,count_L = 0,0
    count = 0
    while i<len(string) :

        if string[i] == 'R':
            count_R += 1
            i += 1
            if count_L == count_R:
                count+= 1
                count_R = 0
                count_L = 0

        if i == len(string):
            break
        
        if string[i] == 'L':
            count_L += 1
            i += 1
            if count_L == count_R:
                count+= 1
                count_R = 0
                count_L = 0
        

    return count
print(sub_cadenas_balanceadas(s1))
print(sub_cadenas_balanceadas(s2))
print(sub_cadenas_balanceadas(s3))
print(sub_cadenas_balanceadas(s4))'''


#                                  Ejercicio 3
#--------------------------------------------------------------------------------#

'''s1 = "cczazcc"; repeat_limit_1 = 3
s2 = "aababab"; repeat_limit_2 = 2

def order_limit(string:str, limit:int)->str:
    string = ''.join(sorted(string, reverse=True))
    
    count = 0 
    for i in range(len(string)):
        if i != 0 and string[i] != string[i-1]:
            count = 0

        count += 1
        if count > limit:
            if string[-1] == string[i]:
                return string[:i]
            string = string[:i] + string[-1] + string[i:-1]
            


    return string

print(order_limit(s1,repeat_limit_1))
print(order_limit(s2,repeat_limit_2))'''