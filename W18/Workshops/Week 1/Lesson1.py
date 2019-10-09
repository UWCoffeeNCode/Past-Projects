# We'll be using the interactive interpreter.
# In this case, it will print out anything that we give it.


# Begin with print statements. BRACKETS.
print("Hello world")
help()                  # Enters an interactive helper


# Next, variables.
x = 5       # In this case, '=' is actually like an '<-'
            # x now has the value 5 for the rest of the program.

x = 5 + 2   # Whatever is on the left side of the '=' goes to the left.

print x     # Prints 7




# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# Starting with objects.
class Car(object):

    def drive(self):
        print "Vroom vroom"

    def brake(self):
        print "SCREEECH"

    def openDoor(self, num):
        print "Opening door number %i." % num


# The brackets means we are making a new OBJECT.
# Create a new Car OBJECT.
car = Car()

# Now we make the car do things.
# '()' means we are calling something. -> running code somewhere else.
car.drive()
car.brake()

# We make the car open, but this time we pass in an ARGUMENT.
# An ARGUMENT is something we give to the code that's running somewhere else.
car.openDoor(2)
car.openDoor(3)



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# NOTES:

# - Start with goal, end with solution,
# - SAVE before RUNNING

# INSTALLATION:
# For using pip:
# - Add Python to PATH variable.
# - Use python -m pip install numpy matplotlib
# For using conda:
# - ???

# 1. Open editor.
# 2. Type print("Hello world.")
# 3. Save as "???.PY" in same folder as fractals.py
# 4. ENTER "quit()" in terminal.
# 5. python ***drag file THAT WAS WORKED ON into terminal***

# Create glossary:
# - class -> 
# - object
# - variables
# - functions
# - comments
# - indentation
# - for loops
# - "==" vs "="



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# Start with some IMPORTS.
# IMPORT -> taking code from somewhere else.
# From fractals file, get Mandelbrot CLASS so we can make Mandelbrots.
# CLASS -> like a factory which makes objects.

# In the fractals.py file, we've created the code for doing this.
# In our "???.PY"
# '=' takes a value from the right side, puts it in the container on the left.
# Every time we do something with that container, we're doing something with
# our Mandelbrot.

# Mandelbrot is the name of the type of fractal we are creating.
from fractals import Mandelbrot

# Create a new Mandelbrot OBJECT.
# '()' means we are creating a new object.
fractal1 = Mandelbrot()

# This time, '()' means we are calling something.
# We are calling 'render'.
# This is going to the FILE WE IMPORTED.
fractal1.render()



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# Import Julia now.
from fractals import Julia

# Create a new Julia OBJECT.
fractal2 = Julia()

# Make the Julia render.
fractal2.render()



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# Let's try to make some different kind of fractals.
# The function 'render' can take some 'keyword arguments'.

# *** Show defaults again. ***

#NOTE: *** COLORS not COLOURS ***
# Try to add some more colours.
# We can say 'colors=50' because the function wants 'colors' as an input.
fractal1.render(colors=50)
fractal2.render(colors=50)

# Let's change some other fields.
fractal1.render(p=1.5)
fractal2.render(p=1.5)



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# NOTE: Remove previous 'render' calls.

# Let's cycle through some different values.
# i goes from 1 -> 4, meaning:
# i = 0: run code in loop.
# i = 1: run code in loop.
# ...
# i = 4: run code in loop.
for i in range(1, 5):         
    fractal1.render(colors=i * 10)        # Make the image with 'i' colors.

# What if we want to use decimal values instead?



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# We use a for loop again, but this time divide 'i' by 10.
# i goes from 0 -> 5,
# j goes from 0 -> 0.5
for i in range(1, 5): 
    j = (i / 10.0)

    fractal2.render(p=i / 10.0 + 1)



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# What if we want the user to decide what to create?
# Let's use the 'input' function.

# Input -> ask a question, get an answer, 
# assigns to 'fractal_type'.

# NOTE: for Python 2 users, add the following line of code.
input = raw_input

# Input -> shows a message, gets typed message from user, 
# assigns to 'fractal_type'.
fractal_type = input("What kind of fractal do you want to create?")

print fractal_type

# Now we know what the user wants to do.
# If fractal_type is "Mandelbrot", create a Mandelbrot set.
# Otherwise, if fractal_type is "Julia", create a Julia set.
# Otherwise, don't do anything.



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# Note that '==' is comparison, it either returns True or False.
# COMPLETELY DIFFERENT FROM "=".
# If the user writes "Bob" for example.
# tell the user they made a mistake.
if fractal_type == "Mandelbrot":
    fractal1.render()

elif fractal_type == "Julia":
    fractal2.render()

else:
    # Otherwise, warn user.
    print "That's not a valid type of fractal."



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# Let's give the user control of the other controls from before too.

colors = input("How many colours?")

# Note that 'input' returns a STRING.
# STRING - a combination of letters, numbers, spaces.
# We want to give our function a number (in this case, integer).

# The int FUNCTION (technically a constructor) converts the STRING you give it
# into an int.
# TELLING COMPUTER 'colors' is a number.
colors = int(colors)



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# Let's add this back to our program.

if fractal_type == "Mandelbrot":
    colors = input("How many colours?")
    colors = int(colors)
    fractal1 = Mandelbrot()
    fractal1.render(colors=colors)

elif fractal_type == "Julia":
    colors = input("How many colours?")
    colors = int(colors)
    fractal2 = Julia()
    fractal2.render(colors=colors)

else:
    print "That's not a valid type of fractal."



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# Let's add another control.

fractal_type = input("What kind of fractal do you want to create?")

if fractal_type == "Mandelbrot":
    str_colors = input("How many colours?")
    num_colors = int(string_colors)
    str_p = input("Enter a number between 0 and 2.")
    num_p = float(str_p)       # -> Float just means decimal number.
    fractal1 = Mandelbrot()
    fractal1.render(colors=number_colors, p=num_p)

elif fractal_type == "Julia":
    str_colors = input("How many colours?")
    num_colors = int(string_colors)
    str_p = input("Enter a number between 0 and 2.")
    num_p = float(str_p)
    fractal2 = Julia()
    fractal2.render(colors=number_colors, p=num_p)

else:
    print "That's not a valid type of fractal."

# We have a lot of redundant code. Let's fix this.



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# Let's make a FUNCTION.
# A function is a group of code that we can run at any time.
# It sometimes returns a value.
def get_colors():
    str_colors = input("How many colours?")
    num_colors = int(string_colors)

    # RETURN - means this is the value the function gives after finishing.
    return number_colors


def get_p():
    str_p = input("Enter a number between 0 and 2.")
    num_p = float(str_p)

    return num_p



fractal_type = input("What kind of fractal do you want to create?")

if fractal_type == "Mandelbrot":
    colors = get_colors()
    p = get_p()
    fractal1 = Mandelbrot()
    fractal1.render(colors=colors, p=p)

elif fractal_type == "Julia":
    colors = get_colors()
    p = get_p()
    fractal2 = Julia()
    fractal2.render(colors=colors, p=p)

else:
    print "That's not a valid type of fractal."



# {{{ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# }}}

# Some more contorls to mess around with.
# - width
# - height
# MANDELBROT:
# - p
# JULIA:
# - p
# - c1
# - c2
# NEWTON (more math-based):
# - f
# - a



# What is Python? What is it used for?
# What is a terminal?
# What is a text editor? Why do we need to use it?

# Google doc for coding
# - can correct for bad syntax
# - colour coding
