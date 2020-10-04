import turtle as t

def up():
    t.setheading(90)
    t.forward(20)

def down():
    t.setheading(270)
    t.forward(20)

def left():
    t.setheading(180)
    t.forward(20)

def right():
    t.setheading(0)
    t.forward(20)

t.shape('turtle')
t.setup(1000, 1000)
t.Screen().bgcolor("sky blue")
t.color("dark green")
t.turtlesize(3, 3, 2)
t.listen()
t.onkey(up, "Up")
t.onkey(down, "Down")
t.onkey(left, "Left")
t.onkey(right, "Right")
t.mainloop()