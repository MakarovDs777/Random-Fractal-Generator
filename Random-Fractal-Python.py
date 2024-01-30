import turtle
import random

def draw_line(t, x, y, ln, angle):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(angle)
    t.forward(ln)

def draw_tree(t, x, y, ln, min_ln, angle, add_angle):
    if ln <= min_ln:
        return
    
    ln *= 0.75
    draw_line(t, x, y, ln, angle)
    
    new_x = x + ln * turtle.cos(angle)
    new_y = y - ln * turtle.sin(angle)
    draw_tree(t, new_x, new_y, ln, min_ln, angle + add_angle, add_angle)
    draw_tree(t, new_x, new_y, ln, min_ln, angle - random.randint(1, 20) / 180 * turtle.pi)

def init():
    a = float(input("Введите положение ствола: "))
    b = float(input("Введите минимальную длину линии: "))
    c = float(input("Введите положение ствола: "))
    d = float(input("Введите ширину линий: "))
    e = float(input("Введите начальную длину линии: "))
    f = float(input("Введите самоподобие: "))

    canvas = turtle.Screen()
    canvas.setup(800, 600)
    canvas.bgcolor('#fff')

    t = turtle.Turtle()
    t.speed(0)
    t.width(d)
    t.penup()
    t.goto(20 + (canvas.window_width() / random.randint(1, 10)), -250 + canvas.window_height())
    t.pendown()

    draw_tree(t, t.xcor(), t.ycor(), e, a, turtle.pi / 2, b / 180 * turtle.pi)

    turtle.done()

init()
