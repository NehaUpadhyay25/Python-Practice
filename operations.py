import sys

def encryptionShift(text, index):
    s=text
    transformedChar=""
    transformedChar = ord(s[index]) + 1

    if(transformedChar > 90):
        transformedChar=chr(ord(s[index]) + 1 - 26)
    else:
        transformedChar = chr(transformedChar)

    print("Single Shift Encrypted text: " +s[:index] + transformedChar + s[(index+1):])

def encryptionMultipleShift(text, index, power):
    s=text
    transformedChar=""

    transformedChar = ord(s[index]) + (power % 26)
    if (transformedChar >= 90):
        transformedChar = chr(64 + (transformedChar - 90))
    else:
        transformedChar = chr(transformedChar)

    print("Multiple Shift Encrypted text : " + s[:index] + transformedChar + s[(index + 1):])

def encryptionRotate(text):
    s = text
    transformedChar = ""
    transformedChar = s[-1] + s[:-1]

    print("Single Rotation Encrypted text : " + transformedChar)

def encryptionMultipleRotate(text, power):
    s = text
    transformedChar = ""
    transformedChar = s[-power:] + s[:-(power)]

    print("Multiple Rotation Encrypted text : " + transformedChar)

def encryptionDuplicate(text, index):
    s = text
    transformedChar = ""
    transformedChar = "" + s[:index] + s[index] * 2 + s[(index + 1):]

    print("Single time Duplicated Encrypted text : " + transformedChar)

def encryptionMultipleDuplicate(text, index, power):
    s = text
    transformedChar = ""
    transformedChar = "" + s[:index] + s[index] * power + s[(index + 1):]

    print("Multiple times Duplicated Encrypted text : " + transformedChar)

def encryptionSwap(text, index1, index2):
    s = text
    transformedChar = ""

    swapIndex1 = s[index1]
    swapIndex2 = s[index2]

    prevText = s[:index1]
    midText = s[(index1+1):index2]
    endText = s[(index2+1):]

    transformedChar = prevText + swapIndex2 + midText + swapIndex1 + endText

    print("Swapped Encrypted text : " + transformedChar)

def encryptionDivideSwap(text, size, index1, index2):
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

        print("Encrypted Divided Swapped text : " + transformedChar)

    else:
        print("Encrypted Divided Swapped text : " + s)

def decryptionShift(text, index):
    s = text
    transformedChar = ""
    transformedChar = ord(s[index]) - 1

    if (s[index] == 'A'):
        transformedChar = chr(ord(s[index]) - 1 + 26)
    else:
        transformedChar = chr(ord(s[index]) - 1)

    print("Single Shift Decrypted text: " + s[:index] + transformedChar + s[(index + 1):])

def decryptionMultipleShift(text, index, power):
    s = text
    transformedChar = ""

    transformedChar = ord(s[index])
    if (power > 26):
        power = power % 26
        transformedChar = chr((transformedChar - power))

    else:
        transformedChar = chr((transformedChar) - power)

    print("Multiple Shift Decrypted text : " + s[:index] + transformedChar + s[(index + 1):])

def decryptionRotate(text):
    s = text
    transformedChar = ""
    transformedChar = s[1:] + s[0]

    print("Single Rotation Decrypted text : " + transformedChar)

def decryptionMultipleRotate(text, power):
    s = text
    transformedChar = ""
    transformedChar = s[power:] + s[0:power]

    print("Multiple Rotation Decrypted text : " + transformedChar)

def decryptionDuplicate(text, index):
    s = text
    transformedChar = ""

    if(s[index] == s[index+1] or s[index] == s[index-1]):
        transformedChar = "" + s[:index] + s[(index + 1):]

    else:
        transformedChar = s

    print("Single time Duplicated Encrypted text : " + transformedChar)

def decryptionMultipleDuplicate(text, index, power):
    s = text
    transformedChar = ""

    if (s[index] == s[index + 1] and s[index] == s[index - 1]):
        transformedChar = "" + s[:index] + s[(index+2):]

    elif(s[index] == s[index + 1] and s[index] == s[index + 2]):
        transformedChar = "" + s[:index+1] + s[(index+power):]

    elif (s[index] == s[index - 1] and s[index] == s[index - 2]):
        transformedChar = "" + s[:index-2] + s[index:]

    else:
        transformedChar = s

    print("Multiple time Duplicated Decrypted text : " + transformedChar)

def decryptionSwap(text, index1, index2):
    s = text
    transformedChar = ""

    swapIndex1 = s[index1]
    swapIndex2 = s[index2]

    prevText = s[:index1]
    midText = s[(index1 + 1):index2]
    endText = s[(index2 + 1):]

    transformedChar = prevText + swapIndex2 + midText + swapIndex1 + endText

    print("Swapped Decrypted text : " + transformedChar)

def decryptionDivideSwap(text, size, index1, index2):
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

        print("Decrypted Divided Swapped text : " + transformedChar)

    else:
        print("Decrypted Divided Swapped text : " + s)

def encrypt(message,transform):

    if(transform[0] == "S"):
        if(len(transform) == 3):
            encryptionShift(message, int(transform[1]))
        else:
            print("here" +transform[4])
            encryptionMultipleShift(message, int(transform[1]), int(transform[3]))

    elif(transform[0] == "R"):
        if(len(transform) == 2):
            encryptionRotate(message)
        else:
            encryptionMultipleRotate(message, int(transform[1]))


    elif(transform[0] == "D"):
        if(len(transform) == 3):
            encryptionDuplicate(message, int(transform[1]))
        else:
            encryptionMultipleDuplicate(message, int(transform[1]), int(transform[3]))

    elif(transform[0] == "T"):
        if(len(transform) == 5):
            encryptionSwap(message, int(transform[1]), int(transform[3]))
        else:
            encryptionDivideSwap(message, int(transform[2]), int(transform[4]), int(transform[6]))

    else:
        print("no transformation exist")

def decrypt(message,transform):
    print("you called decrypt")
    print(message)
    print(transform)
    print(type(transform))


def userchoice(li,choice,line):
    message = li
    transform = line

    if choice=="encrypt":
        encrypt(message,transform)

    elif choice=="decrypt":
        decrypt(message,transform)

    else:
        print("invalid - should be encrypt or decrypt")

def read(fileName,filetransform):

    with open(fileName) as f:
        for li in f:
            choice = input("Ecnrypt or decrypt")
            with open(filetransform) as f:
                for line in f:
                    userchoice(li,choice,line)



def main():
    try:
        fileName = input("Enter filename: ")
        filetransform = input("Enter the transformed file name")
        read(fileName,filetransform)
    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)

if __name__=='__main__':
    main()