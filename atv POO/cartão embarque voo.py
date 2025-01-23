from datetime import datetime
import random

class cartao_embarque_voo:
	def __init__(self,nome,num_voo,cod_reserva,data_embarque,hora_embarque,check=False,assento=['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'B4']):
		#Atributos imutáveis
		self.nome = nome
		self.num_voo = num_voo
		self.cod_reserva = self.validar_reserva(cod_reserva)
		
		self.data_embarque = self.validar_data(data_embarque)
		self.hora_embarque = self.validar_hora(hora_embarque)
		
		#Atributos mutáveis
		self.check = check
		self.assento = assento
		
	def realiza_check(self):
			if not self.check:
				self.check = 'Realizado'
				assento = self.gera_assento()
				return f' statu : {self.check} | seu assento {assento}'
			else:
				   return 'check já foi realizado'
								
	def gera_assento(self):
			assento_disponivel = random.choice(self.assento)
			self.assento.remove(assento_disponivel)
			return assento_disponivel
			
	def validar_data(self,data_str):
		try:
			data_formata = datetime.strptime(data_str, '%d/%m/%Y')
			return data_formata
		except:
			raise ValueError ('Data inválida')
			
	def validar_hora(self,hora_str):
		try:
			hora_formatada = datetime.strptime(hora_str,'%H:%M')
			return hora_formatada
		except:
			raise ValueError ('Hora inválida')
			
	def validar_reserva(self,cod_reserva):
				if len(cod_reserva) == 6:
					return cod_reserva
				else:
					raise ValueError('códogo reserva deve ter exatamente 6 caracteres')
	
	
	def __str__(self):
		data_formatada = self.data_embarque.strftime('%d/%m/%Y')
		hora_formatada = self.hora_embarque.strftime('%H:%M')
		return f'nome : {self.nome}|número voo : {self.num_voo}|código reserva : {self.cod_reserva}|data embarque : {data_formatada}|hora embarque : {hora_formatada}|'
		
	
             
def main():
	
	print('Primeiro Cartao de voo\n')
	nome = input('Nome do passageiro : ')
	
	try:
		
		num_voo = int(input('Digite número do voo : '))
	except:
		raise ValueError('número voo tem ser número inteiro ')
	
	
	cod_reserva = input('Digite Código da reserva (deve 6 caracteres alfanuméricos ) : ')
		
	data_embarque = input('Digite Data (dd/mm/aaaa) : ')
	
	hora_embarque = input('Digite Hora (h:m) : ')
	
	
	cartao_voo = cartao_embarque_voo(nome,num_voo,cod_reserva,data_embarque,hora_embarque)
	
		
	statu_check = input('deseja realiza check digite (s) para confirma ou pressione Enter para não realizar check : ').lower()
	if statu_check == 's':
		print(cartao_voo.realiza_check())
	else:
			print('Check-in não realizado.')
			
	print('informação primerio Cartão de voo\n')
	print(cartao_voo)
	
	#segunda instancia
	print('Segundo cartão de voo\n')
	
	cartao_voo2 = cartao_embarque_voo('Luis','2','abc123','20/11/2024','03:40')
	
	print(cartao_voo2.realiza_check())
	
	print(cartao_voo2)
	
	#terceira instancia
	print('Teceiro Cartão de voo\n')
	
	cartao_voo3 = cartao_embarque_voo('João','3','f1g2h3','21/11/2024','16:40')
	
	print(cartao_voo3.realiza_check())
	
	print(cartao_voo3)
	
	
	
	
if __name__ == '__main__':
	main()
	
	