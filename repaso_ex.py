from typing import List 

# =====================================================================
# GUÍA DE COMPLEJIDAD DE TIEMPO (BIG O) - LISTAS Y DICCIONARIOS
# =====================================================================
# n = cantidad de elementos en la estructura actual
# k = cantidad de elementos en la estructura que se pasa como parámetro

# ---------------------------------------------------------------------
# 1. MÉTODOS DE LISTAS (Arrays dinámicos)
# ---------------------------------------------------------------------
# mi_lista.append(x)       # O(1)      - Agrega un elemento al final.
# mi_lista.pop()           # O(1)      - Elimina y devuelve el último elemento.
# len(mi_lista)            # O(1)      - Obtiene el tamaño de la lista.
# mi_lista[i]              # O(1)      - Acceso directo a un índice.
# mi_lista[i] = x          # O(1)      - Asignación en un índice específico.

# mi_lista.pop(i)          # O(n)      - Elimina en índice 'i' (rueda los demás).
# mi_lista.insert(i, x)    # O(n)      - Inserta en índice 'i' (rueda los demás).
# mi_lista.remove(x)       # O(n)      - Busca 'x' y lo elimina (rueda los demás).
# mi_lista.index(x)        # O(n)      - Busca 'x' secuencialmente.
# mi_lista.count(x)        # O(n)      - Recorre toda la lista contando 'x'.
# mi_lista.reverse()       # O(n)      - Invierte los elementos en su lugar.
# mi_lista.copy()          # O(n)      - Crea una copia nueva en memoria.
# x in mi_lista            # O(n)      - Búsqueda secuencial.
# min/max/sum(mi_lista)    # O(n)      - Recorre todos los elementos.

# mi_lista.extend(iter)    # O(k)      - Agrega 'k' elementos al final.
# mi_lista[i:j]            # O(k)      - Slicing: copia 'k' elementos a nueva lista.

# mi_lista.sort()          # O(n log n)- Ordena la lista (algoritmo Timsort).

# ---------------------------------------------------------------------
# 2. MÉTODOS DE DICCIONARIOS (Tablas Hash)
# ---------------------------------------------------------------------
# Nota: Para diccionarios, la complejidad mostrada es el "Caso Promedio".
# En el "Peor Caso" (colisiones masivas de hash), casi todas las O(1) 
# podrían degradarse a O(n), pero en Python esto es extremadamente raro.

# dicc[clave]              # O(1)      - Acceso al valor de la clave.
# dicc[clave] = valor      # O(1)      - Creación o actualización de clave.
# del dicc[clave]          # O(1)      - Eliminación de una clave.
# clave in dicc            # O(1)      - Verifica si la clave existe (¡muy rápido!).
# len(dicc)                # O(1)      - Obtiene cantidad de pares.
# dicc.get(clave, def)     # O(1)      - Obtiene valor o el 'def' si no existe.
# dicc.pop(clave, def)     # O(1)      - Elimina clave y devuelve su valor.
# dicc.popitem()           # O(1)      - Elimina y devuelve el último par insertado.
# dicc.setdefault(c, v)    # O(1)      - Obtiene valor, si no existe lo crea con 'v'.
# dicc.clear()             # O(1)      - Vacía el diccionario.

# dicc.keys()              # O(1)*     - (*Crear la vista es O(1), iterarla es O(n)).
# dicc.values()            # O(1)*     - (*Crear la vista es O(1), iterarla es O(n)).
# dicc.items()             # O(1)*     - (*Crear la vista es O(1), iterarla es O(n)).

# dicc.copy()              # O(n)      - Crea una copia independiente del diccionario.
# dict.fromkeys(iter, v)   # O(k)      - Crea dicc a partir de 'k' elementos del iter.
# dicc.update(otro_dicc)   # O(k)      - Fusiona 'k' elementos del otro_dicc.
# =====================================================================

def Permutaciones(lista:List[int])->List[int]:
    if len(lista)<= 1:
        return [lista]


    permutaciones=[]
    for i in range (len(lista)):
        actual = lista[i]
        resto = lista[:i] + lista[i+1:]

        for j in Permutaciones(resto):
            permutaciones.append([actual]+j)
        print(permutaciones)

    return permutaciones