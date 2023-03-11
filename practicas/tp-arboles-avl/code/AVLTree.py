class AVLTree:
  root = None


class AVLNode:
  parent = None
  leftnode = None
  rightnode = None
  key = None
  value = None
  bf = None


def rotateLeft(Tree, avlnode):
  aux = avlnode
  Tree.root = avlnode.rightnode
  aux_2 = Tree.root.leftnode
  Tree.root.leftnode = aux
   
