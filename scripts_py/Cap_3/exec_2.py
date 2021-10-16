#calcular o volume e a área de uma esfera 
def main():
	import math
	
	d = eval(input("Digite o diametro da pizza: "))
	p = eval(input("Digite o preco  da pizza: "))
	
	r = d / 2
	a = math.pi * (r**2)
	resp =  p / a
	
	print("O custo por metro quadrado é :", resp)
main()