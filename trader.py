__author__ = "Neha Upadhyay"

"""
CSCI-603 : LAB ASSIGNMENT 5
FILENAME : trader.py
Authors  : Neha Upadhyay  (nxu3128@rit.edu)

This program reads the town data from two files and computes from which town
to purchase items so as to make the maximum profit.
"""

import sys

def readFile(f1,f2,fname1,fname2,quantity):
    """
    Read the files
    :param f1: file pointer of file1
    :param f2: file pointer of file2
    :param fname1: name of file1
    :param fname2: name of file2
    :param quantity: is the total quantity given by the user ie the number of
           items the user is allowed to buy
    :return:
    """
    vList=[]
    f1.readline()
    for f1_line in f1:
        vList.append(f1_line.strip())

    hList = []
    f2.readline()
    for f2_line in f2:
        hList.append(f2_line.strip())
    splitList(vList,hList,fname1,fname2,quantity)


def sortList(list1,list2):
    """
    This function is used to sort the list in case the contents of the lists are
    not same when mapped or during comparision
    :param list1: List according to which the second list is sorted
    :param list2: The list to be sorted
    :return: sorted second list
    """
    i=0
    j=0
    while i<len(list1) and j<len(list2):
        if list1[i][0]==list2[j][0]:
            i=i+1
            j=j+1
        else:
            for k in range(0,len(list2)):
                if list1[i][0]==list2[k][0]:
                    temp=list2[k]
                    list2[k]=list2[i]
                    list2[i]=temp
                else:
                    continue
    return list2

def splitList(vList,hList,fname1,fname2,quantity):
    """
    Splits the content of list into smaller list split on the basis of
    whitespaces for easy indexing. creates individual list consisting of name
    of item,price and quantity
    :param vList: Town1 list
    :param hList: Town2 list
    :param fname1: name of file1
    :param fname2: name of file2
    :param quantity: is the total quantity given by the user ie the number of
           items the user is allowed to buy
    :return:
    """
    finalVlist=[]
    finalHlist=[]
    for i in range(len(vList)):
        vList[i].split(",")
        finalVlist.append(vList[i].split())
    for i in range(len(hList)):
         hList[i].split(",")
         finalHlist.append( hList[i].split())
    finalSecondtownSortedList=sortList(finalVlist,finalHlist)
    compare(finalVlist,finalSecondtownSortedList,fname1,fname2,quantity)

def compare(finalVlist,finalHlist,fname1,fname2,quantity):
    """
    Compares the price of item
    :param finalVlist: Town1 list
    :param finalHlist: Town 2 list
    :param fname1: name of first file
    :param fname2: name of second file
    :param quantity: is the total quantity given by the user that is the number
           of items the user is allowed to buy
    :return:
    """
    i=0
    newprofitList=[]
    while(i<len(finalVlist) and i<len(finalHlist)):
        if(finalVlist[i][2]>finalHlist[i][2]):
            newprofitList.append(store(fname2,finalVlist[i][0],max(finalVlist[i][2],finalHlist[i][2]),finalHlist[i][1]))
        if(finalVlist[i][2]<finalHlist[i][2]):
            newprofitList.append(store(fname1, finalHlist[i][0], max(finalVlist[i][2], finalHlist[i][2]),finalVlist[i][1]))
        i=i+1
    finalList=sort(newprofitList,quantity)
    computation(finalList, quantity,fname1,fname2)

#store in list
def store(fname,name,maxValue,noofItems):
    """
    To store a elements in the profitlist after performing comparision
    :param fname: name of the file
    :param name: name of the item
    :param maxValue: profit of each item
    :param noofItems: quantity of items available for that town
    :return: returns profit list
    """
    newProfitlist=[]
    profitList=[fname,name,maxValue, noofItems]
    newProfitlist.extend(profitList)
    return newProfitlist

def max(a,b):
    """
    To determine the profit value of an item
    :param a: price of item in list1
    :param b: price of item in list2
    :return: profit value of that particular item
    """
    if int(a)>int(b):
        return int(a)-int(b)
    else:
        return int(b)-int(a)

'''sort in descending order. Gives the final profit list with filename, item name
   and selling cost '''
def sort(profitlist,quantity):
    """
    Function to sort the profits (Bubble sort)
    :param profitlist: list containing profit value of each item and its
           corresponding attributes
    :param quantity: is the total quantity given by the user ie the number
           of items the user is allowed to buy
    :return: sorted profit list
    """
    for i in range(len(profitlist)-1):
         for j in range(i,len(profitlist)):
             if profitlist[i][2]<profitlist[j][2]:
                 temp=profitlist[i]
                 profitlist[i]=profitlist[j]
                 profitlist[j]=temp
             else:
                continue
    return profitlist

def computation(list,quantity,fname1,fname2):
    """
    Computation is the main function where we find how much quantity can be taken
    at that time and add it to the final list along with its corresponding values
    :param list: profit list of item
    :param quantity: is the total quantity given by the user ie the number of
           items the user is allowed to buy
    :param fname1: name of first file
    :param fname2: name of second file
    :return: prints final result
    """
    compareList=[]
    nameList=[]
    sumList=[]
    i=0
    if quantity<=int(list[0][3]) and list[0][3]!='0': #first case
            tempSellValue=quantity*list[0][2]
            nameList=list[0][1]
            fileList=list[0][0]
            compareList.append(fileList)
            compareList.append(tempSellValue)
            compareList.append(nameList)
            print("Go to ", compareList[0].strip(".txt"), "and buy:")
            print(quantity,compareList[2], "for a profit of", float(compareList[1]))

    if quantity>int(list[0][3]): #summation case
        total=quantity
        sum=0
        for j in range(0,len(list)):
            if list[0][0]==list[j][0]: #checks if items are being bought from same town
                sum+= check(int(list[j][3]),total,quantity)*list[j][2]
                sumList.append(resultArray(list[j][0],check(int(list[j][3]),total,quantity),list[j][1],sum))
                total=total- int(check(list[j][3],total,quantity))
                if total==0:
                    break
        if(total==0):
                    print("Go to", sumList[0][0].strip(".txt"), "and buy:")
                    for i in range(0, len(sumList)):
                        if i == 0:
                            print(sumList[i][1], sumList[i][2], " for a profit of ", float(sumList[i][3]))
                        else:
                            print(sumList[i][1], sumList[i][2], " for a profit of ",float(sumList[i][3]) - float(sumList[i - 1][3]))
                    print("income is", float(sumList[len(sumList) - 1][3]))



        if(total!=0):
                    print("End of list. You can only buy a maximum of ", quantity-total,"items from",sumList[0][0].strip(".txt"),"for maximum profit")
                    print("Go to", sumList[0][0].strip(".txt"), "and buy:")
                    for i in range(0, len(sumList)):
                        if i == 0:
                            print(sumList[i][1], sumList[i][2], " for a profit of ", float(sumList[i][3]))
                        else:
                            print(sumList[i][1], sumList[i][2], " for a profit of ",float(sumList[i][3]) - float(sumList[i - 1][3]))
                    print("income is", float(sumList[len(sumList) - 1][3]))

def check(itemsAvailable,total,quantity):
    """
    Checks if the required quantity is present in the particular town
    :param itemsAvailable: quantity of items available for buying
    :param total: total is the quantity required more for satisfying the
           maximum quantity given by the user
    :param quantity: is the total quantity given by the user ie the number of
           items the user is allowed to buy
    :return: returns the number of items the user can buy at that point of time
    """
    if int(itemsAvailable)<quantity:
        if int(itemsAvailable)<total:
            return itemsAvailable
        else:
            return total
    else:
        return total

def resultArray(fname,value,itemName,profit):
    """
    List created to retrieve the resultant elements we require for our output
    :param fname: File name or here the town from which we need to buy the items
    :param value: Value of the item
    :param itemName: Name of the item
    :param profit: The profit we can make by selling that item
    :return: result List
    """
    resultList=[fname,value,itemName,profit]
    return resultList

def main():
    """
    main function
    :return:
    """
    try:
        fname1 = input("Enter the first file name")
        fname2 = input("Enter the second file name")
        f1 = open(fname1)
        f2 = open(fname2)
        quantity = int(input("Enter the maximum quantity allowed"))
        readFile(f1, f2, fname1, fname2, quantity)
    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)

if __name__ == '__main__':
 main()