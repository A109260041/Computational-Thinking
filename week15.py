import turtle
turtle.colormode(255)
pen = turtle.Turtle()
pen.color(255, 215, 0)
pen.pensize(5)

#將比向前移動100個單位, 向右轉144度, 做五次畫五角星。
for i in range(5):
    pen.forward(250)
    pen.right(144)
