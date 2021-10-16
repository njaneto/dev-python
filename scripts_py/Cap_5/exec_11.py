
import os
def main():
	print ("Esse aqui e um arquivo batch")
	caminho = os.path.dirname(os.path.realpath(__file__))
	outfileName = input("Qual nome do aquivo de saida ") + ".txt"

	outfile = open(caminho +"\\" + outfileName, 'w')

	for i in range(100):		
		print(pont(i), file=outfile)

	outfile.close()
	print ("Os nomes dos usuarios foram armasenados em :", outfileName)

def pont(pontuacao):
	result = pontuacao // 10 - 5
	niveis = ['F','D','C','B','A']
	return niveis[result]
main()