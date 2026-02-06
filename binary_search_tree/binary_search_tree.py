# Un árbol es recursivo por naturaleza
# Un BST tiene una raíz y ese nodo apunta a
# otros nodos, cada nodo tiene como máximo dos
# hijos donde: 
# - el nodo izquierdo es menor y el
# - derecho es el mayor.
# Visualizador de Binary Search Tree:
# - https://www.cs.usfca.edu/~galles/visualization/BST.html

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


# Ejemplo visual:
#     8
#    / \
#   3   10
#  / \    \
# 1   6    14

class BinarySearchTree:
	def __init__(self):
		self.root = None
	
	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self._insert_recursive(self.root, data)

	def _insert_recursive(self, current, data):
		if data < current.data:
			if current.left is None:
				current.left = Node(data)
			else:
				self._insert_recursive(current.left, data)
		else:
			if current.right is None:
				current.right = Node(data)
			else:
				self._insert_recursive(current.right, data)

	def delete(self, data):
		self.root = self._delete_recursive(self.root, data)

	def _delete_recursive(self, current, data):
		if current is None:
			return current
		# Buscar nodo
		if data < current.data:
			current.left = self._delete_recursive(current.left, data)
		elif data > current.data:
			current.right = self._delete_recursive(current.right, data)
		else:
			# Nodo encontrado
			# Si no tiene hijos o solo uno:
			if current.left is None:
				return current.right
			elif current.right is None:
				return current.left
			# Si tiene dos hijos:
			# Buscar el sucesor para cambiar el puntero
			# El más pequeño a la derecha
			sucesor = self._min_node_value(current.right)
			current.data = sucesor.data
			current.right = self._delete_recursive(current.right, sucesor.data)

		return current

	def _min_node_value(self, nodo):
		current = nodo
		while current.left is not None:
			current = current.left
		return current

	def search(self, data):
		return self._search_recursive(self.root, data)

	def _search_recursive(self, current, data):
		if current is None or current.data == data:
			return current
		if data < current.data:
			return self._search_recursive(current.left, data)
		return self._search_recursive(current.right, data)

	def inorder(self):
		result = []
		self._inorder_recursive(self.root, result)
		return result

	def _inorder_recursive(self, current, result):
		if current:
			self._inorder_recursive(current.left, result)
			result.append(current.data)
			self._inorder_recursive(current.right, result)



BST = BinarySearchTree()
BST.insert(4)
BST.insert(9)
BST.insert(2)
BST.insert(11)
BST.insert(3)
BST.insert(20)

print(BST.inorder())

nodo_encontrado = BST.search(15)
print(f"¿Encontrado?: {nodo_encontrado is not None}")

BST.delete(3)
print(BST.inorder())
