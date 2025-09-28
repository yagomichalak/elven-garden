# Criar o menu principal
import turtle
import time
import winsound

from levels.levels_menu import LevelMenu

# Variáveis globais
IMAGE_PATH = "assets/images/"
SOUND_PATH = "assets/sounds/"

# Registrar imagens
imagens = ['Elven_Elf_Left.gif', 'Elven_Elf_Right.gif', 'Elven_Block.gif', 'Elven_Coin.gif',
           'Elven_Center.gif', 'Elven_Player_Down.gif', 'Elven_Player_Up.gif',
           'Elven_Player_Left.gif', 'Elven_Player_Right.gif', 'Elven_Info.gif',
           'Elven_Exit.gif', 'Elven_Tree.gif', 'Elven_Orc_Down.gif', 'Elven_Orc_Up.gif',
           'Elven_Orc_Left.gif', 'Elven_Orc_Right.gif', 'Elven_Staff.gif','Elven_OrbFlash.gif',
           'Elven_Bat_Up.gif', 'Elven_Bat_Down.gif', 'Elven_Knight_Down.gif', 'Elven_CastleBrick.gif',
           'Elven_CastleWoodDoor.gif']
for i in imagens:
    turtle.register_shape(IMAGE_PATH + i)


class ElvenGarden(LevelMenu):
    """ Elven Garden Game - Main Class """

    def __init__(self) -> None:
        # Registers the images

        for i in imagens:
            turtle.register_shape(IMAGE_PATH + i)

    def main(self):
        # Tela do Menu
        turtle.register_shape(IMAGE_PATH + 'Elven_Main_Menu.gif')
        menu = turtle.Screen()
        menu.setup(width=750, height=750)
        menu.bgcolor('black')
        menu.bgpic(IMAGE_PATH + "Elven_Main_Menu.gif")
        menu.title('Elven Garden')

        #Música tema do menu principal
        theme = winsound.PlaySound(SOUND_PATH + 'Elven_Main_Menu_Theme', winsound.SND_LOOP | winsound.SND_ASYNC | winsound.SND_FILENAME)

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
                self.level_menu()

            if x >= -150 and x <= 130 and y <= -145 and y >= -225:
                print('Bora configurar esse jogo aê!')

        # Keyboard bindings do menu principal
        turtle.listen()
        turtle.onscreenclick(botão_clickado, 1)

        # Looping infinito da função
        turtle.mainloop()


if __name__ == '__main__':
    game = ElvenGarden()
    game.main()
