import turtle
wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

score_a=0
score_b=0
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:"+str(score_a)+" Player B:"+str(score_b), align="center", font=("courier", 24, "normal"))

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
def paddle_a_up():
    if paddle_a.ycor()<=225:
        y = paddle_a.ycor()
        y += 35
        paddle_a.sety(y)
    else:
        paddle_a.sety(225)
def paddle_a_down():
    if paddle_a.ycor() >= -225:
        y = paddle_a.ycor()
        y -= 35
        paddle_a.sety(y)
    else:
        paddle_a.sety(-225)
def paddle_b_up():
   if paddle_b.ycor() <= 225:
        y = paddle_b.ycor()
        y += 35
        paddle_b.sety(y)
   else:
       paddle_b.sety(225)
def paddle_b_down():
    if paddle_b.ycor() >= -225:
        y = paddle_b.ycor()
        y -= 35
        paddle_b.sety(y)
    else:
        paddle_b.sety(-225)
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
ball.dx = 0.13
ball.dy = 0.13



x=1
while x==1:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if ball.xcor() > 390:
        score_a=score_a+1
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A:" + str(score_a) + " Player B:" + str(score_b), align="center", font=("courier", 24, "normal"))
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.xcor() < -390:
        score_b=score_b+1
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A:" + str(score_a) + " Player B:" + str(score_b), align="center", font=("courier", 24, "normal"))
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1

