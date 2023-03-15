from XC3 import XC3Node
from plotting import PlotGroup
import matplotlib.pyplot as plot

'''
Create XC3-Trees with degrees 0 to 25. In your report, based off your trees write an equation for
nodes(i), where nodes(i) returns the number of nodes in a degree i XC3-Tree. At first glance this may
seem tricky, but take a look at the values and see if you can find a pattern. Have you seen this pattern or
a similar pattern to this before. You do not need to formally prove your claim, but give a plain English
explanation to why you believe your claim holds. This explanation should relate back to the structure of
XC3-Trees.
'''

def test():

    #New Dict
    nodes = PlotGroup("Node Count of XC3 Tree")

    rang = range(0,25,1)
    for i in rang:
        root = XC3Node(i)
        n = root.get_number_of_nodes()
        nodes.add_point(i, n)
        print(f"({i},{n})")

    name = f"The Number of Nodes in XC3 tree"
    plot.title(name)

    plot.xlabel("Degree of Tree (d)")
    plot.ylabel("Node Count of Tree (s)")

    nodes.plot()

    plot.legend()
    plot.show()

    print(nodes.ypoints)


if (__name__ == "__main__"):
    test()
