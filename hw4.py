inword=input()
outword=""
for i in range(len(inword)):
	outword=inword[len(inword)-i:]
	outword+=inword[i:]
	print(outword)
