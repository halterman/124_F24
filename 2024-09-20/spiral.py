import turtle

turtle.home()
length = 10
angle = 5

for i in range(100):
    turtle.forward(length)
    turtle.left(angle)
    #length -= 5
    angle -= 2