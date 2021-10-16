def main():
	frase = input("Digite a  letra :  ")
	variavel = ""
	for caracter in frase:
		variavel += convert(caracter)
	return(variavel)

def convert(char):
	return chr( ( ( (ord(char) + 1) - ord("a")  )  % 26 ) + ord("a"))

print(main())