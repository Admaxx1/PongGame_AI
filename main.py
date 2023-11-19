import random
import turtle

WIDTH = 800
HEIGHT = 600
PADDLE_SPEED = 10
BALL_SPEED = 3
SCORE_FONT = ('Courier',24,'normal')
INFO_FONT = ('Courier',14,'normal')
AISWITCH = True


# Score

player_1 = 0
player_2 = 0



# Making the paddles

def create_paddle(x,y):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("lime")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, y)
    paddle.dy = 0
    return paddle

def create_ball(x,y):
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape('circle')
    ball.color('white')
    ball.penup()
    ball.goto(x, y)
    ball.dx = BALL_SPEED
    ball.dy = BALL_SPEED
    return ball

pen = turtle.Pen()
def display_text():

    pen.clear()
    pen.hideturtle()
    pen.speed(0)
    pen.color('white')
    pen.penup()
    pen.goto(0, 260)
    pen.write('Player 1:{} Player 2:{}'.format(player_1, player_2), align='center', font=SCORE_FONT)
    pen.goto(0, 230)
    pen.write('Use W and S and arrow keys to move', align='center', font=INFO_FONT)
    return pen


def ai_controller():
    global AISWITCH, paddle_2

    if AISWITCH:

        if paddle_2.ycor() > ball.ycor() - 20:

            paddle_down(paddle_2, PADDLE_SPEED)

        elif paddle_2.ycor() < ball.ycor() + 20:

            paddle_up(paddle_2, PADDLE_SPEED)

        else:

            paddle_stop(paddle_2)


def aiswitch():
    global AISWITCH
    if AISWITCH == True:
        AISWITCH=False
    else:
        AISWITCH=True

def paddle_up(paddle,speed):
    paddle.dy=speed

def paddle_down(paddle,speed):
    paddle.dy=-speed
def paddle_stop(paddle):
    paddle.dy=0

wn = turtle.Screen()  # wn is the screen
wn.tracer(0)
wn.title("Turtle Game!")
wn.bgcolor("black")
wn.setup(WIDTH, HEIGHT)

paddle_1 = create_paddle(-350,0)
paddle_2 = create_paddle(350,0)
ball = create_ball(0,0)
pen = display_text()

wn.listen()
wn.onkeypress(lambda :paddle_up(paddle_1,PADDLE_SPEED), "w")
wn.onkeypress(lambda :paddle_down(paddle_1,PADDLE_SPEED), "s")
wn.onkeypress(lambda :paddle_up(paddle_2,PADDLE_SPEED), "Up")
wn.onkeypress(lambda :paddle_down(paddle_2,PADDLE_SPEED), "Down")

wn.onkeyrelease(lambda :paddle_stop(paddle_1), "w")
wn.onkeyrelease(lambda :paddle_stop(paddle_1), "s")
wn.onkeyrelease(lambda :paddle_stop(paddle_2), "Up")
wn.onkeyrelease(lambda :paddle_stop(paddle_2), "Down")
wn.onkeypress(aiswitch,'g')





def update_game():
    global player_1
    global player_2
    wn.update()
    ai_controller()

    for paddle in [paddle_1,paddle_2]:
        paddle.sety(paddle.ycor()+paddle.dy)
        if paddle.ycor()>HEIGHT/2-10:
            paddle.sety(HEIGHT/2-10)
        if paddle.ycor()<-HEIGHT/2+10:
            paddle.sety(-HEIGHT/2+10)


    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > HEIGHT / 2 - 10 or ball.ycor() < -HEIGHT / 2 + 10:
        ball.dy *= -1

    if ball.xcor() > WIDTH / 2 - 10 or ball.xcor() < -WIDTH / 2 + 10:
        if ball.xcor() > WIDTH / 2 - 10:
            player_1 += 1
        else:
            player_2 += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        display_text()

        # Ball collision with paddles
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_2.ycor() + 50 > ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_1.ycor() + 50 > ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
    wn.ontimer(update_game,10)
update_game()

turtle.done()




