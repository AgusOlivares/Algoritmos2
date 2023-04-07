import trie as tr

Arbol = tr.Trie()
# Caso 1: Inserto una palabra      # Funciona
tr.insert(Arbol, "Hola")
# Caso 2: Inserto varias palabras distintas      # Funciona
tr.insert(Arbol, "Rapido")
tr.insert(Arbol, "Javier")
tr.insert(Arbol, "Mameluco")
# Caso 3: Inserto palabras con el mismo prefijo sobre la "Rama Ppal"       # Funciona
tr.insert(Arbol, "Hollin")
tr.insert(Arbol, "Homero")
tr.insert(Arbol, "Hollow")
# Caso 4: Inserto palabras mas largas y mas cortas sobre la "Rama Ppal"      # Funciona
tr.insert(Arbol, "Hol")
tr.insert(Arbol, "Holanda")
tr.insert(Arbol, "Holandas")
# Caso 5: Inserto palabras distintas en ramas "secundarias"
tr.insert(Arbol, "Mama") 
tr.insert(Arbol, "Mamarracho")
tr.insert(Arbol, "Java")
tr.insert(Arbol, "Ja")
tr.insert(Arbol, "Javiera")
tr.insert(Arbol, "Rapidin")
tr.insert(Arbol, "Rapaz")



print(tr.search(Arbol, "Hola"))
print(tr.search(Arbol, "Holanda"))
print(tr.search(Arbol, "Holandas"))
print(tr.search(Arbol, "Hollin"))
print(tr.search(Arbol, "Hollow"))
print(tr.search(Arbol, "Hol"))
print(tr.search(Arbol, "Homero"))
print(tr.search(Arbol, "Mameluco"))
print(tr.search(Arbol, "Mama"))
print(tr.search(Arbol, "Mamarracho"))
print(tr.search(Arbol, "Javier"))
print(tr.search(Arbol, "Javiera"))
print(tr.search(Arbol, "Java"))
print(tr.search(Arbol, "Rapido"))
print(tr.search(Arbol, "Rapidin"))
print(tr.search(Arbol, "Rapaz"))










