# Criar o menu principal
import turtle
import time
import random
import math
import winsound

# Registrar imagens
imagens = ['Elven_Elf_Left.gif', 'Elven_Elf_Right.gif', 'Elven_Block.gif', 'Elven_Coin.gif',
           'Elven_Center.gif', 'Elven_Player_Down.gif', 'Elven_Player_Up.gif',
           'Elven_Player_Left.gif', 'Elven_Player_Right.gif', 'Elven_Info.gif',
           'Elven_Exit.gif', 'Elven_Tree.gif', 'Elven_Orc_Down.gif', 'Elven_Orc_Up.gif',
           'Elven_Orc_Left.gif', 'Elven_Orc_Right.gif', 'Elven_Staff.gif','Elven_OrbFlash.gif',
           'Elven_Bat_Up.gif', 'Elven_Bat_Down.gif', 'Elven_Knight_Down.gif', 'Elven_CastleBrick.gif',
           'Elven_CastleWoodDoor.gif']
for i in imagens:
    turtle.register_shape(i)


def main_menu():
    # Tela do Menu
    turtle.register_shape('Elven_Main_Menu.gif')
    menu = turtle.Screen()
    menu.setup(width=750, height=750)
    menu.bgcolor('black')
    menu.bgpic('Elven_Main_Menu.gif')
    menu.title('Elven Garden')

    #Música tema do menu principal
    theme = winsound.PlaySound('Elven_Main_Menu_Theme', winsound.SND_LOOP | winsound.SND_ASYNC | winsound.SND_FILENAME)

    # Caneta do menu
    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.speed(0)
            self.penup()
            self.pensize(5)
            self.hideturtle()

    # Instãncias
    pen = Pen()

    # Botão de play do menu
    pen.color('green', 'lightgreen')
    pen.goto(-150, -40)
    pen.begin_fill()
    pen.pendown()
    for v in range(2):
        pen.forward(280)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(-10, -95)
    pen.write('Jogar', align='center', font=('Courier', 24, 'bold'))

    # Botão de Configurações do jogo
    pen.color('green', 'lightgreen')
    pen.goto(-150, -145)
    pen.begin_fill()
    pen.pendown()
    for v in range(2):
        pen.forward(280)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(-10, -195)
    pen.write('Configurações', align='center', font=('Courier', 24, 'bold'))

    # Função dos botões
    def botão_clickado(x, y):
        if x >= -150 and x <= 130 and y <= -40 and y >= -120:
            time.sleep(0.5)
            turtle.clearscreen()
            level_menu()

        if x >= -150 and x <= 130 and y <= -145 and y >= -225:
            print('Bora configurar esse jogo aê!')

    # Keyboard bindings do menu principal
    turtle.listen()
    turtle.onscreenclick(botão_clickado, 1)

    # Looping infinito da função
    turtle.mainloop()


def level_menu():
    # Level Menu
    level_menu = turtle.Screen()
    level_menu.setup(width=750, height=750)
    level_menu.bgcolor('black')
    level_menu.bgpic('Elven_Level_Menu.gif')
    level_menu.title('Level Menu')

    # Caneta do Level Menu
    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.speed(0)
            self.pensize(5)
            self.penup()
            self.hideturtle()

    # Instâncias
    pen = Pen()

    # Botão da Fase 1
    pen.goto(-300, 220)
    pen.color('green', 'lightgreen')
    pen.begin_fill()
    pen.pendown()
    for v in range(2):
        pen.forward(250)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(-175, 165)
    pen.write('Fase 1', align='center', font=('Courier', 24, 'bold'))

    # Botão da Fase 2
    pen.goto(50, 220)
    pen.color('green', 'lightgreen')
    pen.begin_fill()
    pen.pendown()
    for v in range(2):
        pen.forward(250)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(175, 165)
    pen.write('Fase 2', align='center', font=('Courier', 24, 'bold'))

    # Botão da Fase 3
    pen.goto(-300, 80)
    pen.color('green', 'lightgreen')
    pen.begin_fill()
    pen.pendown()
    for v in range(2):
        pen.forward(250)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(-175, 25)
    pen.write('Fase 3', align='center', font=('Courier', 24, 'bold'))

    # Botão da Fase 4
    pen.goto(50, 80)
    pen.color('green', 'lightgreen')
    pen.begin_fill()
    pen.pendown()
    for v in range(2):
        pen.forward(250)
        pen.right(90)
        pen.forward(80)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(175, 25)
    pen.write('Fase 4', align='center', font=('Courier', 24, 'bold'))

    # Botão voltar pro menu principal
    pen.goto(-370, 370)
    pen.color('green', 'lightgreen')
    pen.begin_fill()
    pen.pendown()
    for v in range(2):
        pen.forward(115)
        pen.right(90)
        pen.forward(40)
        pen.right(90)
    pen.end_fill()
    pen.penup()
    pen.goto(-310, 335)
    pen.write('Voltar', align='center', font=('Courier', 18, 'bold'))

    # Função dos botões
    def botão_clickado(x, y):
        if x >= -300 and x <= -50 and y <= 220 and y >= 140:
            winsound.PlaySound('Elven_Coin_Sound', winsound.SND_ASYNC | winsound.SND_FILENAME)
            time.sleep(0.5)
            turtle.clearscreen()
            level_1()

        if x >= 50 and x <= 300 and y <= 220 and y >= 140:
            winsound.PlaySound('Elven_Coin_Sound', winsound.SND_ASYNC | winsound.SND_FILENAME)
            time.sleep(0.5)
            turtle.clearscreen()
            level_2()

        if x >= -300 and x <= -50 and y <=  80 and y >= 0:
            winsound.PlaySound('Elven_Coin_Sound', winsound.SND_ASYNC | winsound.SND_FILENAME)
            time.sleep(0.5)
            turtle.clearscreen()
            level_3()

        if x >= 50 and x <= 300 and y <=  80 and y >= 0:
            print('Calma man, acabei de fazer a fase 3, espera aê!')

    # Keyboard Bindings do Level Menu
    level_menu.listen()
    level_menu.onscreenclick(botão_clickado, 1)


def level_1():
    # Configurações da Tela
    tela = turtle.Screen()
    tela.setup(width=750, height=750)
    tela.bgcolor('black')
    tela.title('Level 1')

    # Objetivo fase 1
    objetivo = 'O objetivo desta fase é pegar as 4 moedas do mapa e ir ao Centro Élfico!'

    # Botão info
    botinfo = turtle.Turtle()
    botinfo.speed(0)
    botinfo.shape('Elven_Info.gif')
    botinfo.color('blue')
    botinfo.penup()
    botinfo.goto(288, 320)

    def info(x, y):
        print(objetivo)

    # Botão exit
    botexit = turtle.Turtle()
    botexit.speed(0)
    botexit.shape('Elven_Exit.gif')
    botexit.color('blue')
    botexit.penup()
    botexit.goto(-288, 320)

    def exit(x, y):
        time.sleep(0.5)
        turtle.clearscreen()
        main_menu()

    # Score de vidas
    qnt_vida = 3
    score_vidas = turtle.Turtle()
    score_vidas.speed(0)
    score_vidas.shape('square')
    score_vidas.color('red')
    score_vidas.penup()
    score_vidas.hideturtle()
    score_vidas.goto(190, 300)
    score_vidas.write(f'Vidas: {qnt_vida}', align='center', font=('Courier', 24, 'normal'))

    # Score de moedas
    qnt_moeda = 4
    score_moedas = turtle.Turtle()
    score_moedas.speed(0)
    score_moedas.shape('square')
    score_moedas.color('yellow')
    score_moedas.penup()
    score_moedas.hideturtle()
    score_moedas.goto(-80, 300)
    score_moedas.write(f'Moedas Obtidas: 0/{qnt_moeda}', align='center', font=('Courier', 24, 'normal'))

    # Caneta
    class Caneta(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape('square')
            self.color('white')
            self.penup()
            self.speed(0)
            self.hideturtle()

    # Lista de inimigos
    inimigos = []

    class Inimigo(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.color('red')
            self.shape('Elven_Elf_Right.gif')
            self.speed(0)
            self.penup()
            self.goto(x, y)
            self.direction = random.choice(['up', 'down', 'right', 'left'])

        # Movimentação do Inimigo
        def move(self):
            if self.direction == 'up':
                dx = 0
                dy = 24

            elif self.direction == 'down':
                dx = 0
                dy = -24

            elif self.direction == 'right':
                dx = 24
                dy = 0
                self.shape('Elven_Elf_Right.gif')

            elif self.direction == 'left':
                dx = -24
                dy = 0
                self.shape('Elven_Elf_Left.gif')

            else:
                dx = 0
                dy = 0

            # Calcular o spot para se mover
            move_to_x = self.xcor() + dx
            move_to_y = self.ycor() + dy

            # Verificar se não tem uma parede no spot
            if (move_to_x, move_to_y) not in paredes:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(['up', 'down', 'right', 'left'])

            # Setar o timer para o próximo movimento
            turtle.ontimer(self.move, t=random.randint(100, 300))

    # Tesouro
    class Tesouro(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape('Elven_Coin.gif')
            self.color('gold')
            self.speed(0)
            self.gold = 100
            self.penup()
            self.goto(x, y)

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    # Lista de fases
    fases = ['']

    # Fase
    fase_1 = [
        'XXXXXXXXXXXXXXXXXXXXXXXXX',
        'XT   XX     X     XX   TX',
        'XXX     XXX   XXX     XXX',
        'XXXX    XXX   XXX    XXXX',
        'XXXX    XXX P XXX    XXXX',
        'XXXX    XXX   XXX    XXXX',
        'XXXX XX XXX X XXX XX XXXX',
        'XXXX XX XXX X XXX XX XXXX',
        'XXXX    XXX   XXX    XXXX',
        'XXXX    XXX   XXX    XXXX',
        'XXXX    XXX   XXX    XXXX',
        'XXX     XXX   XXX     XXX',
        'XI   XX     C     XX   IX',
        'XXX     XXX   XXX     XXX',
        'XXXX    XXX   XXX    XXXX',
        'XXXX    XXX   XXX    XXXX',
        'XXXX    XXX   XXX    XXXX',
        'XXXX XX XXX X XXX XX XXXX',
        'XXXX XX XXX X XXX XX XXXX',
        'XXXX    XXX   XXX    XXXX',
        'XXXX    XXX   XXX    XXXX',
        'XXXX    XXX   XXX    XXXX',
        'XXX     XXX   XXX     XXX',
        'XT   XX   I X I   XX   TX',
        'XXXXXXXXXXXXXXXXXXXXXXXXX'
    ]

    # Adicionar uma lista de tesouros
    tesouros = []

    # Adicionar uma lista de inimigos
    inimigos = []

    # Adicionar a fase na lista de fases
    fases.append(fase_1)

    # Jogador
    class Jogador(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.color('blue')
            self.shape('Elven_Player_Down.gif')
            self.speed(0)
            self.penup()
            self.gold = 0
            self.moedas = 0
            self.vidas = qnt_vida
            self.direction = 'stop'

        # Movimentação do Jogador
        def go_up(self):
            mover_para_x = jogador.xcor()
            mover_para_y = jogador.ycor() + 24
            self.shape('Elven_Player_Up.gif')
            self.direction = 'Up'

            # Checar se não tem uma parede no spot
            if (mover_para_x, mover_para_y) not in paredes:
                jogador.goto(mover_para_x, mover_para_y)

        def go_down(self):
            mover_para_x = jogador.xcor()
            mover_para_y = jogador.ycor() - 24
            self.shape('Elven_Player_Down.gif')
            self.direction = 'Down'

            # Checar se não tem uma parede no spot
            if (mover_para_x, mover_para_y) not in paredes:
                jogador.goto(mover_para_x, mover_para_y)

        def go_right(self):
            mover_para_x = jogador.xcor() + 24
            mover_para_y = jogador.ycor()
            self.shape('Elven_Player_Right.gif')
            self.direction = 'Right'

            # Checar se não tem uma parede no spot
            if (mover_para_x, mover_para_y) not in paredes:
                jogador.goto(mover_para_x, mover_para_y)

        def go_left(self):
            mover_para_x = jogador.xcor() - 24
            mover_para_y = jogador.ycor()
            self.shape('Elven_Player_Left.gif')
            self.direction = 'Left'

            # Checar se não tem uma parede no spot
            if (mover_para_x, mover_para_y) not in paredes:
                jogador.goto(mover_para_x, mover_para_y)

        def flash(self):
            if self.direction == 'Right':
                move_to_x = self.xcor() + 48
                move_to_y = self.ycor()
            elif self.direction == 'Left':
                move_to_x = self.xcor() - 48
                move_to_y = self.ycor()
            elif self.direction == 'Up':
                move_to_x = self.xcor()
                move_to_y = self.ycor() + 48

            elif self.direction == 'Down':
                move_to_x = self.xcor()
                move_to_y = self.ycor() - 48
            else:
                move_to_x = self.xcor()
                move_to_y = self.ycor()

            if move_to_x <= 288 and move_to_x >= -288 and move_to_y <= 288 and move_to_y >= -288:
                if (move_to_x, move_to_y) not in paredes:
                    self.goto(move_to_x, move_to_y)
            else:
                print('O jogador não pode ir para essa área')

        def passar_fase(self):
            x = self.xcor()
            y = self.ycor()
            if (x, y) == (0, 0) and jogador.moedas == qnt_moeda:
                print('Você passou de fase!')
                time.sleep(0.5)
                turtle.clearscreen()
                main_menu()
            elif (x, y) == (0, 0) and jogador.moedas != qnt_moeda:
                print('Você não tem moedas o suficientes para passar de fase!')
            elif (x, y) != (0, 0) and jogador.moedas == qnt_moeda:
                print('Você precisa estar no Centro Élfico para completar a fase!')
            else:
                print('Cumpra o seu objetivo e vá para o Centro Élfico para completar a fase!')

        def colisão(self, outro):
            a = self.xcor() - outro.xcor()
            b = self.ycor() - outro.ycor()
            distância = math.sqrt((a ** 2) + (b ** 2))

            if distância < 5:
                return True
            else:
                return False

    # Criar uma função das fases
    def setup_fase(fase):
        for y in range(len(fase)):
            for x in range(len(fase[y])):
                # Colocar as entidades em cada coordenada x, y
                entidade = fase[y][x]
                tela_x = -288 + (x * 24)
                tela_y = 288 - (y * 24)

                # Checar se é um X (representando uma parede)
                if entidade == 'X':
                    caneta.shape('Elven_Block.gif')
                    caneta.goto(tela_x, tela_y)
                    caneta.stamp()
                    # Adicionar coordenadas para a lista de paredes
                    paredes.append((tela_x, tela_y))
                # Checar se é um P (representando o player)
                if entidade == 'P':
                    jogador.goto(tela_x, tela_y)

                # Chegar se é um T (representando o tesouro)
                if entidade == 'T':
                    tesouros.append(Tesouro(tela_x, tela_y))

                # Checar se é um I (representando o inimigo)
                if entidade == 'I':
                    inimigos.append(Inimigo(tela_x, tela_y))

                # Checar se é um C (representando o centro)
                if entidade == 'C':
                    caneta.shape('Elven_Center.gif')
                    caneta.goto(tela_x, tela_y)
                    caneta.stamp()

    # Criar uma instância de classe
    caneta = Caneta()
    jogador = Jogador()

    # Lista de coordenadas das paredes
    paredes = []

    # Ligar a fase
    setup_fase(fases[1])

    # Desliga os updates da tela
    tela.tracer(0)

    # Precionar teclas
    tela.listen()
    tela.onkeypress(jogador.go_up, 'Up')
    tela.onkeypress(jogador.go_down, 'Down')
    tela.onkeypress(jogador.go_right, 'Right')
    tela.onkeypress(jogador.go_left, 'Left')
    tela.onkeypress(jogador.flash, 'x')
    tela.onkeypress(jogador.passar_fase, 'b')
    botinfo.onclick(info)
    botexit.onclick(exit)

    # Começar a mover os inimigos
    for inimigo in inimigos:
        turtle.ontimer(inimigo.move, t=250)

    # Looping infinito do game
    while True:
        # Checar a colisão do jogador com os inimigos
        for inimigo in inimigos:
            if jogador.colisão(inimigo):
                jogador.vidas -= 1
                jogador.goto(0, 0)
                score_vidas.clear()
                score_vidas.write(f'Vidas: {jogador.vidas}', align='center', font=('Courier', 24, 'normal'))
                if jogador.vidas == 0:
                    print(f'Jogador morre!')
                    turtle.clearscreen()
                    main_menu()

        # Checar a colisão do jogador com o tesouro
        for tesouro in tesouros:
            if jogador.colisão(tesouro):
                jogador.gold += tesouro.gold
                jogador.moedas += 1
                print(f'Ouro do Jogador {jogador.gold}')
                score_moedas.clear()
                score_moedas.write(f'Moedas Obtidas: {jogador.moedas}/{qnt_moeda}', align='center',
                                   font=('Courier', 24, 'normal'))
                if jogador.moedas == 1:
                    winsound.PlaySound('Elven_Coin_Sound', winsound.SND_ASYNC | winsound.SND_FILENAME)
                elif jogador.moedas > 1:
                    winsound.PlaySound('Elven_Coin_Sound4', winsound.SND_ASYNC | winsound.SND_FILENAME)

                # Destruir o tesouro
                tesouro.destroy()
                # Remover o tesouro da lista de tesouros
                tesouros.remove(tesouro)

        # Atualizar a tela
        tela.update()


def level_2():
    # Configurações da Tela
    tela = turtle.Screen()
    tela.setup(width=750, height=750)
    tela.bgcolor('black')
    tela.title('Level 2')

    # Objetivo fase 1
    objetivo = 'O objetivo desta fase é pegar a sua primeira arma!'

    # Botão info
    botinfo = turtle.Turtle()
    botinfo.speed(0)
    botinfo.shape('Elven_Info.gif')
    botinfo.color('blue')
    botinfo.penup()
    botinfo.goto(288, 320)

    def info(x, y):
        print(objetivo)

    # Botão exit
    botexit = turtle.Turtle()
    botexit.speed(0)
    botexit.shape('Elven_Exit.gif')
    botexit.color('blue')
    botexit.penup()
    botexit.goto(-288, 320)

    def exit(x, y):
        time.sleep(0.5)
        turtle.clearscreen()
        main_menu()

    # Score de vidas
    qnt_vida = 3
    score_vidas = turtle.Turtle()
    score_vidas.speed(0)
    score_vidas.shape('square')
    score_vidas.color('red')
    score_vidas.penup()
    score_vidas.hideturtle()
    score_vidas.goto(190, 300)
    score_vidas.write(f'Vidas: {qnt_vida}', align='center', font=('Courier', 24, 'bold'))

    # Score do Objetivo
    qnt_moeda = 4
    score_objetivo = turtle.Turtle()
    score_objetivo.speed(0)
    score_objetivo.shape('square')
    score_objetivo.color('yellow')
    score_objetivo.penup()
    score_objetivo.hideturtle()
    score_objetivo.goto(-80, 300)
    score_objetivo.write(f'Arma: 0/1', align='center', font=('Courier', 24, 'bold'))

    # Caneta
    class Caneta(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape('square')
            self.color('white')
            self.penup()
            self.speed(0)
            self.hideturtle()

    # Lista de inimigos
    inimigos = []
    inimigos2 = []

    class Inimigo(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.color('red')
            self.shape('Elven_Elf_Right.gif')
            self.speed(0)
            self.penup()
            self.goto(x, y)
            self.direction = random.choice(['up', 'down', 'right', 'left'])

        # Movimentação do Inimigo
        def move(self):
            if self.direction == 'up':
                dx = 0
                dy = 24

            elif self.direction == 'down':
                dx = 0
                dy = -24

            elif self.direction == 'right':
                dx = 24
                dy = 0
                self.shape('Elven_Elf_Right.gif')

            elif self.direction == 'left':
                dx = -24
                dy = 0
                self.shape('Elven_Elf_Left.gif')

            else:
                dx = 0
                dy = 0

            # Calcular o spot para se mover
            move_to_x = self.xcor() + dx
            move_to_y = self.ycor() + dy

            # Verificar se não tem uma parede no spot
            if (move_to_x, move_to_y) not in paredes:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(['up', 'down', 'right', 'left'])

            # Setar o timer para o próximo movimento
            turtle.ontimer(self.move, t=random.randint(100, 300))

    class Inimigo2(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.color('red')
            self.shape('Elven_Orc_Down.gif')
            self.speed(0)
            self.penup()
            self.goto(x, y)
            self.direction = random.choice(['up', 'down', 'right', 'left'])

        # Movimentação do Inimigo
        def move(self):
            if self.direction == 'up':
                dx = 0
                dy = 24
                self.shape('Elven_Orc_Up.gif')

            elif self.direction == 'down':
                dx = 0
                dy = -24
                self.shape('Elven_Orc_Down.gif')

            elif self.direction == 'right':
                dx = 24
                dy = 0
                self.shape('Elven_Orc_Right.gif')

            elif self.direction == 'left':
                dx = -24
                dy = 0
                self.shape('Elven_Orc_Left.gif')

            else:
                dx = 0
                dy = 0

            # Checar se o jogador está próximo
            # Se está, vá em tal direção
            if self.tá_perto(jogador):
                if jogador.xcor() < self.xcor():
                    self.direction = 'left'
                if jogador.xcor() > self.xcor():
                    self.direction = 'right'
                if jogador.ycor() < self.ycor():
                    self.direction = 'down'
                if jogador.ycor() > self.ycor():
                    self.direction = 'up'

            # Calcular o spot para se mover
            move_to_x = self.xcor() + dx
            move_to_y = self.ycor() + dy

            # Verificar se não tem uma parede no spot
            if (move_to_x, move_to_y) not in paredes:
                self.goto(move_to_x, move_to_y)
            else:
                self.direction = random.choice(['up', 'down', 'right', 'left'])

            # Setar o timer para o próximo movimento
            turtle.ontimer(self.move, t=random.randint(100, 300))

        def tá_perto(self, other):
            a = self.xcor() - other.xcor()
            b = self.ycor() - other.ycor()
            distance = math.sqrt((a ** 2) + (b ** 2))

            if distance < 75:
                return True
            else:
                return False

    # Tesouro
    class Tesouro(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape('Elven_Coin.gif')
            self.color('gold')
            self.speed(0)
            self.gold = 100
            self.penup()
            self.goto(x, y)

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    # Arma
    class Arma(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape('Elven_Staff.gif')
            self.color('brown')
            self.speed(0)
            self.gold = 100
            self.penup()
            self.goto(x, y)

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    # Lista de fases
    fases = ['']

    # Fase
    fase_2 = [
        'AAAAAAAAAAAAAAAAAAAAAAAAA',
        'Ai  A     X   X     A  iA',
        'A T A     X C X     A T A',
        'A   A     X   X     A   A',
        'AAAAA      X X      AAAAA',
        'A                       A',
        'AX XXXXXXXXXXXXXXXXXXX XA',
        'A          XXX          A',
        'AXXXXXXXX  XXX  XXXXXXXXA',
        'AI        AXXXA        IA',
        'AA XXXXXXX     XXXXXXX AA',
        'A                       A',
        'XXXXXXXXXXX   XXXXXXXXXXX',
        'AI      AAAX XAAA      IA',
        'A                       A',
        'AO   AA           AA   OA',
        'A                       A',
        'AI          X          IA',
        'AA  AAAAAAAXXXAAAAAAA  AA',
        'A         X   X         A',
        'A   AAA   X W X   AAA   A',
        'XI        X   X        IX',
        'XX  AAAAAAAX XAAAAAAA  XX',
        'XI                      X',
        'XXAAAAAAAAAAAAAAAAAAAAAXX'
    ]

    # Adicionar uma lista de tesouros
    tesouros = []

    # Adicionar uma lista de armas
    armas = []
    # Adicionar uma lista de inimigos
    inimigos = []

    # Adicionar uma lista de inimigos 2 (orcs)
    inimigos2 = []

    # Adicionar a fase na lista de fases
    fases.append(fase_2)

    # Jogador
    class Jogador(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.color('blue')
            self.shape('Elven_Player_Down.gif')
            self.speed(0)
            self.penup()
            self.gold = 0
            self.arma = 'Não'
            self.moedas = 0
            self.vidas = qnt_vida
            self.direction = 'stop'
            self.goto(0, 240)

        # Movimentação do Jogador
        def go_up(self):
            mover_para_x = jogador.xcor()
            mover_para_y = jogador.ycor() + 24
            self.shape('Elven_Player_Up.gif')
            self.direction = 'Up'

            # Checar se não tem uma parede no spot
            if (mover_para_x, mover_para_y) not in paredes:
                jogador.goto(mover_para_x, mover_para_y)

        def go_down(self):
            mover_para_x = jogador.xcor()
            mover_para_y = jogador.ycor() - 24
            self.shape('Elven_Player_Down.gif')
            self.direction = 'Down'

            # Checar se não tem uma parede no spot
            if (mover_para_x, mover_para_y) not in paredes:
                jogador.goto(mover_para_x, mover_para_y)

        def go_right(self):
            mover_para_x = jogador.xcor() + 24
            mover_para_y = jogador.ycor()
            self.shape('Elven_Player_Right.gif')
            self.direction = 'Right'

            # Checar se não tem uma parede no spot
            if (mover_para_x, mover_para_y) not in paredes:
                jogador.goto(mover_para_x, mover_para_y)

        def go_left(self):
            mover_para_x = jogador.xcor() - 24
            mover_para_y = jogador.ycor()
            self.shape('Elven_Player_Left.gif')
            self.direction = 'Left'

            # Checar se não tem uma parede no spot
            if (mover_para_x, mover_para_y) not in paredes:
                jogador.goto(mover_para_x, mover_para_y)

        def flash(self):
            if self.direction == 'Right':
                move_to_x = self.xcor() + 48
                move_to_y = self.ycor()
            elif self.direction == 'Left':
                move_to_x = self.xcor() - 48
                move_to_y = self.ycor()
            elif self.direction == 'Up':
                move_to_x = self.xcor()
                move_to_y = self.ycor() + 48

            elif self.direction == 'Down':
                move_to_x = self.xcor()
                move_to_y = self.ycor() - 48
            else:
                move_to_x = self.xcor()
                move_to_y = self.ycor()

            if move_to_x <= 288 and move_to_x >= -288 and move_to_y <= 288 and move_to_y >= -288:
                if (move_to_x, move_to_y) not in paredes:
                    self.goto(move_to_x, move_to_y)
            else:
                print('O jogador não pode ir para essa área')

        def passar_fase(self):
            x = self.xcor()
            y = self.ycor()
            if (x, y) == (0, 240) and jogador.arma == 'Sim':
                print('Você passou de fase!')
                time.sleep(0.5)
                turtle.clearscreen()
                main_menu()
            elif (x, y) == (0, 240) and jogador.arma != 'Sim':
                print('Você não pegou a arma para passar de fase!')
            elif (x, y) != (0, 240) and jogador.arma == 'Sim':
                print('Você precisa estar no Centro Élfico para completar a fase!')
            else:
                print('Cumpra o seu objetivo e vá para o Centro Élfico para completar a fase!')

        def colisão(self, outro):
            a = self.xcor() - outro.xcor()
            b = self.ycor() - outro.ycor()
            distância = math.sqrt((a ** 2) + (b ** 2))

            if distância < 5:
                return True
            else:
                return False

    # Criar uma função das fases
    def setup_fase(fase):
        for y in range(len(fase)):
            for x in range(len(fase[y])):
                # Colocar as entidades em cada coordenada x, y
                entidade = fase[y][x]
                tela_x = -288 + (x * 24)
                tela_y = 288 - (y * 24)

                # Checar se é um X (representando uma parede)
                if entidade == 'X':
                    caneta.shape('Elven_Block.gif')
                    caneta.goto(tela_x, tela_y)
                    caneta.stamp()
                    # Adicionar coordenadas para a lista de paredes
                    paredes.append((tela_x, tela_y))
                # Checar se é um P (representando o player)
                if entidade == 'P':
                    jogador.goto(tela_x, tela_y)

                # Chegar se é um T (representando um tesouro)
                if entidade == 'T':
                    tesouros.append(Tesouro(tela_x, tela_y))

                # Checar se é um I (representando um inimigo)
                if entidade == 'I':
                    inimigos.append(Inimigo(tela_x, tela_y))

                # Checar se é um C (representando o centro)
                if entidade == 'C':
                    caneta.shape('Elven_Center.gif')
                    caneta.goto(tela_x, tela_y)
                    caneta.stamp()

                # Checar se é um A (representando a árvore)
                if entidade == 'A':
                    caneta.shape('Elven_Tree.gif')
                    caneta.goto(tela_x, tela_y)
                    caneta.stamp()
                    # Adicionar coordenadas para a lista de paredes
                    paredes.append((tela_x, tela_y))

                # Checar se é um O (representando um orc)
                if entidade == 'O':
                    inimigos2.append(Inimigo2(tela_x, tela_y))

                # Checar se é um W (representando a arma[Weapon])
                if entidade == 'W':
                    armas.append(Arma(tela_x, tela_y))

    # Criar uma instância de classe
    caneta = Caneta()
    jogador = Jogador()

    # Lista de coordenadas das paredes
    paredes = []

    # Ligar a fase
    setup_fase(fases[1])

    # Desliga os updates da tela
    tela.tracer(0)

    # Precionar teclas
    tela.listen()
    tela.onkeypress(jogador.go_up, 'Up')
    tela.onkeypress(jogador.go_down, 'Down')
    tela.onkeypress(jogador.go_right, 'Right')
    tela.onkeypress(jogador.go_left, 'Left')
    tela.onkeypress(jogador.flash, 'x')
    tela.onkeypress(jogador.passar_fase, 'b')
    botinfo.onclick(info)
    botexit.onclick(exit)

    # Começar a mover os inimigos
    for inimigo in inimigos:
        turtle.ontimer(inimigo.move, t=250)

    for inimigo in inimigos2:
        turtle.ontimer(inimigo.move, t=250)

    # Looping infinito do game
    while True:
        # Checar a colisão do jogador com os inimigos
        for inimigo in inimigos:
            if jogador.colisão(inimigo):
                jogador.vidas -= 1
                jogador.goto(0, 240)
                score_vidas.clear()
                score_vidas.write(f'Vidas: {jogador.vidas}', align='center', font=('Courier', 24, 'normal'))
                if jogador.vidas == 0:
                    print(f'Jogador morre!')
                    turtle.clearscreen()
                    main_menu()

        # Checar a colisão do jogador com os inimigos 2
        for inimigo in inimigos2:
            if jogador.colisão(inimigo):
                jogador.vidas -= 1
                jogador.goto(0, 240)
                score_vidas.clear()
                score_vidas.write(f'Vidas: {jogador.vidas}', align='center', font=('Courier', 24, 'normal'))
                if jogador.vidas == 0:
                    print(f'Jogador morre!')
                    turtle.clearscreen()
                    main_menu()

        # Checar a colisão do jogador com o tesouro
        for tesouro in tesouros:
            if jogador.colisão(tesouro):
                jogador.gold += tesouro.gold
                jogador.moedas += 1
                print(f'Ouro do Jogador {jogador.gold}')

                if jogador.moedas == 1:
                    winsound.PlaySound('Elven_Coin_Sound', winsound.SND_ASYNC)
                elif jogador.moedas > 1:
                    winsound.PlaySound('Elven_Coin_Sound4', winsound.SND_ASYNC)

                # Destruir o tesouro
                tesouro.destroy()
                # Remover o tesouro da lista de tesouros
                tesouros.remove(tesouro)

        # Checar a colisão do jogador com a arma
        for arma in armas:
            if jogador.colisão(arma):
                jogador.arma = 'Sim'
                score_objetivo.clear()
                score_objetivo.write(f'Arma: 1/1', align='center', font=('Courier', 24, 'bold'))
                print(f'O jogador pegou a arma!')

                # Destruir o tesouro
                arma.destroy()
                # Remover o tesouro da lista de tesouros
                armas.remove(arma)

        # Atualizar a tela
        tela.update()


def level_3():
    # Configurações da Tela
    tela = turtle.Screen()
    tela.setup(width=750, height=750)
    tela.bgcolor('black')
    tela.title('Level 3')

    # Objetivo fase 1
    objetivo = 'O objetivo desta fase é pegar a Orb localizada no centro do castelo e voltar ao Centro Élfico!'

    # Botão info
    botinfo = turtle.Turtle()
    botinfo.speed(0)
    botinfo.shape('Elven_Info.gif')
    botinfo.color('blue')
    botinfo.penup()
    botinfo.goto(288, 320)

    def info(x, y):
        print(objetivo)

    # Botão exit
    botexit = turtle.Turtle()
    botexit.speed(0)
    botexit.shape('Elven_Exit.gif')
    botexit.color('blue')
    botexit.penup()
    botexit.goto(-288, 320)

    def exit(x, y):
        time.sleep(0.5)
        turtle.clearscreen()
        main_menu()

    # Score de vidas
    qnt_vida = 3
    score_vidas = turtle.Turtle()
    score_vidas.speed(0)
    score_vidas.shape('square')
    score_vidas.color('red')
    score_vidas.penup()
    score_vidas.hideturtle()
    score_vidas.goto(210, 300)
    score_vidas.write(f'Vidas: {qnt_vida}', align='center', font=('Courier', 18, 'bold'))

    # Score do Objetivo
    qnt_moeda = 4
    score_objetivo = turtle.Turtle()
    score_objetivo.speed(0)
    score_objetivo.shape('square')
    score_objetivo.color('orange')
    score_objetivo.penup()
    score_objetivo.hideturtle()
    score_objetivo.goto(85, 300)
    score_objetivo.write(f'Orb: 0/1', align='center', font=('Courier', 18, 'bold'))

    # Score de moedas
    qnt_moeda = 4
    score_moedas = turtle.Turtle()
    score_moedas.speed(0)
    score_moedas.shape('square')
    score_moedas.color('yellow')
    score_moedas.penup()
    score_moedas.hideturtle()
    score_moedas.goto(-120, 300)
    score_moedas.write(f'Moedas Obtidas: 0/{qnt_moeda}', align='center', font=('Courier', 18, 'bold'))

    # Caneta
    class Caneta(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape('square')
            self.color('white')
            self.penup()
            self.speed(0)
            self.hideturtle()

    #Lista de inimigos
    inimigos = []


    class Inimigo3(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.color('red')
            self.shape('Elven_Knight_Down.gif')
            self.speed(0)
            self.penup()
            self.goto(x, y)
            self.direction = 'Down'


    class Inimigo4(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.color('red')
            self.shape('Elven_Bat_Down.gif')
            self.speed(0)
            self.penup()
            self.goto(x, y)
            self.direction = 'Down'

        # Movimentação do Inimigo
        def move(self):
            self.forward(48)
            self.left(90)



    # Tesouro
    class Tesouro(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape('Elven_Coin.gif')
            self.color('gold')
            self.speed(0)
            self.gold = 100
            self.penup()
            self.goto(x, y)

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    # Orb
    class Orb(turtle.Turtle):
        def __init__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape('Elven_OrbFlash.gif')
            self.color('gold')
            self.speed(0)
            self.gold = 100
            self.penup()
            self.goto(x, y)

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()

    # Lista de fases
    fases = ['']

    # Fase
    fase_3 = [
        '  A BB             BB A  ',
        ' A B  BBBBBBBBBBBBB  B A ',
        'A  B TB           BT B  A',
        'A   BB             BB   A',
        'A   B               B   A',
        'A   B                   A',
        'A   B       R       B   A',
        'A   B               B   A',
        'A   B               B   A',
        'A   B       F       B   A',
        'A   B               B   A',
        'A   B               B   A',
        'A   B       R       B   A',
        'A   B               B   A',
        'A   B               B   A',
        'A   BB             BB   A',
        'A  B TB           BT B  A',
        'A  B  BBBBDDDDDBBBB  B  A',
        '    BB    K   K    BB    ',
        ' A                     A ',
        '  A                   A  ',
        '  A                   A  ',
        '  A                   A  ',
        ' A          P          A ',
        '            C            '
    ]

    # Adicionar uma lista de tesouros
    tesouros = []

    # Adicionar uma lista de orbs
    orbs = []

    # Adicionar uma lista de inimigos
    inimigos3 = []

    # Adicionar uma lista de inimigos
    inimigos4 = []

    # Adicionar a fase na lista de fases
    fases.append(fase_3)

    # Jogador
    class Jogador(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.color('blue')
            self.shape('Elven_Player_Down.gif')
            self.speed(0)
            self.penup()
            self.orb = 'Não'
            self.gold = 0
            self.moedas = 0
            self.vidas = qnt_vida
            self.direction = 'stop'

        # Movimentação do Jogador
        def go_up(self):
            mover_para_x = jogador.xcor()
            mover_para_y = jogador.ycor() + 24
            self.shape('Elven_Player_Up.gif')
            self.direction = 'Up'

            # Checar se não tem uma parede no spot
            if (mover_para_x, mover_para_y) not in paredes:
                jogador.goto(mover_para_x, mover_para_y)

        def go_down(self):
            mover_para_x = jogador.xcor()
            mover_para_y = jogador.ycor() - 24
            self.shape('Elven_Player_Down.gif')
            self.direction = 'Down'

            # Checar se não tem uma parede no spot
            if (mover_para_x, mover_para_y) not in paredes:
                jogador.goto(mover_para_x, mover_para_y)

        def go_right(self):
            mover_para_x = jogador.xcor() + 24
            mover_para_y = jogador.ycor()
            self.shape('Elven_Player_Right.gif')
            self.direction = 'Right'

            # Checar se não tem uma parede no spot
            if (mover_para_x, mover_para_y) not in paredes:
                jogador.goto(mover_para_x, mover_para_y)

        def go_left(self):
            mover_para_x = jogador.xcor() - 24
            mover_para_y = jogador.ycor()
            self.shape('Elven_Player_Left.gif')
            self.direction = 'Left'

            # Checar se não tem uma parede no spot
            if (mover_para_x, mover_para_y) not in paredes:
                jogador.goto(mover_para_x, mover_para_y)

        def flash(self):
            if self.orb == 'Sim':
                if self.direction == 'Right':
                    move_to_x = self.xcor() + 48
                    move_to_y = self.ycor()
                elif self.direction == 'Left':
                    move_to_x = self.xcor() - 48
                    move_to_y = self.ycor()
                elif self.direction == 'Up':
                    move_to_x = self.xcor()
                    move_to_y = self.ycor() + 48

                elif self.direction == 'Down':
                    move_to_x = self.xcor()
                    move_to_y = self.ycor() - 48
                else:
                    move_to_x = self.xcor()
                    move_to_y = self.ycor()

                if move_to_x <= 288 and move_to_x >= -288 and move_to_y <= 288 and move_to_y >= -288:
                    if (move_to_x, move_to_y) not in paredes:
                        self.goto(move_to_x, move_to_y)
                else:
                    print('O jogador não pode ir para essa área!')
            else:
                print('Você não tem a habilidade Flash!')

        def passar_fase(self):
            x = self.xcor()
            y = self.ycor()
            if (x, y) == (0, -288) and jogador.orb == 'Sim':
                print('Você passou de fase!')
                time.sleep(0.5)
                turtle.clearscreen()
                main_menu()
            elif (x, y) == (0, -288) and jogador.orb != 'Sim':
                print('Você não pegou a Orb!')
            elif (x, y) != (0, -288) and jogador.orb == 'Sim':
                print('Você precisa estar no Centro Élfico para completar a fase!')
            else:
                print('Cumpra o seu objetivo e vá para o Centro Élfico para completar a fase!')

        def colisão(self, outro):
            a = self.xcor() - outro.xcor()
            b = self.ycor() - outro.ycor()
            distância = math.sqrt((a ** 2) + (b ** 2))

            if distância < 5:
                return True
            else:
                return False

    # Criar uma função das fases
    def setup_fase(fase):
        for y in range(len(fase)):
            for x in range(len(fase[y])):
                # Colocar as entidades em cada coordenada x, y
                entidade = fase[y][x]
                tela_x = -288 + (x * 24)
                tela_y = 288 - (y * 24)

                # Checar se é um B (representando uma parede do castelo)
                if entidade == 'B':
                    caneta.shape('Elven_CastleBrick.gif')
                    caneta.goto(tela_x, tela_y)
                    caneta.stamp()
                    # Adicionar coordenadas para a lista de paredes
                    paredes.append((tela_x, tela_y))

                # Checar se é um P (representando o player)
                if entidade == 'P':
                    jogador.goto(tela_x, tela_y)

                # Chegar se é um T (representando o tesouro)
                if entidade == 'T':
                    tesouros.append(Tesouro(tela_x, tela_y))

                # Checar se é um K (representando o Knight)
                if entidade == 'K':
                    inimigos3.append(Inimigo3(tela_x, tela_y))

                # Checar se é um R (representando o Morcego)
                if entidade == 'R':
                    inimigos4.append(Inimigo4(tela_x, tela_y))

                # Checar se é um C (representando o centro)
                if entidade == 'C':
                    caneta.shape('Elven_Center.gif')
                    caneta.goto(tela_x, tela_y)
                    caneta.stamp()

                #Checar se é um D (representando a porta de madeira do castelo)
                if entidade == 'D':
                    caneta.shape('Elven_CastleWoodDoor.gif')
                    caneta.goto(tela_x, tela_y)
                    caneta.stamp()
                    # Adicionar coordenadas para a lista de paredes
                    paredes.append((tela_x, tela_y))

                # Checar se é um T (representando a árvore)
                if entidade == 'A':
                    caneta.shape('Elven_Tree.gif')
                    caneta.goto(tela_x, tela_y)
                    caneta.stamp()
                    # Adicionar coordenadas para a lista de paredes
                    paredes.append((tela_x, tela_y))

                # Checar se é um F (representando a orb do flash)
                if entidade == 'F':
                    orbs.append(Orb(tela_x, tela_y))

    # Criar uma instância de classe
    caneta = Caneta()
    jogador = Jogador()

    # Lista de coordenadas das paredes
    paredes = []

    # Ligar a fase
    setup_fase(fases[1])

    # Desliga os updates da tela
    tela.tracer(0)

    # Precionar teclas
    tela.listen()
    tela.onkeypress(jogador.go_up, 'Up')
    tela.onkeypress(jogador.go_down, 'Down')
    tela.onkeypress(jogador.go_right, 'Right')
    tela.onkeypress(jogador.go_left, 'Left')
    tela.onkeypress(jogador.flash, 'x')
    tela.onkeypress(jogador.passar_fase, 'b')
    botinfo.onclick(info)
    botexit.onclick(exit)

    # Começar a mover os inimigos
    for inimigo in inimigos4:
        turtle.ontimer(inimigo.move, t=250)


    # Looping infinito do game
    while True:
        # Checar a colisão do jogador com os Knights
        for inimigo in inimigos3:
            if jogador.colisão(inimigo):
                jogador.vidas -= 1
                jogador.goto(0, -288)
                score_vidas.clear()
                score_vidas.write(f'Vidas: {jogador.vidas}', align='center', font=('Courier', 18, 'bold'))
                if jogador.vidas == 0:
                    print(f'Jogador morre!')
                    turtle.clearscreen()
                    main_menu()


        # Checar a colisão do jogador com os Bats
        for inimigo in inimigos4:
            if jogador.colisão(inimigo):
                jogador.vidas -= 1
                jogador.goto(0, -288)
                score_vidas.clear()
                score_vidas.write(f'Vidas: {jogador.vidas}', align='center', font=('Courier', 18, 'bold'))
                if jogador.vidas == 0:
                    print(f'Jogador morre!')
                    turtle.clearscreen()
                    main_menu()


        # Checar a colisão do jogador com o tesouro
        for tesouro in tesouros:
            if jogador.colisão(tesouro):
                jogador.gold += tesouro.gold
                jogador.moedas += 1
                print(f'Ouro do Jogador {jogador.gold}')
                score_moedas.clear()
                score_moedas.write(f'Moedas Obtidas: {jogador.moedas}/{qnt_moeda}', align='center', font=('Courier', 18, 'bold'))
                if jogador.moedas == 1:
                    winsound.PlaySound('Elven_Coin_Sound', winsound.SND_ASYNC | winsound.SND_FILENAME)
                elif jogador.moedas > 1:
                    winsound.PlaySound('Elven_Coin_Sound4', winsound.SND_ASYNC | winsound.SND_FILENAME)

                # Destruir o tesouro
                tesouro.destroy()
                # Remover o tesouro da lista de tesouros
                tesouros.remove(tesouro)

        # Checar a colisão do jogador com a arma
        for orb in orbs:
            if jogador.colisão(orb):
                jogador.orb = 'Sim'
                score_objetivo.clear()
                score_objetivo.write(f'Orb: 1/1', align='center', font=('Courier', 18, 'bold'))
                print(f'O jogador pegou a orb!')

                # Destruir a orb
                orb.destroy()
                # Remover a orb da lista de orbs
                orbs.remove(orb)

        # Atualizar a tela
        tela.update()

main_menu()
