def count_line():
    f = open("Исландский корпус.xml", 'r', encoding='utf-8')
    S = 0
    lines = f.readlines()
    for line in lines:
        S = S + 1
    return S

def get_keys():
    import re
    dictionary = {}
    f = open("Исландский корпус.xml", 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        findkey = re.search('<w lemma="(.*?)"',line)
        if findkey != None:
            key = findkey.group(1)
            if key in dictionary:
                dictionary[key] = dictionary[key] + 1
            else:
                dictionary[key] = 1
    keysarray = list(dictionary.keys())
    return keysarray

def get_adjectives():
    import re
    dictionary = {}
    f = open("Исландский корпус.xml", 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        findkey = re.search('type="(l.f.*?)"',line)
        if findkey != None:
            key = findkey.group(1)
            if key in dictionary:
                dictionary[key] = dictionary[key] + 1
            else:
                dictionary[key] = 1
    keysarray = list(dictionary.keys())
    valuesarray = list(dictionary.values())
    with open ("Результат по прилагательным.txt",'w',encoding='utf-8') as writing:
        for i in range(len(keysarray)):
            line = keysarray[i]
            line += ' - '
            line += str(valuesarray[i])
            line += '\n'
            writing.write(line)
            
with open('Результат.txt', 'w', encoding='utf-8') as m:
    m.write(str(count_line()))
    for word in get_keys():
        writeword = '\n'
        writeword += word
        m.write(writeword)
get_adjectives()
