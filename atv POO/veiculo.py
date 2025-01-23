class veiculo:

  def __init__(self,chassi,marca,modelo,ano,placa='Não especificada',cor='Não especificada',proprietario='Não especificado',quilometragem=0):
    self.chassi = chassi
    self.placa = placa
    self.marca = marca
    self.modelo = modelo
    self.ano = ano
    self.cor = cor
    self.proprietario = proprietario
    self.quilometragem = quilometragem
  def atualizar_quilometragem(self):

    self.quilometragem += self.quilometragem
    return self.quilometragem
  def __str__(self):

     return f'|placa : {self.placa}| marca :{self.marca} | modelo : {self.modelo} | ano : {self.ano} | cor : {self.cor} | proprietario : {self.proprietario} | quilometragem : {self.quilometragem} km/h |'

def main():
    chassi = input('digite chassi do carro : ')
    placa = input('digite placa do carro : ')
    if placa == '':
        placa='Não especificada'

    marca = input('digite marca do carro : ')

    modelo = input('digite modelo do carro : ')
    try:
        ano = int(input('digite ano de fabricação  :'))
    except:
        raise ValueError('ano invalido! ):')

    # except ValueError:
    #     print('Ano invalido! ')



    cor = input('digite cor do carro : ')
    if cor == '':
        cor = 'Não especificada'

    proprietario = input('digite proprietário do carro : ')
    if proprietario == '':
        proprietario='Não especificado'

    quilometragem = input ('digite quilometragem do carro : ')
    if quilometragem == '':
      quilometragem = 0
      print(f'quilometragem padrão : {quilometragem} km/h')
    else:
      try:
        quilometragem = int(quilometragem)
      except ValueError:
        print("Por favor, digite um número válido.")


    carro = veiculo(chassi,marca,modelo,ano,placa,cor,proprietario,quilometragem)

    print(f'Sua quilometragem atualizada : {carro.atualizar_quilometragem()} km/h')

    print(carro)

if __name__ == '__main__':
    main()