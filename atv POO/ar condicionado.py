# modo ['automático','frio','ventilar']
# mudar_modo(modo): no modo automático,não é permitido alterar a velocidade
# temperatura ; temperatura_escolhida dentro dos limites 15 a 27
# velocidade ; velocidade escolhida dentro dos limites 16 a 20

class ArCondicionado:
    def __init__(self,temp_min=15,temp_max=27,vel_min=16,vel_max=20,modo='automático',ligado=False):
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.vel_min = vel_min
        self.vel_max = vel_max
        self.modo = modo
        self.ligado = ligado
        # self.temperatura_atual = temp_min

    

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            return'ar-condicionado esta ligado'
        else:
            return'ar-condicionado já estar ligado'
            

        
    def desligar(self):
        if  self.ligado:
            self.ligado = False
            return'ar-condicionado esta desligado'

        else:
            return'ar-condicionado já estar desligado'
        
    def validar_temperatura(self,temperatura_escolhida):
        return self.temp_min <= temperatura_escolhida <= self.temp_max
    

    def validar_velocidade(self,velocidade_escolhida):
        return self.vel_min <= velocidade_escolhida <= self.vel_max
    
    # método para consulta temperatura está no limites
    # def consulta_temperatura(self,nova_temperatura):
    #     if self.validar_temperatura(nova_temperatura):
    #         self.temperatura_atual = nova_temperatura
    #         print('temperatura validar')
    #
    #     else:
    #         print(f'temperatura invalida! entre limites {self.temp_min} a {self.temp_max}')

        
        
        


    def aumentar_temperatura(self,temp):
        temp = input('Em quantos graus deseja aumentar a temperatura?')
        if self.validar_temperatura(temp):
            pass

    def diminuir_temperatura(self):
        pass

    def aumentar_velocidade(self):
        pass
    def diminuir_velocidade(self):
        pass
    def mudar_modo(self):
        pass

    def __str__(self):
        pass


def main():
    p1 = ArCondicionado()

    # p1.consulta_temperatura(14) teste para consulta temperatura


    

    











if __name__ == '__main__':
    main()