def main():
	print("Aula02 Exe1")
	aux = 0
	soma = 0
	x = 0
	while x < 3:
		print ("Digite o %d numero" %(x + 1))
		num = int(input("numero: "))
		if num < 99999 and num > aux:
			aux = num
		soma = soma + num
		x = x + 1 
	print ("o maior numero eh: ", aux)
	print ("a media dos 3 numeros eh: ", soma / 3)
main()
