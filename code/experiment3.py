from XC3 import XC3Node
from plotting import PlotGroup
import matplotlib.pyplot as plot

'''
Create XC3-Trees with degrees 0 to 25. In you report, based off your trees write an equation h(i), where
h(i) returns the height of a degree i XC3-Tree. Explain why this is the case. These results likely aren’t
mind-blowing but it is a reasonable place to start.
'''

def test():

    #New Dict
    nodes = PlotGroup("Height of XC3 Tree")

    rang = range(0,25,1)
    for i in rang:
        root = XC3Node(i)
        nodes.add_point(i, root.get_height())

    name = f"The Height of XC3 trees"
    plot.title(name)

    plot.xlabel("Degree of Tree (d)")
    plot.ylabel("Height of Tree (s)")

    #Show each label
    plot.xticks(rang)

    nodes.plot()

    plot.legend()
    plot.show()


if (__name__ == "__main__"):
    test()
