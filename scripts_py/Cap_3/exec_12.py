#ENCONTRA MEDIA DE N NUMEROS

def main():
	x  = eval(input("quantidade de numeros a serem somados: "))
	soma = 0
	for i in range(x):
		soma  += eval(input("Digite o numero : "))
	print(soma / x )
main()
input("Enter para sair")
