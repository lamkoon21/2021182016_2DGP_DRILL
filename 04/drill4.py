import turtle

width = -150
height = 0

turtle.penup()
turtle.goto(0,-150)
turtle.pendown()

while width <= 350:
    turtle.goto(0,width)
    turtle.pendown()
    turtle.forward(500)
    width += 100
    turtle.penup()

turtle.goto(0,350)
turtle.right(90)

while height <= 500:
    turtle.goto(height, 350)
    turtle.pendown()
    turtle.forward(500)
    height += 100
    turtle.penup()
    
turtle.exitonclick()