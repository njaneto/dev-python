def main():
	print("Informe um numero inteiro ")
	num = int(input("numero: "))
	fat = 1
	for i in range(2,num+1):
		fat = fat * i 
	
	print ("%d! = %d " %(num,fat))
main()
