class Node:
    def __init__(self, value, height):
        self.value = value
        self.right = None
        self.left = None
        self.height = height #assumption, doesn't change

    def is_leaf(self):
        return self.left == None and self.right == None
    def __str__(self):
        return "(" + str(self.value) + ")"
        

class BST:
    def __init__(self):
        self.root = None
        self.count = 0
        self.max_height = 0
    
    def is_empty(self):
        return self.count == 0
    
    def insert(self, value):
        if self.is_empty():
            self.root = Node(value, 1)
            self.max_height = 1
        else:
            temp = self.root
            while temp:
                if value > temp.value: 
                    if not temp.right:
                        temp.right = Node(value, temp.height+1)
                        self.max_height = max(self.max_height, temp.height+1)
                        break
                    else:
                        temp = temp.right
                elif value <= temp.value:
                    if  not temp.left:
                        temp.left = Node(value, temp.height+1)
                        self.max_height = max(self.max_height, temp.height+1)
                        break
                    else:
                        temp = temp.left

        self.count += 1

    def get_count(self):
        return self.count
    
    def get_height(self):
        return self.max_height
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def find_min(self):
        return self._find_min(self.root)

    def _find_min(self, node):
        if (node.left is None):
            return node
            
        return self._find_min(node.left)

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"


if (__name__ == '__main__'):
    tree =  BST()
    tree.insert(5)
    tree.insert(1)
    tree.insert(2)
    tree.insert(12)
    print(tree)
    print(tree.find_min())