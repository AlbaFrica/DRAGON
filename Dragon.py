import turtle
t = turtle.Turtle() #Funhouse
u = turtle.Turtle() #Jenaka
r = turtle.Turtle() #
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
t.color("black", "Olive")#
t.forward(180)
t.right(90)
t.forward(60)
t.left(90)
t.forward(45)
t.left(90)
t.forward(25)
t.right(90)
t.forward(15)
t.right(20)#20
t.forward(90)#90
t.left(158)#155
t.begin_fill()
t.forward(87)#90
t.left(99)#105
t.forward(32.78)
t.right(180) #180
t.end_fill()#
t.forward(32.78)

#horns 
t.left(33)
t.forward(5)
t.right(80)
t.forward(90)

#first arm

#spots

#wing(r)
r.left(180)
r.forward(30)
r.right(90)
r.forward(60)
r.right(90)
r.forward(80)
r.left(100)
r.forward(30)
r.left(50)
r.forward(25)
r.right(80)
r.forward(10)
r.left(160)
r.forward(10)
r.right(50)
r.forward(40)
r.left(150)
r.forward(30)
r.right(130)
r.forward(30)
r.left(160)
r.forward(60)
r.right(90)
r.forward(20)

#neck puff
r.left(90)
r.forward(33)
r.left(90)
r.forward(120)
r.left(120)
r.forward(5)
r.right(60)
r.forward(15)
r.right(60)
r.forward(10)
r.right(25)
r.forward(7)
r.left(140)
r.forward(10)
r.right(60)
r.forward(15)
r.right(30)
r.forward(15)
r.right(50)
r.forward(20)
r.right(15)
r.forward(10)
r.left(170)
r.forward(15)
r.right(80)
r.forward(15)
r.right(70)
r.forward(20)
r.right(40)
r.forward(20)
r.right(40)
r.forward(20)
r.right(50)
r.forward(30)

#2nd arm

#headband piece

#face(u)

turtle.Screen().exitonclick()
