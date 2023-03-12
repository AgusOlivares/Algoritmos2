import binarytree as bt
import AVLTree as avl

'''
B = bt.BinaryTree()
bt.insert(B , "A" , 10)
bt.insert(B , "B" , 12)
bt.insert(B , "D" , 11) 
bt.insert(B , "C" , 15) 


print(B.root.value)
print(B.root.rightnode.value)
print(B.root.rightnode.leftnode.value)
print(B.root.rightnode.rightnode.value)
print("--"*5)

B = avl.rotateLeft(B , B.root )
print(B.value)
print(B.leftnode.value)
print(B.rightnode.value)
print(B.leftnode.rightnode.value)

'''
## Codigo de pruba hecho por victor, probar

#Llenamos un arbol avl
B = avl.AVLTree()
#Nodo 1
nodeA = avl.AVLNode()
nodeA.value = "A"
nodeA.key = 10
#Nodo B
nodeB = avl.AVLNode()
nodeB.value = "B"
nodeB.key = 5
#Nodo C
nodeC = avl.AVLNode()
nodeC.value = "C"
nodeC.key = 15

#Nodo D
nodeD = avl.AVLNode()
nodeD.value = "D"
nodeD.key = 3

#Hacemos que el B.root sea el nodoA y asignamos los hijos de A
nodeA.leftnode = nodeB
nodeA.rightnode = nodeC
nodeA.leftnode.leftnode = nodeD
B.root = nodeA

new_arbol = avl.calculateBalance(B.root)

print(new_arbol.bf)
print(new_arbol.leftnode.bf)
print(new_arbol.rightnode.bf)
print(new_arbol.leftnode.leftnode.bf)