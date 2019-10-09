# Lesson 2
Last week we took a look at using the command line and also at using our first web API.
This week we want to start doing some real programming and show why this is going to be a great tool going forward.
To do so we'll go over two things:
  1. Installing Python
  2. Leverage pre-built libraries to get the weather

Let's get started!

## Introduction to Python
Python is a general purpose programming language created by Guido van Rossum.
In technical circles, Python is known as an interpreted, high-level, duck-typed, object oriented programming language, but we don't necessarily care about any of that.
We care about what we can do with Python.... That is pretty much anything!
There are obviously some disadvantages, and there are some places you can't put a Python (interpreter) in, but for the most part Python is a modern programming language that is being used more and more professionally.
As a brief example, you can use Python to do machine learning, engineering, math, automation, program motors, microcontrollers and many other things.
One of the reasons for Python being so useful is the very active community; you can easily find that most common (and niche) tasks have already been worked on.
So for the most part, if you are just getting started at programming you'll be gluing other people's code together to make your own unique solutions to problems.
As you become more experienced you can build your own libraries and solutions from scratch if you need to, or you could even use your Python knowledge to transition into other programming languages.

### Installation
Before we get ahead of ourselves we need to install Python.
This process can be a bit different for different operating systems, but once we get that done, the commands will be the same regardless of what operating system you're using.
There are many different ways to install Python (Anaconda, miniconda, [python.org](https://www.python.org), etc).
The way I'm showing you here is meant to be educational, but also straightforward.
That is to say you might find easier ways online, but I don't think they will necessarily allow you to understand what is happening inside of your own computer.
Rule number 1 of reading someone telling you to install things from the internet: Understand every step that you're being asked to do!
In this case that means ask questions, google things, and most importantly *read all the instructions* before doing anything.

#### Windows
Installing Python on Windows is going to be a multi-step process.
None of these steps are hard, but they can seem a bit opaque.
I'll be doing my best to explain everything as we go along so that it is a clear as possible.

1. We'll go to the official Python [website](https://www.python.org) and download the latest version of Python (3.7.2 as of writing) from the Downloads dropdown.
This is just as straightforward as it sounds.
Click link, say yes, make some tea, boom you're done.

2. Run the executable you just downloaded, and make sure you understand all the options you're agreeing to.
Again not difficult.
You'll be asked *where* (you'll need this for later) you want to put Python, probably whether to make shortcuts or not, and some other things.
I recommend trying to keep everything as default as possible, since that will give you the best chance of finding other people online with the same kind of installation as you.
The only non-standard thing that Python will ask you is if you want to change the Windows character limit. 
This has to do with an old-school DOS limit on the length of file names.
Modern Windows doesn't suffer from this limit, but it is enabled as default for backwards compatability.
It's up to you if you care about this limit or not, I've personally never run into it, but I don't program on Windows often.

3. Check to see if Python is working by opening up PowerShell and typing `python`. 
If it works you'll see version information being printed on to your screen and the `>>` prompt waiting for you to type.
If you see that type `exit()` to get out and try the following command `pip -V`.
If you see pip's version number then you're good to go.
The more likely scenario is that one of these two did not work.
Check out step 4.

4. We need to add Python's directory to Window's environment variables.
At this point, you're probably wondering what is an environment variable.
Your command line terminal (powershell or command prompt [or terminal for you mac/linux people reading Windows instructions]) is actually a fully capable interpreter for another kind of programming language.
We won't really be getting into that for these lessons, but it useful to know if you ever find yourself being a sysadmin for a system.
In any case, environment variables are bits of memory that are encoding information about the current state of your computer.
For example, are you using Windows 10 or 8.1? Or which time-zone are you in? What is your preferred web browser? or in our case, if given a command, where should I look to try and execute that command?
We will be adding Python's directory to the PATH environment variable.
PATH is just a list of folders that Windows will look through if it ever doesn't know what to do with a command you give it.

Okay so let's add Python to the PATH.
You need to find `System Properties` and click on the `Advanced` tab.
I've found that on Windows 10 you can just search for `Environment Variable` and you'll have an option that takes you straight to the `System Properties` window.
On the bottom right you'll see the `Environment Variables` option; click it.
Now select the PATH and click edit.
We'll want to add the path to where Python is located.
This is the part where you pull out the path from Step 2 that you were supposed to remember.
If you didn't change any of the default settings then it will be under `C:\Python37` or `C:\Users\<username>\AppData\Local\Programs\Python\Python37-*`, but *confirm this* by checking those directories.
Now just approve all changes and close these windows.
You'll probably need to restart powershell before the changes take effect.

You should be all ready to go.
I recommend playing around in `IDLE` for a bit.

#### Mac
The instructions are a bit simpler for Mac, but you'll be dealing with some pretty deep stuff.
On MacOS, you actually already have Python installed, but it happens to be legacy Python.
What's more, if we're not careful we might mess with that Python interpreter and break your computer.
So our goal is to install Python, while at the same time leaving your built-in Python interpreter intact.
Thankfully you're not the first nor the last person that wants to turn a Mac into an actual programming machine.

To do so we'll be using [Homebrew](https://brew.sh/), which is a very robust, third-party tool used to set up all kinds of programming and development tools on Macs.
After we get homebrew installed, we'll use it to install Python.
Homebrew is programmed to leave the built-in Python (also called system Python) alone, and it will set up our environment variables for us as well.
In the future if you decide to get into more complicated projects, be it with Python or other tools, homebrew will let you install those tools as well.

1. Before we can get homebrew, we'll need to install xcode, Apple development envirionment.
We can do so by running `xcode-select --install` on your terminal.
This will download and install the command line xcode tools.
If you want, you could also download the entiriety of xcode, but that isn't necessary.

2. Next you'll want to run `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` in your terminal.
Hopefully you didn't just copy and paste this random line into your terminal before reading the rest of this paragraph. (Remember rule number 1!)
Anyways, this line is telling your computer to use Ruby, another programming language, to run some the code that it will be _downloading_ from GitHub (an online code hosting website).
Read that again: our computer will download whatever is the target of the `curl` command, and then _immediately_ start executing it with a completely fully featured programming language.
This is why it is imperative that we understand what we are running when we get code from the Internet; the easiest way to install a virus is to get the victim to do it themselves!
With that lesson out of the way, the homebrew installler will ask you some set-up options.
It will do it's best to be safe and informative, but if something doe not make sense you should look it up before making a decision.
After it is done you can see if there are any warnings or errors by running `brew doctor` in your terminal.

3. Now that we have homebrew installed we can ask it to install Python for us.
Run `brew install python` in your terminal, it should be fairly straightforward.
You might need to open a new terminal to get the changes, but you should be able to use the commnad `python` to open the interpreter (you'll see some version information and the `>>` prompt) or `pip3 -V` to see pip's version information.

4. Now you'll want to run `brew linkapps` to finish the process and tell homebrew to link any apps it installed to the rest of the system environment. If you don't do this it will be a bit harder (but not impossible to find IDLE).

You should be ready to go.
I recommend playing around in `IDLE` for a bit.

### Getting Started

For the rest of these lessons I'll assume that you'll be doing your programming inside IDLE or another suitable programming text editor.
A programming text editor is one that will do _syntax_ highlighting.
Syntax are going to be the special words, phrases or structures that our programming languge requires.
You can totally write code in notepad, or Word, or Google Docs, but you'll quickly find it tedious.
If you're looking for other editor recommendations, I usually recommend lightweight editors to beginners (Atom, Sublime, Notepad++), and recommend that for now you stay away from some of the really cool but also more complicated tools like PyCharm, Spyder, or VisualStudio.
These more advanced tools are totally worth it, but if you've never programmed before they introduce too much, too quickly.

For now let's open up IDLE (should be searchable with your OS's preferred search option).
You should see a white screen with a `>>>` waiting for you.
This is what we call a REPL: Read-Evaluate-Print-Loop.
You can type something in, and Python will read it, evaluate the expression, print the result and get ready to do it all over again. 
Let's try some simple math:

```python
>>> 2+2
4
>>> 2*2
4
>>> 5 ** 2
25
>>> 10/3
3.333333333333
```

As you can see we just installed a very complicated calculator!
The important part here is that _we_ aren't doing the math, the computer is.
We can do a lot more than math.
For the moment I'll try to cram in a quick overview of the basic data types in Python, and some useful programming constructs.
You'll see me using `#` to leave comments in the code. 
Anything that appears after a # in a line is ignored by Python.

#### Variables
It's not any good if you can do math or any operations if you can't _store_ the results somewhere you can use them again later.
That is what variables are for!

```python
>>> a = 3
>>> b = 4
>>> a+b # But we lose the value of the result!
7
>>> c = a + b
>>> c  # Now anytime we say c, we'll get the 7!
7
>>> c = 4 # But we don't have to be afraid of changing it!
>>> c
4
>>> my_crazy_variable_name = 3.14 # Our variables are not limited to single letters, though there are some restrictions
>>> cat, dog = 2.71, 1.68 # we can even assign multiple variables at a time by using commas
```

#### Lists and Tuples
Okay so we can make variables, but what if we need to store sequential data, or we just want to list out more than one piece of data at a time?
That is where lists and tuples come in!
Lists are _mutable_ containers of arbitrary objects.
That means that you can put anything you want in a list, and you can change your mind later.
Tuples are _immutable_ containers of arbitrary objects.
You can put anything you want, but after you put it in, you can't take away or add elements.

```python
>>> [0, 3, 'a string'] # We make lists with square brackets
[0, 3, 'a string']
>>> (-9, 'another string', 'a third one!') # We make tuples with parentheses
(-9, 'another string', 'a third one!')
>>> my_list = ['name', 'age', 'program'] # We can assign lists or tuples to variables just like any other object
>>> my_list[0] # We can index into our list (or tuple) with square brackets. Counting starts at 0!
name
>>> my_list[0:2] # We can slice, index more than one element, with colon. The first number is inclusive, the second number is exclusive.
['name', 'age']
>>> my_list + ['another list', 'wow!'] # We can add lists together to concatenate them. This will return a new list
['name', 'age', 'program', 'another list', 'wow']
>>> my_list.append('another element') # We can also add to a list by appending to it. This will change the list in-place
>>> my_list
['name', 'age', 'program', 'another element']
>>> my_list.pop() # We can also remove elements from the list. Pop will return the last element
'another element'
>>> my_list
['name', 'age', 'program']
>>> that_var = my_list.pop(0) # We can also pop the first (zeroth) element, or anything in between, and catch it
>>> that_var
name
>>> my_list
['age', 'program']
```

There is a lot more that you can do with lists and tuples.
You can try turning any object into a list by calling `list(an_object)` on it, though it won't always work.
You should also avoid using the variable `list` or `tuple` since those are special words in the language.
You can see more documentation [here](https://docs.python.org/3.7/tutorial/datastructures.html), though it's not all of it!

#### Numbers
As far as numbers are concerned, we won't worry too much.
We can do that because Python handles a lot of number issues really easily.
There are a few number types, but I just want to draw the distinction between `int` and `float`.
In Python, if there is no decimal component, the number will be an integer or `int`.
If there is a decimal component, or there was a decimal component at any point in the history of that object, it will be a floating point precision number or `float`.

If you're ever not sure what the type of something is, you can always use `type` to figure it out.

```python
>>> a=3
>>> type(a)
int
>>> b = 3.14
>>> type(b)
float
>>> c = a+b
>>> type(c)
float
>>> b = 2
>>> type(a/b) # the result is 1.5
float
```

#### Strings (characters and text)
Strings we will care about quite a bit, since they represent text in our programming language.
Strings are _immutable_ that means that after you make one, you can't change it.
You can however, combine it with other strings to make a _new_ string.

Most web APIs also work by communicating text to each other (usually but not necessarily in JSON format).
In modern Python there is a disctintion between byte-strings and text-strings.
A byte-string is a collection of 0's and 1's.
You'll need to know how it was encoded, to decode it.
We shouldn't have to deal with these directly.
Text strings are a lot more useful though.

```python
>>> my_string = 'I can write anything I want between these two single quotes' # We can also use double quotes "
>>> another_string = "No I'm using double quotes because otherwise I couldn't use contractions!" # We can also use triple quotes ''' or """ if we need both single and doubles in our string
>>> 'I like ' + 'apple pie!' # We can concatenate strings by adding them together. This makes a new string
I like apple pie!
>>> my_string[0:10] # We can index and slice just like we could with lists and tuples. This makes a new string
I can writ
>>> a = str(3291) # We can turn most other data types into strings by calling str on them
>>> type(a)
str
>>> surprise = 'This string can be {} later, by using curly braces a place holder'
>>> surprise.format('formatted') # Guess what? This also makes a new string
This string can be formatted later, by using curly braces a place holder
>>> surprise.format(3.141) # The format method will automatically try to turn non-strings into strings
This string can be 3.141 later, by using curly braces a place holder
```

Again a lot more documentation can be found [here](https://docs.python.org/3.7/library/string.html).

#### Loops
For the next couple of sections we'll want to use a brand new text file in IDLE to program in.
That is we don't want the REPL. We could do this in the REPL but it will be easier wihout.
You can click on File in IDLE and make a new file.
Make sure that when you save it you do so with a `.py` extension.

Now that we know about a few basic data types, we can really start to leverage our computers' power by using loops.
Loops are instructions that we want our computers to run multiple times in a row, usually with slightly different parameters.
The _syntax_ for loops in Python is quite simple.
For now we'll cover only the for-loop, but be aware that a while-loop also exists.

```python
# In our brand new file we'll type a simple loop

# range is a built-in function that will give us an object to iterate over
for i in range(10):
    # In every loop iteration, i will take on a different value
    # First 0, then 1, then 2 and so on
    # Unlike the REPL, we need to remember to print results if we want to see them
    print(i)
```

Remember that you don't have to copy any of the lines with a # in them.
It is very important to use consistent _white space_ in Python.
The standard amount of space to leave for the body of the for-loop is 4 spaces.
Notice as well how easily the syntax flows in English: for this variable i inside this object: do the following.
If you run this (with F5) you should see the computer print out the number from 0 to 9.

Let's try another for-loop
```python
my_string = 'This is a very unimaginative string'
for letter in my_string:
    print(letter)
```
Can you guess what that will do, before running it?

How about the following:
```python
for city in ['Montreal', 'Toronto', 'Calgary', 'Vancouver']:
    tmp = city[::-1] # Might be a bit hard, but I believe in your google-fu
    print(tmp.upper())
```

Now, let's show a bit of the power of being able to use for-loops.
Your math teacher is annoyed with you and tells you to figure out what is the sum of all natural numbers under 100.
They think that this will keep you busy for awhile.
Instead you write the following:

```python
a = 0
for i in range(100):
    a = a + i

print(a)
```

Which only took you a couple of seconds.
Your teacher more annoyed, asks you to compute the sum of all natural numbers under 1000...

```python
a = 0
for i in range(1000):
    a = a + i

print(a)
```

Then a million...
```python
a = 0
for i in range(1000000):
    a = a + i

print(a)
```

Python allows us to use our knowledge to tell the computer to do things that are boring, and tedious, but also very useful!

#### Functions
One of the most important core principle of software engineering is Don't Repeat Yourself (DRY).
What this means is that, whenever possible you should write code that can be re-used, and make it accessible for other programs to use.
Functions are a way of adressing this issue.
A function is a series of commands, just like the ones we've been using already, that be triggered on command by just invoking it's name.
Perhaps more importantly, we can pass _arguments_ to the function so that it can act on different objects or perform slightly different tasks.

Imagine that we're asked to calculate the area of a square.
We know that we'll probably need to know the areas of many squares, so we should strive to write code so that we don't have to repeat ourselves.
Let's say we get our first four square lengths: 1.68, 2.71, 3.14, 6.28

One way of doing this would be the following:
```python
print(1.68*1.68)

print(2.71*2.71)

print(3.14*3.14)

print(6.28*6.28)
```

But we know this is _bad_. So bad.
Let's make a function that can do this task instead.

```python
def square_area(length):
    return length*length

all_lengths = [1.68, 2.71, 3.14, 6.28]
for length in all_lengths:
    area = square_area(length)
    print(area)
```

Let's take a look at the function syntax.
First we let python know that we want to declare a function by using the `def` keyword.
We then follow that with the name of the function.
Parentheses are used to enclose the function arguments, which need to be comma separated; if we don't need any arguments then we can just leave the space between the parentheses empty.
We finish that line with a colon (:).
The body of the function is indented. Again, the standard Python indentation is 4 spaces.
We can do anything we want inside the function, including calling other functions!
Once we have the result we need, we can end the function and pass the value back by using the `return` keyword.
You can pass back multiple objects as well, just use a commas to separate them.

This might not look that impressive right now, but imagine if you had a list of 100 squares.
The first method would grow quickly and be difficult to manage, whereas the second method would barely change.
What if you need calculate triangular areas, or rectangle areas?

```python
def triangle_area(base, height):
    area = base*height/2
    return area

def rectangle_area(length, width):
    area = 2*trianle_area(length, width)
    return area

def square_area(length):
    area = rentangle_area(length, length)
    return area
```

Again this is just an example of how you can use functions to be DRY.
You should always be looking for opportunities to clean up your code and use functions.

More importantly we can also use other programmer's functions, which is what we're going to be doing next.

## Requests Library
We don't want to write all our code from scratch.
Plenty of people with years or decades of experience have already written and shared some of their code online to do most any task you can imagine.
Our job is to understand how to put all these pieces together to build new and exciting things.
We're going to briefly take a looks at the [requests](http://docs.python-requests.org/en/master/) Python library.
This library of functions was created by people that found that using Python's (very capable) built-in functions to handle web requests was not very nice to use.
They have spent weeks or months wrapping common tasks up into easy to use functions taht we can benefit from.
This library has been downloaded millions of times, so we know that plenty of people have found it useful.

### Installation
The Python Software Foundation (PSF) are the guys in charge of maintaining and adding new features to the language.
They also manage the Python Package Index (PyPI), which is an online repository of Python code.
Here you can find anything from Google backed open-source projects like Tensorflow, to niche scientific libraries like AstroPy, and of course Requests.
All versions of Python ship with `pip`, the Python package manager.
Pip will directly talk with the PyPI server, download and install their code on your computer!

If you we did everything right installing Python above, you should be able to run this line in your terminal to install requests.

`pip3 install requests`

You should see pip download and intall the library.
You can check that it has been installed by going into a terminal and typing `import requests`.
If you don't see an error, you're good to go.

### An Example
We're going to get kinda meta here and actually request this very lesson plan from GitHub's server.

```python
import requests

resp = requests.get('https://raw.githubusercontent.com/UWCoffeeNCode/Lessons/master/W19/Projects/SMS_Newsfeed/Lesson_2/ReadMe.md')
print(resp.status_code) # Should be 200 (ie all good!)
print(resp.text)
```

As you can see it's very easy to request a page using this library!

### Getting the Weather
Now we can put everything together to write a function that will use our OpenWeatherMap API key to request the local weather.
I recommend taking a look through this [documentation](http://docs.python-requests.org/en/master/user/quickstart/) to figure out how to pass parameters over URLs (city name, units, api_key, etc).
You can refer back to the previous lesson to refresh yourself on how to construct the URL we need to get the local weather.
You can also turn the response text (JSON) into a Python dictionary, another container type.
I encourage you to figure out how to do all of these things on your own, but if you are struggling there will be code in the next lesson that will do these.


## Conclusions
In this lesson we installed Python and learned about some of the basic data types and how to build for-loops and functions.
We learned about assigning variables, using lists, the different number types in Python, and strings.
We also learned how to install third-party libraries using pip, and made our first programatic web request using the Requests Python library.
As homework we're going to be writing a function to combine last week's lesson with this week.
Next week we will be making a Twilio account and downloading their library so we can send our first text message.

