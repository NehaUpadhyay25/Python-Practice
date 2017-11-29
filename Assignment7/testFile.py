__author__ = "Neha Upadhyay"

"""
CSCI-603 : LAB ASSIGNMENT 7
FILENAME : testFile.py
Authors  : Neha Upadhyay  (nxu3128@rit.edu)

This is the test case file for the implemented tatracker file.
There are three test cases implemented in the file.
"""

from tatracker import Node
from tatracker import Colleen
from tatracker import Oliver
from tatracker import Service

def main():
    """
    main function
    :return:
    """
    oliver = Oliver()
    coleen = Colleen()
    service = Service()

    # Below is the third test case.
    '''
        This test case checks for all the possible orders Colleen and Oliver can make requests.
        This also includes a check if student name is Colleen.
        It also checks for the list when there are no students in the waiting list and comes out of the loop.
        It checks for both Colleen's and Oliver's data structure with consequent request from Colleen and Oliver
    '''
    print("Test Case 1")
    list1 = ["Bob 3", "Dan 6", "Melissa 4", "Oliver ready", "Colleen ready", "Nate 1", "Gertrude 3", "Jessi 9",
               "John 11", "Colleen 7", "Colleen ready", "Colleen ready",
               "Oliver ready", "Oliver ready", "Colleen ready", "Oliver ready", "Colleen ready"]
    for j in list1:
        f3_line = j
        if f3_line.strip().split(" ")[1] != "ready":

            oliver.addStudent(f3_line.strip().split(" ")[0], f3_line.strip().split(" ")[1])
            coleen.addStudent(f3_line.strip().split(" ")[1], f3_line.strip().split(" ")[0])
            print(f3_line.strip().split(" ")[0], "is looking for help!")
        else:
            if oliver.size() > 0 and coleen.size() > 0:
                if f3_line.strip().split(" ")[0] == "Oliver":
                    service.popFromColleen(oliver.printFirstNode(), coleen)
                    oliver.printHelpingWhom()
                    oliver.deleteStudent()
                    continue

                elif f3_line.strip().split(" ")[0] == "Colleen":
                    service.popFromOliver(coleen, oliver)
                    coleen.helpingWhom()
                    coleen.popStudent()
                    continue
            else:
                break

    if oliver.size() == 0 and coleen.size() == 0:
        print("All students helped")
    elif oliver.size() > 0:
        print("Students left unhelped:")
        oliver.printName()
    else:
        print("Students left unhelped:")
        coleen.printName()
    print()

    # Below is the second test case
    '''
        This test case checks for all the possible orders Colleen and Oliver can make requests.
        This also includes a check if student name is Oliver.
        It also checks for the list when there are no students in the waiting list and comes out of the loop.
        It checks for Oliver's data structure with request from Oliver. As Oliver is the last TA to request help from waiting list
        It will print "All students helped" when there is no students in waiting list
    '''
    print("Test Case 2")
    list2 = ["Bob 3", "Dan 6", "Melissa 4", "Oliver ready", "Colleen ready", "Nate 1",
              "Gertrude 3", "Jessi 9", "John 11", "Oliver 7", "Colleen ready", "Colleen ready",
              "Oliver ready", "Oliver ready", "Colleen ready", "Colleen ready"]
    for m in list2:
        f2_line = m
        if f2_line.strip().split(" ")[1] != "ready":

            oliver.addStudent(f2_line.strip().split(" ")[0], f2_line.strip().split(" ")[1])
            coleen.addStudent(f2_line.strip().split(" ")[1], f2_line.strip().split(" ")[0])
            print(f2_line.strip().split(" ")[0], "is looking for help!")
        else:
            if oliver.size() > 0 and coleen.size() > 0:
                if f2_line.strip().split(" ")[0] == "Oliver":
                    service.popFromColleen(oliver.printFirstNode(), coleen)
                    oliver.printHelpingWhom()
                    oliver.deleteStudent()
                    continue

                elif f2_line.strip().split(" ")[0] == "Colleen":
                    service.popFromOliver(coleen, oliver)
                    coleen.helpingWhom()
                    coleen.popStudent()
                    continue
            else:
                break

    if oliver.size() == 0 and coleen.size() == 0:
        print("All students helped")
    elif oliver.size() > 0:
        print("Students left unhelped:")
        oliver.printName()
    else:
        print("Students left unhelped:")
        coleen.printName()
    print()

    # Below is the first test case
    '''
        This test case checks for all the possible orders Colleen and Oliver can make requests.
        The basic case as given in the lab assignment
    '''
    print("Test Case 3")
    list3 = ["Bob 3","Dan 6","Melissa 4","Oliver ready","Colleen ready","Nate 1","Gertrude 3","Colleen ready","Oliver ready"]
    for n in list3:
        f1_line = n
        if f1_line.strip().split(" ")[1] != "ready":
            oliver.addStudent(f1_line.strip().split(" ")[0], f1_line.strip().split(" ")[1])
            coleen.addStudent(f1_line.strip().split(" ")[1], f1_line.strip().split(" ")[0])
            print(f1_line.strip().split(" ")[0], "is looking for help!")
        else:
            if oliver.size() > 0 and coleen.size() > 0:
                if f1_line.strip().split(" ")[0] == "Oliver":
                    service.popFromColleen(oliver.printFirstNode(), coleen)
                    oliver.printHelpingWhom()
                    oliver.deleteStudent()
                    continue

                elif f1_line.strip().split(" ")[0] == "Colleen":
                    service.popFromOliver(coleen, oliver)
                    coleen.helpingWhom()
                    coleen.popStudent()
                    continue
            else:
                break

    if oliver.size() == 0 and coleen.size() == 0:
        print("All students helped")
    elif oliver.size() > 0:
        print("Students left unhelped:")
        oliver.printName()
    else:
        print("Students left unhelped:")
        coleen.printName()
    print()

if __name__ == '__main__':
 main()