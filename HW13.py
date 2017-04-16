import re
import os

def findfiles():
    elements = os.listdir()
    dic = {}
    filesfound = 0
    for element in elements:
        if os.path.isfile(element) and not re.search(r'[^a-zA-Z]',os.path.splitext(element)[0]):
            filesfound += 1
            if element not in dic:
                dic[element] = True
    print ('Found %d file(s)\n' % filesfound)
    return dic

def printfiles():
    for file in sorted(list(findfiles().keys())):
        print(file)

def main():
    printfiles()

main()
