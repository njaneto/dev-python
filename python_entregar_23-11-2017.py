def main():
	import numpy as np
	from scipy import stats as st

	data=[]
	entrada = input("Digite a sequencia numerica separadas por ',': ") 
	numerosComoString = entrada.split(",")
	numeros = [int(numero) for numero in numerosComoString] 
	
	data.append(numeros)
	shapiro_results = st.shapiro(data)

	print ("Shapiro:", shapiro_results  )
	print ("Resultado:", shapiro_results[0] )
	print ("Significância:", shapiro_results[1] )
	
	if(shapiro_results[1] < 0.05):
		print("Nao Normal!")
		print("Mediana:", np.mean(data) )
		print('Minimo:', np.min(data))
		print('Máximo:', np.max(data))
		print('Primeiro Quartil ',np.percentile(data,25))
		print('Terceiro Quartil ',np.percentile(data,75))
		print('Intervalo de quartil (IQ)',(np.percentile(data,75)- np.percentile(data,25)))
	else:
		print("Normal!")
		print("Media:", np.mean(data) )
		print('Desvio Padrão:' ,np.std(data))
		print('Minimo:', np.min(data))
		print('Máximo:', np.max(data))
		print('Coeficiencia de Variação:',(np.std(data) / np.mean(data)))
main()

#################################################################################################
#						Custo total de propriedade ?											#
#	TCO é uma analise onde é possível descobrir todos os custos ao longo da vida. 				#
#	Essa analise é muito utilizado por grandes empresas de Tecnologias para tomar 				#
#	decisões necessárias para aquisição de TI (hardware/software), máquinas, equipamentos, etc.	#
#																								#
#################################################################################################