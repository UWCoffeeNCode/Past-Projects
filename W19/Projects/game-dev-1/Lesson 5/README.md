# Lesson 5: Audio and Enemies

## Adding Sound Effects
*Music's in my soul, I can hear it every day and every night. It's the one thing on my mind*
-Jonas Brothers

Music does a lot to set the tone of a game, and give feedback to the player about how their mechanics are functioning. We will be adding music and sound effects all through the **Audio Source** component in Unity.

Open the audio clips included in the project under *Assets/Audio.*. Here you will find a variety of clips and sound effects, and we can add them to the GameObjects in our game by dragging and dropping.

From within the Project View, expand the folder *Assets/Prefabs/Explosions*. **Double click** the *explosion_asteroid* prefab to inspect JUST the prefab. Then select the *explosion_asteroid* sound effect, and drag and drop it onto the *explosion_asteroid* inspector in the empty space under *Add Component*. This will automatically add an Audio Source component to the GameObject and set the clip used in the source to the one we selected.

<p align="center">
  <img src="https://i.imgur.com/xx7rzOi.png" width="650"/>
</p>

Select the *explosion_asteroid* prefab to inspect it and ensure that the **Play on Awake** field is selected, and the **Spatial Blend** slider is set all the way to 2D. This will ensure the clip will play as soon as the explosion is instantiated in the scene.

<p align="center">
  <img src="https://i.imgur.com/nHFIF2y.png" width="450"/>
</p>

Repeat the procedure with the *explosion_player* audio clip and prefab.

Now we will add the sound effect for our player's weapon firing. Drag and drop the *weapon_player* audio clip onto the player GameObject in the scene, and **unselect Play on Awake** on the Audio Source component on the player. Additionally, set the **Volume** slider to *0.5*. We will be controlling when the clip plays with scripting.

Open up the *Player Controller* script for editing. We will add a couple of lines of code to play the audio clip when we fire a laser bolt.

The code for the updated script is provided below.

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
    private AudioSource audioSource;

    private void Awake() {
        rigidbody = GetComponent<Rigidbody>();
        audioSource = GetComponent<AudioSource>();
    }

    private void Update() {
        if (Input.GetButton("Fire1") && Time.time > nextValidFireTime) {
            nextValidFireTime = Time.time + fireRate;
            Instantiate(shot, shotSpawn.position, shotSpawn.rotation);

            audioSource.Play();
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

Finally, drag and drop the *Music_background* audio clip onto the game controller GameObject. Ensure that **Play on Awake** and **Loop** fields are both selected, and the **Volume** slider is set to 0.5.

That should be it! Play test your game and ensure the audio levels feel right for you, and adjust the volumes as needed.

## Creating Enemy Ships

When you are a game developer its pretty easy to make enemies very quickly, at least in game!

We will be using much of the structure of our player GameObject and system to model our enemy ships after. Start by creating an **Empty GameObject** and naming it *Enemy Ship*. Onto this empty GameObject, please drag and drop the *vehicle_enemyShip* object from *Assets/Models*, reset the transform, and set the rotation of this object, **NOTE, NOT THE PARENT OBJECT!** to be *180* in the **y** axis. This will ensure that the logic of the enemy ship still operates unrotated, but the art will be rotated to face the player.

Additionally drag and drop the *engines_enemy* object from *Assets/Prefabs/VFX/Engines* onto the Enemy Ship GameObject. Create an empty child GameObject of the Enemy Ship GameObject, name it *Shot Spawn* and move it somewhere in the middle of the two arms of the ship model (This will be where the enemy fires its laser bolts from).

Now select the Enemy Ship GameObject and add a Rigidbody component, and unselect **Use Gravity**. Add a sphere collider component and edit it to encapsulate the enemy ship to your liking, and select **Is Trigger**. Add a new tag called *Enemy* and tag the Enemy Ship GameObject with this tag.

Your final Enemy Ship GameObject should look something like this:

<p align="center">
  <img src="https://i.imgur.com/TVLWKw0.jpg" width="650"/>
</p>

Now we will add our script that allows us to destroy this ship by shooting at it. Open up the **DestroybyContact** script to edit it, as we will be adding a case to catch the special case where enemies collide with each other, and prevent them from destroying each other.

The modified DestroybyContact script is shown below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyByContact : MonoBehaviour {
    public GameObject explosion;
    public GameObject playerExplosion;

    private void OnTriggerEnter(Collider other) {
        if (other.tag == "Boundary" || other.tag == "Enemy") {
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
Now add this script as a component to the Enemy Ship GameObject. Drag and drop the *explosion_enemy* audio clip from *Assets/Audio* onto the *explosion_enemy* prefab in *Assets/Prefabs/VFX/Explosions* folder. Populate the **Explosion** field in the DestroyByContact script with the *explosion_enemy* prefab, and the **Player Explosion** field with the *player_explosion* prefab.

Do a quick play test to ensure that shooting the enemy destroys it, and colliding with the enemy destroys it and the player.

Now we will give our Enemy Ship the ability to shoot laser bolts. Create a new script called *WeaponController* under *Assets/Scripts*.

We wil be using another handy way to repeatedly call functions using `InvokeRepeating()` to repeatedly fire shots. This method is a nice way to avoid coroutines if you want to do something simple with just a single repeating function that doesn't require complex timing. More information about this function can be found [here](https://docs.unity3d.com/ScriptReference/MonoBehaviour.InvokeRepeating.html).

The code for the script is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class WeaponController : MonoBehaviour {
    public GameObject shot;
    public Transform shotSpawn;
    public float fireRate;
    public float delay;

    private AudioSource audioSource;

	void Start () {
        audioSource = GetComponent<AudioSource>();
        InvokeRepeating("FireWeapon", delay, fireRate);
	}

    void FireWeapon() {
        Instantiate(shot, shotSpawn.position, shotSpawn.rotation);
        audioSource.Play();
    }
}
```

Now we will need to make a new laser bolt prefab for the enemies. Drag a copy of the *Bolt* prefab from inside of *Assets/Prefabs* and unpack it if you can (don't worry if you cant do this, older versions of unity don't support this and thats okay). Rename this new bolt *Enemy Bolt*. Now under *Assets/Materials* **duplucate** the *fx_bolt_orange* material and rename the new material *fx_bolt_blue*. Change the texture of this material to be the *fx_lazer_cyan_dff* texture. Now drag this new material onto the **Materials** field on the Mesh Renderer component of the *VFX* GameObject on the Enemy Bolt GameObject. Add a **DestroyByContact** component and populate **only the Player Explosion field** with the *explosion_player* prefab. Now drag and drop this new Enemy Bolt GameObject to the *Assets/Prefab* folder and create a new original prefab if prompted.

Your new Enemy Bolt should look something like this:

<p align="center">
  <img src="https://i.imgur.com/A0AtfFU.jpg" width="650"/>
</p>

Now that we have done this, we should also **tag all of our asteroid prefabs with 'Enemy'** so that the laser bolts from the Enemy Ship do not destroy them.

Now feel free to delete this Enemy Bolt object from the Hierarchy and **populate the fields in the WeaponController** script on the Enemy Ship GameObject. Set the **ShotSpawn** field to the Shot Spawn child transform of EnemyShip and the **Shot** GameObject field to the Enemy Bolt prefab we just created. I chose a value of **1.5** for *FireRate* and **0.5** for *Delay* but feel free to choose whatever you would like.

Drag and drop the *weapon_enemy* audio clip from *Assets/Audio* onto the Enemy Ship GameObject to add the shooting sound effect, and unselect **Play on Awake**.

Finally add the **Mover** script to the Enemy Ship and give it a speed, I chose **-5** for the speed so it moves towards the player.

We will be adding some basic maneuvering ability to the enemy, to move towards the center of the screen. You can modify this script later to add more complex maneuvers based on other things, but this basic script will suffice for now.

The `MoveTowards()` function is helpful here in smoothly ensuring a value gets interpolated to a target value without overshooting. You will also notice we use the same logic we used on the player to keep enemies inside the bounds of the screen. We also use Vector2's in a clever way here to store the bounding ends of values we want to randomize between.

The code for the script is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class EvasiveManeuver : MonoBehaviour {

    public float dodge;
    public float smoothing;
    public float tilt;
    public Vector2 startWait;
    public Vector2 maneuverTime;
    public Vector2 maneuverWait;

    private float currentSpeed;
    private float targetManeuver;
    private Rigidbody rigidbody;

	void Start () {
        StartCoroutine(Evade());
        rigidbody = GetComponent<Rigidbody>();
        currentSpeed = rigidbody.velocity.z;
	}

    IEnumerator Evade() {
        yield return new WaitForSeconds(Random.Range(startWait.x, startWait.y));

        while (true) {
            targetManeuver = Random.Range(1, dodge) * -Mathf.Sign(transform.position.x);
            yield return new WaitForSeconds(Random.Range(maneuverTime.x, maneuverTime.y));
            targetManeuver = 0;
            yield return new WaitForSeconds(Random.Range(maneuverWait.x, maneuverWait.y));
        }
    }

    private void FixedUpdate() {
        float newManeuver = Mathf.MoveTowards(rigidbody.velocity.x, targetManeuver, Time.deltaTime * smoothing);
        rigidbody.velocity = new Vector3(newManeuver, 0, currentSpeed);

        Vector3 enemyPosition = Camera.main.WorldToScreenPoint(transform.position);

        Vector3 clampedScreenSpacePosition = new Vector3(Mathf.Clamp(enemyPosition.x, 0.0f, Screen.width), enemyPosition.y, enemyPosition.z);

        Vector3 clampedWorldSpacePosition = Camera.main.ScreenToWorldPoint(clampedScreenSpacePosition);

        rigidbody.position = new Vector3(clampedWorldSpacePosition.x, 0.0f, clampedWorldSpacePosition.z);

        rigidbody.rotation = Quaternion.Euler(0, 0, -1 * rigidbody.velocity.x);
    }
}
```
Feel free to play with the values in the script, the ones I chose are shown listed below.

<p align="center">
  <img src="https://i.imgur.com/jWvZGXy.png" width="450"/>
</p>

Now that the enemy is complete, drag and drop it into the *Assets/Prefabs* folder. You can add enemies into the game by adding to the array of *Hazards* in the game controller, and they should be spawned nice and randomly in the same way they were for the asteroids!
