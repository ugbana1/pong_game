from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time

screen=Screen()

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Score()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

is_game_on =True
while is_game_on:
    time.sleep(ball.move_speed)
    #This updates the screen
    screen.update()
    ball.move()

    #Detect Collision with Walls
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()


    # Detect collision with paddle
    if ball.distance(r_paddle) <50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()




    #Detect L paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()


















screen.exitonclick()