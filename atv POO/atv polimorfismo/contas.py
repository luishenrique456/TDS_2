class ContaCorrente: #Superclasse
    def __init__(self,numero,saldo):
        self._numero = numero
        if self.valorEhIntFloat:
            if self.valorEhMaiorOuIgualZero:
                self._saldo = saldo
        
    @property
    def saldo(self):
        return self._saldo
        
    @saldo.setter
    def saldo(self, valor):
        if self.valorEhIntFloat(valor):
            if self.valorEhMaiorOuIgualZero(valor):
                self._saldo = valor
                    
    def creditar(self, valor):
        if self.valorEhIntFloat(valor):
            if self.valorEhMaiorQueZero(valor):
                self._saldo += valor
        return self._saldo
    
    def debitar(self, valor):
        if self.valorEhIntFloat(valor):
            if self.valorEhMaiorQueZero(valor):
                if self.valorMaiorQueSaldo(valor):
                    self._saldo -= valor
        return self._saldo

    def transferir(self, conta, valor):
        if self.valorEhIntFloat(valor):
            if self.valorEhMaiorQueZero(valor):
                if self.valorMaiorQueSaldo(valor):
                    if isinstance(conta, (ContaCorrente, ContaPoupanca)):
                        self.debitar(valor)
                        conta.creditar(valor)
        return self._saldo, conta._saldo

    def valorEhIntFloat(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Valor deve ser um número')
        return True
    
    def valorEhMaiorOuIgualZero(self, valor):
        if valor <= 0:
            raise ValueError('Valor deve ser maior ou igual a zero')
        return True
    
    def valorEhMaiorQueZero(self, valor):
        if valor < 0:
            raise ValueError('Valor deve ser maior que zero')
        return True
    
    def valorMaiorQueSaldo(self, valor):
        if valor > self._saldo:
            raise ValueError('Saldo insuficiente')
        return True
    
    def __str__(self):
        return f'Conta: {self._numero}\nSaldo: {self._saldo}'
                
class ContaPoupanca(ContaCorrente): #Subclasse 
    def __init__(self,numero,saldo,taxa_juros):
        super().__init__(numero, saldo)
        if self.valorEhIntFloat(taxa_juros):
            if self.valorEhMaiorQueZero:
                self._taxa_juros = taxa_juros

    @property
    def taxa_juros(self):
        return self._taxa_juros

    def renderJuros(self):
        self._saldo += self._saldo * self.taxa_juros
        return self._saldo
        
    def __str__(self):
        return f'Conta: {self._numero}\nSaldo: {self._saldo}\nTaxa de juros: {self._taxa_juros}'
    
class ContaImposto(ContaCorrente): #Subclasse
    def __init__(self,numero,saldo,percentual_imposto):
        super().__init__(numero, saldo)
        if self.valorEhIntFloat(percentual_imposto):
            if self.valorEhMaiorQueZero:
                self._taxa_imposto = percentual_imposto

    @property
    def taxa_imposto(self):
        return self._taxa_imposto

    def calcularImposto(self):
        self._saldo -= self._saldo * self.taxa_imposto
        return self._saldo
       
    def __str__(self):
        return f'Conta: {self._numero}\nSaldo: {self._saldo}\nTaxa de impostos: {self._taxa_imposto}'
        
class Banco:
    def __init__(self):
        self._contas = []
        self._total_valor = 0

    def adicionarConta(self, conta):
        if isinstance(conta, ContaCorrente):
            self._contas.append(conta)

    def removerConta(self, conta):
        if isinstance(conta, ContaCorrente):
            self._contas.remove(conta)

    def listarContas(self):
        for conta in self._contas:
            self._total_valor += conta._saldo
            print(conta)
        print(f'Valor total depositado: {self._total_valor}')
        return self._total_valor
        