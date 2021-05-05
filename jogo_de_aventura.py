# Um jogo de decisões onde eu terei que criar vários 
# finais diferentes baseados nas respostas que foram dadas

# Cenário do jogo: Uma guerra entre A e B. Somente o lado A irá vencer, 
# e o lado B irá perder! então eu tenho que tomar as decisões corretas para chegar aré a vitória, que somente o lado A irá conseguir

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
        resposta1 = input(self.pergunta1)
        if resposta1 == 'n':
            resposta1b =  input(self.pergunta2)
            if resposta1b == 'espada':
                print(self.final1)
            if resposta1b == 'escudo':
                print(self.final2)
        if resposta1 == 's':
            resposta1b = input(self.pergunta3)
            if resposta1b == 'frente':
                print(self.final3)
            if resposta1b == 'tatico':
                print(self.final4)

jogo = JogoDeAventura()
jogo.Iniciar()