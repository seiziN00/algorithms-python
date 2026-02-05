# Este algoritmo tiene es lo mismo en cuanto a
# nodos con un 'data' y un 'next', pero también apunta
# al nodo anterior, o sea que tiene un 'prev'
# None ← [5] ⇄ [12] ⇄ [17] → None

# Hay head y tail

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert_at_begginig(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = self.tail = new_node
			return

		new_node.next = self.head
		self.head.prev = new_node
		self.head = new_node

	def insert_at_end(self, data):
		new_node = Node(data)

		if self.tail is None:
			self.head = self.tail = new_node
			return

		new_node.prev = self.tail
		self.tail.next = new_node
		self.tail = new_node

	def print_forward(self):
		current = self.head
		while current:
			print(current.data, end=" ⇄ ")
			current = current.next
		print("None")

	def print_backward(self):
		current = self.tail
		while current:
			print(current.data, end=" ⇄ ")
			current = current.prev
		print("None")

	def delete_first(self):
		if self.head is None:
			return

		if self.head == self.tail:
			self.head = self.tail = None
			return

		self.head = self.head.next
		self.head.prev = None

	def delete_last(self):
		if self.tail is None:
			return

		if self.head == self.tail:
			self.head = self.tail = None
			return

		self.tail = self.tail.prev
		self.tail.next = None


dll = DoublyLinkedList()
dll.insert_at_begginig(12)
dll.insert_at_begginig(5)
dll.insert_at_begginig(23)
dll.insert_at_end(17)
dll.insert_at_end(19)
dll.print_forward()
dll.print_backward()
dll.delete_last()
dll.delete_last()
dll.delete_first()
dll.print_forward()
dll.print_backward()

# node1 = Node(5)
# node2 = Node(12)
# node3 = Node(17)

# node1.next = node2

# node2.prev = node1
# node2.next = node3

# node3.prev = node2

# print("node 1:")
# print("→ data:", node1.data)
# print("→ prev:", node1.prev)
# print("→ next:", node1.next.data)

# print("node 2:")
# print("→ data:", node2.data)
# print("→ prev:", node2.prev.data)
# print("→ next:", node2.next.data)

# print("node 3:")
# print("→ data:", node3.data)
# print("→ next:", node3.next)
# print("→ prev:", node3.prev.data)