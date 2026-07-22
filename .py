entrada_1 = "a"*5 + "b" + "a"*5
lista_no_rep = []
"""for i in range(len(entrada_1)):
    aux_string = entrada_1[:i]
    if  (entrada_1[i] in aux_string) == False:
        lista_no_rep.append(entrada_1[i])
    else:
        if entrada_1[i] in lista_no_rep == True:
            lista_no_rep.remove(entrada_1[i])

if lista_no_rep is not []:
    print(lista_no_rep)
"""
for i in range(len(entrada_1)):
    aux_string = entrada_1[i:]
    print(entrada_1[i],aux_string)
    if entrada_1[i] not in aux_string or entrada_1[i]== aux_string:
        s = entrada_1[i]
        break
    else:
        s = None
    print(s)


print(s)



