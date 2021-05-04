#Faça uma pergunta e o programa te dará a resposta
import random
import PySimpleGUI as sg

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você decide',
            'Não faz isso não!',
            'Acho que tá na hora certa!'
        ]
        
    def Iniciar(self):
        #layout
        layout = [
            [sg.Text('Faça sua pergunta: ')],
            [sg.Input()],
            [sg.Button('Decida por mim!')],
            [sg.Output(size=(50,2))],

        ]
        #janela
        self.janela = sg.Window('Decida por mim!', layout=layout)
        while True:
            #ler os valores
            self.eventos, self.valores = self.janela.Read()
            #usar os valores
            if self.eventos == 'Decida por mim!':
                print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()