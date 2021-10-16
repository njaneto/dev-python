def main():
	print ("Dicionario de palavras")
	
	with open ("documento.txt", "r") as f:
		texto = f.readlines()
		dicionario = {}
		
		for linha in texto:
			palavras = linha.split()
			for palavra in palavras:
				palavra = palavra.lower()
				if not palavra in dicionario:
					dicionario[palavra] = 1
				else:
					dicionario[palavra] += 1
	f.close
	
	palavrasRepetidas = max(dicionario)
	print ("Todas as palavras contadas ", dicionario)
	print ("A palavra q mais aparece eh %s " %(palavrasRepetidas) )
main()
