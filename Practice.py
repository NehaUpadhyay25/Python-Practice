
def readFile(fileName):
    '''
    pre : Name of the beam starts with 'B'
    :param fileName:
    :return:
    '''
    BeamList = []
    IndividualBeamList = []
    tempList = []

    with open(fileName) as fh:
        for line in fh:
            tempList = line.strip()
            print(tempList)
    fh.close()























def main():
    try:
        fileName = input("Please enter filename for reading puzzle : ")
        readFile(fileName)
    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)


if __name__ == '__main__':
    main()
