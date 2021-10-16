def main():
	bebida = 10.50
	frete = 0.86
	custoFixo = 1.50

	qtdBebidas = eval(input("Quantas bebidas"))
	result = ((bebida + frete) * qtdBebidas) + custoFixo
	print("O valor total e: ", result)
main()