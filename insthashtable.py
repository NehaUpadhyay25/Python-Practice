__author__ = "Neha Upadhyay"

"""
CSCI-603 : LAB ASSIGNMENT 10
FILENAME : insthashtable.py
Authors  : Neha Upadhyay  (nxu3128@rit.edu)

This program creates a HashMap and tests 2 different HasFunctions and python function for strings
Most part of the code is taken from the lecture code in My courses.
"""

import math
import re
import sys
from collections import namedtuple

Entry = namedtuple('Entry', ('key', 'value'))
numOfCollisions=0
numOfProbes=0

'''
To make sure that the DELETED sentinel does not match
anything we actually want to have in the table, make it
a unique (content-free!) object.
'''


class _delobj: pass


DELETED = Entry(_delobj(), None)


class Hashmap:
    """
    HashMap class
    """
    __slots__ = 'table', 'numkeys', 'cap', 'maxload','hash_func'

    def __init__(self,hashFunc=None, initsz=100, maxload=0.3):
        '''
        Creates an open-addressed hash map of given size and maximum load factor
        :param initsz: Initial size (default 100)
        :param maxload: Max load factor (default 0.7)
        '''
        self.cap = initsz
        self.table = [None for _ in range(self.cap)]
        self.numkeys = 0
        self.maxload = maxload
        self.hash_func=hashFunc

    def put(self, key,value):
        '''
        Adds the given (key,value) to the map, replacing entry with same key if present.
        :param key: Key of new entry
        :param value: Value of new entry
        '''
        global numOfCollisions
        global numOfProbes
        index = self.hash_func(key) % self.cap
        initialIndex=index
        while self.table[index] is not None and \
                        self.table[index] != DELETED and \
                        self.table[index].key != key:


            #For counting number of collisions
            if index==initialIndex and self.table[index] is not None:
                numOfCollisions=numOfCollisions+1

            #For counting number of probes
            if self.table[index] is not None and self.table[index].key!=key:
                numOfProbes=numOfProbes+1

            index += 1
            if index == len(self.table):
                index = 0

        if self.table[index] is None:
            self.numkeys += 1
        self.table[index] = Entry(key, value)

        if self.numkeys / self.cap > self.maxload:
            # rehashing
            oldtable = self.table
            # refresh the table
            self.cap *= 2
            self.table = [None for _ in range(self.cap)]
            self.numkeys = 0
            # put items in new table
            for entry in oldtable:
                if entry is not None:
                    self.put(entry[0],entry[1])


    def remove(self, key):
        '''
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            index += 1
            if index == len(self.table):
                index = 0
        if self.table[index] is not None:
            self.table[index] = DELETED


    def get(self, key):
        global numOfProbes
        '''
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or KeyError if key not present)
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:

            index += 1
            if index == self.cap:
                index = 0
        if self.table[index] is not None:
            numOfProbes += 1
            return self.table[index].value
        else:
            numOfProbes+=1
            raise KeyError('Key ' + str(key) + ' not present')


    def __contains__(self, key):
        global numOfProbes
        '''
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        '''
        index = self.hash_func(key) % self.cap
        while self.table[index] is not None and self.table[index].key != key:
            numOfProbes+=1
            index += 1
            if index == self.cap:
                index = 0

        return self.table[index] is not None

    def findMostOccuredWord(self):
        """
        Finds the word which occurs the most
        :return:
        """

        index=0
        index1=0
        maxValue=0
        while index<=len(self.table)-1:
            if self.table[index] is None:
                index=index+1
            elif self.table[index] is not None and self.table[index].value>maxValue:
                maxValue=self.table[index].value
                index=index+1
            else:
                index=index+1

        while index1<=len(self.table)-1:
            if self.table[index1] is not None and self.table[index1].value==maxValue:
                print("Most occured word is: "," ' ",self.table[index1].key," ' ", "with value: ",maxValue)
                return
            else:
                index1=index1+1

def printMap(map):
    """
    prints the hash map
    :param map: map to be printed
    :return:
    """
    for i in range(map.cap):
        print(str(i) + ": " + str(map.table[i]))
    map.findMostOccuredWord()
    print("Collisions :", numOfCollisions)
    print("Probes :", numOfProbes)


def customHashFunction1(key):
    """
    Custom hash function
    :param key: key whose hashValue needs to be found out
    :return:
    """
    hashValue=0
    for i in range(len(key)):
        hashValue=hashValue + ord(key[i])* math.pow(31,i)
    return int(hashValue)

def customHashFunction2(key):
    """
    custom hash function
    :param key: key whose hash value needs to be found out
    :return:
    """
    hashValue=0
    sum=0
    for i in range(len(key)):
        sum+=ord(key[i])
    hashValue= (sum%1487)*len(key)
    return hashValue

def pythonHashFunction(key):
   return hash(key)

def readFile(f1):
    """
    Read the file
    :param f1:
    :return:
    """
    textList=[]
    for f1_line in f1:
        line=re.split('\W+',f1_line.strip())
        line = process(line)
        textList.extend(line)
    return textList

def process(line):
    newList = []
    for i in range(len(line)):

        if not line[i].isupper() and not line[i].islower():
            val = line[i]
            name = ""
            for i in range(len(val)):
                if val[i].isupper():
                    name = val[i].lower() + name
                else:
                    name = val[i] + name
            name = name[:: -1]
            newList.append(name)

        elif line[i].isupper():
            name = line[i].lower()
            newList.append(name)
        else:
            newList.append(line[i])


    return newList


def main():
    global numOfCollisions
    global numOfProbes
    """
    main function
    :return:
    """
    try:
        fname=input("Enter the name of the file: ")
        f1=open(fname)
        textList=readFile(f1)

    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)

    print("-----------PROBLEM SOVLING FUNCTION----------------")
    map = Hashmap(customHashFunction1,initsz=100)
    for i in range(len(textList)):
        if textList[i]=='':
            continue
        else:
            try:
                count=map.get(textList[i])
                map.put(textList[i],count+1)
            except KeyError:
                map.put(textList[i],1)
    printMap(map)
    a1=numOfCollisions
    b1=numOfProbes
    numOfProbes=0
    numOfCollisions=0
    print("-----------OUR FUNCTION----------------")
    map = Hashmap(customHashFunction2, initsz=100)
    for i in range(len(textList)):
        if textList[i]=='':
            continue
        else:
            try:
                count=map.get(textList[i])
                map.put(textList[i],count+1)
            except KeyError:
                map.put(textList[i],1)
    printMap(map)
    a2=numOfCollisions
    b2=numOfProbes
    numOfProbes = 0
    numOfCollisions = 0
    print("-----------PYTHON FUNCTION------------------")
    map = Hashmap(pythonHashFunction, initsz=100)
    for i in range(len(textList)):
        if textList[i]=='':
            continue
        else:
            try:
                count=map.get(textList[i])
                map.put(textList[i],count+1)
            except KeyError:
                map.put(textList[i],1)
    printMap(map)
    a3=numOfCollisions
    b3=numOfProbes
    print("--------------------")
    print("First Function:")
    print("Collisions: ",a1)
    print("Probes:",b1)
    print("--------------------")
    print("Second Function:")
    print("Collisions: ", a2)
    print("Probes:", b2)
    print("--------------------")
    print("Python Function:")
    print("Collisions: ", a3)
    print("Probes:", b3)



if __name__ == '__main__':
    main()
