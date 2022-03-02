from turtle import *
Fred = Turtle()

Fred.color("blue")
for i in range(10):
    for i in range(2):
        Fred.forward(100)
        Fred.right(60)
        Fred.forward(100)
        Fred.right(120)
    Fred.right(36)
done()