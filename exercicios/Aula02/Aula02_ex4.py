def main():
	print ("Calculo de Salario")
	Salario = eval(input("Digite o Salario :  "))	
	IR = Salario * 0.11
	INSS = Salario * 0.08
	Descontos = IR + INSS
	Liquido = Salario - Descontos
	print("Salario Bruto: %1.2f. IR sobre o salario eh de: %1.2f. INSS sobre o salario eh de: %1.2f." %(Salario,IR,INSS))
	print("Todal de Descontos: %1.2f. Salario liquido: %1.2f." %(Descontos,Liquido))
main()