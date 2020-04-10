# C# in Unity 

Slides: https://docs.google.com/presentation/d/19lMzDSaDBLMtV1KiyH5UL0jhzt4go0JdIr_ZspA2y3U/edit?usp=sharing

## Scripting in Unity 
To creat a script in Unity, you right click in the **Project Windows** click **Create > C# Script**. When you open a new script, first we have Unity default directives at the very top, class declaration, and special methods Start() and Updata(). 

**Classes** are a way to structure a code to wrap collection of variables and functions together, creating a template that defines the properties of an object. We say class is instantiated when it is attached to a GameObject, and we call the instance it is attached to, an 'Object'. \
**MonoBehaviour**  is a base class in Unity, from which every Unity script derives from. MonoBehaviour class can use some special methods that are pre-defined by Unity with their specific method signatures. \
**Methods** are blocks of code that contains series of statements that can be executed by calling the method. To declare a method, first we need to state the return type, in this case void (void is a return type where the method returns nothing), then the name of the method. Then we have a set of parentheses, where the **parameter** (what type of data the method takes in) goes. Since the Start method has no parameters, it's the parantheses are empty. Lastly, you have a pair of squiggly brackets where you put the block of code that gets executed when you call the method. 

## Special Methods: Start(), Update() and FixedUpdate() 
These special methods don’t need to be called from your code because Unity calls them automatically at specific times. 
**Start()** method is called as soon as the GameObject is on / starts (which is usually when the game starts). \
**Update()** method is called every frame (screen update) before something is rendered to the screen. Since some frames taking longer than other, Update() method is not called on regular timeline. \
**FixedUpdate()**  is called before the physics calculations comes in and it is called on regular time interval, so it is used when you need to apply physics (like force and torque) to your GameObject so your code can be executed in sync with the physics engine. 

## Key Points 
In C#, order of the method declarations doesn’t matter. You can call the method even if it is declared after the method you are trying to call it from. However, the order in which the method performs the operations matter.

Naming Convention: \
**camelCase** is a naming conventions where all variables start with a lowercase letter but any words after starts with an uppercase letter. It is used for variables in private properties and fields. \
**PascalCase** is when we write a variable name starting with **m_** and all words start with an uppercase letter. We use it for variables in public and protected properties and fields. 

## Variables 
Variables hold values and reference to objects.    
**Public** variables can be called from anywhere. If your variable is in public scope, you can set the value / reference of that variable in the **Inspector Window**.    
**Private** variables are variables that cannot be access anywhere other than the script it is declared in.    

## Value vs. Reference Variables 
**Value Variable** is a variable that contain a value. Some examples of value variable types are: Int that holds integer value, float that can hold decimal values, bool that stores true or false values and Structures that contain one or more variables. When value variables are changed, only the value type is changed. \
**Reference Variable** contain a memory address where the variable is stored. When reference variables are changed, all variables that contain that memory address will be affected. Some reference variable types include Array, Transform and GameObject. 

## If.. Else.. Statement 
**If... Else...** statement identifies which statement to run based on the boolean condition. The structure of an if statement starts with an if with a pair of parentheses to take in a boolean value as it’s condition. Then the code that executes when the condition is true goes into the squiggly brackets after that. Then we can either have else, to specify a block of code if the condition is false, or else if to specify a new condition to test, if the first condition is false (you can have as many ‘else if’s).    

## Loop 
**Loop** is used to execute a block of code multiple times.    

## Array 
**Arrary** is a collection of variables in the same data type. It is declared with the name of the array, and a pair of square brackets. We call the variables in the array as elements and to access these elements, we use their index in the array. Think of index as the number of elements you need to pass before reaching your element. So the first element has an index of 0 and the second element has an index of 1.   
