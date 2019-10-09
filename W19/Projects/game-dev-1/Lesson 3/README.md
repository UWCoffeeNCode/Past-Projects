# Lesson 3: Adding Player Functionality and the Boundary

## Controlling our player
*Like controlla, controlla, yeah*
-Drake

We will be adding and modifying our player controller over the course of the lesson. This class will do everything related to moving and controlling our player, but we will begin with something simple: movement.

In the first version of this script, we will be utilizing that handy Rigidbody component we added to the player GameObject to move it with physics. We will also be using some slightly advanced helper classes in the Camera class to make sure our player stays within the bounds of the window.

Create a new C# script in our *Scripts* folder and name it *PlayerController*, and program it as shown below.

A note about the `FixedUpdate()` function, it is similar to `Update()`, but it will get called at a fixed rate, instead of at the maximum framerate that a device can play the game at.

The code for the script is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour {
    public float speed;
    public float tilt;

    private Rigidbody rigidbody;

    private void Awake() {
        rigidbody = GetComponent<Rigidbody>();
    }

    private void FixedUpdate() {
        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");

        Vector3 moveVector = new Vector3(moveHorizontal, 0.0f, moveVertical);
        rigidbody.velocity = moveVector * speed;

        Vector3 playerPosition = Camera.main.WorldToScreenPoint(transform.position);

        Vector3 clampedScreenSpacePosition = new Vector3(Mathf.Clamp(playerPosition.x, 0.0f, Screen.width), Mathf.Clamp(playerPosition.y, 0.0f, Screen.height), playerPosition.z);

        Vector3 clampedWorldSpacePosition = Camera.main.ScreenToWorldPoint(clampedScreenSpacePosition);

        rigidbody.position = new Vector3(clampedWorldSpacePosition.x, 0.0f, clampedWorldSpacePosition.z);

        rigidbody.rotation = Quaternion.Euler(0, 0, rigidbody.velocity.x * -tilt);
    }
}
```

Once the script is complete, add it as a component to the player GameObject.

I used a value of **10** for the *speed* field and **4** for the *tilt* field, but feel free to use whatever you feel is fun.

## Creating Lazer Bolt Shots
What would an old-school arcade style shooter be without, well, the shooting!

We will be structuring our shooting system to create GameObjects for shots, and have them govern their own logic. This choice lets all of our scripts mind their own business and only deal with the things related to them (i.e the player controller should only be doing things related to player control, not moving each and every shot it makes).

We will be structuring our *Bolt* GameObject in a way where the art is in a separate child GameObject compared to the actual GameObject that contains the logic, so that we can re-use the work we do here later when we create enemy shots. This is a common pattern that is used everywhere in the industry, and it will also just generally save you time in production.

In the Hierarchy, create an **Empty GameObject** and rename it to *Bolt*. Then, create a **Quad** and rename it to *VFX*. Reset both the transforms of these GameObjects. Now similar to what we did with the background, rotate the Quad 90 in the *x* direction to make it face our camera.

Now head on over to the Project View and you should see a folder named *Materials*, click that folder to navigate to it. Within here there may be a material named *fx_bolt_orange*, which basically the finished version of the new material we are going to make for our bolt. We will be making this material from scratch so you may go ahead and delete it. Within the Materials folder, right click, and select the **Create** sub menu, and from within there, click **Material** to create a new material and name it *fx_bolt_orange*. Change the shader of this Material to be *Mobile/Particles/Additive*. This will allow the bolt to show up very well against our darker background.

<p align="center">
  <img src="https://i.imgur.com/5zhhpDC.jpg" width="650"/>
</p>

Next, select our material in the inspector and find the grey box to the right. This box indicates what texture is currently associated with this material. Click on the **Select** button inside the square window and you should see a window appear with all possible textures you could add to this material, so find *fx_lazer_orange.dff* and double click to select it.

<p align="center">
  <img src="https://i.imgur.com/ODukQV9.jpg" width="650"/>
</p>

Now you may drag this material onto the VFX Quad and you should see a lovely orange lazer bolt show up in our game! Select the Quad and be sure to **remove the Mesh Collider component** by clicking the little gear icon on top right of the Mesh Collider component, as we will be adding our own collider to this GameObject later. Drag the VFX Quad onto the Bolt GameObject to make it a child of the Bolt GameObject.

Now select the parent Bolt GameObject and add a Rigidbody component, and be sure to **uncheck the Use Gravity flag** so that it doenst fall through the space to nothingness. Add a **Capsule Collider** component as well. This component will allow us to detect collisions as if this object were the shape of the capsule. Change the **Direction** of the collider to be the **Z-Axis** to match the direction of our bolt, and adjust the **Radius** to be *0.03* and the **Height** to be *0.5*. Finally, make sure the **Is Trigger** flag is set, as this will allow us to programmatically react to when our collider collides with other GameObjects. Now your final Bolt GameObject shoud look something like this:

<p align="center">
  <img src="https://i.imgur.com/BuBorP8.jpg" width="650"/>
</p>

We will be adding the moving functionality of the Bolt through scripting, so make a new C# script in the *Scripts* folder and name it *Mover*.

This script will be very simple, as we will only be moving the Bolt GameObject in the forward direction forever, as that is all lazer beams tend to do!

The code for the script is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Mover : MonoBehaviour {
    public float speed;

    private Rigidbody rigidbody;

    private void Awake() {
        rigidbody = GetComponent<Rigidbody>();
    }

    private void Start() {
        rigidbody.velocity = transform.forward * speed;
    }
}
```

Once this script is complete, add it as a component to the Bolt GameObject and set the *Speed* field to **20** or roughly twice the speed of our player ship. Again feel free to set this to whatever feels best for you!

Now we will be using this Bolt a lot, so we will be turning it into a **Prefab**. Prefabs are preassigned packages of GameObjects, components, and renderers that can be associated together to be used repeatedly in an efficient way. To make the Bolt GameObject into a prefab, simply select it in the Hierarchy, and drag and drop it to the Project View into the *Prefabs* folder. Once you confirm it is in your Project View as a Prefab, you may delete it from the Hierarchy.

## Adding Player Shooting functionality

Now that our Bolts are ready, we can shoot them from our player!

Select our player GameObject and **right click the GameObject to and create an Empty GameObject**, and rename it to *Shot Spawn*.

<p align="center">
  <img src="https://i.imgur.com/3xwlyGC.jpg" width="650"/>
</p>

This will make a new empty GameObject and automatically make it a child of our player GameObject. Reset the Shot Spawn GameObject's transform, and position it slightly in front of our player. This will be where our lazer bolts emerge from when we click to shoot.

Now we will be changing our *PlayerController* script to add shooting functionality. We will be checking for an input to the shooting button every frame, and if there is an input we will be using the `Instantiate()` function to create the Bolt GameObject we stored as a prefab.

We will also be making sure that the player doesnt do this too often, to save us some performance. To do this, we will limit the time between shots.

The code for your adjusted *PlayerController* script is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour {
    public float speed;
    public float tilt;
    public GameObject shot;
    public Transform shotSpawn;
    public float fireRate;

    private Rigidbody rigidbody;
    private float nextValidFireTime;

    private void Awake() {
        rigidbody = GetComponent<Rigidbody>();
    }

    private void Update() {
        if (Input.GetButton("Fire1") && Time.time > nextValidFireTime) {
            nextValidFireTime = Time.time + fireRate;
            Instantiate(shot, shotSpawn.position, shotSpawn.rotation);
        }
    }

    private void FixedUpdate() {
        float moveHorizontal = Input.GetAxis("Horizontal");
        float moveVertical = Input.GetAxis("Vertical");

        Vector3 moveVector = new Vector3(moveHorizontal, 0.0f, moveVertical);
        rigidbody.velocity = moveVector * speed;

        Vector3 playerPosition = Camera.main.WorldToScreenPoint(transform.position);

        Vector3 clampedScreenSpacePosition = new Vector3(Mathf.Clamp(playerPosition.x, 0.0f, Screen.width), Mathf.Clamp(playerPosition.y, 0.0f, Screen.height), playerPosition.z);

        Vector3 clampedWorldSpacePosition = Camera.main.ScreenToWorldPoint(clampedScreenSpacePosition);

        rigidbody.position = new Vector3(clampedWorldSpacePosition.x, 0.0f, clampedWorldSpacePosition.z);

        rigidbody.rotation = Quaternion.Euler(0, 0, rigidbody.velocity.x * -tilt);
    }
}
```

Now if you click the player GameObject you should see the new fields that we added show up in the component. From the Project View, **drag and drop the Bolt Prefab into the Shot field** on the *PlayerController* component. Now in the Hierarchy, expand the player GameObject's children if you need to and locate the *Shot Spawn* GameObject you set up earlier. **Drag and drop the Shot Spawn GameObject onto the Shot Spawn field** on the *PlayerController* component. Set the *Fire Rate* to whatever you feel is appropriate, I set mine to **0.25**.

Test the game in Play Mode to see if everything is working properly! You will notice something unideal though, the shots never die out, and we fill our game with Bolt GameObjects! We will fix this by adding a boundary that destroys these Bolts when they are no longer needed.

## Adding the boundary
Despite what everyone tells you, sometimes its worth it to think **within** the box.

We will be using a box collider to set the bounds of our game, and subsequently destroy anything that goes outside of this boundary. This will prevent us from having to manage resources for GameObjects that are no longer within the playing field of the game.

Right click on the Hierarchy and find the **3D Object** menu, and select **Cube** from within it. Reset this new GameObject's transform.

<p align="center">
  <img src="https://i.imgur.com/EuiQq1R.jpg" width="650"/>
</p>

This will spawn us a cube with all the components we need, and some renderers for us to see it with. However, because this boundary will be invisible, we can **remove the Mesh Filter and Mesh Renderer components**. Now all that should be left is a Transform, and a Box Collider component. Make sure to check the flag for **Is Trigger** on the box collider component.

We are going to control the bounds of the boundary to meet the edges of our play window with scripting, similar to how we determined when a player was at the edge of our screen.

Create a new script in the *Scripts* folder and name it *Boundary*. We will be using a function called `OnTriggerExit()`, which will get called automatically when-*you guessed it*-something leaves the trigger of this GameObject. For us, when something leaves this trigger area we will be destroying it.

We will also be using this script to resize the Box Collider to fit the bounds of our play window.

The code for the script is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Boundary : MonoBehaviour {

    BoxCollider collider;

    private void Start() {

        collider = GetComponent<BoxCollider>();

        transform.position = new Vector3(transform.position.x, transform.position.y, Camera.main.transform.position.z);

        float xScale = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, 0)).x;
        float zScale = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, 0)).y;

        collider.size = new Vector3(2.0f * xScale, collider.size.y, 2.0f * zScale);
    }

    private void OnTriggerExit(Collider other) {
        Destroy(other.gameObject);
    }
}
```

Add this script to the *Boundary* GameObject and test out its destructive power in Play Mode!
