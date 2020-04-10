# Unity Scripting Reference 
## Logical Operators 
**&&** is a logical **and** operator. It returns true if both sides of the operater evaluates to true, otherwise false. 

**||** is a logical **or** operator. It compares the boolean value on both sides and if either of them are true then it equates to true, otherwise it equates to false. 

**==** is a **equality** operator. If both operands have the same value, it returns true, otherwise false. 

**!** is a logical **negation** operator. It invert/s boolean values: setting true to false and false to true. 

## Classes / Methods / Constructors 
**Application.Quit();** 

Shut down the running application. 


**CanvasGroup** 

Canvas Group can be used to control certain aspects of a whole group of UI elements from one place without needing to handle them each individually. The properties of the Canvas Group affects the GameObject it is on as well as all children. 
- CanvasGroup_Name.alpha 
Alpha is a property of Canvas Group. It determines the opacity of the UI elements in the group CanvasGroup_Name. The value is between 0 and 1, where 0 is fully transparent and 1 is fully opaque.


**GetComponent<>();** 

Return the component of Type <type> if the game object has one attached, null if it doesn't. 


**Input** 

Input class reads the axes set up in the Input Manager. 
- Input.GetAxis("Horizontal"); and Input.GetAxis("Vertical"); 
Input.GetAxis returns the value of the virtual axis identified by axisName. 


**Mathf.Approximately(float1, float2);** 

Approximately is a method from Mathf class. It takes two float parameters and returns a bool value - true if the two floats are approximately equal and false otherwise. 


**Normalize();** 

Normalizing a vector means keeping the vector's direction the same, but changing its magnitude to 1. 


**OnTriggerEnter(Collider other);** 

OnTriggerEnter happens on the FixedUpdate function when two GameObjects collide. 


**OnTriggerExit(Collider other);** 

OnTriggerExit is called when the (Collider other) has stopped touching the trigger. 


**Quaternion** 

Quaternion is a structure that represents/stores rotation. 


**Set();**

Set method assigns a value to your variable. 


**Time.deltaTime** 

Provides the time between the current and previous frame. 


**Vector3** 

Vector3 is a structure that stores 3D positions and directions. It is structured with given x, y, z components where x represent x component of the vector, y for y component, and z for z component of the vector. 


You can learn more about Unity Scripting here: https://docs.unity3d.com/ScriptReference/ 
