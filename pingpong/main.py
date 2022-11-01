import turtle

window = turtle.Screen()
window.title("Ping-pong")
window.setup(width=1.0,height=1.0)
window.bgcolor("black")

border = turtle.Turtle()
border.color("green")
border.speed(0)
border.begin_fill()
border.goto(-500,300)
border.goto(500,300)
border.goto(500,-300)
border.goto(-500,-300)
border.goto(-500,300)
border.end_fill()

border.goto(0,300)
border.color("white")
border.goto(0,-300)

border.hideturtle()

rocket_a = turtle.Turtle()
rocket_a.color("white")
rocket_a.shape("square")
rocket_a.shapesize(stretch_len=1,stretch_wid=5)
rocket_a.penup()
rocket_a.goto(-450,0)

def move_up():
    y = rocket_a.ycor()
    if y > 240:
        y = 240
    rocket_a.sety(y+10)

def move_down():
    y = rocket_a.ycor() - 10
    if y < -240:
        y = -240
    rocket_a.sety(y-10)

rocket_b = turtle.Turtle()
rocket_b.color("white")
rocket_b.shape("square")
rocket_b.shapesize(stretch_len=1,stretch_wid=5)
rocket_b.penup()
rocket_b.goto(450,0)

def move_upr():
    y = rocket_b.ycor()
    if y > 240:
        y = 240
    rocket_b.sety(y+10)

def move_downr():
    y = rocket_b.ycor() - 10
    if y < -240:
        y = -240
    rocket_b.sety(y)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.dx = 3
ball.dy = 3
ball.penup()


window.listen()
window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_upr, "Up")
window.onkeypress(move_downr, "Down")

while True:

    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    elif ball.ycor() >= -290:
        ball.dy = -ball.dy

    elif ball.xcor() >= 490:
        ball.goto(0,0)

window.mainloop()