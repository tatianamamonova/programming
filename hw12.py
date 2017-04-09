import re

def doubledic_print(doubledic):
	for outerkey in doubledic:
		print('{}:'.format(outerkey))
		template = '\t{} ({})'
		for innerkey in doubledic[outerkey]:
			print(template.format(innerkey,doubledic[outerkey][innerkey]))
			
def clear_word(word):
	word = re.sub(r'[,.?!":]','',word)
	if re.search("[a-яёА-ЯЁ]",word) == None:
            word = ""
	return word

def main():
	with open ('t.txt' , 'r', encoding='utf-8') as f:
		arr = re.split(r'ENDMARK',re.sub(r'([!?.:]|(\.\.\.)) "?([А-ЯЁ])',r'ENDMARK\3',re.sub(r'- ','',re.sub(r'\t|\n',' ',f.read()))))
		outdict = {sentence: {clear_word(word): len(clear_word(word)) for word in sentence.split() if clear_word(word)} for sentence in arr if sentence}
#		print(outdict)
		doubledic_print(outdict)

main()
