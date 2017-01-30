def find_vypit():
    with open('text.txt', 'r', encoding='utf-8') as text:
        text = text.readlines()
        for line in text:
            linelist = line.split()
            for w in linelist:
                import re
                if re.match("[Вв]ып(ь(ют?|е(шь|т|м|те|й|йте))|и(л(а|о)?|т(о(го|му?|й|е)?|ы(й|ми?|е|х)?)?|в|вш(и(й|е|х|ми?)?|е(й|го|му?)?|ая|ую)))\Z", w) != None:
                    print(w) 
