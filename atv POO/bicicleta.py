# Implemente a classe Bicicleta, colocando limites máximos e mínimos para os estados: veloc_atual,
# altura_cela e calibragem_pneus através de seus respectivos métodos. Altere os métodos: regular_cela,
# calibrar_pneus para permitirem as mudanças caso a bicicleta esteja parada (veloc_atual=0).
class bicicleta:
    def __init__(self,veloc_atual=0,altura_cela=10,calibragem_pneus=10,):
        self.veloc_atual = max(0,min(veloc_atual,20))
        self.altura_cela = min(10,max(veloc_atual,20))
        self.calibragem_pneus = min(10,max(veloc_atual,80))
    def anda(self,veloc):
        nova_veloc = self.veloc_atual + veloc
        if nova_veloc <= 20:
            self.veloc_atual = nova_veloc
            return f'bicicleta esta andando {self.veloc_atual} km/h'
        else:
            return 'Velocidade ultrapassa o limite de 20 km/h'
    def para(self):
        if self.veloc_atual == 0:
            return 'bicicleta esta parada'
    def regular_cela(self,nova_altura):
        if 10 <= nova_altura <= 20:
            self.altura_cela = nova_altura
            return f'você regulou altura cela para  {self.altura_cela}'
        else:
            return 'altura deve estar entre 10 e 20 cm'
    def calibrar_pneus(self,nova_calibrar):
        if 10 <= nova_calibrar <= 80:
            
            self.calibragem_pneus = nova_calibrar
            return f'você caligrou pneus para {self.calibragem_pneus}'
        else:
            return 'calibragem deve estar entre 10 e 80 pis'
            
def main():
    bike = bicicleta()
    while True:
        print("\nEscolha uma opção:")
        print("1. Andar com a bicicleta")
        print("2. Parar a bicicleta")
        print("3. Regular altura da cela")
        print("4. Calibrar pneus")
        print("5. Sair")
        
        opcao = int(input('Digite um número da sua escolha : '))
        
        if opcao == 1:
            veloc = int(input('Digite sua velocidade (max é 20) : '))
            print(bike.anda(veloc))
            
        elif opcao == 2:
            print(bike.para())
            
        elif opcao == 3:
            nova_altura = int(input('Digite altura da cela : '))
            print(bike.regular_cela(nova_altura))
        elif opcao == 4:
            nova_calibrar = int(input('Digite a calibra o pneus : '))
            print(bike.calibrar_pneus(nova_calibrar))
        elif opcao == 5:
            print('Encerrando o programa.')
            break
        else:
            print('opção invalida')
    
    
if __name__ == '__main__':
    main()