# Um jogo de decisões onde eu terei que criar vários 
# finais diferentes baseados nas respostas que foram dadas

# Cenário do jogo: Uma guerra entre A e B. Somente o lado A irá vencer, 
# e o lado B irá perder! então eu tenho que tomar as decisões corretas para chegar aré a vitória, que somente o lado A irá conseguir
import PySimpleGUI as sg
from time import sleep

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no Norte ou no Sul? (n/s)' # Norte = A, Sul = B
        self.pergunta2 = 'Você prefere a espada ou escudo? (espada/escudo)' # Espada = A, Escudo B
        self.pergunta3 = 'Qual é a sua especialidade? (frente/tatico)' # Linha de frente = A, Tático = B
        self.final1 = 'Você irá lutar pelo povo'
        self.final2 = 'Você defenderá o povo'
        self.final3 = 'Você lutará diretamente com os inimigos'
        self.final4 = 'Você será um herói nas sombras'
       
    def Iniciar(self):
        #Layout
        layout = [
            [sg.Output(size=(30, 8),key='respostas')],
            [sg.Input(size=(12,0),key='resposta_do_user')],
            [sg.Button('Iniciar'), sg.Button('Responder')]
            ]       
        #Janela
        self.janela = sg.Window('Defina seu destino!', layout=layout)
        #Ler valores
        self.lerValores() #Nesse ponto o self.lerValores foi utilizado somente para o programa entender o evento 'Responder', e iniciar o IF
        #Usar valores
        while True:
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.lerValores() #Aqui ele é usado para ler os valores realmente inseridos após
                if self.values['resposta_do_user'][0].lower() == 'n':
                    print(self.pergunta2)
                    self.lerValores()
                    if self.values['resposta_do_user'].lower() == 'espada':
                        print(self.final1)
                    elif self.values['resposta_do_user'].lower() == 'escudo':
                        print(self.final2)
                elif self.values['resposta_do_user'][0].lower() == 's':
                    print(self.pergunta3) 
                    self.lerValores()
                    if self.values['resposta_do_user'].lower() == 'frente':
                        print(self.final3)
                    elif self.values['resposta_do_user'].lower() == 'tatico':
                        print(self.final4)
                else:
                    print('Insira um valor válido!')
    
    def lerValores(self):
        self.evento, self.values = self.janela.Read()

jogo = JogoDeAventura()
jogo.Iniciar()
