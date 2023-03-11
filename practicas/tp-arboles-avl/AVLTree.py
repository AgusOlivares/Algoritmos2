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
  Tree.root = Tree.root.rightnode
  Tree.root.leftnode = Tree.root.parent
  Tree.root.parent = None
  return Tree.root.key

  ## Falta agregar caso en que el nodo 2 tenga un hijo izq


'''
  avlnode.leftnode = Tree.root
  Tree.root = Tree.root.rightnode
  return Tree.root.key

'''