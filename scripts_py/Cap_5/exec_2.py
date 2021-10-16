def main():
	print("DIGITE A CS ")
	pontuacao = eval(input("Digite a sua pontuacao"))

	niveis = [(0,'F'),(1,'F'),(2,'D'),(3,'C'),(4,'B'),(5,'A')]
	print(niveis[pontuacao])

main()