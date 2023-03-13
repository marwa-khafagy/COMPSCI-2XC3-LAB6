from lab6 import RBTree
from bst import BST
import timeit
import random
from plotting import PlotGroup
import matplotlib.pyplot as plot

'''
What is the average difference in the height between the two? Comment on whether you think
there is a case where you would prefer a BST over an RBT. You do not need to empirically validate this,
but what is your instinct on the performance of a BST insert to a RBT insert for trees of similar heights?
In your report your experiment should include:...
'''

#-----------------------------------------------------------------------------------------------------------#
# Trial Functions

def run_xtrials(trials, num_of_nodes, max_value, min_value):

    bstHeight = 0
    rbHeight = 0

    #Loop Over
    for _ in range(trials):

        #E
        bst = BST()
        rbt = RBTree()

        for i in range(num_of_nodes):
            value = random.randint(min_value, max_value)
            bst.insert(value)
            rbt.insert(value)

        #Get Height
        bstHeight+= bst.get_height()    
        rbHeight+= rbt.get_height()
    
    #Average
    bstHeight = bstHeight/trials
    rbHeight = rbHeight/trials
    
    #Return
    return (rbHeight, bstHeight)

def run_comparison_test(trials, listSizes, listMaxValue, listMinValue):

    #New Dict
    bstPlot = PlotGroup("BST", 'b')
    rbPlot = PlotGroup("RB Tree" ,'r')

    for listSize in listSizes:

        timesForTrial = run_xtrials(trials, listSize, listMaxValue, listMinValue)
        
        bstPlot.add_point(listSize, timesForTrial[1])
        rbPlot.add_point(listSize, timesForTrial[0], )
        print("Added point at listSize ", listSize)

    name = f"The Difference in Height between RBTrees and BST ({trials} trails)"
    plot.title(name)

    plot.xlabel("Size of tree (n)")
    plot.ylabel("Height of Tree (s)")

    bstPlot.plot()
    rbPlot.plot()

    plot.legend()
    plot.show()
        


#-----------------------------------------------------------------------------------------------------------#
# Running

if (__name__ == "__main__"):

    test = run_comparison_test(100, range(0, 1000, 10), 0, 10000) #Attempt on Unique Values
    test = run_comparison_test(100, range(0, 1000, 10), 0, 10) #Attempt on Very Similar Values
    #test = run_comparison_test(100, BBL, range(0, 500, 5), 1000)
#print(test)    
