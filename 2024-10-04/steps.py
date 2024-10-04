import turtle

def draw(n: int) -> None:
    for x in range(n):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(20)
        turtle.right(90)

draw(10)
turtle.hideturtle()
turtle.done()