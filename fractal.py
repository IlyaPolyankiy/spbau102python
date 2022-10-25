import turtle as tl

def draw_fractal(size):
    if size >= 5:
        draw_fractal(size / 3.0)
        draw_fractal(size / 3.0)
        tl.left(90)
        draw_fractal(size / 3.0)
        tl.right(180)
        draw_fractal(size / 3.0)
        tl.left(90)
        draw_fractal(size / 3.0)
    else:
        tl.forward(size)
        
size = 800

tl.hideturtle()
tl.speed(0)
tl.delay(0)
tl.pensize(1)
tl.penup()
tl.goto(-size/2, -size/4)
tl.pendown()

draw_fractal(size)
tl.done()