def main():
	from math import sqrt
	a, b, c = eval(input("Digite os lados de um triagulo separados por virgula: "))
	s =  (a+b+c)/2	
	a =  sqrt(s * ((s - a)*(s-b)*(s-c)) )
	print("O calculo das areas de um trigulo e  ", a)
main()