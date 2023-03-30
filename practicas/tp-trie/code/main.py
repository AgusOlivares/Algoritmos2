import trie as tr

Arbol = tr.Trie()

tr.insert(Arbol, "hola")
print(Arbol.root.children.key)