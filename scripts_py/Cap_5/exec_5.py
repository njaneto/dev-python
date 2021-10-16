def main():
	print("digite sua frase")
	frase = input("Digite a frase")
	variavel = 0
	for caracter in frase:
		variavel += ord(caracter) - 96
	return variavel

print(main())