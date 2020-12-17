import turtle
import math

# turtle setup
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
s.tracer(0)
t.ht()


class Triangle:
    def __init__(self, depth, height, peak=None):
        self.height = height
        self.length = (self.height / math.sqrt(3)) * 2  # calculate side length using 30 60 90 triangle rules
        if peak is None:
            self.peak = (0, height / 2)  # Initialize peak for first triangle
        else:
            self.peak = peak
        self.children = []
        if depth > 0:
            peak2 = (self.peak[0] - self.length / 4, self.peak[1] - self.height / 2)
            peak3 = (self.peak[0] + self.length / 4, self.peak[1] - self.height / 2)

            self.children.append(Triangle(depth - 1, self.height / 2, self.peak))
            self.children.append(Triangle(depth - 1, self.height / 2, peak2))
            self.children.append(Triangle(depth - 1, self.height / 2, peak3))

    def draw(self):
        # if triangle has children, draw them, else draw the triangle
        if len(self.children) == 3:
            for child in self.children:
                child.draw()
        else:
            t.pu()
            t.setpos(self.peak)
            t.seth(-60)
            t.pd()
            for i in range(3):
                t.fd(self.length)
                t.rt(120)
            t.pu()


if __name__ == '__main__':
    triangle = Triangle(int(input("Recursion Depth (Recommend < 8): ")), 500)
    triangle.draw()
    s.update()
    turtle.done()
