import random

def makedict (tablename):
    dic = {}
    with open(tablename, 'r', encoding='utf-8') as sheet:
        sheet = sheet.readlines()
        for row in sheet:
            s = row
            s = s.replace(' ','')
            s = s.replace('\n','')
            s = s.replace(',',';')
            keyvalarr = s.split(';')
            if len(keyvalarr) == 2:
                dic[keyvalarr[0]] = keyvalarr[1]
            else:
                continue
    return dic

def testdict (dictionary):
    hints = list(dictionary.keys())
    nouns = list(dictionary.values())
    hint = random.choice(hints)
    while True:
        s = hint + ' '
        for c in range(len(hint)):
            s += '.'
        print(s)
        answer = input()
        if dictionary[hint] == answer:
            print("Верный ответ!")
            break
        else:
            print ("Неверный ответ")

testdict(makedict("in.csv"))
