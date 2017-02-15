import re

def field(location):
    with open (location,'r',encoding='utf-8') as webpage:
        rawhtml=webpage.read()
        r = re.search('id="P101">(.*)</span>',rawhtml)
        found = r.group(1)
        found = re.sub('</?a(.*?)?>','',found)
        print(found)

field('mendeleev.html') 
