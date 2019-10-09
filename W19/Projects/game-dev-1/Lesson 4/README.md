# Lesson 4: Creating hazards and the main game controller

## Hazard GameObjects
What's life without a little risk right?

We will be creating the asteroid hazards that our player will be avoiding and shooting to score points in our game. Similar to the architecture that we followed to create the *Bolts* our player was shooting, we will be structuring these GameObjects to have their art and logic separated, as we **will** be re-using them!

Start by creating an empty GameObject and renaming it *Asteroid 1*. Reset the transform of this GameObject and feel free to move it to somewhere comfortable so we can see it easily. Now in the project view, under *Assets/Models* locate one of the *prop_asteroid* items. Pick whichever one you would like to start with, as we will be using them all eventually. Drag and drop the file from the project view **onto the Asteroid GameObject in the Hierarchy** and this will automatically parent the art onto the Asteroid GameObject. Reset the transform of the *prop_asteroid* so that it is centered on our main GameObject.

Now with the *Asteroid* GameObject selected, add a **Rigidbody** component and **unselect the Use Gravity field**, and set the **Angular Drag** field to 0. This will allow the asteroid to spin forever during its life time without slowing down. Add a **Capsule Collider** component as well, and use the **Edit Collider** button to drag the square handles on the green capsule bounds to what you think is most suitable for the asteroid you chose.

<p align="center">
  <img src="https://i.imgur.com/5mR7t2i.jpg" width="650"/>
</p>

Now we will be making a script that will randomly rotate the asteroids as they move, to give a feeling that the obstacles are all uniquely generated.

Locate the *Assets/Scripts* folder and create an new C# script called *RandomRotator*. We will be using the provided *Random* class from Unity to generated a random rotation value that we can apply to our asteroid. The unit sphere us to create a random 3D value, instead of having to generate 3 random values and assign them all individually.

The code for the script is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RandomRotator : MonoBehaviour {
    public float tumble;

    private Rigidbody rigidbody;

    private void Start() {
        rigidbody = GetComponent<Rigidbody>();

        rigidbody.angularVelocity = Random.insideUnitSphere * tumble;
    }
}
```

Once the script is completed, add it as a component to the *Asteroid* GameObject. Feel free to experiment with the *Tumble* value, I chose a value of **5**.

We will also be creating the script that destroys the Asteroid when it gets hit by a laser bolt. This logic will be re-used for enemies as well, so make sure you are familiar with the logic inside the script. Inside the *Assets/Scripts* folder create a new C# script and name it *DestroyByContact*.

Similar to what we did with the boundary, we will be using the `OnTriggerEnter()` function, to detect when the laser bold trigger collider enters our Asteroid collider. The *Tag* system in Unity will allow us to differentiate between when we have entered the *Boundary* collider and when we are getting hit with a laser bolt. We will also be adding to this script as we add more features to our game.

The code for the script is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyByContact : MonoBehaviour {
    private void OnTriggerEnter(Collider other) {
        if (other.tag == "Boundary") {
            return;
        }

        Destroy(other.gameObject);
        Destroy(gameObject);
    }
}
```

Once the script is complete, we will need to tag our *Boundary* GameObject accordingly so that it does not destroy everything it touches. Select the *Boundary* GameObject in the Hierarchy and locate the **Tag** field in the top left of the inspector (it should currently read *Untagged*). Click the field and select **Add Tag**. This will bring up the **Tags and Layers** window.

<p align="center">
  <img src="https://i.imgur.com/lVFMl3U.jpg" width="650"/>
</p>

Use the small **+** icon in the **Tags** list to add a new tag, and name it *Boundary*. Once this is done, reselect the *Boundary* GameObject and go back to the **Tag** field and click it to find the newly created **Boundary Tag**. Select this tag and ensure that the field changes.

Test the asteroid in Play Mode to make sure that the tumbling, and destruction works as expected!

Now we can add some style to our logic. We can modify the *DestroyByContact* script to have some explosions when we destroy the asteroid or the player! We will be using references to some expl0sion art that has already been created by Unity for us to use. We will use the familiar `Instantiate()` method to create some explosions for the asteroid, and accommodate the special case of when the Player rams into the asteroid.

First, select the **Player GameObject** in the Hierarchy and find its **Tag** field. If you click the field to access the drop down, you should find that a *Player* tag already exists, as it is a default tag included with all Unity Projects. Set the **Player GameObject**'s tag to **Player**.

Now you can update the *DestroyByContact* script to the code shown below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyByContact : MonoBehaviour {
    public GameObject explosion;
    public GameObject playerExplosion;

    private void OnTriggerEnter(Collider other) {
        if (other.tag == "Boundary") {
            return;
        }

        if (explosion != null) {
            Instantiate(explosion, transform.position, transform.rotation);
        }

        if (other.tag == "Player" && playerExplosion != null) {
            Instantiate(playerExplosion, other.transform.position, other.transform.rotation);
        }

        Destroy(other.gameObject);
        Destroy(gameObject);
    }
}
```

Save the script and you should see the two fields you added on the *DestroyByContact* component when you look at the Unity Editor again (give it a moment, it will take some time for Unity to reload and recompile the script). Populate the *explosion* and *playerExplosion* fields with the **explosion_asteroid** and **explision_player** objects from inside *Assets/Prefabs/VFX/Explosions*.

To get the asteroid to move, we can use the *Mover* script we already created for the laser bolt, so add it as a component to the *Asteroid* GameObject. Set the *speed* field to whatever you would like **as long as the value is negative**, this will ensure it moves towards the player. I used a value of **-5**.

Now that the asteroid is complete, feel free to make a new folder called *Asteroids* inside of *Assets/Prefabs* and drag the *Asteroid* GameObject from the Hierarchy to the folder to make it a prefab. Now you can delete the instance of the *Asteroid* GameObject from the scene once the prefab has been saved.

## Adding more Hazards

As they say, three is a crowd but this crowd is going to be *out of this world*!! (get it, because asteroids? and space? Okay moving on)

Now that we have a basic hazard asteroid setup, we can re-use the work we did to create some new looking asteroids.

Drag the *Ateroid* prefab from the *Assets/Prefabs/Asteroids* folder into the Hierarchy two times, to create two GameObjects. Right click each GameObject and select **Unpack Prefab**, this will allow us to modify this GameObject without modifying the prefab. (This may not be necessary depending on what version of Unity you have! If you don't see this option, when you right click a prefab, feel free to just modify it without).

<p align="center">
  <img src="https://i.imgur.com/547uXcS.jpg" width="650"/>
</p>

Now locate the other *prop_asteroid* art assets from inside *Assets/Models* and drag a new one onto each of the Asteroid GameObjects to parent them, and delete the original art from the original prefab.

<p align="center">
  <img src="https://i.imgur.com/23GjyT6.jpg" width="650"/>
</p>

Now with the new art in place, go back to each asteroid GameObject and adjust the colliders as necessary. After doing this, you can save each of the new asteroids as a new prefab inside of *Assets/Prefabs/Asteroids*, as we can re-use the properties we already set on the first asteroid. Rename them all to be numbered to keep things organized if you wish. Now you should have 3 unique asteroids to choose from when spawning hazards!

## The Game Controller

One script to rule them all...one script to find them...one script to bring them all and in game, bind them.

Our Game Controller will be the central script that controls all the high level aspects of the game. Right now we have many different functioning parts, but our Game Controller will be a central system that brings all these functions together to make a playable game. This is a very common pattern in industry so remember it and use it well! Often times complicated projects will have multiple controllers responsible for controlling smaller subsystems.

Start by making an **empty GameObject** in the Hierarchy and renaming it to *Game Controller*. Reset the transform and tag the GameObject with the pre-existing tag *GameController*. This will help us find our Game Controller from other scripts later in the game.

Now we will need to create the actual script. Inside of *Assets/Scripts* make a new script ant name it *GameController*.

This script will be using a new concept, the **Coroutine**. A coroutine is a function that can stop executing at some point in the function, and continue later. This is very useful for us if we want to wait and do things, and do things continuously forever. We will be using a coroutine to continuously spawn hazards. For more information about coroutines see the Unity [documentation](https://docs.unity3d.com/Manual/Coroutines.html), it has great examples!

We will also be using an array of GameObjects to select a hazard randomly to spawn, so that the player faces unique hazards every wave. Similar to what we did with the boundary, we will be using `Camera.main.ScreenToWorldPoint()` to find the limits in which we want to spawn hazards. We then modify these bounds to be juuuuust outside the view of the game, so that it appears like the asteroids are coming from beyond the game view.

The code for the script is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameController : MonoBehaviour {
    public GameObject[] hazards;
    public int hazardCount;
    public float spawnWait;
    public float startWait;
    public float waveWait;

    float maxZValue;
    float maxXValue;

    private void Start() {
        Vector3 screenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, 0f));
        maxZValue = screenBounds.z * 1.2f;
        maxXValue = screenBounds.x * 0.9f;

        StartCoroutine(SpawnWaves());
    }

    IEnumerator SpawnWaves() {
        yield return new WaitForSeconds(startWait);

        while (true) {
            for (int i = 0; i < hazardCount; i++) {
                GameObject hazard = hazards[Random.Range(0, hazards.Length)];

                Vector3 spawnPosition = new Vector3(Random.Range(-maxXValue, maxXValue), 0f, maxZValue);
                Quaternion spawnRotation = Quaternion.identity;
                Instantiate(hazard, spawnPosition, spawnRotation);
                yield return new WaitForSeconds(spawnWait);
            }

            yield return new WaitForSeconds(waveWait);
        }
    }
}
```

Now add this script as a component to the *Game Controller* GameObject in the Hierarchy. Populate the fields in the array of hazard GameObjects by first **setting the size** to be 3, and dragging the asteroid prefabs we made earlier to the individual fields.

Populate the fields for *Hazard Count*, *Spawn Wait*, *Start Wait*, and *Wave Wait* with whatever you would like after doing some play testing. I chose values of **12**, **0.5**, **1** and **4** respectively.

Test the game in Play Mode and you should see waves of asteroids come at your player!
