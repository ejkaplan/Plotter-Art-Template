import elkplot

def main():# the turtle starts at (0, 0) facing right
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

    # render the drawing
    d = gamera.drawing()
    width, height, margin = 11, 8.5, 1

    # make the drawing as big as possible while still fitting on a letter size
    # page with a one inch border
    d = elkplot.scale_to_fit(d, width, height, margin)

    # Uncomment the line below to rearrange the lines to minimize pen-up travel distance
    # d = elkplot.optimize(d)

    # Draw the picture. You can change the dpi to change the size of the preview window
    # Change the plot argument to True if you want to actually run it on an axidraw
    elkplot.draw(d, width, height, plot=False, preview_dpi=50)


if __name__ == "__main__":
    main()
