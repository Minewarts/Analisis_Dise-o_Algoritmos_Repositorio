from typing import List
import string

mensj = "dyshéjkgfysimésdgójésáék aíjyjsékléseéfkybéskésóyfyjtsmfshmflgsáéshyj ayd"

alf = string.ascii_lowercase + " áéíóú"

def descifrado_cesar (mensaje:str, alf:str)->List[str]:
    index = [l for l in range (len(mensaje))]
    print(len(mensaje))
    
    

    for i in range(len(alf)):
        mensaje_final = ""
        text=[alf[-i:]+alf[:-i]]
        print("\n -",text)


        index = [l for l in range (len(mensaje))]
        for j,value_j in enumerate(text):
            for k,value_k in enumerate(mensaje):
                if value_j == value_k: 
                    index[k] = j
                    print("\n",index)

        
        for n in range(len (alf)):
            for m in range (len(index)):
                if index[m] == n:
                    mensaje_final += alf[m]

        print(mensaje_final)

descifrado_cesar(mensj,alf)


def combinaciones_dos_1 (cifras:int)->List[int]:

    combinaciones = []
    ...