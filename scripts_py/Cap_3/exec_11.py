#SOMA N NUMEROS FORNECIDOS PELO USUARIO
def main():
	x  = eval(input("quantidade de soma entre numeros: "))
	soma = 0
	for i in range(x):
		y  = eval(input("digite o numero: "))
		soma += y
	print(soma)
main()
input("Enter para sair")
