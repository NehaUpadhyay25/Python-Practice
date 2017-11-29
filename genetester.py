__author__ = "Neha Upadhyay"

"""
CSCI-603 : LAB ASSIGNMENT 6
FILENAME : genetester.py
Authors  : Neha Upadhyay  (nxu3128@rit.edu)

This program executes the test functions for the
DNAList. It tests the functions of the DNAList
and prints the results.
"""


from dnalist import DNAList

def test1():
    """
    This is a simple test case which checks all the functions
    :return:
    """
    print("TEST CASE 1")
    dna = DNAList()

    # items with values will be appended in the gene list
    dna.append("A")
    dna.append("B")
    dna.append("C")

    print("After append method " , dna)

    other = DNAList()
    other.append("D")
    other.append("E")
    other.append("F")
    other.append("G")

    # list with values will be appended in the gene list
    dna.join(other)
    print("After join method with the list provided"  , dna)

    # if gene list is not empty then it will copy the current items in the list in a new list
    newList = dna.copy()
    print("After copy method"  , newList)

    newother = DNAList()
    newother.append("H")
    newother.append("I")
    newother.append("J")
    newother.append("K")

    # list with elements after the index will be added in the list
    dna.splice(4,newother)
    print("After splice method at index 4 " , dna)

    # index of elements specified will be removed from the list
    dna.snip(4,5)
    print("After snip method with index 4 and 5 " , dna)

    newotherlist = DNAList()
    newotherlist.append("W")
    newotherlist.append("Q")
    newotherlist.append("R")

    # the string given will be replaced with the list given
    dna.replace("BCD",newotherlist)
    print("After replace method with string BCD" , dna)
    print()

def test2():
    """
    The second test function
    """
    print("TEST CASE 2")

    dna = DNAList()
    # checks for test case of copy cannot copy when gene list is empty
    dna.copy()

    # checks the append function if empty string is appended it wont append the empty String
    dna.append("")

    # if the item is None it also won't be appended in the gene list
    dna.append(None)

    # items with values will be appended in the gene list
    dna.append("A")
    dna.append("B")
    dna.append("C")
    print("After append method " , dna)

    normList = DNAList()
    # empty list wont be appended in the gene list
    dna.join(normList)

    newother = DNAList()
    newother.append("H")
    newother.append("I")
    newother.append("J")
    newother.append("K")

    # will append the elements in the front if index is 0
    dna.splice(0,newother)
    print("After splice method at index 0 " , dna)
    # will not append the gene list if the list passed in the function is empty
    dna.splice(0,normList)

    newotherlist = DNAList()
    newotherlist.append("W")
    newotherlist.append("Q")
    newotherlist.append("R")

    # will not replace if the given object is of list is empty
    dna.replace("BCD",normList)
    #cannot replace if string to be replaced is None or empty
    dna.replace("",newotherlist)
    dna.replace(None,newotherlist)

    # replaces the starting value of the gene list with other list
    # replace any substring with any other list of elements provided
    dna.replace("H",newotherlist)

def main():
    """
    This is the main method which calls the test functions
    """
    test1()
    test2()

if __name__ == "__main__":
    main()