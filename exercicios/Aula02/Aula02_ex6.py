def main():
	print ("Media")
	Pnota = eval(input("Digite a 1 nota : "))
	Snota = eval(input("Digite a 2 nota : "))
	media = ( Pnota + Snota ) / 2 

	letra = "E"	
	if media >= 9:
		letra = "A"
	elif media <= 9.0 and media > 6.0:
		letra = "B"
	elif media <= 6.0 and media > 4.0:
		letra = "D"		

	print ("Sua media eh %.2f e sua nota eh %s " %(media,letra))
main()
