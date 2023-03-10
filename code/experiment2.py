from random import randrange

from bst import BST
from lab6 import RBTree
from plotting import PlotGroup
import matplotlib.pyplot as plot

# =========================================================================

def generate_near_sorted_list(size, swaps):

    #randge to list
    sortedList = list(range(size))

    #n swaps
    for _ in range(swaps):
        i = randrange(size-1)
        j = randrange(size-1)

        temp = sortedList[i]
        sortedList[i] = sortedList[j]
        sortedList[j] = temp

    #return
    return sortedList

# =========================================================================

def height_test(trialCount, cInputSize, swapRange):

    assert trialCount > 0

    #Custom Plotting API
    bstPlot = PlotGroup('Height of BST')
    rbtPlot = PlotGroup('Height of RBT')

    for swaps in swapRange:

        print(f'Starting Swaps Number = {swaps}')

        bstAvgHeight = 0
        rbtAvgHeight = 0

        #Loop
        for _ in range(trialCount):

            #Empty
            bst = BST()
            rbt = RBTree()

            insertions = generate_near_sorted_list(cInputSize, swaps)

            #Insert
            for insert in insertions:
                bst.insert(insert)
                #print(f'\tbst: {insert}')

            for insert in insertions:
                rbt.insert(insert)
                #print(f'\trbt: {insert}')

            # Add
            bstAvgHeight += bst.get_height()
            rbtAvgHeight += rbt.get_height()

        # Avg
        bstAvgHeight /= trialCount
        rbtAvgHeight /= trialCount
        print(f'Done {swaps}. BST:{bstAvgHeight}, RBT:{rbtAvgHeight}')
        
        # Plot
        bstPlot.add_point(swaps, bstAvgHeight)
        rbtPlot.add_point(swaps, rbtAvgHeight)

    # Done Experiment for all swaps in range

    # Plot Here
    name = f"Average Insertion Disorder On List Size {cInputSize} vs Tree Heights, {trialCount} Trials"
    plot.title(name)

    plot.xlabel("Number of Swaps in List")
    plot.ylabel("Height of Tree (Nodes)")

    bstPlot.plot()
    rbtPlot.plot()

    plot.legend()
    plot.show()


if (__name__ == '__main__'):

    n = 10000
    skips = 250

    figA = height_test(1, n, range(0, n, skips))
    figB = height_test(10, n, range(skips, n+5*skips, skips))