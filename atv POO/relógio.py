'''Exercitando o processo de abstração, modele uma classe Relógio_Digital_Simples com seus estados e 
comportamentos. Crie a respectiva classe em python e depois crie 2 objetos, imprima os valores de seus 

atributos e execute os métodos criados. Recomendação: criar estados que possam ter seus valores alterados 
por seus métodos. '''

from datetime import datetime

class Relogio_Digital_Simples:
    def __init__(self, hora=0, min=0):
        self.hora = hora
        self.min = min

    def mostra_hora(self):
        print(f'{self.hora}H : {self.min}min')

    def valida_hora(self, hora, min):
        try:
            # Tenta criar um objeto de tempo com a hora e minuto passados
            datetime.strptime(f'{hora}:{min}', '%H:%M')
            return True
        except ValueError:
            print("Hora ou minuto inválido. Insira valores corretos.")
            return False


def main():
    print('Primeiro Relogio')
    relogio1 = Relogio_Digital_Simples()

    # Loop até que uma hora válida seja inserida
    while True:
        hora = int(input('Digite hora: '))
        minuto = int(input('Digite minuto: '))
        if relogio1.valida_hora(hora, minuto):
            relogio1.hora = hora
            relogio1.min = minuto
            break

    relogio1.mostra_hora()

    print('Segundo Relogio')
    relogio2 = Relogio_Digital_Simples()

    # Loop até que uma hora válida seja inserida
    while True:
        hora = int(input('Digite hora: '))
        minuto = int(input('Digite minuto: '))
        if relogio2.valida_hora(hora, minuto):
            relogio2.hora = hora
            relogio2.min = minuto
            break

    relogio2.mostra_hora()


if __name__ == '__main__':
    main()
