def main():
	import json
	import requests
	
	print ("Consulta CEP")
	cep = str(input("Informe o CEP: "))
	uri = "https://viacep.com.br/ws/%s/json/" %cep 

	response = requests.get(uri)
	address = json.loads(response.text)
	print ( "Endereco: {}, Bairro: {}, Cidade: {}, Cep: {} ".format( address["logradouro"],address["bairro"], address["localidade"], address["cep"]))

main()