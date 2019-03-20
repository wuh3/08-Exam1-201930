"""
Exam 1, problem 1.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg

# -----------------------------------------------------------------------------
# TODO: 2. Right-click on the  src  folder and
#              Mark Directory as ... Sources Root,
#          if you have not already done so.
# -----------------------------------------------------------------------------


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1()


def run_test_problem1():
    """ Tests the   problem1  function. """
    print()
    print('--------------------------------------------------')
    print('Testing the  problem1  function:')
    print('  See the graphics windows that pop up.')
    print('--------------------------------------------------')

    # TWO tests on ONE window.
    title = 'Tests 1 & 2 of problem 1: '
    title += 'cyan/green fills, then black/magenta'
    window = rg.RoseWindow(450, 350, title)

    # Test 1:
    circle = rg.Circle(rg.Point(150, 50), 30)
    circle.fill_color = 'cyan'
    circle.outline_color = 'blue'
    circle.outline_thickness = 3

    rect = rg.Rectangle(rg.Point(325, 50), rg.Point(365, 150))
    rect.fill_color = 'green'
    rect.outline_color = 'black'
    rect.outline_thickness = 5

    problem1(circle, rect, 'red', 50, window)
    window.continue_on_mouse_click()

    # Test 2:
    circle = rg.Circle(rg.Point(275, 200), 40)
    circle.fill_color = 'black'
    circle.outline_color = 'red'
    circle.outline_thickness = 15

    rect = rg.Rectangle(rg.Point(40, 340), rg.Point(10, 300))
    rect.fill_color = 'magenta'
    rect.outline_color = 'green'
    rect.outline_thickness = 4

    problem1(circle, rect, 'blue', 140, window)
    window.close_on_mouse_click()

    # A third test on ANOTHER window.
    title = 'Test 3 of problem 1: purple/yellow fills'
    window = rg.RoseWindow(300, 200, title)

    # Test 3:
    circle = rg.Circle(rg.Point(50, 150), 20)
    circle.fill_color = 'purple'
    circle.outline_color = 'blue'
    circle.outline_thickness = 5

    rect = rg.Rectangle(rg.Point(100, 20), rg.Point(140, 70))
    rect.fill_color = 'yellow'
    rect.outline_color = 'grey'
    rect.outline_thickness = 10

    problem1(circle, rect, 'green', 170, window)
    window.close_on_mouse_click()


def problem1(circle, rectangle, color, length, window):
    """
    See   problem1_picture.pdf   in this project for pictures
    that may help you better understand the following specification:

    What comes in:
      -- An rg.Circle.
      -- An rg.Rectangle
      -- A string that represents a Rosegraphics color
      -- A positive integer
      -- An rg.RoseWindow.
    What goes out:  Nothing (i.e., None)
    Side effects:
      -- Draws, on the given rg.RoseWindow, in the following order:
           -- The given rg.Circle.
           -- The given rg.Rectangle
           -- An rg.Line from the center of the given rg.Circle
                to the center of the given rg.Rectangle, such that:
                -- The rg.Line has the given color
                -- The rg.Line has thickness the same as the outline thickness
                     of the given rg.Circle.  (SEE THE PICTURES.)
           -- A vertical rg.Line whose:
                -- midpoint is the midpoint of the above rg.Line,
                -- length is the given length,
                -- color is the fill color of the given rg.Circle, and
                -- thickness is the sum of the thicknesses of the given
                     rg.Circle and rg.Rectangle.  (SEE THE PICTURES.)

      Note: Attach the rg.Line AFTER attaching the rg.Circle and rg.Rectangle.
      Must render but   ** NOT close **   the window.

    Type hints:
      :type circle:    rg.Circle
      :type rectangle: rg.Rectangle
      :type color:     str
      :type window:    rg.RoseWindow
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.  SEE THE PICTURES in the PDF!
    #          Tests have been written for you (above).
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
