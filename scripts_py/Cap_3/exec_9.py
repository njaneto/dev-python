#encontrar a soma dos n primeiros números naturais
def main():
	x = eval(input("Digite um número para fazer a soma: "))
	cont =  0
	for i in range(x):
		cont += i	
	print("A soma dos números é :", cont)
main()
