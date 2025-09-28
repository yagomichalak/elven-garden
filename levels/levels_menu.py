import turtle
import time
import winsound

from .level_1 import Level1
from .level_2 import Level2
from .level_3 import Level3

levels = [Level1, Level2, Level3]

# Variáveis globais
IMAGE_PATH = "assets/images/"
SOUND_PATH = "assets/sounds/"

class LevelMenu(*levels):
    def level_menu(self):
        # Level Menu
        level_menu = turtle.Screen()
        level_menu.setup(width=750, height=750)
        level_menu.bgcolor('black')
        level_menu.bgpic(IMAGE_PATH + 'Elven_Level_Menu.gif')
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
                winsound.PlaySound(SOUND_PATH + 'Elven_Coin_Sound', winsound.SND_ASYNC | winsound.SND_FILENAME)
                time.sleep(0.5)
                turtle.clearscreen()
                self.level_1()

            if x >= 50 and x <= 300 and y <= 220 and y >= 140:
                winsound.PlaySound(SOUND_PATH + 'Elven_Coin_Sound', winsound.SND_ASYNC | winsound.SND_FILENAME)
                time.sleep(0.5)
                turtle.clearscreen()
                self.level_2()

            if x >= -300 and x <= -50 and y <=  80 and y >= 0:
                winsound.PlaySound(SOUND_PATH + 'Elven_Coin_Sound', winsound.SND_ASYNC | winsound.SND_FILENAME)
                time.sleep(0.5)
                turtle.clearscreen()
                self.level_3()

            if x >= 50 and x <= 300 and y <=  80 and y >= 0:
                print('Calma man, acabei de fazer a fase 3, espera aê!')

        # Keyboard Bindings do Level Menu
        level_menu.listen()
        level_menu.onscreenclick(botão_clickado, 1)
