def main():
	print("Informe 5 numeros ")
	aux = 0
	x = 0
	while x < 5:
		print ("Digite o %d numero" %(x + 1))
		num = int(input("numero: "))
		if num < 99999 and num > aux:
			aux = num
		x = x + 1 
	print ("o maior numero eh: ", aux)
main()
	