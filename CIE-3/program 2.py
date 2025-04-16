
class TreeNode():
    def __init__(self, data):
        self.data = data  #the data storeed in node
        self.left = None  #left child
        self.right = None  #right child

class BinaryTree:
    def __init__(self):
        self.root = None  #root of the binary tree
#this is to insert data into binarytree
    def insert(self, data):
        new_node = TreeNode(data)  #creating a new node
        if self.root is None:
            self.root = new_node  #if the tree is empty the new node is root
        else:
            self._insert_recursive(self.root, new_node) #if its not empty the new node gets added in order recursive

    def _insert_recursive(self, current_node, new_node):
   
        if new_node.data < current_node.data:  #if the data is less than the current node
            if current_node.left is None:
                current_node.left = new_node  #insert to the left
            else:
                self._insert_recursive(current_node.left, new_node)  #recur to the left
        else:  #the data is greater or equal to current node
            if current_node.right is None:
                current_node.right = new_node  #insert to the right
            else:
                self._insert_recursive(current_node.right, new_node)  # recur to the right
    def in_order_traversal(self):#this is to perform in order and to return traversal
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)  #traverse the left subtree
            result.append(node.data)  #visit the node
            self._in_order_recursive(node.right, result)  #traverse the right subtree

#example below
if __name__ == "__main__":
    tree = BinaryTree()
   
    #inserting data into the binary tree
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)
    tree.insert(12)
    tree.insert(20)
   
    #performing in-order traversal and printing the result
    print("In-order traversal:", tree.in_order_traversal())
