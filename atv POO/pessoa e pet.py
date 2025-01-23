# Definir um código principal com a criação de pelo menos 3 objetos (Pessoas).

class Pet:
  def __init__(self,tipo,nome,idade,peso,raca,cor,castrado=False):
    self.__tipo = tipo
    self.__nome = nome
    self.__idade = idade
    self.__peso = peso
    self.__raca = raca
    self.__cor = cor
    self.__castrado = castrado



  

  @property
  def nome(self):
    return self.__nome
  
  @property
  def tipo(self):
    return self.__tipo
  
  @property
  def idade(self):
    return self.__idade
  
  @property
  def peso(self):
    return self.__peso
  
  @property
  def raca(self):
    return self.__raca
  
  @property
  def cor(self):
    return self.__cor
  
  @property
  def castrado(self): 
    return self.__castrado

  @castrado.setter
  def castrado(self,castrado):
    self.__castrado = castrado



    
  
  
  


class Pessoa:
  def __init__(self,cpf,nome,endereço):
    self.__cpf = cpf
    self.__nome = nome.title()
    self.__endereço = endereço
    self.__meus_pets = []

  @property
  def cpf(self):
    return self.__cpf

  @property
  def nome(self):
    return self.__nome
  
  @property
  def meu_pets(self):
    return self.__meus_pets


  def castrar(self,pet):
    if type(pet)==Pet:
      opcao = int(input('Digite 1 para castrar ou 2 para não castrar : '))
      if opcao == 1:
        pet.castrado = True
        print(f'Seu pet {pet.nome} foi castrado {pet.castrado}')
      elif opcao == 2:
        pet.castrado
        print(f'Seu pet {pet.nome} não foi castrado {pet.castrado}')
      else:
        print('opção invalidar')
    return

  def cadastrar_pet(self,pet):



    if type(pet)== Pet:
      self.__meus_pets.append(pet)
      print(f'{self.__nome} adotou um pet {pet.nome}')
      return
    else:
      print('não é um pet!')

    return





  def excluir_pet(self,nome):
    for pet in self.__meus_pets:
      if pet.nome == nome:
        self.__meus_pets.remove(pet)
        print(f'seu pet {pet.nome} morreu ):')

    return


  
  def mostrar_meus_pets(self):
    for pet in self.__meus_pets:
      print(f'Nome dono(a) : {self.__nome}\nNome do pet : {pet.nome.title()}\nTipo do pet : {pet.tipo}\nIdade do pet : {pet.idade} anos\nPeso do pet : {pet.peso}kg\nRaça do pet : {pet.raca}\nCor do pet : {pet.cor}\ncastrado : {pet.castrado}')
      return



  
  
def main():

  #criação de 3 obj pessoas
  luis = Pessoa('123.456.789-10','luis','rua 100')

  joao = Pessoa('321.654.987-01','joao','rua 20')

  maria = Pessoa('987.654.321-12','maria','rua 001')


  #criação de 3 obj pets
  pet1 = Pet('gato','mini',12,2.0,'siamê','preto')

  pet2 = Pet('cachorro', 'rex', 3, 15.0, 'labrador', 'amarelo')

  pet3 = Pet('coelho', 'snow', 2, 1.5, 'anão', 'branco')


  # método para cadastrar pet
  luis.cadastrar_pet(pet1)

  joao.cadastrar_pet(pet2)

  maria.cadastrar_pet(pet3)


  #método para castrar pet
  luis.castrar(pet1)


  #método para mostra informação
  luis.mostrar_meus_pets()

  joao.mostrar_meus_pets()

  maria.mostrar_meus_pets()



  # Simular a perda de um deles e a consequente atualização (remoção) da lista de pets
  luis.excluir_pet(pet1.nome)




  

  
if __name__ == '__main__':
  main()
