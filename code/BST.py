class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def is_leaf(self):
        return self.left and self.right
        



class BST:
    def __init__(self):
        self.root = None
        self.height = 0
    
    def is_empty(self):
        return self.height == 0
    
    def add(self, value):
        if self.height == 0:
            self.root = Node(value)
        else:
            temp = self.root
            while temp.right or temp.left:
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

        self.height += 1

    def get_height(self):
        return self.height
    
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


                

