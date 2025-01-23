estações = {89.5: 'Cocais', 91.5: 'Mix', 94.1: 'Boa', 99.1: 'Clube'}

class RadioFM:
    def __init__(self, vol_max, estações):
        self.volume_min = 0
        self.volume_max = vol_max
        self.freq_min = 88
        self.freq_max = 108
        self.estações = estações
        self.volume = None
        self.ligado = False
        self.estação_atual = None
        self.frequencia_atual = None
        self.antena_habilitada = False

    def ligar(self):
        self.ligar = True

    def desligar(self):
        pass

    def aumentar_volume(self):
        pass

    def diminuir_volume(self):
        pass

    def mudar_frequencia(self):
        pass
