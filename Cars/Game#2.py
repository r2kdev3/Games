import turtle as t
import os

dirPath = os.path.dirname(os.path.abspath(__file__)) 
image_left = dirPath + "/car_left.gif"
image_right = dirPath + "/car_right.gif"
image_up = dirPath + "/car_up.gif"
image_down = dirPath + "/car_down.gif"
t.Screen().register_shape(image_left)
t.Screen().register_shape(image_right)
t.Screen().register_shape(image_up)
t.Screen().register_shape(image_down)
distance=10
shape = t.Turtle()
shape.shape(image_left)

def up():
    shape.shape(image_up)
    shape.setheading(90)
    shape.forward(distance)

def down():
    shape.shape(image_down)
    shape.setheading(270)
    shape.forward(distance)

def left():
    shape.shape(image_left)
    shape.setheading(180)
    shape.forward(distance)

def right():
    shape.shape(image_right)
    shape.setheading(0)
    shape.forward(distance)

t.setup(500, 500)
t.Screen().bgcolor("sky blue")
t.color("green")
t.turtlesize(3, 3, 2)
t.listen()

t.onkey(up,"Up")
t.onkey(down,"Down")
t.onkey(left,"Left")
t.onkey(right,"Right")
t.mainloop()
