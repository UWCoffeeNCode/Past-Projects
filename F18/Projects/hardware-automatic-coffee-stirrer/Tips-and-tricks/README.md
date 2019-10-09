## Table of contents
#### 1. Hardware best practices
#### 2. Tips for debugging Arduino hardware

# 1. Hardware best practices
#### It is recommended that you follow these simple guidelines while work with any hardware components
1. Always remove power from your circuit before changing any connections or wires.
2. Double check your wiring before you connect power.
3. If you see smoke unplug power and find a Project Lead.
4. If any component starts to get warm or hot, unplug power and find a Project Lead.
5. Use red or light wires for higher voltages.
6. Use black or darker wires for lower voltages.

# 2. Tips for debugging Arduino hardware

Always start by looking at the least complicated component first!

## If you do not know if the **hardware** OR **software** is working.
1. Generally the hardware is less complex than the software, so it is recommended to start looking at the hardware first.
2. If the hardware is more complicated then create a simple sample program that tests the basic functionality of each hardware component.

## If you know that the **software works** but the **hardware** does not.
1. Check all the wire connections and make sure the wires are plugged into the correct pins.
2. Re-wire your circuit to isolate each component and test each one separately. *For example: if you have a button and an led in the same circuit, then remove the button from the circuit and test the led by itself first.*


## If you know that the **hardware works** but the **software** does not.
1. Use Serial.print() statements to isolate the section of code that is not working properly.

  - Here is how to get Serial.print() to work, if you have never used it:
[Arduino sampe code: ](https://www.arduino.cc/en/Serial/Print)

2. Then use Serial.print() statements to see what values your variables hold to find the problem.
