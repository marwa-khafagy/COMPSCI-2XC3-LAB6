from lab6 import RBTree
from bst import BST
import timeit
import random
from plotting import PlotGroup
import matplotlib.pyplot as plot

# plotting functions


# Testing function


# run the testing function


#-----------------------------------------------------------------------------------------------------------#
# Trial Functions


def run_xtrials(trials, num_of_nodes, max_value, min_value):


    bstHeight = 0
    rbHeight = 0

    #Loop Over
    for _ in range(1, trials, 1):
        bst = BST()
        rbt = RBTree()

        for i in range(1,num_of_nodes, 1):
            value = random.randint(min_value, max_value)
            bst.insert(value)
            rbt.insert(value)

        bstHeight+= bst.get_height()    
        rbHeight+= rbt.get_height()
    
    bstHeight = bstHeight/trials
    rbHeight = rbHeight/trials
        

    return (rbHeight, bstHeight)

def run_comparison_test(trials, listSizes, listMaxValue, listMinValue):


    #New Dict
    bstPlot = PlotGroup("BST", 'b')
    rbPlot = PlotGroup("RB Tree" ,'g')
    difPlot = PlotGroup("Difference", 'r')

    for listSize in listSizes:

        timesForTrial = run_xtrials(trials, listSize, listMaxValue, listMinValue)
        
        bstPlot.add_point(timesForTrial[1], listSize)
        rbPlot.add_point(timesForTrial[0], listSize)
        difPlot.add_point(abs(timesForTrial[0] -timesForTrial[0]), listSize)
        print("Added point at listSize ", listSize)

    name = f"The Difference in Height between RBTrees and BST ({trials} trails)"
    plot.title(name)

    plot.xlabel("Size of tree (n)")
    plot.ylabel("Height of Tree (s)")

    bstPlot.plot()
    rbPlot.plot()
    difPlot.plot()

    plot.legend()
    plot.show()
        


#-----------------------------------------------------------------------------------------------------------#
# Running

if (__name__ == "__main__"):

    test = run_comparison_test(1, range(0, 5, 1), 100, -100)
    #test = run_comparison_test(100, BBL, range(0, 500, 5), 1000)
#print(test)    
