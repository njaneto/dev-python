def main():
	x1 = eval(input("Digite a 1(x1) coordenada "))
	x2 = eval(input("Digite a 2(x2) coordenada "))
	y1 = eval(input("Digite a 3(y1) coordenada "))
	y2 = eval(input("Digite a 4(y2) coordenada "))
	
	inclinacao = (y2 - y1) / (x2 - x1)
	print("O calculo da inclinacao dois pontos sao ", inclinacao)
main()