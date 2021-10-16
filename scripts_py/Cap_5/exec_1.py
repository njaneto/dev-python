def main():
	dia, mes, ano =  eval(input("Digite o dia, mes e ano"))

	data = "{0}/{1}/{2}".format(dia,mes, ano)
	
	meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro","Dezembro"]

	mesStr = meses[mes - 1]
	
	data2 = "{0} {1},  {2}".format(mesStr, dia, ano)

	print("A data eh {0} ou {1}".format(data, data2))
main()