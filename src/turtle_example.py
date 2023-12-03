import elkplot

w, h = elkplot.sizes.LETTER

# the turtle starts at (0, 0) facing right
gamera = elkplot.Turtle(use_degrees=True)

# draw the left eye
gamera.turn_right(90)
gamera.forward(2)
gamera.raise_pen()

# draw the right eye
gamera.goto(2, 0)
gamera.lower_pen()
gamera.forward(2)
gamera.raise_pen()

# draw the mouth
gamera.goto(-1.5, 2.5)
gamera.lower_pen()
gamera.turn_left(45)
gamera.forward(1.5)
gamera.turn_left(45)
gamera.forward(3)
gamera.turn_left(45)
gamera.forward(1.5)

# render the drawing, center it on a letter size sheet, and draw
d = gamera.drawing() 
d = elkplot.center(d, w, h)
elkplot.draw(d, w, h, plot=True)