def main():
	frase = input("Digite a frase :    ")
	lista = frase.split();
	result = 0
	for palavra in lista:
		result += len(palavra)
	print (result / len(lista))	
main()