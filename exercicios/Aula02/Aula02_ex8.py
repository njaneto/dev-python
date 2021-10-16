def main():
	print("Informe 5 numeros")
	soma = 0
	x = 0
	while x < 5:
		print ("Digite o %d numero" %(x + 1))
		num = int(input("numero: "))
		soma = soma + num
		x = x + 1 
	print ("A soma dos 5 numeros eh: ", soma )
	print ("a media dos 5 numeros eh: ", soma / 3)
main()
