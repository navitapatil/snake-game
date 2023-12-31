from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]   #coz one square is 20*20 so 1st square
                                                # in centre and second at -20 and 3rd at -40
                                                # caps coz these are constant and constant value variables are in caps
MOVE_DISTANCE = 20
UP = 90  #coz when snake is at up he cant go down and vice versa
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        # for changing direction of snake
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # assigning index 2-1 = 1 xcor value to new_x
            new_y = self.segments[seg_num - 1].ycor()  # assigning index 2-1 = 1 ycor value to new_y
            self.segments[seg_num].goto(new_x, new_y)  # now index 2 have to move at index 1 coordinates
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
