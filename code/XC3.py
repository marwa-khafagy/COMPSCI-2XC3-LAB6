import math


class XC3Node:
    degree = 0
    children = []
    height = 0

    def __init__(self, degree):
        self.degree = degree
        self.children = []
        self.height = 0
        self.build_tree()

    def build_tree(self):
        for i in range(1, self.degree + 1):
            if i <= 2:
                self.children.append(XC3Node(0))
            else:
                self.children.append(XC3Node(i - 2))

    def get_height(self):
        
        #Height of a tree with a node(i am a node) is at least 1
        maxx = 1

        for child in self.children:
            maxx = max(maxx, 1 + child.get_height())

        return maxx



    def get_number_of_nodes(self):
        if self.degree == 0 or self.degree == 1 or self.degree == 2:
            return self.degree + 1
        if not self.children:
            return 1
        res = 1
        for child in self.children:
            res += child.get_number_of_nodes()
        return res

    def get_string(self, tab=0):
        if not self.children:
            return "Leaf"
        res = "\n" + "\t" * tab + "["
        tab += 1
        for child in self.children:

            res += child.get_string(tab) + ", "

        res += "]"

        return res

if (__name__ == '__main__'):

    for i in range(10):
        rootx = XC3Node(i)
        print(rootx.get_string())
