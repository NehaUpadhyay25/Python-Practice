__author__ = "Neha Upadhyay"

"""
CSCI-603 : LAB ASSIGNMENT 4
FILENAME : transformer.py
Authors  : Neha Upadhyay  (nxu3128@rit.edu)

This program implements the encryption and the decryption process.
It takes in the message file encrypts and decypts the file according
to the transformations given through another file.
"""

import sys

def encryptionShift(text, index):
    """
    This function shifts the indexed letter(character) to the next letter
    :param text: String in file to be encrypted/decrypted
    :param index: location of character that needs to be shifted
    :return: prints new String with indexed character shifted by 1
    """
    s=text
    transformedChar=""
    transformedChar = ord(s[index]) + 1

    if(transformedChar > 90):
        transformedChar=chr(ord(s[index]) + 1 - 26)
    else:
        transformedChar = chr(transformedChar)

    print("Single Shift Encrypted text: ")
    return s[:index] + transformedChar + s[index+1:]

def encryptionMultipleShift(text, index, power):
    """
    This function shifts the indexed letter(character) by power number of times
    :param text: String in file to be encrypted/decrypted
    :param index: location of character that needs to be shifted
    :param power: the number of shifts the character needs to be shifted by
    :return: prints new String with indexed character shifted by power
    """
    s=text
    transformedChar=""

    transformedChar = ord(s[index]) + (power % 26)
    if (transformedChar >= 90):
        transformedChar = chr(64 + (transformedChar - 90))
    else:
        transformedChar = chr(transformedChar)

    print("Multiple Shift Encrypted text : " )
    return s[:index] + transformedChar + s[index+1:]

def encryptionRotate(text):
    """
    This function removes the last character of the string and appends it to the beginning of the String
    :param text: String in file to be encrypted/decrypted
    :return: prints new String rotated by 1
    """
    s = text
    transformedChar = ""
    transformedChar = s[-1] + s[:-1]

    print("Single Rotation Encrypted text : " )
    return transformedChar

def encryptionMultipleRotate(text, power):
    """
    This function removes the last character of the string and appends it to the beginning of the String power number of times
    :param text: String in file to be encrypted/decrypted
    :param power: number of times the characters are rotated one by one from the end of the string to the beginning of the string
    :return: prints new String rotated by power number of times
    """
    s = text
    transformedChar = ""
    transformedChar = s[-power:] + s[:-(power)]

    print("Multiple Rotation Encrypted text : " )
    return transformedChar

def encryptionDuplicate(text, index):
    """
    This function duplicates the character at the given index by 1
    :param text: String in file to be encrypted/decrypted
    :param index: location of the character that needs to be duplicated
    :return: prints new String with duplicated character at the given index
    """
    s = text
    transformedChar = ""
    transformedChar = "" + s[:index] + s[index] * 2 + s[(index + 1):]

    print("Single time Duplicated Encrypted text : " )
    return transformedChar

def encryptionMultipleDuplicate(text, index, power):
    """
     This function duplicates the character at the given index by power number of times
    :param text: String in file to be encrypted/decrypted
    :param index: location of the character that needs to be duplicated
    :param power: the number of times character needs to be duplicated
    :return: prints new String with duplicated character by power number of times at the given index
    """
    s = text
    transformedChar = ""
    transformedChar = "" + s[:index] + s[index] * power + s[(index + 1):]

    print("Multiple times Duplicated Encrypted text : " )
    return transformedChar

def encryptionSwap(text, index1, index2):
    """
    This function swaps two characters given at the two indexed positions in a String
    :param text: String in file to be encrypted/decrypted
    :param index1: first character that needs to be swapped
    :param index2: second character that needs to be swapped
    :return: prints new String with characters swapped to their respective positions
    """
    s = text
    transformedChar = ""

    swapIndex1 = s[index1]
    swapIndex2 = s[index2]

    prevText = s[:index1]
    midText = s[(index1+1):index2]
    endText = s[(index2+1):]

    transformedChar = prevText + swapIndex2 + midText + swapIndex1 + endText

    print("Swapped Encrypted text : " )
    return transformedChar

def encryptionDivideSwap(text, size, index1, index2):
    """
    This function first divides the String in equal sizes specified by size and then swaps the groups index1 and index2
    :param text: String in file to be encrypted/decrypted
    :param size: String is divided in 'size' equal sized group of letters
    :param index1: first group that needs to be swapped
    :param index2: second group that needs to be swapped
    :return: prints new String with groups swapped to their respective positions
    """
    s = text
    temp = []
    transformedChar = ""

    if len(s)%size==0:
        setLength=int(len(s)/ size)
        temp=[]
        i=0
        j=0
        while i<len(s):#dividing in chunks
            temp.append(s[i:setLength+i])
            i=i+setLength
            j=j+1
        #print(chunkList)
        firstswapText=temp[index1]
        secondswapText=temp[index2]

        prevText = ''.join(temp[0:index1])  #Converting list to string
        midText = ''.join(temp[index1 + 1:index2])
        endText = ''.join(temp[index2 + 1:])

        transformedChar = prevText + secondswapText + midText + firstswapText + endText

        print("Encrypted Divided Swapped text : " )
        return transformedChar

    else:
        print("Encrypted Divided Swapped text : " )
        return s

def encryptionSelfMadeFunction(text,index):
    """
    This function removes the character at the indexed postion and appends it to the end of the String
    :param text: String in file to be encrypted/decrypted
    :param index: location of the character that needs to be removed
    :return: prints new String with indexed character appended at the end of the String
    """
    s = text
    transformedChar = ""

    transformedChar = s[0:index] + s[index+1:] +s[index]

    print("Encrypted Transformed text : " )
    return transformedChar



def decryptionShift(text, index):
    """
    This function shifts the indexed letter(character) to the previous letter
    :param text: String in file to be encrypted/decrypted
    :param index: location of character that needs to be shifted
    :return: prints new String with indexed character shifted by -1
    """
    s = text;
    transformedChar = ""
    transformedChar = ord(s[index]) - 1

    if (s[index] == 'A'):
        transformedChar = chr(ord(s[index]) - 1 + 26)
    else:
        transformedChar = chr(ord(s[index]) - 1)

    print("Single Shift Decrypted text: " )
    return s[:index] + transformedChar + s[index+1:]

def decryptionMultipleShift(text, index, power):
    """
    This function shifts the indexed letter(character) by power number of times
    :param text: String in file to be encrypted/decrypted
    :param index: location of character that needs to be shifted
    :param power: the number of shifts the character needs to be shifted by
    :return: prints new String with indexed character shifted by power
    """
    s = text
    transformedChar = ""

    transformedChar = ord(s[index])
    if (power > 26):
        power = power % 26
        transformedChar = chr((transformedChar - power))

    else:
        transformedChar = chr((transformedChar) - power)

    print("Multiple Shift Decrypted text : " )
    return s[:index] + transformedChar + s[(index + 1):]

def decryptionRotate(text):
    """
    This function removes the first character of the string and appends it to the end of the String
    :param text: String in file to be encrypted/decrypted
    :return: prints new String rotated by 1
    """
    s = text;
    transformedChar = ""
    transformedChar = s[1:] + s[0]

    print("Single Rotation Decrypted text : " )
    return transformedChar

def decryptionMultipleRotate(text, power):
    """
    This function removes the first character of the string and appends it to the end of the String power number of times
    :param text: String in file to be encrypted/decrypted
    :param power: number of times the characters are rotated one by one from the beginning of the string to the end of the string
    :return: prints new String rotated by power number of times
    """
    s = text;
    transformedChar = ""
    transformedChar = s[power:] + s[0:power]

    print("Multiple Rotation Decrypted text : " )
    return transformedChar

def decryptionDuplicate(text, index):
    """
    This function removes the duplicate characters at the given index by 1
    :param text: String in file to be encrypted/decrypted
    :param index: location of the character where duplication of character is removed
    :return: prints new String with removed duplicated character at the given index
    """
    s = text
    transformedChar = ""

    if(s[index] == s[index+1] or s[index] == s[index-1]):
        transformedChar = "" + s[:index] + s[(index + 1):]

    else:
        transformedChar = s

    print("Single time Duplicated Decrypted text : " )
    return transformedChar

def decryptionMultipleDuplicate(text, index, power):
    """
    This function removes the duplicate character at the given index by power number of times
    :param text: String in file to be encrypted/decrypted
    :param index: location of the character where duplication of character is removed
    :param power: the number of times the character had been duplicated
    :return: prints new String with removed duplicated character at the given index
    """
    s = text
    i= index
    count=0

    for j in range(power):
        if(s[index] == s[i+j]):
            count = 1

        else:
            count = 0

    if(count==1):
        print("Multiple time Duplicate Decrypted text :  " )
        return s[:index] + s[(i+power):]
    else:
        print("Multiple time Duplicate Decrypted text :  " )
        return s

def decryptionSwap(text, index1, index2):
    """
    This function swaps two characters given at the two indexed positions in a String
    :param text: String in file to be encrypted/decrypted
    :param index1: first character that needs to be swapped
    :param index2: second character that needs to be swapped
    :return: prints new String with characters swapped to their respective positions
    """
    s = text
    transformedChar = ""

    swapIndex1 = s[index1]
    swapIndex2 = s[index2]

    prevText = s[:index1]
    midText = s[(index1 + 1):index2]
    endText = s[(index2 + 1):]

    transformedChar = prevText + swapIndex2 + midText + swapIndex1 + endText

    print("Swapped Decrypted text : " )
    return transformedChar

def decryptionDivideSwap(text, size, index1, index2):
    """
     This function first divides the String in equal sizes specified by size and then swaps the groups index1 and index2
    :param text: String in file to be encrypted/decrypted
    :param size: String is divided in 'size' equal sized group of letters
    :param index1: first group that needs to be swapped
    :param index2: second group that needs to be swapped
    :return: prints new String with groups swapped to their respective positions
    """
    s = text
    temp = []
    transformedChar = ""

    if len(s) % size == 0:
        setLength = int(len(s) / size)
        temp = []
        i = 0
        j = 0
        while i < len(s):  # dividing in chunks
            temp.append(s[i:setLength + i])
            i = i + setLength
            j = j + 1
        # print(chunkList)
        firstswapText = temp[index1]
        secondswapText = temp[index2]

        prevText = ''.join(temp[0:index1])  # Converting list to string
        midText = ''.join(temp[index1 + 1:index2])
        endText = ''.join(temp[index2 + 1:])

        transformedChar = prevText + secondswapText + midText + firstswapText + endText

        print("Divided Swapped Decrypted text : " )
        return transformedChar

    else:
        print("Divided Swapped Decrypted text : " )
        return s

def decryptionSelfMadeFunction(text,index):
    """
    This function removes the character at the end of the String and appends it to the indexed position of the String
    :param text: String in file to be encrypted/decrypted
    :param index: location of the character that needs to be removed
    :return: prints new String with character at end of the String inserted at the given index position
    """
    s = text
    transformedChar = ""

    transformedChar = s[:index] + s[-1] + s[index:len(s)-1]

    print("Decrypted Transformed text : " )
    return transformedChar

def encrypt(message,transform):
    """
    Encryption function
    :param message: message file
    :param transform: transformation file
    :return: encrypted function value
    """

    if(transform[0] == "S"):
        if(len(transform) == 2):
            return encryptionShift(message, int(transform[1]))
        else:
            return encryptionMultipleShift(message, int(transform[1]), int(transform[3]))

    elif(transform[0] == "R"):
        if(len(transform) == 1):
            return encryptionRotate(message)
        else:
            return encryptionMultipleRotate(message, int(transform[1]))

    elif(transform[0] == "D"):
        if(len(transform) == 2):
            return encryptionDuplicate(message, int(transform[1]))
        else:
            return encryptionMultipleDuplicate(message, int(transform[1]), int(transform[3]))

    elif(transform[0] == "T"):
        if(len(transform) == 4):
            return encryptionSwap(message, int(transform[1]), int(transform[3]))

        else:
            return encryptionDivideSwap(message, int(transform[2]), int(transform[4]), int(transform[6]))

    elif(transform[0] == "M"):
        return encryptionSelfMadeFunction(message, int(transform[1]))

    else:
        print("No Transformation Exist")

def decrypt(message,transform):
    """
    Decryption function
    :param message: Message file
    :param transform: Transformation file
    :return: decrypted function value
    """

    if(transform[0] == "S"):
        if(len(transform) == 2):
            return decryptionShift(message, int(transform[1]))
        else:
            return decryptionMultipleShift(message, int(transform[1]), int(transform[3]))

    elif(transform[0] == "R"):
        if(len(transform) == 1):
            return decryptionRotate(message)
        else:
            return decryptionMultipleRotate(message, int(transform[1]))


    elif(transform[0] == "D"):
        if(len(transform) == 2):
            return decryptionDuplicate(message, int(transform[1]))
        else:
            return decryptionMultipleDuplicate(message, int(transform[1]), int(transform[3]))

    elif(transform[0] == "T"):
        if(len(transform) == 4):
            return decryptionSwap(message, int(transform[1]), int(transform[3]))
        else:
            return decryptionDivideSwap(message, int(transform[2]), int(transform[4]), int(transform[6]))

    elif(transform[0] == "M"):
        return decryptionSelfMadeFunction(message, int(transform[1]))

    else:
        print("No Transformation Exist")

def simulate(li,choice,line):
    """
    This function helps in multiple transformations seperated by ;
    :param li: line of Message file
    :param choice: choice of user
    :param line: line of Transformation
    :return:
    """

    data = line.split(";")
    message = li
    newmessage = message
    print("Performed the following transformations : ")
    for i in range(len(data)):
        transform = data[i]

        if choice=="ENCRYPT":
            newmessage = encrypt(newmessage,transform)

        elif choice=="DECRYPT":
            newmessage = decrypt(newmessage,transform)

        else:
            print("Invalid - Should be 'ENCRYPT' or 'DECRYPT : ")

    print("After the continuous tranformations the message is " +newmessage)

def userchoice(li,choice,line):
    """
    This function takes in the choice of the User
    :param li: line of Message file
    :param choice: choice of the User
    :param line: line of Transformation file
    :return:
    """
    message = li
    transform = line

    if choice=="ENCRYPT":
        somemessage = encrypt(message,transform)
        print(somemessage)

    elif choice=="DECRYPT":
        somemessage = decrypt(message,transform)
        print(somemessage)

    else:
        print("Invalid - Should be 'ENCRYPT' or 'DECRYPT : ")

def read(fileName,filetransform):
    """
    This function reads the files
    :param fileName: Message file
    :param filetransform: Transformation file
    :return:
    """

    with open(fileName) as f:
        for li in f:
            li = li.strip()
            print("")
            choice = input("You want to 'ENCRYPT' or 'DECRYPT : ' " + li )
            print("")
            with open(filetransform) as f:
                for line in f:
                    line = line.strip()
                    if ";" in line:
                        simulate(li,choice,line)
                    else:
                        userchoice(li,choice,line)

def main():
    """
    main function to input the file names
    :return:
    """

    try:
        fileName = input("Enter filename to read messages : ")
    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)


    try:
        filetransform = input("Enter filename to read transformations : ")
    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)

    read(fileName,filetransform)

if __name__=='__main__':
    main()