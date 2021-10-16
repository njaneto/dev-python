def main():
	frase = input("Digite a frase :    ")
	variavel = 0
	frase = frase.replace(" ", "")
	for caracter in frase:
		variavel += ord(caracter) - 96
	return variavel
print(main())