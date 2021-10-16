def main():
	print ("Calculo de IMC")
	Altura = eval(input("Digite a Altura :  "))	
	Peso = eval(input("Digite a Peso :  "))
	IMC = Peso / ( Altura * 2 )
	
	if IMC < 18.5:
		situacao = "BAIXO"
	elif IMC >= 18.5 and IMC <= 24.99:
		situacao = "NORMAL"
	elif IMC >= 25:
		situacao = "SOBREPESO"
		
	print ("Seu IMC eh de: %.2f. Q eh considerado %s !" %( IMC, situacao ))
main()