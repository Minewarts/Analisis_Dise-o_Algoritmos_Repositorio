from typing import List
import string

mensj = "dyshéjkgfysimésdgójésáék aíjyjsékléseéfkybéskésóyfyjtsmfshmflgsáéshyj ayd"

alf = string.ascii_lowercase + " áéíóú"

'''def descifrado_cesar (mensaje:str, alf:str)->None:
    for desplazamiento in range(len(alf)):
        mensaje_final = ""
        
        for letra in mensaje:
            if letra in alf:
                # Buscamos el índice original y aplicamos el desfase modular
                indice_original = alf.index(letra)
                nuevo_indice = (indice_original - desplazamiento) % len(alf)
                mensaje_final += alf[nuevo_indice]
            else:
                # Si es un espacio o símbolo no definido, lo dejamos intacto
                mensaje_final += letra
                
        print(f"Desplazamiento {desplazamiento}: {mensaje_final}")
        

descifrado_cesar(mensj,alf)
'''

def combinaciones_dos_1 (cifras:int)->List[int]:

    combinaciones : List[str]= []
    aux_combinaciones : List [List[int]]= []
    for i in range (10):
        aux_combinaciones.append([i])


    while aux_combinaciones :
        current = aux_combinaciones.pop(0)
        if len(current) == cifras:
            combinaciones.append(current)
            continue

        
        for i in range (10):
            aux_combinaciones.append(current+[i])

    
    combinaciones_validas: List[List[int]] = []
        
    for comb in combinaciones:
        tiene_dos_unos = False
        for num in range(len(comb) - 1):
            if comb[num] == 1 and comb[num + 1] == 1:
                tiene_dos_unos = True
                break
        
        if not tiene_dos_unos:
            combinaciones_validas.append(comb)

    return combinaciones_validas

print(combinaciones_dos_1(4))




    