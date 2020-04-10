# Lesson #2

So now we've (hopefully) completed all the installations for Unity and Unity assets, but just in case, make sure that you have the following

- Unity Hub (optional)
- Unity (2018.3+)
- "3D Beginner: Tutorial Resources" pack from the Asset Store

If you have trouble finding any of these, there is more information in Lesson 1.

Now we can start with animating the player model! From your assets window, go to the __Assets > Models > Characters__ folder and drag __JohnLemon__ into the Hierarchy Window and press 'F' to focus onto him. John Lemon already has some pre-established components within, which you can expand in the hierarchy window.

## Prefabs

To save us some pain later, we're going to turn JohnLemon into a __Prefab__ which is basically an instance of JohnLemon we can reuse in later levels.

To turn JohnLemon into a prefab, drag him from the Hierarchy window into __Assets > Prefabs__ and select __Original Prefab__ on the popup.

## Animation

In Unity, it's most intuitive to animate GameObjects with an __Animator Controller__. We'll place ours in the __Assets > Animation > Animators__ folder for easy access but you can place it anywhere. Now, right click and press __Create > Animator Controller__.

We have 2 animations for JohnLemon, one for when he's walking, and one for when he's idle. To control which one happens when, we're going to create a __bool__ parameter and name is __IsWalking__, you'll notice that there is a checkbox next to our created variable. We don't want John Lemon to immediately start walking at the beginning of the game, so it should be disabled.

Now go into __Assets > Animation > Animation__ to find our animations for John Lemon which will be named __John@Idle__ and __John@Walk__. The assets themselves are GameObjects, not animations, so we must expand their children and find the actual animations we want to use in our Animation Controller, which are named __Idle__ and __Walk__ respectively. Drag them into our Animator Controller so we can use them.

Now, in the Controller window, right click __Idle__ and select __Make Transition__ and then click on __Walk__. Do the same for __Walk__ to __Idle.__ Now we must edit these transitions to make them work properly. Click the transition line from __Idle__ to __Walk__ to edit it in the inspector. Disable the __Has Exit Time__ checkbox since we don't want a state change if the player hasn't explicitly changed states. However, we still need a way to transition the states, which is what a __Condition__ is. Add a condition to the empty list, and what we want is to transition when __IsWalking__ is true.
Similarly for the __Walk__ to __Idle__ transition, we need to disable the __Has Exit Time__ checkbox and add a condition but for when __IsWalking__ is __false__.

That's it for our animation of John Lemon! Add our Animator Controller by dragging it from __Assets > Animation > Animators__ to the JohnLemon GameObject in the hierarchy window.

## Physics

Now let's add some good ol' physics to John Lemon to make sure nothing weird happens like falling through the floor. In our JohnLemon prefab, we have two already set components: __Transform__ and __Animator__. We need to add two more: __Rigidbody__ and __Collider__. (Make sure you don't choose Rigidbody 2D, as our game works in 3D!). So now we theoretically should have a JohnLemon that reacts to gravity, but you'll see that it doesn't quite work as we want it to if you click Play.

To fix our problem, we have to disable __Apply Root Motion__ in the Animator component of our prefab. In the drop-down for __Update mode__ inside the Animator component, select __Animate Physics__ so that JohnLemon adheres to the rules of physics. Then, we need to fix up the vertical root motion as well by restricting his vertical movement with __Rigidbody > Constraints__. In the drop down, you can see options to freeze position and rotation for any of the x, y, or z coordinates. Since we don't want John Lemon to be moving up and down in our game, check the __Freeze Position__ checkbox for the __y__ coordinate. But we also don't want to be able to rotate in the x or the z direction, so we must __Freeze Rotation__ for the __x__ and __z__ coordinates.

Our final step is to add a __Collider__ so that something happens when John Lemon runs into another object in the environment. We can do so by adding another component to our John Lemon object called the __Capsule Collider__ (make sure you don't select the 2D option again). When we add this collider, Unity automatically sets the bounds but we want to customize them to fit our player model. so set __Height__ to __1.4__, __Center__ to __(0, 0.7, 0)__, and __Radius__ to __0.4__. In the scene window, you should see that the collider fits John Lemon quite well!
