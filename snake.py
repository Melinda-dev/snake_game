from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __int__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in range(3):
            self.add_segment(position)


    def add_segment(self,position):
        segment = Turtle()
        segment.shape("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        self.segments[0].setheading(UP)

    def down(self):
        self.segments[0].setheading(DOWN)

    def left(self):
        self.segments[0].setheading(LEFT)

    def right(self):
        self.segments[0].setheading(RIGHT)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)










