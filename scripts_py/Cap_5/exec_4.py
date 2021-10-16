def acronimo(cadeia):
	siglas = ''
	nova_cadeia = cadeia.split()

	for pal in nova_cadeia:
		siglas += pal[0]
	return siglas.upper()

print(acronimo("takai perreira mestre dos magos"))