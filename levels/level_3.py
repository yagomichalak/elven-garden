import turtle
import time
import math
import winsound

# Variáveis globais
IMAGE_PATH = "assets/images/"
SOUND_PATH = "assets/sounds/"


class Level3:
    def level_3(self):
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
        botinfo.shape(IMAGE_PATH + 'Elven_Info.gif')
        botinfo.color('blue')
        botinfo.penup()
        botinfo.goto(288, 320)

        def info(x, y):
            print(objetivo)

        # Botão exit
        botexit = turtle.Turtle()
        botexit.speed(0)
        botexit.shape(IMAGE_PATH + 'Elven_Exit.gif')
        botexit.color('blue')
        botexit.penup()
        botexit.goto(-288, 320)

        def exit(x, y):
            time.sleep(0.5)
            turtle.clearscreen()
            self.main()

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
                self.shape(IMAGE_PATH + 'Elven_Knight_Down.gif')
                self.speed(0)
                self.penup()
                self.goto(x, y)
                self.direction = 'Down'


        class Inimigo4(turtle.Turtle):
            def __init__(self, x, y):
                turtle.Turtle.__init__(self)
                self.color('red')
                self.shape(IMAGE_PATH + 'Elven_Bat_Down.gif')
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
                self.shape(IMAGE_PATH + 'Elven_Coin.gif')
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
                self.shape(IMAGE_PATH + 'Elven_OrbFlash.gif')
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
                self.shape(IMAGE_PATH + 'Elven_Player_Down.gif')
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
                self.shape(IMAGE_PATH + 'Elven_Player_Up.gif')
                self.direction = 'Up'

                # Checar se não tem uma parede no spot
                if (mover_para_x, mover_para_y) not in paredes:
                    jogador.goto(mover_para_x, mover_para_y)

            def go_down(self):
                mover_para_x = jogador.xcor()
                mover_para_y = jogador.ycor() - 24
                self.shape(IMAGE_PATH + 'Elven_Player_Down.gif')
                self.direction = 'Down'

                # Checar se não tem uma parede no spot
                if (mover_para_x, mover_para_y) not in paredes:
                    jogador.goto(mover_para_x, mover_para_y)

            def go_right(self):
                mover_para_x = jogador.xcor() + 24
                mover_para_y = jogador.ycor()
                self.shape(IMAGE_PATH + 'Elven_Player_Right.gif')
                self.direction = 'Right'

                # Checar se não tem uma parede no spot
                if (mover_para_x, mover_para_y) not in paredes:
                    jogador.goto(mover_para_x, mover_para_y)

            def go_left(self):
                mover_para_x = jogador.xcor() - 24
                mover_para_y = jogador.ycor()
                self.shape(IMAGE_PATH + 'Elven_Player_Left.gif')
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
                    self.main()
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
                        caneta.shape(IMAGE_PATH + 'Elven_CastleBrick.gif')
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
                        caneta.shape(IMAGE_PATH + 'Elven_Center.gif')
                        caneta.goto(tela_x, tela_y)
                        caneta.stamp()

                    #Checar se é um D (representando a porta de madeira do castelo)
                    if entidade == 'D':
                        caneta.shape(IMAGE_PATH + 'Elven_CastleWoodDoor.gif')
                        caneta.goto(tela_x, tela_y)
                        caneta.stamp()
                        # Adicionar coordenadas para a lista de paredes
                        paredes.append((tela_x, tela_y))

                    # Checar se é um T (representando a árvore)
                    if entidade == 'A':
                        caneta.shape(IMAGE_PATH + 'Elven_Tree.gif')
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
                        self.main()


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
                        self.main()


            # Checar a colisão do jogador com o tesouro
            for tesouro in tesouros:
                if jogador.colisão(tesouro):
                    jogador.gold += tesouro.gold
                    jogador.moedas += 1
                    print(f'Ouro do Jogador {jogador.gold}')
                    score_moedas.clear()
                    score_moedas.write(f'Moedas Obtidas: {jogador.moedas}/{qnt_moeda}', align='center', font=('Courier', 18, 'bold'))
                    if jogador.moedas == 1:
                        winsound.PlaySound(SOUND_PATH + 'Elven_Coin_Sound', winsound.SND_ASYNC | winsound.SND_FILENAME)
                    elif jogador.moedas > 1:
                        winsound.PlaySound(SOUND_PATH + 'Elven_Coin_Sound4', winsound.SND_ASYNC | winsound.SND_FILENAME)

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

