import AVLTree as avl

Tree = avl.AVLTree()


avl.insert(Tree, 5)
avl.insert(Tree, 10)
avl.insert(Tree, 3)
avl.insert(Tree, 7)
avl.insert(Tree, 12)
#avl.insert(Tree, 13)

## Verificacion Raiz 
# print(Tree.root.key)

## Agrega el balance factor a los nodos
## Esto hay que mejorarlo, tiene que ir dentro de las implementaciones, no hacerlo de forma manual


## Prueba reBalance

# solo 3 nodos: 5, 10, 7 ## Falla
print(Tree.root.key)

avl.reBalance(Tree)

print(Tree.root.key)
print(Tree.root)



'''
print(Tree.root.rightnode.key)





print(Tree.root.rightnode.key)

'''


