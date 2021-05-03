# Simulador de Dado
# Simulae o uso de um dado, gerando um valor de 1 até 6
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
    
    def Iniciar(self):
        resposta = input(self.mensagem).lower()
        try:
            if resposta[0] == 's':
                self.GerarValorDoDado()
            elif resposta[0] == 'n':
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