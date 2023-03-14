import binarytree as bt
import AVLTree as avl

Tree = avl.AVLTree()
#nodo1
A = avl.AVLNode
A.key = 5

#nodo2
B = avl.AVLNode()
B.key = 10

#nodo3
C = avl.AVLNode()
C.key = 3

#nodo4
D = avl.AVLNode()
D.key = 14

#nodo5
E = avl.AVLNode()
E.key = 12

avl.insert(Tree, 5)
avl.insert(Tree, 10)
avl.insert(Tree, 3)
avl.insert(Tree, 14)
avl.insert(Tree, 12)


print(Tree.root.key)

## Agrega el balance factor a los nodos
avl.calculateBalance(Tree)


