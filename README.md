# python-project
Project for Core Training

1. Overview

This mini-project is used to calculate the area of various 2-D Shapes

The program will ask the user to identify which shape they wish to calculate the area for,
should the user input an invalid command it will ask the user again to enter a valid command,
esc is the command used to escape the program.

If a user inputs a shape e.g. square, the program will ask them for the appropriate measurements,
in this case the program would ask for the length of the height and the base of the square. Upon
entering in these measurements, the program will calculate the area of the shape. A counter was also
implemented to keep track of how many calculations for area were performed during the session. The user
can keep calculating different shapes until they type esc command to escape the program. Upon exiting the program
the display counter for how many areas that were calculated is shown, along with a goodbye message.

2. Required Features

if elif and else functions were used to determine what a user has input, if a user has input square, this would then enter
the block of code reserved for entering square values, and for calculating the area of a square.

A menu of options was provided for the user to input i.e. square, circle etc. One of these options was esc which allowed the
user to exit the program. These options were contained within a while loop that would repeatedly ask the user the question,
until they typed esc.

A counter was used which was updated every time an area calculation was done, this was then printed upon
exiting the program.

3. Future Improvements

In order to enhance the program, more error checking is needed for the calculation of area section. This would prevent
users from entering in invalid negative numbers, or typing in non-numbers. In order to prevent this a try and catch clause
could be potentially used to deal with errors.


