import trie as tr

Arbol = tr.Trie()
# Caso 1: Inserto una palabra     # Funciona
tr.insert(Arbol, "Hola")
# Caso 2: Inserto varias palabras distintas      # >2 Falla
tr.insert(Arbol, "Rapido")
tr.insert(Arbol, "Javier")
tr.insert(Arbol, "Mameluco")
# Caso 3: Inserto palabras con el mismo prefijo sobre la "Rama Ppal" 
tr.insert(Arbol, "Hollin")
tr.insert(Arbol, "Hollow")
# Caso 4: Inserto palabras mas largas sobre la "Rama Ppal"
tr.insert(Arbol, "Holanda")