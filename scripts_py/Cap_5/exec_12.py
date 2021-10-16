import os
def main():
	print ("Esse aqui e um arquivo batch")
	caminho = os.path.dirname(os.path.realpath(__file__))
	infileName = input("Qual nome do aquivo de entrada ") 
	outfileName = input("Qual nome do aquivo de saida ") 

	infile = open(caminho +"\\" + infileName, 'r')
	outfile = open(caminho +"\\" + outfileName, 'w')

	num_words = 0
	num_lines = 0
	num_chars = 0
	
	for line in infile:
		num_lines += 1
		num_chars += len(line)
		words = line.split()
		num_words += len(words)
	STR = num_words ," - ", num_lines ," - ", num_chars
	print( STR , file=outfile)

	infile.close()
	outfile.close()
	print ("Os nomes dos usuarios foram armasenados em :", outfileName)

main()