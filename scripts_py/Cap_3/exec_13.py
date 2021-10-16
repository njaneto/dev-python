#aproximacao do pi
from math import pi
def main():	
	n = 10000
	result = 0
	sinal = 1
	for i in range(1, n, 2):
		result += 4/i *  
		sinal = sinal * -1
	print("O valor aproximado e : ",result,"o valor de pi e ", pi," o valor arredondado e ",  result - pi)
main()