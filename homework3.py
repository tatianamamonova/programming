arr=[]
while True:
    inword=input()
    if inword=="":
        break
    arr.append(inword)
for i in arr:
    if i[-3:]=="are":
        print(i)
    elif i[-3:]=="ire":
        print(i)
    elif i[-3:]=="ere":
        print(i)
    elif i[-3:]=="ari":
        print(i)
    elif i[-3:]=="iri":
        print(i)
    elif i[-3:]=="eri":
        print(i)
    elif i[-4:]=="isse":
        print(i)
    elif i[-4:]=="esse":
        print(i)
