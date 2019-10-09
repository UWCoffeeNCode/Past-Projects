# Lesson 6: Adding UI, the End Game, and Exporting.

## Using UI for Score
U and I were meant to be, like a user...and their interface? I think I have to work on that one.

Horrendous jokes aside, this lesson we will be learning about one of the most powerful parts of the Unity Engine: the UI Canvas. This set of GameObjects and Components will allow us to make a variety of customizable text, and control it with the same scripting we are used to using for controlling GameObjects.

Right click on an empty part of the Hierarchy view and select **UI/Text** from the drop down of available options. Once you create this text, you will notice Unity automatically creates a *Canvas* GameObject and an *EventSystem* GameObject. These are default GameObjects needed for UI functionality in the engine. For now, select the **Text** GameObject which is a child of the *Canvas* GameObject and rename it to *Score Text*.

Select the *Score Text* GameObject and take a look at the inspector. Notice that this GameObject has a *Rect Transform* instead of a traditional Transform Component. This is what allows us to position this UI element in those handy **Screen Space** co-ordinates! Click on the square in the top left of the component **while holding the Alt key**, then click on the square with the red lines in the top left corner.

<p align="center">
  <img src="https://i.imgur.com/cAQOvtT.png" width="450"/>
</p>

This **changes the anchor point** of the UI element, which basically just changes the point at which all distances in the Rect Transform are relative to. By changing our anchor to the top left, we can now position our text element relative to the top left corner, and know that the element's position will be the same relative to that corner, **no matter the resolution the game is played at.**

Now to change and update the values of the score in this text element, we will be adding some functionality to our Game Controller. We will use this class as the centralized place all other parts of the game can use to update anything related to UI in the game.

The code for the updated Game Controller is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class GameController : MonoBehaviour {
    public GameObject[] hazards;
    public int hazardCount;
    public float spawnWait;
    public float startWait;
    public float waveWait;
    float maxZValue;
    float maxXValue;

    public Text scoreText;

    private int score;

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

    public void AddScore(int newScoreValue) {
        score += newScoreValue;
        UpdateScore();
    }

    void UpdateScore() {
        scoreText.text = "Score: " + score;
    }
}
```

After the script compiles, return to the Editor and populate the *Score Text* reference in the *Game Controller* GameObject in the Hierarchy with the text element GameObject we created earlier by dragging and dropping it onto the field.

Now that our Game Controller can update the score, we must add the functionality to the gameplay elements in our game. To add score when an enemy is destroyed, we need to update our *DestroyByContact* script to access the Game Controller and call the functions we just created. Note that we will need to manually search for and populate the reference for the Game Controller when the script starts, because we cannot store a reference to an instance of a scene object in a prefab.

The code for the updated script is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyByContact : MonoBehaviour {
    public GameObject explosion;
    public GameObject playerExplosion;
    public int scoreValue;

    private GameController gameController;

    private void Start() {
        GameObject gameControllerObject = GameObject.FindWithTag("GameController");

        if (gameControllerObject != null) {
            gameController = gameControllerObject.GetComponent<GameController>();
        } else {
            Debug.Log("Cannot find 'GameController' GameObject");
        }
    }

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

        gameController.AddScore(scoreValue);

        Destroy(other.gameObject);
        Destroy(gameObject);
    }
}
```

Now feel free to go to each *Asteroid* prefab in *Assets/Prefabs/Asteroids* and give them each a *Score Value* number in the field in each *DestroyByContact* script. I chose a value of **10** for asteroids. Do the same for the *Enemy Ship* prefabs we created last lesson, I gave mine a score of **20**.

## Ending and Restarting the Game
All good things must come to an end. But that doesn't mean you can't press the R key and restart them after!

To add an end game and replay functionality, we will need a few more text labels. **Right click** on the *Canvas* in the Hierarchy and create two new UI Text objects. Name one *Restart Text* and the other *Game Over Text*. Using the same method from earlier, change the anchor points of both of these text elements to the center of the screen, and then position them according to your liking.

We will be building the end game functionality into the Game Controller, so we will have to create some more functions that other classes can use. We will be adding restart functionality by simply reloading the scene when the player presses the "R" key after the game ends. The `SceneManager` class from Unity lets us manage many different functions in with scenes in a Unity Project, more information about this class can be found [here](https://docs.unity3d.com/ScriptReference/SceneManagement.SceneManager.html).

The updated scripts is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class GameController : MonoBehaviour {
    public GameObject[] hazards;
    public int hazardCount;
    public float spawnWait;
    public float startWait;
    public float waveWait;
    float maxZValue;
    float maxXValue;

    public Text scoreText;
    public Text restartText;
    public Text gameOverText;

    private bool gameOver;
    private bool restart;
    private int score;

    private void Start() {
        gameOver = false;
        restart = false;

        restartText.text = "";
        gameOverText.text = "";

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

            if (gameOver) {
                restartText.text = "Press 'R' for Restart";
                restart = true;
                break;
            }
        }
    }

    private void Update() {
        if (restart) {
            if (Input.GetKey(KeyCode.R)) {
                SceneManager.LoadScene(SceneManager.GetActiveScene().name);
            }
        }
    }

    public void GameOver() {
        gameOverText.text = "Game Over";
        gameOver = true;
    }

    public void AddScore(int newScoreValue) {
        score += newScoreValue;
        UpdateScore();
    }

    void UpdateScore() {
        scoreText.text = "Score: " + score;
    }
}
```

Now populate the new *Restart Text* and *Game Over Text* fields on the Game Controller object in the Hierarchy with the text UI elements we created earlier. Finally, we must utilize the functions we exposed earlier to actually end the game.

We will modify the *DestroyByContact* script one last time to restart the game when the player is blown up.

The code for the modified script is provided below.

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DestroyByContact : MonoBehaviour {
    public GameObject explosion;
    public GameObject playerExplosion;
    public int scoreValue;
    private GameController gameController;

    private void Start() {
        GameObject gameControllerObject = GameObject.FindWithTag("GameController");

        if (gameControllerObject != null) {
            gameController = gameControllerObject.GetComponent<GameController>();
        } else {
            Debug.Log("Cannot find 'GameController' GameObject");
        }
    }

    private void OnTriggerEnter(Collider other) {
        if (other.tag == "Boundary" || other.tag == "Enemy") {
            return;
        }

        if (explosion != null) {
            Instantiate(explosion, transform.position, transform.rotation);
        }

        if (other.tag == "Player" && playerExplosion != null) {
            Instantiate(playerExplosion, other.transform.position, other.transform.rotation);
            gameController.GameOver();
        }

        gameController.AddScore(scoreValue);

        Destroy(other.gameObject);
        Destroy(gameObject);
    }
}
```

Finally play your game and you should be able to restart the game upon player death!

## Exporting the Game
Alright, so we have a fantastic game that is ready for players in the real world to lovingly play, but how do we get it out of the editor and into their hands?

The answer lies in the **Build** tool inside the Unity Engine. Navigate to the top left of the editor and find *File/Build Settings*. This will bring up the build settings menu, which you can use to turn your Unity Project into an executable for desktop, mobile, or even the web!

I will be walking you through how to export for Mac and Windows, but the process for mobile and web is much the same.

<p align="center">
  <img src="https://i.imgur.com/Yg7VXJV.png" width="550"/>
</p>

Ensure that the **Scenes in Build** window shows the scene you have been working on, and if it does not, click the **Add Open Scenes** button to ensure that our scene will be built into the game. Set the **Platform** field on the left to be *PC, Mac and Linux Standalone*, and target the platform of your choice on the right. Once you are set up, press the **Build** button and select where you would like to store the executable, and give your game a name!

Once the build is complete, you can navigate to where you exported your game and double click the executable with the same name you saved to launch the game.

**Congratulations, you just built your first Unity game!**
