def main():
	ano = 2016
	c = ano//100
	epacta = ((8 + (c//4)) - c + (((8*c) +13 )//25) + 11 * (ano %19 )) % 30
	print(epacta)
main()