#Faça uma pergunta e o programa te dará a resposta
import random

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você decide',
            'Não faz isso não!',
            'Acho que tá na hora certa!'
        ]
        
    def Iniciar(self):
        input('Faça sua pegunta: ')
        print(random.choice(self.respostas))

decida = DecidaPorMim()
decida.Iniciar()