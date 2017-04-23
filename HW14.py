import os

def startingletters():
    lettersarray = []
    for root, dirs, files in os.walk('.'):
        if dirs:
                for folder in dirs:
                        if folder:
                                lettersarray.append(folder[0].lower())
    if not lettersarray:
        return 'No folders found'
    lettersarray = sorted(lettersarray)
    maxl = 1
    letter = lettersarray[0]
    currl = 1
    for i in range(1,len(lettersarray)):
        if lettersarray[i-1] == lettersarray[i]:
            currl += 1
            if currl > maxl:
                maxl = currl
                letter = lettersarray[i]
        else:
            currl = 1
    return letter


def main():
    print(startingletters())

main()
