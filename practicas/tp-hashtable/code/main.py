import dictionary as d


# Los comandos de abajo estan hechos para una lista de longitud 3
# list = [None]*int(input("Longitud de tabla = "))        # Asi puedo hacer una lista de longitud n
list = [None]*3



d.insert(list, 5, "Papá") #2
d.insert(list, 9, "Mandarina") #0
d.insert(list, 7, "Par") #1
d.insert(list, 13, "Pan") #1
d.insert(list, 24, "Pera") #0

#print(d.delete(list, 9))


#print(list)

print(d.isConj("elm"))