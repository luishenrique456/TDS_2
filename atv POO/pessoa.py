class Pessoa:
  seq=0
  def __init__(self,nome,idade,peso,altura,sexo,estado="vivo",est_civil="solteiro",mae=None):
    Pessoa.seq += 1
    self.__id = Pessoa.seq

    self.__nome = nome.title()
    self.__idade = idade
    self.__peso = peso
    self.__altura = altura
    self.__sexo = sexo
    self.__estado = estado
    self.__est_civil = est_civil
    self.__mae = None
    self.__pai = None
    self.__mae_adotiva = None
    self.__pai_adotivo = None
    self.__conjuge = None
    self.filhos = []



  @property
  def id(self):
    return self.__id


  @property
  def pai_adotivo(self):
    return self.__pai_adotivo

  @property
  def nome(self):
    return self.__nome

  @property
  def conjuge(self):
    return self.__conjuge

  @property
  def est_civil(self):
    return self.__est_civil
  

  

  @nome.setter
  def nome(self,valor):
    if self.__est_civil == "casado(a)":
      nome_antigo = self.__nome.split(" ")
      nome_conjuge = self.__conjuge.nome.split(" ")
      novo_nome = valor.split(" ")
      for i in novo_nome:
        if (i not in nome_antigo) and (i not in nome_conjuge):
           print("nome inválido!")
           return
      self.__nome = valor
      print ("Alteração efetuada com sucesso!")

  def casar(self,conjuge):



    if conjuge.__est_civil == 'casado(a)':
      print(f'\n{self.__conjuge.nome} não pode casar novamente')
      return



    #verificar se as instancias estão em posições diferentes de memória
    if type(conjuge)==Pessoa:
      if self.id != conjuge.id:

        if self.__est_civil != 'casado(a)' and conjuge.__est_civil != 'casado(a)':

          self.__conjuge = conjuge
          self.__est_civil = 'casado(a)'
          self.__conjuge.__est_civil = "casado(a)"
          self.__conjuge.__conjuge = self
          print(f'\n{self.__nome} e {self.__conjuge.nome} casamento com sucesso (:')
        else:
          print('\nPessoa não pode casar com ela mesma!')

  def morrer(self):
    # alterar o estado para "morto"
    # verificar se a pessoa que morreu era casada e alterar o conjuge reséctivo para "viuvo"


    if self.__estado != 'morto(a)':
      self.__estado = 'morto(a)'
      self.__conjuge.__est_civil = 'viuvo(a)'
      print(f'\n{self.__nome} Estado : {self.__estado}')
      return



  def divorciar(self,conjuge):
    # mudar o estado civil das pessoas para "divorciado"
    # se pessoa estive morto(a) não pode divorciado

    # Verifica se a pessoa está morto(a)
    if self.__estado == 'morto(a)':
      print(f'\n{self.__nome} faleceu\nNão é permidio {self.__est_civil}')
      return

    # mudar o estado civil da pessoa para "divorciado"
    if self.__est_civil != 'divorciado(a)':
      self.__est_civil = 'divorciado(a)'
      self.__conjuge = None
      if type(conjuge)==Pessoa:
        conjuge.__est_civil = 'divorciado'
        conjuge.__conjuge = None
        print(f'\n{self.__nome} realizado com sucesso {self.__est_civil}')
        return

    if self.__est_civil == 'divorciado(a)':
      print(f'{self.__nome} não pode divorciado(a) novamente')
      return

    

    

  def ter_filhos(self,filho):
    # pessoas envolvidas tem que ser de sexos opostos
    # Retornar uma nova pessoa
    # criar o vinculo

    if self.__estado == 'morto(a)':
      print(f'não pode ter filhos quando estar {self.__estado}')
      return

    if self.__sexo != self.__conjuge.__sexo :
      nome_fil = input('digite nome do filho : ').title()
      idade_fil = 0
      peso_fil = float(input('digite peso do filho : '))
      altura_fil = float(input('digite altura do filho : '))
      sexo_fil = input('digite sexo do filho : ')[0].upper()


      filho = Pessoa(nome_fil,idade_fil,peso_fil,altura_fil,sexo_fil)

      filho.__pai = self if self.__sexo == 'M' else self.__conjuge
      filho.__mae = self if self.__sexo == 'F' else self.__conjuge

      self.filhos.append(filho)
      self.__conjuge.filhos.append(filho)

      print(f'{self.__nome} e {self.__conjuge.nome} tiveram um(a) filho(a): {filho.nome}.')

      print('\nInformação do filho(a)\n')

      print(f'Nome do Filho : {nome_fil}\nIdade do filho : {idade_fil}\nPeso do filho : {peso_fil}kg\naltura {altura_fil}m\nsexo do filho : {sexo_fil}\nNome da mãe : {self.__nome}\nNome do pai : {self.__conjuge.nome}')

      return filho
    else:
      print('sexo igual não pode ter filhos')

  def adotar_filhos(self,criança): #condição: criança ser órfã.
    pass

  def __str__(self):
    r = '-'
    n = f'{r*10} Nome : {self.__nome} {r*10}'
    a = f'\nIdade : {self.__idade}\nPeso : {self.__peso}kg\nAltura : {self.__altura}m\nSexo : {self.__sexo}'
    b = f'\nEstado civil : {self.__est_civil}\nNome mãe : {self.__mae if self.__mae else None}\nNome do pai : {self.__pai if self.__pai else None} '
    c = f'\nEstado : {self.__estado }\nmãe adotiva : {self.__mae_adotiva if self.__mae_adotiva else None }\npai adotivo : {self.__pai_adotivo if self.__pai_adotivo else None} \nNome Cônjuge : {self.__conjuge.nome if self.__conjuge else None}'
    return n+a+b+c


####### execução ########
def main():
  maria = Pessoa('maria',30,65,1.7,'F')
  joao  = Pessoa('João',33,64,1.7,'M')
  ana = Pessoa('ana',29,60,1.6,'F')

  #cria 2 pessoas solteiros(as)

  
  print(maria)

  print(joao)

  #casamento entre Maria e João

  maria.casar(joao)

  # não pode casar mais de uma vezes

  maria.casar(joao)

  #mostra nova situação de Maria

  print(maria)

  # Maria morreu
  maria.morrer()

  #atualizado nova informação Maria estar morto(a) e João estar viuvo
  print(maria)
  print(joao)

  # não pode divorciar com morto(a)
  maria.divorciar(joao)
  print(maria)
  print(joao)



  # João casar com Ana

  joao.casar(ana)
  print(joao)
  print(ana)

  # João vai ter filhos com Ana

  ana.ter_filhos(joao)

  # Maria estar morto(a) não pode ter filhos
  maria.ter_filhos(joao) #tá funcionado (:


  # João vai divorciar com Ana

  # joao.divorciar(ana)  #tá funcionado (:   
  # print(joao)
  # print(ana)

  

  














if __name__ == '__main__':
  main()




