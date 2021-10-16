def main():
	import csv
	print ("contar forma de pagamento")
	pagamento = {}	
	with open('SalesJan2009.csv') as csvFile:
		reader = csv.DictReader(csvFile, delimiter=',')
		for row in reader:
			if not row['Payment_Type'].upper() in pagamento:
				pagamento[row['Payment_Type'].upper()] = 1
			else:
				pagamento[row['Payment_Type'].upper()] += 1 

	csvFile.close
	cartao = max(pagamento)				
	print ("O cartao mais utilizado foi o: %s " %(cartao) )
	print ("Quantidades de vezes que foi utilizado:", pagamento["VISA"] )
main()