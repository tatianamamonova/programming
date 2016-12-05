f=open("text hw5.txt", 'r', encoding='utf-8')
num=0
res=0
ln=0
for word in f.read().split():
    print(word)
    ln=ln+1
    if word.endswith('.') or word.endswith(','):
        num=num+1
res=num*100/ln
print(res, '%')
