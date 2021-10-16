def main():
	frase = input("Digite a letra :    ")
	variavel =""
	for caracter in frase:
		variavel += chr(ord(caracter) + 2)
	return(variavel)
print(main())