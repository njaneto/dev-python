def main():
	import sqlite3
	print ("Calcular a media de todos os salario da tabela COMPANY")
	
	conn = sqlite3.connect('test.db')
	cursor = conn.execute("SELECT ID,NAME,AGE,ADDRESS,SALARY FROM COMPANY")
	
	cont = 0
	soma = 0
	for row in cursor:
		soma += int(row[4])
		cont += 1
	conn.close()
	
	print("Media dos salarios eh de %.2f:" %(soma/cont))
main()