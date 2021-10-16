def main():
	print("DIGITE A CS NAO SEI O QUE E PORRA DE CS")
	t1,t2,b1,b2,exame = eval(input("Digite os dados do aluno"))

	mb1 = 0.7 * b1 + 0.3 * t1
	mb2 = 0.7 * b2 + 0.3 * t2

	media = (mb1 + mb2) / 2
	if (media >= 7 and  frequencia >= 75) :
		print("APROVADO")
	else:
		if (media >= 3 and frequencia >= 75  ):
			media = (media + exame) / 2
			if (media >= 5 ):
				print("APROVADO")
			else:
				print("REPROVADO")
		else:
			print("REPROVADO")

main()