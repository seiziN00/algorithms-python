from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        # Mientras exista un nodo next, entra al bucle
        while current.next:
            current = current.next

        current.next = new_node

    def delete_first(self):
        # Python libera el objeto automáticamente cuando no hay referencias
        self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return
            
        current = self.head
        # El siguiente del siguiente exista
        while current.next.next:
            current = current.next
        current.next = None

    def print_list(self):
        current = self.head
        # Aquí si quiero llegar a None
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    
    def search(self, target):
        current = self.head
        while current:
            if current.data == target:
                return True
            current = current.next
        return False


ll = LinkedList()
ll.insert_at_beginning(12)
ll.insert_at_beginning(17)
ll.insert_at_beginning(5)
ll.insert_at_end(21)
ll.insert_at_end(9)

ll.print_list()

ll.delete_first()

ll.print_list()

ll.delete_last()
ll.delete_last()
ll.delete_last()

ll.print_list()