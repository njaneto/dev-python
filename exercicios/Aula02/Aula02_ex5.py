def main ():
	print ("Qual eh seu turno")
	turno = input("digite seu torno: ")
	Texto = "Valor Invalido!"
	if  turno.upper() == "M" :
		Texto = "Bom Dia!"
	elif turno.upper() == "V":
		Texto = "Boa Tarde!"
	elif turno.upper() == "N":
		Texto = "Boa Noite!"

	print ("Um(a) %s " %(Texto))
main()
