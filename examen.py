from typing import List
import string

mensj = "dyshéjkgfysimésdgójésáék aíjyjsékléseéfkybéskésóyfyjtsmfshmflgsáéshyj ayd"

alf = string.ascii_lowercase + " áéíóú"

def descifrado_cesar (mensaje:str, alf:str)->List[str]:
    index_og = []
    print(len(mensaje))
    for j,value_j in enumerate(alf):
        for k,value_k in enumerate(mensaje):
            if value_j == value_k: 
                index_og[k] = j
                print("\n",index_og)

    for i in range(len(alf)):
        mensaje_final = ""
        text=[alf[-i:]+alf[:-i]]
        print("\n -",text)
        
        for n in range(len(index_og)):
            for m in range (len (text)):
                if index_og[n] == m:
                    mensaje_final += text[m]

        print(mensaje_final)

descifrado_cesar(mensj,alf)


def combinaciones_dos_1 (cifras:int)->List[int]:

    combinaciones = []
    ...