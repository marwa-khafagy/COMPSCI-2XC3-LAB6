class RBNode:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.colour = "R"

    def is_leaf(self):
        return self.left == None and self.right == None

    def is_left_child(self):
        return self == self.parent.left

    def is_right_child(self):
        return not self.is_left_child()

    def is_red(self):
        return self.colour == "R"

    def is_black(self):
        return not self.is_red()

    def make_black(self):
        self.colour = "B"

    def make_red(self):
        self.colour = "R"

    def get_brother(self):
        if self.parent.right == self:
            return self.parent.left
        return self.parent.right

    def get_uncle(self):
        return self.parent.get_brother()

    def uncle_is_black(self):
        if self.get_uncle() == None:
            return True
        return self.get_uncle().is_black()

    def __str__(self):
        return "(" + str(self.value) + "," + self.colour + ")"

    def __repr__(self):
         return "(" + str(self.value) + "," + self.colour + ")"

    def rotate_right(self):

        #We are a left child

        #attach my left child to my parent's right
        self.parent.right = self.left
        if (self.left != None):
            self.left.parent = self.parent

        # I am now decoupled from the tree

        #Get what needs to be moved
        leftsRight = None
        if self.left != None:
            leftsRight = self.left.right

        #Put me Below my Left Child Now
        self.left.right = self;
        self.parent = self.left;
    
        #Move Subtree below me
        self.left = leftsRight
        if (leftsRight != None):
            leftsRight.parent = self

    def rotate_left(self):
        
        self.parent.right = self.right
        if (self.right != None):
            self.right.parent = self.parent

         # I am now decoupled from the tree

        #Get what needs to be moved
        rightsLeft = None
        if self.right != None:
            rightsLeft = self.right.left

        #Put me Below my Left Child Now
        self.right.left = self;
        self.parent = self.right;
    
        #Move Subtree below me
        self.right = rightsLeft
        if (rightsLeft != None):
            rightsLeft.parent = self


class RBTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def get_height(self):
        if self.is_empty():
            return 0
        return self.__get_height(self.root)

    def __get_height(self, node):
        if node == None:
            return 0
        return 1 + max(self.__get_height(node.left), self.__get_height(node.right))

    def insert(self, value):
        if self.is_empty():
            self.root = RBNode(value)
            self.root.make_black()
        else:
            self.__insert(self.root, value)

    def __insert(self, node, value):
        if value < node.value:
            if node.left == None:
                node.left = RBNode(value)
                node.left.parent = node
                self.fix(node.left)
            else:
                self.__insert(node.left, value)
        else:
            if node.right == None:
                node.right = RBNode(value)
                node.right.parent = node
                self.fix(node.right)
            else:
                self.__insert(node.right, value)

    def fix(self, node):
        #You may alter code in this method if you wish, it's merely a guide.
        if node.parent == None:
            node.make_black()

        while node != None and node.parent != None and node.parent.is_red(): 
            
            #We insert nodes as red, therefor parent is red

            #Get Uncle Redness
            uncle = node.get_uncle()
            redUncle = False
            if uncle != None:
                redUncle = uncle.is_red()

            #Perform Color flip
            if (redUncle):
                node.parent.make_black()
                node.parent.parent.make_red()
                node.get_uncle().make_black()

                node = node.parent.parent

            #Rotate
            else:

                # Check if it is a line or triangle rotation
                leftChild = node.is_left_child()
                lineRotation = leftChild == node.parent.is_left_child()


                if (lineRotation):

                    #Rotate Grand Parent
                    if (leftChild):
                        node.parent.parent.rotate_right()
                    else:
                        node.parent.parent.rotate_left()

                    # Recolour!!
                    # These are the new references
                    node.parent.make_black()
                    if (node.get_brother() != None):
                        node.get_brother().make_red()

                #Triangle
                else:

                    #Rotate Parent
                    prevParent = node.parent
                    if (leftChild):
                        prevParent.rotate_right()
                        node.parent.rotate_left() #new parent

                        node.make_black()
                        node.left.make_red()
                        node.right.make_red()
                    else:
                        prevParent.rotate_left()
                        node.rotate_right()
                        
                        #if (grandparent != None):
                            #node.rotate_right()


                    #Continue Self, Retest


        #Ensure Black Root (subsequent black nodes allowed)
        self.root.make_black()
                    
        
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

#
#
#

t = RBTree()
insertions = [3, 1, 5, 7, 6, 8, 9, 10]

for insertion in insertions:


    if (insertion == insertions[-1]):
        hi = 0
    t.insert(insertion)

    print(t)

pass