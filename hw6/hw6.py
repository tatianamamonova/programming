import random

def verb(syllables):
	 
	verbs2 = []
	f = open("verbs2.txt", 'r', encoding='utf-8')
	for word in f:
		verbs2.append(word)
	verbs3 = []
	f = open("verbs3.txt", 'r', encoding='utf-8')
	for word in f:
		verbs3.append(word)
	if syllables == 2:
		return random.choice(verbs2)[:-1]
	else:
		return random.choice(verbs3)[:-1]

def noun(syllables):    
	nouns2 = []
	f = open("nouns2.txt", 'r', encoding='utf-8')
	for word in f:
		nouns2.append(word)
	nouns3 = []
	f = open("nouns3.txt", 'r', encoding='utf-8')
	for word in f:
		nouns3.append(word)
	if syllables == 2:
		return random.choice(nouns2)[:-1]
	else:
		return random.choice(nouns3)[:-1]

def pronouns():
	pronouns = []
	f = open("pronouns.txt", 'r', encoding='utf-8')
	for word in f:
		pronouns.append(word)
	return random.choice(pronouns)[:-1]

def liketypeverb():
	liketypeverbs = []
	f = open("liketypeverbs.txt", 'r', encoding='utf-8')
	for word in f:
		liketypeverbs.append(word)	
	return random.choice(liketypeverbs)[:-1]
    
def adjective():
	adjectives = []
	f = open("adjectives.txt", 'r', encoding='utf-8')
	for word in f:
		adjectives.append(word)	
	return random.choice(adjectives)[:-1]

def verse7a():
	return pronouns() + ' ' + liketypeverb() + ' ' + noun(3)

def verse7b():
	return noun(2) + ' ' + adjective() + ' ' + verb(3)

def verse7c():
	return noun(3) + ' ' + adjective() + ' ' + verb(2)

def verse5a():
	return noun(2) + ' ' + verb(3)

def verse5b():
	return noun(3) + ' ' + verb(2)

def make_verse7():
	verse = random.choice([1,2,3])
	if verse == 1:
		return verse7a()
	elif verse == 2:
		return verse7b()
	else:
		return verse7c()

def make_verse5():
	verse = random.choice([1,2])
	if verse == 1:
		return verse5a()
	else:
		return verse5b()


for n in range(random.randint(1,6)):
	print(make_verse5())
	print(make_verse7())
	print(make_verse5())
	print()
