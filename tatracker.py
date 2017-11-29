__author__ = "Neha Upadhyay"

"""
CSCI-603 : LAB ASSIGNMENT 7
FILENAME : tatracker.py
Authors  : Neha Upadhyay  (nxu3128@rit.edu)

This program implements TA Tracker and its functions.
It makes use of the ListNode as per the lecture's code
and some part of lecture in the prescribed text book (Miller and Ranum).
"""

import sys

class Node:
    _slots_={"name","value","prev","next"}

    def __init__(self,name,value):
        self.name=name
        self.value=value
        self.next=None
        self.prev=None

class Oliver:
    """
    Oliver's data structure
    """
    _slots_ = {"head", "tail"}

    def __init__(self):
        """
        init function to initialize
        """
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def addStudent(self, name, value):
        """
        add the student
        :param name: Name of the student
        :param value: Confusion value of the student
        :pre: Confusion value should not be negative or 0
        :return:
        """
        student = Node(name, value)
        if self.isEmpty():
            self.head = student
            self.head.prev = None
            self.tail = student
            self.tail.next = None
        else:
            self.tail.next = student
            student.prev = self.tail
            self.tail = student
            self.tail.next = None

    def deleteStudent(self):
        """
        Function to delete the student
        :return:
        """
        if self.head.next == None:
            self.head = None

        else:
            self.head = self.head.next
            self.head.prev = None

    def removeStudentFromMiddle(self, index):
        """
        Function to delete student from Middle
        :param index: index of the student to delete
        :return:
        """
        student = self.head
        for n in range(index):
            student = student.next
        if student.next == None:
            student.prev.next = student.next
        else:
            student.prev.next = student.next
            student.next.prev = student.prev

    def printList(self):
        """
        function to print oliver's list
        :return:
        """
        student = self.head
        while student is not None:
            print(student.name, student.value)
            student = student.next

    def printName(self):
        """
        Function to print names of students in oliver's list
        :return:
        """
        student = self.head
        while student is not None:
            print(student.name)
            student = student.next

    def printFirstNode(self):
        """
        function to return first student in oliver's list
        :return:
        """
        student = self.head
        return student.name, student.value

    def size(self):
        """
        return size of oliver's list
        :return:
        """
        student = self.head
        size = 0
        while student is not None:
            size = size + 1
            student = student.next
        return size

    def printHelpingWhom(self):
        """
        function to print who oliver is helping
        :return:
        """
        student = self.head
        print("Oliver helping", student.name)


class Colleen:
    """
    Colleen's data structure. Max Heap
    Some of the Heap Code used form Miller and Ranum (OK as per the discussion with Grader and Professor)
    """
    _slots_ = {"heapList", "nameList", "currentSize"}

    def __init__(self):
        """
        Init function
        """
        self.heapList = [0]
        self.nameList = ["empty"]
        self.currentSize = 0

    def addStudent(self, value, name):
        """
        Function to add a a student
        :param value: confusion value of the student
        :param name: name of student
        :pre: Confusion value should not be negative or 0
        :return:
        """
        self.heapList.append(value)
        self.nameList.append(name)
        self.currentSize = self.currentSize + 1
        self.bubbleUp(self.currentSize)

    def bubbleUp(self, i):
        """
        Bubble up function for heapifying.
        :param i: index of the node
        :return:
        """
        while i // 2 > 0:
            if int(self.heapList[i]) > int(self.heapList[i // 2]):
                tmp = self.heapList[i // 2]
                tmpName = self.nameList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.nameList[i // 2] = self.nameList[i]
                self.heapList[i] = tmp
                self.nameList[i] = tmpName
            i = i // 2

    def popStudent(self):
        """
        Function to pop student from Heap
        :return:
        """
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.nameList[1] = self.nameList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.nameList.pop()
        self.bubbleDown(1)

    def popFromMiddle(self, index):
        """
        Function to pop student from middle of the heap
        :param index: index of the value to be popped
        :return:
        """
        retValName = self.nameList[index]
        retValValue = self.heapList[index]
        self.heapList[index] = self.heapList[self.currentSize]
        self.nameList[index] = self.nameList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.nameList.pop()
        self.bubbleDown(index)

    def bubbleDown(self, i):
        """
        Function to heapify
        :param i: index of the node
        :return:
        """
        while (i * 2) <= self.currentSize:
            mc = self.maxChild(int(i))
            if int(self.heapList[i]) < int(self.heapList[mc]):
                tmp = self.heapList[i]
                tmpName = self.nameList[i]
                self.heapList[i] = self.heapList[mc]
                self.nameList[i] = self.nameList[mc]
                self.heapList[mc] = tmp
                self.nameList[mc] = tmpName
            i = mc

    def maxChild(self, i):
        """
        Function that returns max child
        :param i: index of the node
        :return:
        """
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] > self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def printList(self):
        """
        Function to print Colleens list
        :return:
        """
        for i in range(len(self.heapList)):
            print(self.heapList[i], self.nameList[i])

    def helpingWhom(self):
        """
        Function to print who Colleen is helping
        :return:
        """
        print("Colleen helping", self.nameList[1])

    def size(self):
        """
        Returns size of the heap
        :return: current size
        """
        return self.currentSize

    def printName(self):
        """
        prints remaining students names in Colleens list
        :return:
        """
        for i in range(1, len(self.nameList)):
            print(self.nameList[i])

class Service:
    def findInColleen(self, elementName, Namelist, elementValue, ValueList):
        """
        index of student in Coleens list
        :param elementName: name of person
        :param Namelist: namelist of Colleen
        :param elementValue: confusion value of person
        :param ValueList: confusion value list of Colleen
        :return: index
        """
        for i in range(len(Namelist)):
            if elementName == Namelist[i] and elementValue == ValueList[i]:
                return i

    def findIndexInOliver(self, colleen, oliver):
        """
        Finds index of a student in Olivers list
        :param colleen: Colleen heap
        :param oliver:  oliver link list
        :return: -1
        """
        oliver = oliver.head
        index = 0
        while oliver is not None:
            if colleen.nameList[1] == oliver.name and colleen.heapList[1] == oliver.value:
                return index
            else:
                index = index + 1
                oliver = oliver.next
        return -1

    def popFromOliver(self, colleen, oliver):
        """
        To delete student from Olivers data structure
        :param colleen: Colleens data structure
        :param oliver:  Olivers data structure
        :return:
        """
        index = self.findIndexInOliver(colleen, oliver)
        if index == 0:
            oliver.deleteStudent()
        else:
            oliver.removeStudentFromMiddle(index)

    def popFromColleen(self, node, colleen):
        """
        Pop student from Colleens data structure
        :param node: first element of Olivers data structure
        :param colleen: Colleen heap
        :return:
        """
        index = self.findInColleen(node[0], colleen.nameList, node[1], colleen.heapList)
        colleen.popFromMiddle(index)

def readFile(f1):
    """
    Reads file
    :param f1: file pointer of file1
    :return:
    """
    oliver = Oliver()
    coleen = Colleen()
    service = Service()
    for f1_line in f1:
        if f1_line.strip().split(" ")[1]!="ready":

            oliver.addStudent(f1_line.strip().split(" ")[0],f1_line.strip().split(" ")[1])
            coleen.addStudent(f1_line.strip().split(" ")[1],f1_line.strip().split(" ")[0])
            print(f1_line.strip().split(" ")[0],"is looking for help!")
        else:
            if oliver.size() > 0 and coleen.size() > 0:
                if f1_line.strip().split(" ")[0]=="Oliver":
                    service.popFromColleen(oliver.printFirstNode(),coleen)
                    oliver.printHelpingWhom()
                    oliver.deleteStudent()
                    continue

                elif f1_line.strip().split(" ")[0]=="Colleen":
                        service.popFromOliver(coleen,oliver)
                        coleen.helpingWhom()
                        coleen.popStudent()
                        continue
            else:
                break

    if oliver.size()==0 and coleen.size()==0:
        print("All students helped")
    elif oliver.size()>0:
        print("Students left unhelped:")
        oliver.printName()
    else:
        print("Students left unhelped:")
        coleen.printName()

def main():
    """
    main function
    :return:
    """
    try:
        fileName = input("Please enter filename for reading message : ")
        f1 = open(fileName)
        readFile(f1)
    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)

if __name__ == '__main__':
 main()