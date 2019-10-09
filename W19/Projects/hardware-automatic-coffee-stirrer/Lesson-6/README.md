# Meet-Up #6 Agenda:

**Objective**: Bonus lesson, upgrade your circuit!!

## 1. Adding Displays
This lesson is a bonus lesson that is not required for the project.
If you want to upgrade your circuit with a display we have two different types of displays you can chose from!

## 2. The Seven Segment Display
![Seven Segment Display](http://arduinolearning.com/wp-content/uploads/2015/12/ARduino-and-TM1637_bb.png)

##### Setup
- Use the above diagram for wiring
- Download [this repository](https://github.com/avishorp/TM1637/tree/77a9adc788f549d0a5786fff0c2aefd24a60b0c3) as a zip.
    - Note the linked version is the most recent known working version. Some newer version don't work.
- Install that zip as a library in the Arduino IDE.

##### Code
- The sample code can be found [on the github repo](https://github.com/avishorp/TM1637/blob/77a9adc788f549d0a5786fff0c2aefd24a60b0c3/examples/TM1637Test/TM1637Test.ino)

## 3. The 128x32 OLED Display

![OLED Display](https://cdn.instructables.com/F21/O2WO/JC0U6G3R/F21O2WOJC0U6G3R.LARGE.jpg)

##### Setup
- Follow [this guide](https://www.instructables.com/id/Tutorial-to-Interface-OLED-091inch-128x32-With-Ard/) to get setup.

##### Code
- Ensure that you are using the example code in the above tutorial.
- Note that they provide the library in a `.rar` format. You can manually install the library by...
    - unarchiving the `.rar` folder and
    - moving the `U8g2` folder into your libraries folder.
    - The libraries folder should be located in `Documents\Arduino\libraries`
