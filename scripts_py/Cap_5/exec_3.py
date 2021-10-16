def main(pontuacao):
	# print("DIGITE A CS")
	# pontuacao = eval(input("Digite a pontuacao"))
	result = pontuacao // 10 - 5
	niveis = ['F','D','C','B','A']
	print(pontuacao , niveis[result])	

for i in range(100):
	main(i)