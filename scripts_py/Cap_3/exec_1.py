#calcular o volume e a área de uma esfera 
def main():
	import math
	r = eval(input("Digite a area do Circulo em metros:  "))
	v = (4/3) * math.pi * (r**3)
	a = 4 * math.pi * (r**2)
	print("A area do circulo: ",a," e o volume e: ", v)
main()