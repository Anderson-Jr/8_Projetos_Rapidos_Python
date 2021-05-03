# Simulador de Dado
# Simulae o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
        # Layout 
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]
    def Iniciar(self):
        # Criar uma janela
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)
        # ler os valores da tela 
        self.eventos, self.valores = self.janela.Read()
        #fazer alguma coisa com esses valores
        try:
            if self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'n':
                print('Agradecemos a sua participação')
            else:
                print('*'*25)
                print('Favor digitar sim ou não:')
                simulador.Iniciar()
        except:
            print('Ocorreu um erro ao receber sua resposta, favor insira uma resposta entre: \n "s" para "sim" ou "n" para "não"')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()