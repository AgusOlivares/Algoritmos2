import dictionary as d
import parte2 as pt2


dict = d.Dictionary(None, 3)

### Insert
## Si el diccionario esta vacio
dict.insert(dict.D, 0, "Papá") #0
dict.insert(dict.D, 1, "Mandarina") #1
dict.insert(dict.D, 2, "Par") #2
## Si no esta vacio
dict.insert(dict.D, 3, "Pan") #0 
dict.insert(dict.D, 4, "Pera") #1 
dict.insert(dict.D, 5, "Rapaz") #2 
dict.insert(dict.D, 6, "Remo") #0
## Si hay una key repetida
dict.insert(dict.D, 0, "Paralelo")
## Si en la key hay un valor repetido
dict.insert(dict.D, 7, "Papá")

### Search
print(dict.search(dict.D, 0))
print(dict.search(dict.D, 10))
print(dict.search(dict.D, 6))
print(dict.search(dict.D, 2))

### Delete
dict.delete(dict.D, 6)
dict.delete(dict.D, 4)
dict.delete(dict.D, 80)
## Inserto en los lugares cosas nuevas
dict.insert(dict.D, 4, "Pragmatico") #1 
dict.insert(dict.D, 6, "H0") #1 
 



# PARTE 2


## Ejercicio 3: En papel

## Ejercicio 4: 

print(pt2.isPermutation("hola", "oahl"))
print(pt2.isPermutation_ver2("hola", "oahl")) 


## Ejercicio 5: 

lista_a = [2, 1, 1, 9]
lista_b = [2, 22, 1, 5]
lista_c = ["a", "h", "g"]
lista_d = ["a", "a", "h"]

print(pt2.isConj(lista_a))
print(pt2.isConj(lista_b))
print(pt2.isConj(lista_c))
print(pt2.isConj(lista_d))
print(pt2.isConj_v2(lista_a))
print(pt2.isConj_v2(lista_b))


## Ejercio 6:

dict = d.Dictionary(pt2.Codigo_postal_hash, 100003)

pt2.codigo_postal(dict, "A9341ZJK")
pt2.codigo_postal(dict, "A9371ZJZ")
pt2.codigo_postal(dict, "Z9281KLZ")
pt2.codigo_postal(dict, "K9913LPQ")
pt2.codigo_postal(dict, "L0012ZLP")
pt2.codigo_postal(dict, "U0912KKK")


## Ejercicio 7:
print(pt2.compress("aabcccccaaa")) 
print(pt2.compress("asd"))
 
## Ejercicio 8:

print(pt2.isIn("xxxxyxxxxzzxxxxyz", "xxz"))
print(pt2.isIn_v2("lava", "va"))  # intento con tablas hash


