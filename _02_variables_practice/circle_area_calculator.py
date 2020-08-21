import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    hrfgnrehwnjirfe = simpledialog.askinteger(None,"what is your radius in pixels")

    # Make a new turtle
    FG = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    FG.circle(  radius=hrfgnrehwnjirfe  )

    # Call the turtle .penup() method
    FG.penup()
    # Move your turtle to a new x,y position using .goto()
    FG.goto(69,34)
    # Calculate the area of your circle and store it in a variable, you can use math.pi
    area = math.pi * hrfgnrehwnjirfe *  hrfgnrehwnjirfe
    # Write the area of your circle using the turtle .write() method
    FG.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle
    FG.hideturtle()
    # Call turtle.done()

    turtle.done()
    window.mainloop()