# Lesson 2: Create our background and introduction to programming

## Framing our scene
*It's funny how the beauty of art has so much more to do with the frame than the artwork itself.*
-Chuck Palahniuk, Choke

Lets take some time to adjust the visuals of our game before we move on. In the Hierarchy, select the **Main Camera** GameObject. Once you select this GameObject you should notice a little preview window appear in the bottom right corner of the Scene View. This is a preview window for what this camera sees, and right now you should see it looking a little funny.

By moving the camera, we can change what the final view of our game will look like (you can verify this by checking out the Game View). With the Main Camera GameObject selected, find your way to it's Transform component in the Inspector. Reset the Transform of the Main Camera the same way you did to the player GameObject, and set the *y* and *z* values of the Position field to be **10** and **5** respectively. Set the *x* rotation to be **90**.

Locate the **Camera** Component in the inspector with the Main Camera still selected. This component is special and turns our GameObject into a camera for rendering! You can sometimes have more than 1 camera in a scene if you want, but make sure you manage them properly as only 1 camera can render to the Game View. Within the Camera Component, set the **Clear Flags** value to **Solid Color** by selecting from the drop down, and then click on the colored square next to the **Backgroud** field. This will bring up the color selector, and from here you should select a solid black color by moving the color cursor in the center of the color selector window to the bottom.

<p align="center">
  <img src="https://i.imgur.com/dtfeXc7.jpg" width="650"/>
</p>

Next, set the **Projection** field in the Camera Component to **Orthographic**. This will give us that top down old-school arcade shooter field. More about orthographic projection and game graphics can be found [here](http://www.significant-bits.com/a-laymans-guide-to-projection-in-videogames/). Once you do this, you should see some of the fields in the component change, and from the new ones set **Size** to 10. This will make the field of view of the Camera 10 world units.

Your final Camera Component should look like this:

<p align="center">
  <img src="https://i.imgur.com/c14QEF9.png" width="650"/>
</p>

## Lighting our Scene
Action, Camera...Lights? Is that the order of that saying??

We want our game to have the look and feel of travelling through space, and as such its important that we have absolute control over what is being lit in our scene. Unity by default will ambiently light everything in a scene with a dim light, but we want to turn this off so we can have better control over the look of our game.

Navigate to the **Window** tab at the top of the Editor, and find the **Rendering** menu, and hover over it to expose the **Lighting** option.

<p align="center">
  <img src="https://i.imgur.com/LimVl4d.jpg" width="650"/>
</p>

Within this window, under the **Environment** heading, locate the **Environment Lighting** section. Change the value of the **Source** field to **Color** and similar to what we did with the background of the Camera Component, change the color to black.

<p align="center">
  <img src="https://i.imgur.com/Zvt7KOH.png" width="650"/>
</p>

Now that all the unwanted light is out of our scene, we can add our own lights to the scene to adjust the way the game looks. In the Hierarchy you should already see a light in our scene that every Unity Scene starts with, called **Directional Light**. Select this light and rename it by right clicking on the GameObject, rename it to *Key Light*, and reset its Transform Component. We will be using a simple 3 point lighting system similar to the one shown in this diagram.

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/3_point_lighting.svg/1280px-3_point_lighting.svg.png" width="400"/>
</p>

*Note that our Key Light and Fill Light positions will be interchanged*

Note that Directional Lights in Unity do not exist at any specific point, despite what the GameObject would make you think. The position and rotation of a Directional Light only dictate what direction the light hits objects relative to their position, and the light generated comes from everywhere in the space. Adjust the rotation and **Intensity** of the Key Light to light the player GameObject as you see fit.

Feel free to add more lights by right clicking on the **EMPTY SPACE** in the Hierarchy and selecting the **Light** menu, and selecting **Directional Light** from within. Note I specified the empty space in the Hierarchy because right clicking on a GameObject and adding a light will parent that light to the GameObject.

Adjust the rotations of the Key, Fill and Rim lights as you see fit, and you may even play with the color of the Rim light if you would like. I have included the values I chose to set my lights to for your reference, but you may do whatever you think makes your game looks best.

| Light Name | Rotation X | Rotation Y | Rotation z | Intensity |
|------------|------------|------------|------------|-----------|
| Key Light  |     20     |   -155     |     0      |    1.5    |
| Fill Light |     5      |    125     |     0      |    1      |
| Rim Light  |    -15     |    65      |     0      |    0.5    |

Note that I left **ALL POSITIONS AT WORLD ORIGIN**. This is because we will be organizing these lights! Our Hierarchy is getting a little crowded, so we will be tucking these new lights away into an empty GameObject. Right click on an **EMPTY SPACE** in the Hierarchy and select **Create Empty**, this will make an empty GameObject. Rename this GameObject *Lighting*, and reset its Transform. Empty GameObject are useful for organizing a project into digestible chunks. Empty GameObject do not hamper performance in a noticeable way, so feel free to use as many as you need to organize your project. While **holding the Ctrl/Cmd** key, select all three of the lights and drag them **ON TOP** of the **Lighting** GameObject to parent them. Note that parenting will change all the Transform values to be **RELATIVE TO THE POSITION OF THE PARENT**, this is very important when doing position related programming!

Now feel free to drag the Lighting GameObject up and away so that it does not get in the way of our Scene View.

Your final scene could look something like this:

<p align="center">
  <img src="https://i.imgur.com/TpulYOc.png" width="650"/>
</p>

## Creating the background
As comforting as the endless black void in the background of our game is, I think we could use a bit of color behind our player.

Lets start by making an **Empty GameObject**, renaming it *Background* and resetting its Transform. Now with the newly created GameObject selected in the Hierarchy, right-click the GameObject and select the **3D Object** menu, and select **Quad** from the sub menu. This will create a flat **one sided** plane on which we can drop a fancy texture for our background! Select the Quad GameObject in the Hierarchy and set it's *x* rotation to be 90 so that it faces our Camera.

Now head over to the Project View and navigate to the **Textures** folder. Inside this folder you should be able to see the *tile_nebula_green.dff* file. Select this file, and drag it from the Project View **onto** the white surface of the Quad in the **Scene View**. This will populate the Quad with a new **Material** containing our texture!

<p align="center">
  <img src="https://i.imgur.com/ica5W97.jpg" width="650"/>
</p>

With the Quad selected, scroll down in the inspector until you find the **Material** component. Select the **Shader** field and change it to the **Unlit/Texture** type. This will make the background unaffected by our lights, and display the image we chose for our texture with no lighting effects.

<p align="center">
  <img src="https://i.imgur.com/8votpwk.jpg" width="650"/>
</p>

However, you will notice our texture looks quite squished and uncomfortable on this Quad, and thats because it is scaled to be very small. Adjust the *x* and *y* Scale value to be **15** and **30** respectively. We will also need to duplicate this background to cover the wide aspect ratio of our game, so with the Quad selected in the Hierarchy, press **Ctrl + D** on windows or **Command + D** on Mac (If you are on Linux how are you even here??). This will duplicate the Quad which should appear as a child of the Background GameObject. Do this again and place one of the Quads at an *x* position of **15** and the other at **-15**. Now our background should be covered.

Now duplicate the **entire Background** object in a similar manner, and make it a child of the original Background Object. After the duplicate has been parented to the original, set it's *z* position to be **30**.

Now we are ready to make our background scroll with some programming!
In our Project View, select the Assets Folder, and make a new Folder called *Scripts*. With the folder selected, right it to create a new **C# Script**. This will prompt you to name it, so please name it *BGScroller*. **If the name of the script and the name of the class in the script are not the same, Unity will not be able to use this script!** Please ensure this is case.

Double click the newly created script to edit it. We will be using a Unity Library function called Mathf.Repeat to scroll the position of our background continuously.

The code for the script is provided below:

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class BGScroller : MonoBehaviour {

    public float scrollSpeed;
    public float tileSizeZ;

    private Vector3 startPosition;

    private void Start() {
        startPosition = transform.position;
    }

    void Update () {
	float newPosition = Mathf.Repeat(Time.time * scrollSpeed, tileSizeZ);
        transform.position = startPosition - Vector3.forward * newPosition;
    }
}
```

Now select the Background object in the Hierarchy and find the **Add Component** button. When prompted to search, search for our newly created script, **BGScroller**. When the component is added, populate the values for *Scroll Speed* and *Tile Size Z* with the values of **0.3** and **30** respectively.

Now when you Play the game in the Editor, you should see the background move slowly!
