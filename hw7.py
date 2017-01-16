def make_array(filename):
    wordlist = []
    with open(filename, 'r', encoding='utf-8') as text:
        text = text.readlines()
        for line in text:
            linelist = line.split()
            for word in linelist:
                wordlist.append(check_english_word(word))
    return wordlist

def find_ed(arrayname):
    n=0
    for word in arrayname:
        if word.endswith('ed'):
            n=n+1
    print(n)

def find_ied(arrayname):
    n=0
    for word in arrayname:
        if word.endswith('ied'):
            n=n+1
    print(n)

def check_english_word(word):
    eng_upper = "ABCDEFGHIJKLMONPQRSTUVWXYZ"
    eng_lower = eng_upper.lower()
    end_cleaned = False
    while not end_cleaned:
        if len(word) < 1:
            break
        for i in range(len(eng_upper)):
            if word[-1] == eng_upper[i] or word[-1] == eng_lower[i]:
                end_cleaned = True
                break
        if not end_cleaned:
            word = word[:-1]
    return word

find_ed(make_array('Austen Jane.txt'))
find_ied(make_array('Austen Jane.txt'))