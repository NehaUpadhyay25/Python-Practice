__author__ = "Neha Upadhyay"

"""
CSCI-603 : LAB ASSIGNMENT 6
FILENAME : dnalist.py
Authors  : Neha Upadhyay  (nxu3128@rit.edu)

This program implements the DNAList and its functions.
It makes use of the ListNode as per the lecture's code
and some part of lecture in this code.
"""


class ListNode:
    """
    This class is the node class and returns the node
    when it is called in the main DNAList class.
    """
    __slots__ = ('data','next')

    def __init__(self,data,next):
        self.data = data
        self.next = next

    def __str__(self):
        return "Node contains " + str(self.data)

class DNAList:
    """
    This class is the main DNAList class and it implements
    the given functions.
    """

    __slots__ = ('head','tail')

    def __init__(self , gene = ''):
        """
        Initializes the head and tail attributes.
        :param gene: an empty string
        """
        self.head = None
        self.tail = None

    def isEmpty(self):
        """
        Returns true if the head has no value and if head has
        some value it returns false.
        :return: True or False
        """
        return self.head == None

    def append(self,item):
        """
        This function adds the item to the end of the list.
        :param item: The item to be appended
        """
        newNode = ListNode(item, None)
        if item == None or item == "":
            print("empty item cannot be appended in the list")
        elif self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def __str__(self):
        """
        It returns a string of elements present in the list.
        :return: currentList : String representation of the elements in the list
        """
        currentList = "List : "
        current = self.head
        while current is not None:
            currentList = currentList +  "  " + str(current.data)
            current = current.next
        return currentList

    def join(self,other):
        """
        This function adds another list to the end of the current list
        :param other: list of elements to be added in the end of current list
        """
        if self.isEmpty():
            self.head = other.head
            self.tail = other.tail
        elif other.isEmpty():
            print(self)
        else:
            self.tail.next = other.head
            self.tail = other.tail

    def splice(self,ind,other):
        """
        It adds a list of elements after the index ind in the list
        :param ind: Index after which list of elements is to be added
        :param other: list of elements to be added after ind
        """
        if other.isEmpty():
            print("cannot insert empty list")
        elif self.isEmpty():
            self.head = other.head
            self.tail = other.tail
        elif ind==0 and not self.isEmpty():
            current = self.head
            self.head = other.head
            other.tail.next = current
        else:
            current = self.head
            i = 0
            while current.next is not None:
                i = i + 1
                if i == ind:
                    previous = current.next
                    current.next = other.head
                    other.tail.next = previous
                current = current.next


    def snip(self,i1,i2):
        """
        This function removes the portion of the list.
        :param i1: The postion from which the list is to be removed
        :param i2: The position till which the list is to be removed.
        :return:
        """

        if self.isEmpty():
            print("cannot operate on empty gene list")
        else:
            current = self.head
            i = 0
            while i is not i1-1:
                current = current.next
                i = i + 1
            temp = current
            temptail = current
            for n in range(i1,i2):
                current = current.next
            temp1 = current
            temp.next = temp1
            temptail.next = temp1


    def replace(self, repstr, other):
        """
        This function replaces the part of list specified by other list
        of elements
        :param s: The part of the list which is to be replaced
        :param other: The part by which the part of the list is to be replaced
        :return:
        """
        if repstr == "" or repstr == None:
            print("repstr is empty or none")
        elif other.isEmpty():
            print("cannot replce with empty list")
        elif self.isEmpty():
            self.head = other.head
            self.tail = other.tail
        else:
            current = self.head
            newList = []
            i = 0
            index = 0
            count = 0
            while current is not None:
                while i < len(repstr):
                    count += 1
                    previous = current.next
                    if current.data == repstr[i]:
                        newList.append(repstr[i])
                        current = current.next
                        i += 1
                    else:
                        current = current.next
                        newList = []
                        i=0
                if len(newList) == len(repstr):
                    index = count - len(repstr)
                    current = self.head
                    if(index == 0):
                        self.head = other.head
                        other.tail.next = previous
                    else:
                        for n in range(index):
                            if(n == index - 1):
                                current.next = other.head
                                other.tail.next = previous
                            else:
                                current = current.next
                return print(self)

    def copy(self):
        """
        Copies the elements of gene list into new list and returns the new list
        :return: newList : List of elements in the gene list
        """

        if self.isEmpty():
            print("gene list is empty")
            return None
        else:
            newList = []
            current = self.head
            while current is not None:
                newList.append(current.data)
                current = current.next
            return newList
