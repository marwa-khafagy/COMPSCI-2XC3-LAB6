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
        if self.degree <= 2:
            for i in range(self.degree):
                self.children.append(XC3Node(0))
        else:
            for i in range(self.degree - 1):
                self.children.append(XC3Node(0))
            self.children.append(XC3Node(self.degree - 2))

    def get_height(self):
        return math.ceil(self.degree / 2)

    def get_number_of_nodes(self):
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


root = XC3Node(5)
print(root.get_string())
print(root.get_height())
print(root.get_number_of_nodes())
