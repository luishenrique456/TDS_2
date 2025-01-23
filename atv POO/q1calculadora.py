#Crie uma classe que defina uma calculadora básica.
#Defina os atributos básicos e implemente os comportamentos(métodos)
class calculadora:
	sinal = None
	num1 = None
	num2 = None
	def calcular(self):
		if self.sinal == '+':
			return self.num1 + self.num2
		elif self.sinal == '-':
			return self.num1 - self.num2
		elif self.sinal == '*':
			return self.num1 * self.num2
		elif self.sinal == '/':
			return self.num1 / self.num2

def main():
	
	resul = calculadora()
	
	resul.sinal = input('Digita um sinal (+,-,*,/) : ')
	resul.num1 = int(input('Digite um número : '))
	resul.num2 = int(input('Digite um número : '))
	
	print(f' Seu resultado é {resul.calcular()}')
	
	
if __name__ == '__main__':
	main()