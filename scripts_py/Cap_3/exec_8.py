#comprimento da escada
from math import sin
from math import pi
def main():		
	altura  = eval(input("Digite a altura: "))
	graus  = eval(input("Digite a inclinação (graus): "))
	angulo =  (pi/180)*graus
	comprimento = altura / sin(angulo)
	print("O comprimento da escada ate a casa e: ", round(comprimento))
main()