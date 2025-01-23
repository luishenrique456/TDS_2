from datetime import datetime

class CarteiraHabilitacao:
    def __init__(self, nome, data_nascimento, data_emissao, data_validade, observacao='não especificado'):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.data_emissao = data_emissao
        self.data_validade = data_validade
        self.observacao = observacao

    def validar_data_validade(self):
        hoje = datetime.now().date()
        data_validade_formatada = datetime.strptime(self.data_validade,'%d/%m/%Y').date()
        if data_validade_formatada > hoje:
            return "A data de validade é válida."
        else:
            return "A data de validade expirou."
    def __str__(self):
        return f'nome: {self.nome}|dta nascimento : {self.data_nascimento}|data emissão {self.data_emissao}|data validade : {self.data_validade}|observação : {self.observacao}|'


def main():
    nome = input("Digite o nome: ")
    data_nascimento = input("Digite a data de nascimento (DD/MM/AAA): ")
    data_emissao = input("Digite a data de emissão (DD/MM/AAA): ")
    data_validade = input("Digite a data de validade (DD/MM/AAA): ")
    observacao = input("Digite a observação (ou deixe em branco): ")
    if observacao == '':
        observacao = 'não especificado'

    cnh = CarteiraHabilitacao(nome, data_nascimento, data_emissao, data_validade, observacao)
    
    print(cnh)

    print(cnh.validar_data_validade())
   
    


if __name__ == '__main__':
    main()