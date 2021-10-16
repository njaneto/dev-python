#encontrar a soma dos n primeiros números naturais
def main():
	x = eval(input("Digite a qtd de termos ao cubo a somar: "))
	cont =  0
	for i in range(x):
		cont = cont + (i**3)
	print("A soma dos números é :", cont)
main()
