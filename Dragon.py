import turtle
t = turtle.Turtle()
from operator import truediv

#body
t.color("black", "pink")
t.begin_fill()

draw = 0;
while draw <= 2:

    t.forward(125)
    t.left(90)
    t.forward(180)
    t.right(90)
    t.forward(60)
    t.left(90)
    t.forward(45)
    t.left(90)
    t.forward(25)
    t.right(90)
    t.forward(35)#25
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.left(90)
    t.forward(60)#50
    #t.left(90)
    #t.forward(30)
    t.end_fill()
    break

#tail
t.color("black", "light green")
t.begin_fill()
t.right(70)
t.forward(300)
t.right(170)
t.forward(325)
t.end_fill()

#legs
t.right(120)
t.forward(60)

t.color("black", "violet")
t.begin_fill()

t.forward(25)
t.left(90)
t.forward(29)
t.left(90)
t.forward(25)

t.end_fill()

t.color("black", "light yellow")
t.begin_fill()
t.right(90)
t.forward(14)
t.right(90)
t.forward(25)
t.left(90)
t.forward(29)
t.left(90)
t.forward(25)
t.end_fill()

t.color("black", "coral")
t.begin_fill()
t.right(90)
t.forward(14)
t.right(90)
t.forward(25)
t.left(90)
t.forward(29)
t.left(90)
t.forward(25)
t.end_fill()

t.color("black", "sky blue")
t.begin_fill()
t.right(90)
t.forward(11)
t.right(90)
t.forward(25)
t.left(90)
t.forward(29)
t.left(90)
t.forward(25)

t.end_fill()

#unicorn horn
t.color("black", "tea")
t.begin_fill()
t.right(90)
t.forward(100)
t.end_fill()
#horns 

#neck puff

#first arm

#spots

#wing

#2nd arm

#headband piece

#face

turtle.Screen().exitonclick()
