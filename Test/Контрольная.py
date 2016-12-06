f=open("Текст для кр.txt", 'r', encoding='utf-8')
for line in f:
    if line.find(' союз ')>=0:
        print(line)
f=open("Текст для кр.txt", 'r', encoding='utf-8')
Sum=0
words=""
for line in f:
    if line.find(' сущ ')>=0 and line.find(' жен ')>=0 and line.find(' ед ')>=0:
        splitted=line.split()
        if Sum>0:
            words+=", "
        words+=splitted[0]
        Sum+=float(splitted[len(splitted)-1])
print(words)
words="Сумма ipm: "
words+=str(Sum)
print(words)

checkwords=[]
wordsfound=[]

while True:
    i=input()
    if i=="":
        break
    checkwords.append(i)
    wordsfound.append(False)
f=open("Текст для кр.txt", 'r', encoding='utf-8')

for line in f:
    splitted=line.split()
    for i in range(len(checkwords)):
        if splitted[0]==checkwords[i]:
            checkwords[i]+=": "
            checkwords[i]+=line[len(splitted[0])+3:len(line)-len(splitted[len(splitted)-1])-4:]
            checkwords[i]+="; ipm: "
            checkwords[i]+=splitted[len(splitted)-1]
            wordsfound[i]=True
for i in range(len(checkwords)):
    if wordsfound[i]==False:
        checkwords[i]+=": не найдено"

for i in range(len(checkwords)):
    print(checkwords[i])
