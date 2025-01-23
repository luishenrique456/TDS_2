from datetime import datetime
import random
import string

class Cartao_estacionamento:
	def __init__(self):
		self.__num_cartao = self._gerar_numero_cartao()
		self._data_entrada = datetime.now()
		self._statu = 'ativo'
		self._data_saida = None
		self._preco_total = 0.0
		self.tarifa = 4
	def _gerar_numero_cartao(self):
		digito = ''.join(random.choices(string.digits,k=5))
	
		letra = ''.join(random.choices(string.ascii_uppercase,k=3)) #gera letra maiúsculas
		return digito+letra
		
		
	def registra_saida(self):
		data_saida = input('Data Saida (DD/MM/AAAA) e hora (H:M) : ')
		self._data_saida = datetime.strptime(data_saida,'%d/%m/%Y %H:%M')
		
		self._statu = 'finalizado'
		
		valor_restante, valor_total = self.calcular_valor()
		
		return f'Valor adicional : R$ {valor_restante}\nValor total : R${valor_total}'
		
		
	def calcular_valor(self):
		totalMin = (self._data_saida -self._data_entrada).total_seconds() / 60
		if totalMin > 120:
			minRestante = (totalMin - 120)
			valDoRestante = ((minRestante / 15) * 0.5)
			valTotal = valDoRestante + (self.tarifa * 2)
		else:
			valDoRestante = 0
			valTotal = self.tarifa * 2
		return round(valDoRestante, 2), round(valTotal, 2)

		
	@property
	def num_cartao(self):
		return self.__num_cartao
	
				
		
		
		
	
		
		
		
		
	def __str__(self):
		n = f'Número do cartão : {self.__num_cartao}'
		data_entrada_form = self._data_entrada.strftime('\n Data entrada : ' '%d/%m/%Y' ' Hora : ' '%H:%M')
		return n+data_entrada_form
	
		
		
def main():
	cartao1=Cartao_estacionamento()
	
	#print(f'número do cartão {cartao1.num_cartao}') #gera número cartão automatico
	
	print('Cartão 1')
	print(cartao1)
	print(cartao1.registra_saida())
	print('\n')
	
	print('Cartão 2')
	cartao2 = Cartao_estacionamento()
	print(cartao2)
	print(cartao2.registra_saida())
	print('\n')
	
	print('Cartão 3')
	cartao3 = Cartao_estacionamento()
	print(cartao3)
	print(cartao3.registra_saida())
	
	
	
	
	
	
	
	
	
	
if __name__ == '__main__':
	main()
	