import random
import PySimpleGUI as sg

class ChuteONumero:

    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_maximo = 100
        self.valor_minimo = 1
        self.tentar_novamente = True
    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu Chute',size=(20,0))], 
            [sg.Input(size=(18,0),key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(30,5))],
        ]
        # Criar uma janela
        self.janela = sg.Window('Chute o número!',layout= layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # Receber valores
                self.LerValoresDaTela()
                # Fazer algo com os valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto')
                            break
                        elif int(self.valor_do_chute) == self.valor_aleatorio:
                            print('PARABÉNS, VOCÊ ACERTOU!!')
                            break
        except:
            print("Favor inserir apenas números!")
            self.Iniciar()

    def LerValoresDaTela(self):
        self.evento, self.valores = self.janela.Read()
    
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()