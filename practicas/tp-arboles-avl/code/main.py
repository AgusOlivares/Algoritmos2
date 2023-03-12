import binarytree as bt
import AVLTree as avl

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


