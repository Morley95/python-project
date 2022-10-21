MY_PI = 3.142
shape_counter = 0

print("Welcome to my 2D shape calculator program!")

while True:
    user_input = str(input("Please enter if you wish to calculate area for a square, rectangle, triangle, or circle or type esc to exit!: "))
    if user_input == "square" or user_input == "rectangle":
        square_base = float(input("Please input base number: "))
        square_height = float(input("Please input height number: "))
        square_area = square_base * square_height
        shape_counter += 1
        print("Your square / rectangle area is: " + str(square_area))

    elif user_input == "triangle":
        triangle_base = float(input("Please input base number: "))
        triangle_height = float(input("Please input height: "))
        triangle_area = 0.5*(triangle_base * triangle_height)
        shape_counter += 1
        print("Your triangle area is: " + str(triangle_area))

    elif user_input == "circle":
        circle_radius = float(input("Please input radius number: "))
        circle_area = MY_PI*(circle_radius**2)
        shape_counter += 1
        print("Your circle area is: " + str(circle_area))

    elif user_input == "esc":
        break
    else:
        print("That is not a valid shape or command, please try again!")

print("Thanks for using the calculator!")
print("You calculated the area for " + str(shape_counter) + " shape(s) today, woohoo!")



