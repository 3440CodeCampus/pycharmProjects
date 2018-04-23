# pythonDrawAssign4 coaxial py
import turtle
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.pensize(5)
turtle.pencolor("black")
turtle.goto(0, -100)
turtle.down()
for i in range(4):
    turtle.circle(30 * (i+1))
turtle.done()
