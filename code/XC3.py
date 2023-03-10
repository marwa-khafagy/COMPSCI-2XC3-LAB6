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
        return math.ceil(self.degree / 2)

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


rootx = XC3Node(0)
rooty = XC3Node(1)
root = XC3Node(2)
root0 = XC3Node(3)
root1 = XC3Node(4)
root2 = XC3Node(5)
root3 = XC3Node(6)
root4 = XC3Node(7)
root5 = XC3Node(8)
root6 = XC3Node(9)
print(rootx.get_number_of_nodes())
print(rooty.get_number_of_nodes())
print(root.get_number_of_nodes())
print(root0.get_number_of_nodes())
print(root1.get_number_of_nodes())
print(root2.get_number_of_nodes())
print(root3.get_number_of_nodes())
print(root4.get_number_of_nodes())
print(root5.get_number_of_nodes())
print(root6.get_number_of_nodes())
print(root0.get_string())
