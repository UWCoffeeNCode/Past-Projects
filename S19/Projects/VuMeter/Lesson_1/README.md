# Lesson 1: Meeting Arduino

In this lesson we'll be introducing the basics of arduino programming and give a rough outline for what this project entails.

## What is a Vu-Meter?
A vu-meter or a volume unit meter is a device that is used to display the amplitude of a signal.
Generally it is used to measure audio, but in theory you could use use a vu-meter to measure any kind of signal.

At a high level, to make a vu-meter we just need two components: a way to measure the amplitude of a signal, and a way to display said amplitude. 
Or in other words, we need to measure an input and display an output.
We can do this by using a microphone and by flashing some lights (though there are an infinite number of ways to accomplish the task).

## What is an Arduino?
An Arduino is a microprocessor prototyping platform.
On the board we have access to a microprocessor (a computer) and associated components and terminals.
The processor is weak by today's standards: it works on 8bit at 16MHz with 2kB of RAM and 32kB of storage.
But as it turns out, this is more than enough to get lots of things done.
People have programmed robots, automatic locks, simple drones, automatic plant waterers, and many many more.

To use an Arduino, we'll have to learn to program it.
The people who make Arduino have desgined a subset of C\C++ that is easy to use.
They've even designed an integrated development environment (IDE) to make writing and exporting code super easy.

### Downloading Arduino IDE
* [Arduino IDE](https://www.arduino.cc/en/Main/Software)

OPTIONAL (If there are no physical Arduino boards)
* [Arduino Simulator for Web](https://www.tinkercad.com/circuits)
**OR**
[Arduino Simulator for Windows](https://www.sites.google.com/site/unoardusim/services)

## Our First Program
Using an Arduino circuit board or Arduino Simulator create a program that will flash an LED.
Thankfully our Arduino boards have a built-in test LED so that we don't have to wire anything to start off.
Copy the following code from `void setup` until the end.


```c++
/*
  Blink

  Turns an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the UNO, MEGA and ZERO
  it is attached to digital pin 13, on MKR1000 on pin 6. LED_BUILTIN is set to
  the correct LED pin independent of which board is used.
  If you want to know what pin the on-board LED is connected to on your Arduino
  model, check the Technical Specs of your board at:
  https://www.arduino.cc/en/Main/Products

  modified 8 May 2014
  by Scott Fitzgerald
  modified 2 Sep 2016
  by Arturo Guadalupi
  modified 8 Sep 2016
  by Colby Newman

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Blink
*/

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  delay(1000);                       // wait for a second
}
```

### Analyze Code
Let's take some time to explain what every line of this program is doing.
Right off the bat we a nice big long _comment_.

#### Comments
In C/C++, and thus Arduino, we can leave comments in two different ways.
We can write a multi line comment by using `/*` to start the comment and `*/` to end the comment.
We can write anything we want between those two sets of symbols.
We can also leave a single line comment using `//` (double forward slash).
Everything after the `//` will be a comment until the end of the line.

The computer will ignore comments completely. The comments are there for our (the programmer's) benefit.
This is how we can write down our thoughts and make sure that other programmers have an easier time reading our code.
Sometimes "other programmers" means us in a week or two, so always always leave some comments!

#### The BIG Two Arduino Functions: setup and loop
In programming we have the concept of functions: blocks of code that we want to group together for ease of use, both readability and to avoid bad code (copy-pasted for example).
We will talk more about functions later, but for now we need to discuss `setup` and `loop`.

The `setup` function is only run once, at start-up, and never again. It doesn't return anything (`void`), and it doesn't take any arguments (`setup()`).
The `loop` function is executed over and over again after the `setup` function. This is the function that will do our heavy lifting most of the time. Again it doesn't return anything or take any arguments (`void loop()`).

This scheme of having a setup and loop function is an Arduino specific thing, not a C/C++ standard. In the scheme of C we can write how this works with the following code.

```c
int main(){
  setup();
  while (true){
    loop();
  }
  return 0;
}
```

#### The Other Functions
* pinMode: Each of the pins on our Arduino can be used to take in a signal or produce a signal, but we have to let the computer know what we want to use the pin for. The first argument is an `int` and the second argument is usually one of `INPUT`, `OUTPUT`.

* digitalWrite: If we have set a pin to `OUTPUT` we can use this function to produce an output. The first argument is an `int` and the second argument is a `bool` (true or false).

* delay: this function makes the processor stop and count out a number of milliseconds. The argument for this function is an `int`.

#### Tidbits
Notice the semicolons (`;`) at the end of each line of code. Each statement in C/C++ needs to end with a semicolon.
This is how the computer knows to stop reading and start "thinking" about what to do with the command you just gave.
You'll get errors if you forgot to put your semicolons.

Also notice the braces `{`, `}`. Thse are used to tell the computer where blocks of code start and end. In this example the braces are used to tell the computer where the function definitions (setup and loop here) start and end. If you define a function (or a loop, if statement, etc) and you forget a brace you'll also get an error.

Don't worry though, it's very hard to break an Arduino doing what we're doing, and code errors are going to be caught by our computers before we push the code to the Arduino!


## Optional
* Watch [this tutorial video series](https://www.youtube.com/watch?v=09zfRaLEasY&list=PLZfay8jtbyJt6gkkOgeeapCS_UrsgfuJA)
