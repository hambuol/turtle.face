#turtle.face
#by: oliver hamburger

#this program uses turtle to draw a smiley face

import turtle
turtle.speed(0)

#function that moves the turtle from one point to another without drwing a line
def pen_up_and_down(x,y):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()

#makes large circle that is shaded blue
turtle.setposition(0,0)
turtle.color("blue")
turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()

#makes a smaller circle that is shaded red
pen_up_and_down(-100,250)
turtle.color("red")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

#makes a smaller circle that is shaded red
pen_up_and_down(100,250)
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

#makes a green L
pen_up_and_down(0,200)
turtle.color("green")
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(25)

#puts turtle in correct place/orientation and sets color to orange
turtle.penup()
turtle.setposition(80,100)
turtle.left(77)
turtle.color("orange")
turtle.begin_fill()

#loop that makes an orange smile
for x in range(9):
    turtle.forward(30)
    turtle.right(20)

turtle.end_fill()

#needed so python will not crash 
turtle.exitonclick()