import turtle
#turtle object
t = turtle.Turtle()

t.penup()
t.goto(-200,100)
t.pensize(5)
t.color("blue")

#J
t.pendown()
t.forward(50)
t.backward(100)
t.forward(75)
t.right(90)
t.forward(120)
t.circle(-60,200)

t.penup()
t.goto(-150,50)

#0
t.pendown()
t.fd(50)
t.circle(-30, 90)
t.circle(-30, 90)
t.fd(50)
t.circle(-30, 90)
t.circle(-30, 90)

t.penup()
t.goto(-60,50)

#9
t.pendown()
t.forward(30)
t.circle(-30,90)
t.circle(-30,90)
t.forward(90)
t.circle(-30,90)

t.penup()
t.goto(-60,50)
t.pendown()
t.right(180)
t.forward(55)

t.penup()
t.goto(20,50)

#4
t.pendown()
t.forward(60)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.backward(20)
t.left(90)
t.forward(40)
t.right(90)
t.forward(90)

t.penup()
t.goto(100,20)

#i
t.pendown()
t.right(180)
t.forward(90)
t.penup()
t.forward(10)
t.pendown()
t.forward(5)






turtle.exitonclick()


