class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def is_leaf(self):
        return self.left == None and self.right == None
    def __str__(self):
        return "(" + str(self.value) + ")"
        

class BST:
    def __init__(self):
        self.root = None
        self.count = 0
    
    def is_empty(self):
        return self.count == 0
    
    def insert(self, value):
        if self.count == 0:
            self.root = Node(value)
        else:
            temp = self.root
            while temp:
                if value > temp.value: 
                    if not temp.right:
                        temp.right = Node(value)
                        break
                    else:
                        temp = temp.right
                elif value <= temp.value:
                    if  not temp.left:
                        temp.left = Node(value)
                        break
                    else:
                        temp = temp.left

        self.count += 1

    def get_count(self):
        return self.count
    
    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))
    
    def __str__(self):
        if self.is_empty():
            return "[]"
        return "[" + self.__str_helper(self.root) + "]"

    def __str_helper(self, node):
        if node.is_leaf():
            return "[" + str(node) + "]"
        if node.left == None:
            return "[" + str(node) + " -> " + self.__str_helper(node.right) + "]"
        if node.right == None:
            return "[" +  self.__str_helper(node.left) + " <- " + str(node) + "]"
        return "[" + self.__str_helper(node.left) + " <- " + str(node) + " -> " + self.__str_helper(node.right) + "]"


