__author__ = "Neha Upadhyay"

"""
CSCI-603 : LAB ASSIGNMENT 8
FILENAME : balances.py
Authors  : Neha Upadhyay  (nxu3128@rit.edu)

This program implements balancing tree.
"""

import math
import sys
import turtle as t
class Weight:
    """
    Weight Class has position and value
    """
    __slots__ = {'position', 'value'}
    """
    Each beam has list of weights. Each weight has a position and value
    """
    def __init__(self,position,value):
        self.value=value
        self.position=position

    def __repr__(self):
         return "%s %s " % (self.value,self.position)


class Beam:
    """
    Beam class. Beam has an ID and a weightlist
    """
    __slots__={'id','weightList','left','right'}

    def __init__(self,id, weightList=[],left=None,right=None):
       self.id=id
       self.weightList=weightList
       self.left=None
       self.right=None
    def __repr__(self):
        return "id is: %s Weightlist is: %s" % (self.id,self.weightList)

def checkIfAllNodesHaveDisappeared(list):
    """
    It checks if the new list does not contain anymore nodes after manipulation
    :param list: current weightlist of current object
    :return: result. Yes if no more nodes present. False is nodes present
    """
    for i in range(len(list)):
        if list[i].value[0] != "B":
            continue
        else:
            return "false"
    return "true"


def checkTorque(list):
    """
    checks torque of a single beam passed
    :param list: particular weightlist of a particular object
    :return: if balanced, returns true
    """
    leftweight=0
    rightweight=0
    for i in range(len(list)):
        if int(list[i].position)<0:
            leftweight=leftweight+int(list[i].value)*int(list[i].position)
        else:
            rightweight=rightweight+int(list[i].value)*int(list[i].position)

    if math.fabs(leftweight)==rightweight:
        return "true"

def newWeightCalculate(list,newWeight,index):
    """
    used to manipulate teh list and insert the total weight of a beam in place of beam id
    :param list:
    :param newWeight: weight of the Beam
    :param index: index where weight needs to be manipulated
    :return: new list
    """
    list[index].value=str(newWeight)
    return list


def find(id,list):
    """
    weight list of that beam balance
    :param id: id of beam
    :param list: old list
    :return: which weightlist needs to be manipulated
    """
    for i in range(len(list)-1):

        if(id==list[i].id):

            return list[i].weightList

def checkSingleBeamBalance(list):
    """function to check balance of that single beam which I find in findBeamObject
    """
    leftweight=0
    rightweight=0
    for i in range(len(list)):

        if int(list[i].position)<0:
            leftweight=leftweight+int(list[i].value)
        else:
            rightweight=rightweight+int(list[i].value)

    sum=leftweight+rightweight
    return sum


def findBeamObject(list,objectList):
    """which beams balance to check?"""
    for i in range(len(list)):
        if list[i].value[0] == "B":

            return find(list[i].value,objectList)
        else:
            continue



def checkBalance(list):
    """
    main function to check balance
    :param list: Beam object list
    :return: true if balanced, false if not balanced 
    """
    BalancedBeam=[]
    leftweight=0
    rightweight=0
    i=0
    j=0
    while i<=len(list)-1:
        while j<=len(list[i].weightList)-1:
            if(isNotNode(list[i].weightList)=="true"):
                if(int(list[i].weightList[j].position)<0):
                    leftweight=leftweight+(int(list[i].weightList[j].value)*(int(list[i].weightList[j].position)))
                    j=j+1
                else:
                    rightweight=rightweight+(int(list[i].weightList[j].value)*(int(list[i].weightList[j].position)))
                    j=j+1

                l=i
                if (math.fabs(leftweight) == rightweight):
                    print("It is balanced", list[l].id)
                    BalancedBeam.append(list[l].id)
                    k = 0
                    m=0
                    for m in range(len(list[l].weightList) - 1):
                        while k <= len(list[l].weightList) - 1:
                            k = k + 1
                    l=0
            else:

                 beamweight=checkSingleBeamBalance(findBeamObject(list[i].weightList,list))
                 list[i].weightList=newWeightCalculate(list[i].weightList,beamweight,j)
                 if(checkIfAllNodesHaveDisappeared(list[i].weightList)=="true"):
                    if(checkTorque(list[i].weightList)=="true"):
                        l = i
                        print("It is balanced", list[l].id)
                        BalancedBeam.append(list[l].id)
                    j=j+1



                 else:
                    j=j+1




        i=i+1
        j=0
        leftweight=0
        rightweight=0
    print("Balanced list is",BalancedBeam)
    if(len(BalancedBeam)==len(list)):
        return "true"
    else:
        return "false"



def isNotNode(list):
    """
    Checks whether if it is beam node or not
    :param list: list of nodes
    """
    for i in range(len(list)):
        if list[i].value[0] != "B":
           continue
        else:
            return "false"
    return "true"


def getWeightOnCurrentBeam(list,i):
    """
    Create of list of weights on each beam with position  and value. Every beam has a list of weights.
    :param list: list of nodes
    :return: WeightList : list with weights
    """
    WeightList=[]
    j=1
    k=2
    while k<len(list):

           weight = Weight(value=list[k],position=list[j])  # Creating object of class Weight
           WeightList.append(weight)

           j=j+2
           k=k+2

    return WeightList


def constructBeamObjects(list):
    """
    Constructs Beam objects
    :param list: list of nodes
    :return: List of Beam objects
    """
    ListOfObjects = []


    for i in range(len(list)):

        ListOfObjects.append(Beam(list[i][0] ,weightList=getWeightOnCurrentBeam(list[i],i)))

    print(ListOfObjects) #Prints the list of Beam objects that we have created
    return ListOfObjects

def readPuzzle(f1):
    """
    read puzzle. Each line is a list within a  big list. Each Beam and its weight is a list.
    :param f1 file handle for fileName
    :return:
    """
    BeamList=[]
    IndividualBeamList=[]

    for f1_line in f1:
        BeamList.append(f1_line.strip())
    for i in range(len(BeamList)):
        tempList=BeamList[i].split(",")
        IndividualBeamList.append(BeamList[i].split())
    BeamObjectList=constructBeamObjects(IndividualBeamList)

    if(checkBalance(BeamObjectList)=="true"):
        makeList(IndividualBeamList)
        print("It is balanced")
    else:
        print("Its not balanced")

def makeList(IndividualBeamList):
    """
    draws the turtle diagram for the list

    :param IndividualBeamList: the balanced list
    """
    nameList = []
    list = [["B1", [-2,6,-1,3,3,5]],
            ["B2", [-1,4,1,2,2,1]],
            ["B3", [-1,"B2",1,7]],
            ["B",[-1,"B1",1,"B3"]]
            ]

    for k in range(len(list)):
        nameList.append(list[k][0])

    print(nameList)

    for i in range(len(list)):
        if list[i][0] == "B":
            newList = list[i][1]
            draw(nameList,newList,list)



def draw(nameList,newList,list):
    """
    It draws the balance list of nodes
    :param nameList: names of nodes in the list
    :param newList: individual list B
    :param list: list containing all the elements
    """

    t.showturtle()
    i = 0
    while i < (len(newList)):


        if int(newList[i]) < 0:
                t.left(180)
                t.pendown()
                t.forward((-1 * newList[i]) * 50)
                t.left(90)
                t.forward(50)
                t.penup()
                t.forward(20)


                t.write(newList[i+1] , font = 6)
                t.back(70)
                t.left(90)
                t.forward((-1 * newList[i]) * 50)

        elif int(newList[i]) > 0:
                t.pendown()
                t.forward(newList[i] * 50)
                t.right(90)
                t.forward(50)
                t.penup()
                t.forward(20)
                t.write(newList[i+1] , font = 6)
                t.back(70)
                t.right(90)
                t.forward(newList[i] * 50)
                t.right(180)


        i = i + 2

def drawNew(tempList):

    """
    Helper function to draw the nodes present in the list of that particular nodes
    :param tempList: list of the node
    """
    t.left(90)
    i = 0
    while i < (len(tempList)):


        if int(tempList[i]) < 0:
                t.left(180)
                t.pendown()
                t.forward((-1 * tempList[i]) * 50)
                t.left(90)
                t.forward(50)
                t.penup()
                t.forward(20)
                t.write(tempList[i+1] , font = 6)
                t.back(70)
                t.left(90)
                t.forward((-1 * tempList[i]) * 50)

        elif int(tempList[i]) > 0:
                t.pendown()
                t.forward(tempList[i] * 50)
                t.right(90)
                t.forward(50)
                t.penup()
                t.forward(20)
                t.write(tempList[i+1] , font = 6)
                t.back(70)
                t.right(90)
                t.forward(tempList[i] * 50)
                t.right(180)


        i = i + 2

    t.right(90)

def computeExtent():
    """
    Computes the extent and checks whether the beam is overlapping or not.
    Checks the if the right side of the left node overlaps the left side of the right node.
    """
    distanceOfBeam = 50

    list = [["B1", [-2,6,-1,3,3,5]],
            ["B2", [-1,4,1,2,2,1]],
            ["B3", [-1,"B2",1,7]],
            ["B",[-1,"B1",1,"B3"]]
            ]

    print(list)

    rightSide = 3 * 5
    totalSideNew = distanceOfBeam - rightSide

    leftSide = 1 * 4
    totalSideOld = leftSide

    if(rightSide < leftSide):
        print("overlap")
        print("distance will be increased")
    else:
        print("dont overlap")





def main():
    """
    main function
    """
    try:
        fname=input("enter filename")
        f1=open(fname)
        readPuzzle(f1)
        computeExtent()
        t.mainloop()
    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)



if __name__ == '__main__':
 main()




