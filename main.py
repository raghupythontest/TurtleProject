import turtle as t
import random as rd

tim = t.Turtle()
tim.speed(0)
t.colormode(255)

def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    rd_color = (r, g, b)
    return rd_color


# def draw_shape(shape_side):
#     for _ in range(shape_side):
#         angle=360/shape_side
#
#         tim.forward(100)
#         tim.right(angle)
#
# for i in range(3,7):
#     tim.color(rd.choice(colors))
#     draw_shape(i)

def draw_spirograph(size):
    for _ in range(int(360/size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+size)
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
