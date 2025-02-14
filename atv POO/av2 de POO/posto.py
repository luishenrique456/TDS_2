class PostoDeCombustivel:
    def __init__(self, nome):
        self.nome = nome
        self.bombas = []
        
    # Adicionar bomba de combustivel
    def adicionar_bomba(self, bomba):
        # Recebe bomba e verifica se ela é do tipo BombaDeCombustivel
        if isinstance(bomba, BombaDeCombustivel):
            self.bombas.append(bomba)
            return f'Cadastrando bomba {bomba.identificador}...'
        else:
            raise TypeError('Bomba inválida. A bomba deve ser do tipo BombaDeCombustivel.')

    def listar_bombas(self):
        # Para cada item na lista de bombas, imprime o identificador da bomba
        lista_bombas_formatada = [f'Bomba: {bomba.identificador}' for bomba in self.bombas]
        return ", ".join(lista_bombas_formatada)
   
class BombaDeCombustivel:
    # Contador de bombas
    contadorId = 0
    def __init__(self):
        # Garante que cada Bomba de Combustível tenha seu próprio ID / auto-incremento
        BombaDeCombustivel.contadorId += 1
        # Recebe um identificador
        self.identificador = BombaDeCombustivel.contadorId
        self.combustivel = None
        
    def associar_combustivel(self, combustivel):
        # Recebe combustivel e verifica se ele é do tipo Combustivel
        if isinstance(combustivel, Combustivel): # Testar se é apenas a superclasse ou precisa das subclasses
            self.combustivel = combustivel
            return f'Associando {self.combustivel} à bomba {self.identificador}...'
        else:
            raise TypeError('Combustível inválido. O combustível deve ser do tipo Combustivel.')

    def abastecer(self, qtd_litros, controle):
        if isinstance(self.combustivel, Combustivel):
            if isinstance(qtd_litros, (float, int)):
                if qtd_litros > 0:
                    abastecimento = Abastecimento(self, qtd_litros)
                    return f'Realizando abastecimento na bomba {self.identificador}: {qtd_litros} litros...\nTotal a pagar: R$ {abastecimento.valor:.2f}'
                else:
                    raise ValueError('Quantidade de litros deve ser maior que zero.')
            else:
                raise TypeError('Quantidade de litros deve ser um float ou inteiro.')
        else:
            raise TypeError('Combustível inválido. O combustível não foi associado a essa bomba.')
        
# Superclasse
class Combustivel:
    def __init__(self, nome, preco_por_litro):
        lista_nomes = ['Gasolina', 'Etanol']
        nome_capitalizado = nome.capitalize()
        if nome_capitalizado in lista_nomes:
            self.nome = nome_capitalizado
        else:
            raise ValueError('Nome inválido. O nome deve ser "Gasolina" ou "Etanol".')
        
        if isinstance(preco_por_litro, (float, int)):
            if preco_por_litro > 0:
                self.preco_por_litro = preco_por_litro
            else:
                raise ValueError('Preço por litro deve ser maior que zero.')
        else:
            raise TypeError('Preço por litro deve ser um float ou inteiro.')

    def calcular_valor(self, qtd_litros):
        raise NotImplementedError('Método não implementado na superclasse')
    
    def __str__(self):
        return f'{self.nome} genérico.'
    
# Subclasse
class Gasolina(Combustivel):
    def __init__(self, preco_por_litro, aditivada):
        # Reusa o construtor da superclasse 
        super().__init__('Gasolina', preco_por_litro)
        # Recebe sim ou não e transforma em True ou False
        if aditivada.lower() == 'sim':
            self.aditivada = True
        elif aditivada.lower() == 'não':
            self.aditivada = False
        else:
            raise ValueError('Aditivada deve ser "Sim" ou "Não".')

    # Recebe quantidade de litros
    def calcular_valor(self, qtd_litros):
        # Retorna o valor total do abastecimento
        return qtd_litros * self.preco_por_litro

    def __str__(self):
        return f'Gasolina {"Aditivada" if self.aditivada else "Não aditivada"}'
    
class Etanol(Combustivel):
    def __init__(self, preco_por_litro, origem):
        # Reusa o construtor da superclasse 
        super().__init__('Etanol', preco_por_litro)
        # Lista de origens do etanol do posto
        self.lista_origem = ['Cana de açucar', 'Milho']
        # Recebe origem do etanol e verifica se existe na lista de origens
        origem_capitalizado = origem.capitalize()
        if origem_capitalizado in self.lista_origem:
            self.origem = origem_capitalizado
        else:
            raise ValueError('Origem inválida. A origem deve ser "Cana de açucar" ou "Milho".')

    # Recebe quantidade de litros
    def calcular_valor(self, qtd_litros):
        # Retorna o valor total do abastecimento
        return qtd_litros * self.preco_por_litro
    
    def __str__(self):
        return f'Etanol de {self.origem}'
    
class Abastecimento:
    def __init__(self, bomba, qtd_litros):
        # Posso usar bomba.combustivel para acessar os atributos de Combustivel
        if isinstance(bomba, BombaDeCombustivel):
            self.bomba = bomba
        else:
            raise TypeError('Bomba inválida. A bomba deve ser do tipo BombaDeCombustivel.')
        self.combustivel = bomba.combustivel
        if isinstance(qtd_litros, (float, int)):
            if qtd_litros > 0:
                self.qtd_litros = qtd_litros
            else:
                raise ValueError('Quantidade de litros deve ser maior que zero.')
        else:
            raise TypeError('Quantidade de litros deve ser um float ou inteiro.')
        self.valor = self.combustivel.calcular_valor(qtd_litros)
        
    def resumo_abastecimento(self):
        return f'Abastecimento na bomba {self.bomba.identificador}: {self.qtd_litros} litros -> R$ {self.valor:.2f}'
    
class Controle_De_Abastecimentos:
    def __init__(self):
        self.abastecimentos = []
        self.valor_total_abastecimentos = 0
        
    def registrar_abastecimento(self, abastecimento):
        if isinstance(abastecimento, Abastecimento):
            self.abastecimentos.append(abastecimento)
            return f'Realizando abastecimento na bomba {abastecimento.bomba.identificador}: {abastecimento.qtd_litros} litros...\nTotal a pagar: R$ {abastecimento.valor:.2f}'
        else:
            raise TypeError('Abastecimento inválido. O abastecimento deve ser do tipo Abastecimento.')
        
    def resumo_abastecimentos(self):
        print('Resumo dos abastecimentos:')
        for a in self.abastecimentos:
            if isinstance(a.bomba.combustivel, Gasolina):
                print(f'- Bomba {a.bomba.identificador} ({a.bomba.combustivel}): {a.qtd_litros} litros -> R$ {a.valor:.2f}')
            elif isinstance(a.bomba.combustivel, Etanol):
                print(f'- Bomba {a.bomba.identificador} ({a.bomba.combustivel}): {a.qtd_litros} litros -> R$ {a.valor:.2f}')
                
    def adicionar_valor_abastecimento(self, abastecimento):
        self.valor_total_abastecimentos += abastecimento.combustivel.calcular_valor(abastecimento.qtd_litros)
             
    