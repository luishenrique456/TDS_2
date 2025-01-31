class ContaCorrente:
    def __init__(self, numero = None, saldo = None, nome = None):
        self.__numero = numero
        self.__saldo = saldo
        self.__nome = nome

    # CREDITAR
    def creditar(self, valor_recebido):
        if isinstance(valor_recebido, (int,float)):
            self.saldo += valor_recebido
            return None
        else:
            raise ValueError('Digite um valor numérico;')
       
    # DEBITAR
    def debitar(self, valor_recebido):
        if 0 <= valor_recebido <= self.__saldo:
            self.__saldo -= valor_recebido
            print('\nDébito realizado com sucesso;')
        else:
            print('\nNão foi possível realizar o débito, saldo insulficiente;')
       
    # TRANSFERIR
    def transferir(self, conta, valor_transferencia):
        if self.__saldo < valor_transferencia:
            print('\nTransferência não realizada. Saldo insulficiente;')
        else:
            self.__saldo = self.__saldo - valor_transferencia
            conta.creditar(valor_transferencia)
            print('\nTransferência realizada com sucesso;')
           

    # SALDO
    @property
    def saldo(self):
        return self.__saldo
   
    @saldo.setter
    def saldo(self, x):
        self.__saldo = x

    def mostrar_saldo(self):
        print(f'\nSeu saldo atual é: {self.saldo}R$')

    def __str__(self):
        return f'  <EXTRATO>\n\
|Nome: {self.__nome}\n\
|Numero da conta: {self.__numero}\n\
|Seu saldo é de {self.__saldo:.2f}R$\n'
       
class ContaPoupanca(ContaCorrente):
    def __init__(self, taxa_juros = None, numero = None, saldo = None, nome = None):
        super().__init__(numero, saldo, nome)
        self.taxa_juros = taxa_juros

    def render_juros(self):
        saldo = self.saldo + (self.saldo * (self.taxa_juros/100))
        self.saldo = saldo

    def __str__(self):
        return super().__str__() + f'|Tipo: Conta Poupança\n|Taxa de Juros: {self.taxa_juros}%'
       


# Crie uma classe ContaImposto que herda de ContaCorrente e possui um atributo percentual_Imposto. Método calcula_Imposto()
class ContaImposto(ContaCorrente):    
    def __init__(self, percentual_imposto = None, numero = None, saldo = None, nome = None):
        super().__init__(numero, saldo, nome)
        self.__percentual_imposto = percentual_imposto

    #Calcula Imposto
    def calcula_imposto(self):
        self.saldo -= self.saldo * (self.__percentual_imposto/100)

    def __str__(self):
        return super().__str__() + f'|Tipo: Conta Imposto\n|Percentual de Imposto: {self.__percentual_imposto}%'
       
       

#Criando Objetos
conta1 = ContaPoupanca(1, 123, 1400, 'Luis')
conta2 = ContaPoupanca(90, 456, 90, 'Kallya')
conta3 = ContaPoupanca(3, 789, 2500, 'Pedro')

#Transferência 1
conta1.transferir(conta2, 120)
print(conta2)


