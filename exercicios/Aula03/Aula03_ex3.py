def main():
	import json
	print ("Imprimir codigo do pais")
	
	f = open("country.json")
	country = json.load(f)
	for pais in country['countries']:
		if pais["name"] == "Bosnia":
			print ( "Name: {}, Codigo: {} ".format( pais["name"],pais["code"] ))
	f.close
main()
