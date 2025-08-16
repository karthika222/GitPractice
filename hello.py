'''import turtle

print("hello")

turtle.circle(45)   # turn left 45 degrees
#turtle.forward(100)  # move forward 100 pixels
turtle.triangle(30)

turtle.done()  # keep the window open'''
import turtle

print("hello")

# Draw a triangle with side length 100
for _ in range(3):
    turtle.forward(100)
    turtle.right(120)  # turn left 120° to make a triangle

turtle.done()  # keep the window open

