import random

class regra_jogo:
	opcao = ['pedra','papel','tesoura']
	usuario = None
	bot = None
	def escolhar(self):
		if self.usuario not in self.opcao:
			print('Escolha inválida.Tenta novamente.')
		else:
			self.bot = random.choice(self.opcao)
			print(f'Adversario escolheu : {self.bot}')
		#resultado do usuário
		if self.usuario == self.bot:
			return f'empatou!'
		elif (self.usuario == 'pedra' and self.bot == 'tesoura') or \
		(self.usuario == 'papel' and self.bot == 'pedra')or \
		(self.usuario == 'tesoura' and self.bot == 'papel'):
			return f'Você Venceu ( : '
		else:
			return f'Você perdeu ):'
def main():
	while True:
		
		jg = regra_jogo()
		
		jg.usuario = input('Escolha um opção(pedra,papel,tesoura) ou digite "sair'' encerra jogo : ').strip().lower()
		if jg.usuario == 'sair':
			print('Jogo Acabou!')
			break
		
		
		
		print(jg.escolhar())
	
	
	
	
if __name__ == '__main__':
	main()