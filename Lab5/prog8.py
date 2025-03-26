class cn:
    def __init__(self, data):
        self.data = data
        self.next = None  
class cll:
    def __init__(self):
        self.head = None 

    def insbeg(self, data):
        new_node = cn(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    def trav(self):
        if self.head is None:
            print("Circular linked list is empty.")
            return

        current = self.head
        while True:
            print(current.data, end="->" if current.next != self.head else "")
            current = current.next
            if current == self.head:
                break
        print("(Back to head)")


cll = cll()
cll.insbeg(10)
cll.insbeg(20)
cll.insbeg(30)
cll.insbeg(40)
cll.trav()
