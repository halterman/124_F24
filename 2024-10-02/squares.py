import turtle
import random


def draw_square(x: float, y: float, side: float, color: str) -> None:
    turtle.penup()
    half_side = side / 2
    turtle.setposition(x - half_side, y - half_side)
    turtle.setheading(0)
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()
    turtle.update()


def put_square(x: float, y: float) -> None:
    # draw_square(x, y, 30, 'blue')
    print(f'x = {x}, y = {y}')


turtle.onscreenclick(put_square)

turtle.hideturtle()
turtle.tracer(0)
width = turtle.window_width()
height = turtle.window_height()

for _ in range(20):
    rand_x = width * random.random() - width/2
    rand_y = height * random.random() - height/2
    draw_square(rand_x, rand_y, 20, 'red')

turtle.mainloop()



    
