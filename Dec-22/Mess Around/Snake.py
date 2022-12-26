import turtle
import random 

running = True

window = turtle.Screen()
window.title('Pong')
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0) # stops the game from updating

def paddle(x, y, color):
    obj = turtle.Turtle()
    def __init__(self):
        obj.self.speed(0)
        obj.self.shape('square')
        obj.self.color(color)
        obj.self.shapesize(stretch_wid=5, stretch_len=1)
        obj.self.penup()
        obj.self.goto(x, y)

paddle_a = paddle(-350, 0, "white")
paddle_b = paddle(350, 0, "white")

def main():
    while running:
        window.update()


if __name__ == "__main__":
    main()