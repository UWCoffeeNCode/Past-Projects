# Meet-Up #2 Agenda:

**Objective**: join the slack, get your Arduinos, and create a basic button and LED program.

## 1. Setup
* [Make sure you have the Arduino IDE.](https://www.arduino.cc/en/Main/Software)
* Join the Slack! (Contact a club executive about joining).
* Check out Arduino example code [on their site.](https://www.arduino.cc/en/Tutorial/BuiltInExamples)
* [Millis() information](https://www.arduino.cc/reference/en/language/functions/time/millis/) (for challenge 1).

## 2. Here is your Arduino!
![Arduino board](http://www.robocircuits.com/wp-content/uploads/2018/02/042014_1355_ArduinoGett1.png)

## 3. Coding
**Challenge 1:**
Using 1 push button and Millis(), create a program that will turn on an LED if 4 button is presses exactly are spaced exactly 1 second apart. In other words press the button at 60 bpm for 4 seconds.

**Challenge 2:**
Using multiple push buttons, create a program that will turn on an LED only if the push buttons are pressed in the correct order. You get to decide the order.

*Solution 1*

```c++
const int buttonPin = 2;     // the number of the pushbutton pin
const int ledPin =  12;      // the number of the LED pin

int buttonState = 0;         // variable for reading the pushbutton status
int timeOfPress = 0;         // variable to keep track of when the button was pressed.
int differenceOfPresses = 0; // the time between two presses
int score = 0;               // how many presses has the users gotten with 1 second in a row.
bool pressed = false; // Used so you only read the buttonState once per push

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
  // Turn off LED
  digitalWrite(ledPin, LOW);
  // Setup serial monitor
  Serial.begin(9600);
}

void loop() {
  // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

  // if the buttonState is true and the button was not previously being pressed.
  if (buttonState == HIGH && pressed == false) {
    // Save the time between this button press and the previous button press.
    differenceOfPresses = millis () - timeOfPress;
    // Save the current time as the new previous button press.
    timeOfPress = millis ();
    // If your press is within .2 seconds of 1 second then it counts towards your score.
    if (differenceOfPresses < 1200 && differenceOfPresses > 800)
      score++;
    // If your press is off then reset the score
    else
      score = 0;
    // You are now pressing the button.
    pressed = true;
    // Debuging output
    Serial.print("Difference: ");
    Serial.println(differenceOfPresses);
  }

  // If the buttonState is false, and the button was just being pressed then that means the button is no longer being pressed.
  if (buttonState == LOW && pressed == true){
    pressed = false;
  }

  // If you get 3 presses after the initial press
  // in a row the LED will turn on
  if (score >= 3) {
    digitalWrite(ledPin, HIGH);
  }
}
```

*Solution 2*

The setup for this solution was 3 buttons placed in a row horizontally. The code was left, right, middle, right.
This solution also has a small problem in it. It functions fine, but it could be better. Try to find the bug!
```c++
const int leftButtonPin = 2;     // the number of the left pushbutton pin
const int rightButtonPin = 3;     // the number of the middle pushbutton pin
const int middleButtonPin = 4;     // the number of the right pushbutton pin
const int ledPin =  12;      // the number of the LED pin

int leftButtonState = 0;         // variable for reading the pushbutton status
int middleButtonState = 0;
int rightButtonState = 0;

int input[4];
// The correct order of pressing
const int answer[4] = {2,4,3,4};
// Counts the current press
int counter;
bool solved = false;
bool pressed = false; // Used so you only read the buttonState once per push

void setup() {
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  // initialize the pushbutton pin as an input:
  pinMode(leftButtonPin, INPUT);
  pinMode(middleButtonPin, INPUT);
  pinMode(rightButtonPin, INPUT);
  // Turn off LED
  digitalWrite(ledPin, LOW);
  // Setup serial monitor
  Serial.begin(9600);
}

void loop() {
  // read the state of the pushbutton value:
  leftButtonState = digitalRead(leftButtonPin);
  middleButtonState = digitalRead(middleButtonPin);
  rightButtonState = digitalRead(rightButtonPin);

  // Check left button
  if (leftButtonState == HIGH && pressed == false) {
    input[counter] = leftButtonPin;
    pressed = true;
    // Debuging output
    Serial.print("Pin: ");
    Serial.println(input[counter]);
    counter ++;
  }
  // Check middle button
  else if (middleButtonState == HIGH  && pressed == false) {
    input[counter] = middleButtonPin;
    pressed = true;
    // Debuging output
    Serial.print("Pin: ");
    Serial.println(input[counter]);
    counter ++;
  }
  // Check right button
  else if (rightButtonState == HIGH  && pressed == false) {
    input[counter] = rightButtonPin;
    pressed = true;
    // Debuging output
    Serial.print("Pin: ");
    Serial.println(input[counter]);
    counter ++;
  }

  if ((leftButtonState == LOW && middleButtonState == LOW && rightButtonState == LOW)&& pressed == true){
    pressed = false;
  }

  // Check if solved
  solved = true;
  for (int i = 0; i < 4; i++){
    if (input[i] != answer[i])
      solved = false;
  }

  if (solved)
    digitalWrite(ledPin, HIGH);
  else
    digitalWrite(ledPin, LOW);

 // Reset counter if over 4 presses
  if (counter == 4)
    counter = 0;
}
```

## 4. Optional Homework
* Check out this [advanced Arduino coding tutorial](https://www.youtube.com/watch?v=ZARTUnVUYT0&list=PLwnMi_b_qu7sfMQcoN8u7fiYEr1-vZYn_&index=9)
