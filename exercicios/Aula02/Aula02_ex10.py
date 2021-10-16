def main():
	print ("Gerador de Tabuada")
	yes = input("Deseja imprimir a tabuada do 1 ao 10 s/n ")
	
	if yes.upper() == "S":
		x = 1
		while x < 10:
			print ("Tabuada do %d " %(x))
			for i in range(10):
				print ("%d x %d = %d" %(x, (i+1) , x * (i+1)))
			x = x + 1
	else:
		Tabuada = eval(input("Imprimir a tabuada do : "))
		print ("Tabuada do %d " %(Tabuada))
		for i in range(10):
			print ("%d x %d = %d" %(Tabuada, (i+1) , Tabuada * (i+1)))
main()
