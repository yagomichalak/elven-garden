import turtle


#Window Settings
win = turtle.Screen()
win.setup(width=750, height=750)
win.bgcolor('grey')

#Player Class
class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()
        self.shape('square')
        self.color('blue')
        self.goto(0, 0)

    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24
        self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24
        self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()
        self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()
        self.goto(move_to_x, move_to_y)

#Instâncias
player = Player()

#Keyboard bindings
turtle.listen()
turtle.onkeypress(player.go_right, 'd' )
turtle.onkeypress(player.go_left, 'a')
turtle.onkeypress(player.go_up, 'w')
turtle.onkeypress(player.go_down, 's')

#Keeps off the window from the update
win.tracer(0)

#Main update loop of the screen
while True:
    win.update()

