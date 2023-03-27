# Ejercicio 4
def ordenar_list(list):
    medio = len(list)//2
    aux = list[medio-1] 
    izq = list[:medio-1]
    der = list[medio:]
    #print(izq)
    #print(der)
    #print(aux)
    rta = []

    while izq != [] and der != []:

        if izq != []: 
            rta.append(izq.pop())
        if der != []:
            rta.append(der.pop())

    rta.insert(medio -1 , aux)
    #print(rta)
    return rta


#Ejemplo 1:
print("Caso 1: ")
list = [7,3,2,8,5,4,1,6,10,9]
print(list)
list.sort() #O(n log n)
print(list)
list = ordenar_list(list)
print(list)
print("___"*10)
#Ejemplo 2:
print("Caso 2: ")
list = [7,3,2,8,5,4,1,6,10,9,13,12,11,20,19,15,17,18,16,14]
print(list)
list.sort() #O(n log n)
print(list)
list = ordenar_list(list)
print(list)
print("___"*10)
#Ejemplo 3:
print("Caso 3: ")
list = [7,3,2,8,5,4,1,6,10,9,13,12,11]
print(list)
list.sort() #O(n log n)
print(list)
list = ordenar_list(list)
print(list)


# Ejercicio 5

#Al contener la funcion sort, la complejidad se eleva a O(n log n) en el peor de los casos
# Tita(n log n)
# Omega(n)

def contiene_suma(A, n): 
    A.sort() # O(n log n)
    left = 0
    right = len(A) - 1
    while left < right:
        suma = A[left] + A[right]
        if suma == n:
            return True
        elif suma < n:
            left += 1
        else:
            right -= 1
    return False
