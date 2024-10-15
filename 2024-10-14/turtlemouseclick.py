import turtle as t
import random

def draw_square(x: float, y: float, side: float, color: str) -> None:
    print(f'({round(x)}, {round(y)})')
    t.penup()
    half_side = side/2
    t.setposition(x - half_side, y - half_side)
    t.setheading(0)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    for _ in range(4):
        t.forward(side)
        t.left(90)
    t.end_fill()
    t.update()

def put_square(x: float, y: float) -> None:
    draw_square(x, y, 20, 'red')


t.onscreenclick(put_square)

t.hideturtle()
t.getscreen()
t.tracer(0)

width = t.window_width()
height = t.window_height()

for _ in range(20):
    rand_x = width*random.random() - width/2;
    rand_y = height*random.random() - height/2;
    draw_square(rand_x, rand_y, 10, 'cyan');

t.mainloop()
