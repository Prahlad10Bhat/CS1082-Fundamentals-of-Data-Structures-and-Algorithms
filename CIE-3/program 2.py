class Node():
    def __init__(self, data):
        self.data= data
        self.next= None 
class Stack():
    def __init__(self):
        self.top = None 

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.empty():
            print("Stack is empty!")
            return None
        popped_node = self.top 
        self.top = self.top.next  
        popped_node.next = None  
        return popped_node.data
    def peek(self):
        if self.empty():
            print("Stack is empty!")
            return None
        return self.top.data
    def empty(self):
        return self.top is None 

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())  
    print("Pop:", stack.pop())
    print("Peek after pops:", stack.peek())
    print("Is the stack empty?", stack.empty())
    print("Pop:", stack.pop())
    print("Is the stack empty now?", stack.empty())
