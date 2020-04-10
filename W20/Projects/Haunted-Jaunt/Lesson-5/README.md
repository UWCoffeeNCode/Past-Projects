# Lesson 5 
## Setting Up a Nav Mesh Agent 
We are going to set up our nav mesh agent. Nav mesh agent allows the Ghost to find paths around the Nav Mesh you baked earlier in lesson 3. In the Hierarchy, select Ghost GameObject, enter prefab editor and add a **Nav Mesh Agent** component in the Inspector. Change our settings: **Radius** to **0.25**, **Speed** to **1.5**, **Stopping Distance** to **0.2**. Our agent's height is taller than our Ghost model but since our environment doesn't have a ceiling, this doesn't matter. 

## WaypointPatrol Script 
The ghosts are going to move by patrolling in a loop through a collection of waypoints. We need to create another script to do this. Inside **Assets > Scripts**, create a new C# Script and name it "**WaypointPatrol**". Add the script to our Ghost GameObject (Select the Ghost and drag the script into the Inspector). Double click on the WaypointPatrol Script to edit it. 

    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.AI; // give access to NavMeshAgent class 

    public class WaypointPatrol : MonoBehaviour
    {
        public NavMeshAgent navMeshAgent; 
        public Transform[] waypoints; // public array of Transforms called waypoints 

        int m_CurrentWaypointIndex; // stores the current index of the waypoint array 

        void Start ()
        {
            navMeshAgent.SetDestination (waypoints[0].position); 
            // sets the initial destination of the Nav Mesh Agent to the position of first waypoint in the array 
        }

        void Update ()
        {
            if(navMeshAgent.remainingDistance < navMeshAgent.stoppingDistance) // check if Nav Mesh Agent has arrived at its destination 
            {
                m_CurrentWaypointIndex = (m_CurrentWaypointIndex + 1) % waypoints.Length; // set m_CurrentWaypointIndex to current index 
                navMeshAgent.SetDestination (waypoints[m_CurrentWaypointIndex].position); // set new destination for the Agent 
            }
        }
    }

Now back in our Unity editor, we can assign the Nav Mesh Agent reference and some Transforms for the waypoints. Select our **Ghost** GameObject in the Hierarchy inside Ghost prefab editor. Drag **Nav Mesh Agent** component in the Inspector window down to the Nav Mesh Agent field on the Waypoint Patrol script. This will assign the Nav Mesh Agent reference. Save Ghost Prefab and return to the Scene. Check if our Ghost's Observer script has the reference it needs. In the Hierarchy, expand Ghost GameObject and select **PointOfView** child GameObject. Drag JohnLemon GameObject from the Hierarchy onto the **Player** field of the Observer script to assign its Transform. Next, click the circle next to the GameEnding field to assign the component to the GameEnding script. 

## Placing Enemies 
Let's create duplicates of our enemies. Starting with our ghost, select **Ghost** GameObject from the Hierarchy window. Duplicate it three times by pressing Ctrl/Cmd + D. You should have 4 Ghost GameObjects in your Hierarchy now. Let's assign them positions. Set the position of: 
- **Ghost** to **(-5.3, 0, -3.1)** 
- **Ghost(1)** to **(1.5, 0, 0.4)** 
- **Ghost(2)** to **(3.2, 0, 6.5)** 
- **Ghost(3)** to **(7.4, 0, -3)** 

Now we have them positioned where we want them to be, let's create waypoints and assign them. Waypoints just need to be empty GameObjects, since we are only using their Transform component. In the Hierarchy window, click on the Create button and select **Create Empty**. Rename our GameObject to "**Waypoint**" and duplicate it until you have 10 copies of it. In the Hierarchy, select our **Ghost** and scroll down in the Inspector to **Waypoint Patrol Component**. Drag **Waypoint** and **Waypoint(1)** GameObject from the Hierarchy window onto the name of the Waypoints field to add it to the array. Our first Ghost will have two waypoints. Let's position them as follows: 
- **Waypoint** to **(-5.3, 0, 6.7)** 
- **Waypoint(1)** to **(-5.5, 0, -4.5)**. 

Repeat the same process with all our Ghosts and Waypoints. Assign Waypoint(2) and Waypoint(3) to Ghost(1) and set their position: 
- **Waypoint(2)** to **(1.2, 0, 7.7)** 
- **Waypoint(3)** to **(0.9, 0, -3.5)** 

Our third ghost will be circling the dining room, so we need more waypoints. Assign Waypoint(4), Waypoint(5), Waypoint(6) and Waypoint(7) to Ghost(2). Set their position to: 
- **Waypoint(4)** to **(3.2, 0, 5.6)** 
- **Waypoint(5)** to **(3.2, 0, 12.3)** 
- **Waypoint(6)** to **(6.5, 0, 12.3)**
- **Waypoint(7)** to **(6.5, 0, 5.6)** 

Lastly, assign our Ghost(3) Waypoint(8) and Waypoint(9), and set their position: 
- **Waypoint(8)** to **(3.2, 0, -5)** 
- **Waypoint(9)** to **(7.4, 0, -2)** 

And our Ghosts are placed and finished. Now, let's create more of our Gargoyle and place them in our game. Duplicate the **Gargoyle** GameObject twice. Set the duplicate's position and rotation to: 
- **Gargoyle(1)**: position to **(-2.6, 0, -8.5)**, rotation to **(0, 30, 0)** 
- **Gargoyle(2)**: position to **(-4.8, 0, 10.6)**, rotation to **(0, 0, 0)** 

Feel free to add more Gargoyles and place them wherever you want in your game, and we are now done with enemies. Let's clean up our Hierarchy a little. Create an empty GameObject and name it "**Enemies**". Set the position of Enemies to **(0, 0, 0)**. Hold the Ctrl/Cmd in the Hierarchy and click on each of the Ghost and Gargoyle GameObjects. When they are all selected, drag them onto the **Enemies** GameObject to make it their parent. Let's do the same with our waypoints. Create an empty GameObject and name it "**Waypoints**". Set the position of **Waypoints** to **(0, 0, 0)** and drag all the Waypoint GameObjects into the **Waypoints** GameObject to make it their parent. 

## Audio 
How does audio work in Unity? 
- **Audio Clips** are Assets such as MP3s which contain all the data specific to a particular sound 
- **Audio Sources** are components which act as the origin of a sound in the game world. Most things that make sound in a game should have an Audio Source Component, so that the sound has a location. 
- **The Audio Listener** is a single component in a Scene that works like the virtual ears of the player. By default, the Audio Listener Component is on the Main Camera. 

The Audio Source plays an Audio Clip, and if the Audio Listener is close enough to the Audio Source then the sound is heard. We will be using two different types of audios: 
- **Non-Diegetic Sound**, which has no identifiable source (ex. a soundtrack) 
- **Diegetic Sound**, which has an identifiable source (ex. a gun fire) 

The **Spatial Blend** of a particular Audio Source determines whether it sounds like it's coming from a particular point in the game world, or if it's equally loud no matter the distance between the source and the Audio Listener. When the spatial blend is set to be purely 2D, distance between the Audio Source and the Audio Listener does not affect the volume. It is called 2D because it can still pan left and right using the Stereo Pan setting. If an Audio Source’s spatial blend is set to purely 3D, the volume will vary with distance to the Audio Listener. 

## Non-Diegetic Sound 
Let's start with non-diegetic audio. Since this sound doesn't have an origin, it's **spatial blend** is set to **2D**. In the Hierarchy, create an empty GameObject and name it "**Ambient**". Set it's position to **(0, 0, 0)**. In the Project window, go to **Assets > Audio** and drag **SFXHouseAmbience** Audio Clip into the Inspector window. That creates an Audio Source component and automatically assigns it to the AudioClip section. The **Spatial Blend** property has already been set to 2D, so we don't need to change it. **Play On Awake** has also been enabled by default, which means the audio will play as soon as the level starts. Enable the **Loop** checkbox to loop the ambient track and set the **Volume** property of the Audio Source Component to **0.5**. 

Instead of creating our other two non-diegetic sounds from scratch, we will duplicate Ambient GameObject. Duplicate it twice and name it "**Escape**" and "**Caught**". Select **Escape** GameObject and set the **AudioClip** for its Audio Source Component to **SFXWIN**, either by dragging it from the Project window or by using the circle select button. Select **Caught** and set its **AudioClip** to **SFXGameOver**. Now we have set up our non-diegetic Audio Sources. 

## Game Ending Script Updated 
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;
    using UnityEngine.SceneManagement;

    public class GameEnding : MonoBehaviour
    {
        public float fadeDuration = 1f;
        public float displayImageDuration = 1f;
        public GameObject player;
        public CanvasGroup exitBackgroundImageCanvasGroup;
        public AudioSource exitAudio; // variable that stores reference to AudioSource for exit audio 
        public CanvasGroup caughtBackgroundImageCanvasGroup;
        public AudioSource caughtAudio; // variable that stores reference to AudioSource for caught audio 

        bool m_IsPlayerAtExit;
        bool m_IsPlayerCaught;
        float m_Timer;
        bool m_HasAudioPlayed; // boolean variable that stores whether audio has played or not 

        void OnTriggerEnter (Collider other)
        {
            if (other.gameObject == player)
            {
                m_IsPlayerAtExit = true;
            }
        }

        public void CaughtPlayer ()
        {
            m_IsPlayerCaught = true;
        }

        void Update ()
        {
            if (m_IsPlayerAtExit)
            {
                EndLevel (exitBackgroundImageCanvasGroup, false, exitAudio); // set exitAudio as AudioSource 
            }
            else if (m_IsPlayerCaught)
            {
                EndLevel (caughtBackgroundImageCanvasGroup, true, caughtAudio); // set caughtAudio as AudioSource 
            }
        }

        void EndLevel (CanvasGroup imageCanvasGroup, bool doRestart, AudioSource audioSource) // add AudioSource parameter 
        {
            if (!m_HasAudioPlayed) // make sure our audio source only plays once 
            {
                audioSource.Play(); // play the audio 
                m_HasAudioPlayed = true; // set m_HasAudioPlayed to true 
            }

            m_Timer += Time.deltaTime;
            imageCanvasGroup.alpha = m_Timer / fadeDuration;

            if (m_Timer > fadeDuration + displayImageDuration)
            {
                if (doRestart)
                {
                    SceneManager.LoadScene (0);
                }
                else
                {
                    Application.Quit ();
                }
            }
        }
    }

Back in Unity Editor, select **GameEnding** GameObject and set the **Exit Audio** field to **Escape** and the **Caught Audio** field to **Caught** Audio Source. 

## Diegetic Sound 
Select JohnLemon GameObject. In the Inspector, add an **AudioSource** component. use the circle select button to set the **AudioClip** to **SFXFootstepsLooping**. Despite this being a diegetic sound, we will use a spatial blend of fully 2D so the volume doesn't vary as JohnLemon moves around. We don't want the audio to play as soon as the scene starts as JohnLemon starts stationary. **Disable** the **PlayOnAwake** checkbox and **Enable** the **Loop** checkbox. 

## PlayerMovement Script Updated 
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;

    public class PlayerMovement : MonoBehaviour
    {
        public float turnSpeed = 20f;

        Animator m_Animator;
        Rigidbody m_Rigidbody;
        AudioSource m_AudioSource; // variable to store reference to AudioSource  
        Vector3 m_Movement;
        Quaternion m_Rotation = Quaternion.identity;

        void Start ()
        {
            m_Animator = GetComponent<Animator> ();
            m_Rigidbody = GetComponent<Rigidbody> ();
            m_AudioSource = GetComponent<AudioSource> (); // assign reference to m_AudioSource 
        }

        void FixedUpdate ()
        {
            float horizontal = Input.GetAxis ("Horizontal");
            float vertical = Input.GetAxis ("Vertical");

            m_Movement.Set(horizontal, 0f, vertical);
            m_Movement.Normalize ();

            bool hasHorizontalInput = !Mathf.Approximately (horizontal, 0f);
            bool hasVerticalInput = !Mathf.Approximately (vertical, 0f);
            bool isWalking = hasHorizontalInput || hasVerticalInput;
            m_Animator.SetBool ("IsWalking", isWalking);

            if (isWalking) // check if JohnLemon is walking 
            {
                if (!m_AudioSource.isPlaying) // check if Audio is already playing 
                {
                    m_AudioSource.Play(); // play Audio 
                }
            }
            else
            {
                m_AudioSource.Stop (); // stop Audio 
            }

            Vector3 desiredForward = Vector3.RotateTowards (transform.forward, m_Movement, turnSpeed * Time.deltaTime, 0f);
            m_Rotation = Quaternion.LookRotation (desiredForward);
        }

        void OnAnimatorMove ()
        {
            m_Rigidbody.MovePosition (m_Rigidbody.position + m_Movement * m_Animator.deltaPosition.magnitude);
            m_Rigidbody.MoveRotation (m_Rotation);
        }
    }

Now back in our Unity Editor, we need to move the Audio Listener from the Main Camera to JohnLemon. In the Hierarchy, select the **Main Camera** GameObject. Click on the Audio Listener component's context menu and select **Remove Component**. Then, select **JohnLemon** GameObject in the Hierarchy and add an **Audio Listener** component in the Inspector. Make sure you override any changes you make so it updates JohnLemon's prefabs. 

Next, let's give our Ghost GameObjects AudioSource. In the Hierarchy, expand the **Enemies** GameObject and select one of the **Ghost** GameObject. Use the arrow shortcut to open the Prefab for editing. In the Project window, go to **Assets > Audio** and drag **SFXGhostMove Audio Clip** onto the **Ghost GameObject** in the Hierarchy. In the Audio Source component in the Inspector window, **Enable** the **Loop**, set the **Volume** to **0.4**, and set the **Spatial Blend** to **1**, so that it is fully 3D. Now, we need to adjust the 3D Sound Settings. In the Audio Source component, expand the **3D Sound Settings** section. The 3D Sound Settings control how the audio varies with distance from the Audio Listener. Change the **Max Distance** property to **10**, which means the player is able to hear the Ghost when a Ghost is 10 meters away. Next, we'll set the **Volume Rolloff** to **Custom Rolloff**. Volume Rolloff controls the way the volume changes with distance. We will stick with the default curve. 

Finally, we need to correct the direction of the Ghost sound effect. Because our sound effect is on JohnLemon, it turns with him when JohnLemon turns. This means that when JohnLemon is facing the camera, the virtual eyes and virtual ears are facing in different directions, thus Ghost will sound like they're on the opposite side. Let's fix this. Notice that our **SFXGhostMove** Audio Clip is set to play **Mono** instead of Stereo. This means that the sound is identical through the left and right channels. In the Audio Source for the Ghost Prefab, find the **3D Sound Settings**. The Spread property controls the range in degrees that a sound seems like it is coming from. Set **Spread** property to **180**. Then, half the sound will come from each channel and since these channels are the same, the audio will seem directionless. Save our Ghost Prefab and return to the Scene. 


## Build 
The application you create from the Editor to distribute your game to users is called the **Player**. Let's adjust project settings before creating the Player. Go to **Edit > Project Settings** and select **Player**. The **Company Name** is use to create the folders where the files created for built games will be stored. You could change it, but it's not required. **Product Name** is the name of your game. Change this to "**John Lemon's Haunted Jaunt**" or any other creative name you can think of. The download arrow button at the top of the next section means that all the settings in this section are for **PC, Mac & LInux Standalone Platforms**. If you installed support for other platforms when installing Unity, you will see multiple buttons in that toolbar. 

Let's adjust how our game will display to players. Expand **Resolution and Presentation** section. **Resolution** allows you to define the default mode that the game starts in. The **Run In Background** setting determines whether your game continues to run if the window/application doesn't have the focus. In the **Standalone Player Options** subsection, make sure that **Display Resolution Dialog** is set to **Enabled**. This allows you to show a window when the user launches the game which lets them select the resolution. Finally, in the **Splash Image** section, you can change the logo shown when the game starts **(Logos)**. 

Now we are ready to build our game. In the top menu, select **File > Build Settings**. The **Scene In Build** section at the top lists all the Scenes that will be included in your game. If your MainScene is still open, click **Add Open Scene** to add it to the list. Alternatively, you can drag and drop your Scene from the Project WIndow to the Scenes in Build section of the Buildd Settings window. The **Platform** section at the bottom left allows you to choose which platforms you want your game to run on. By default, the Editor only supports the platform that it is installed on. You can install more platforms in Unity Hub by going to **Installs**, clicking **... > Add Component** next to the relevant Unity version and selecting the platforms you want to install. 

After you have chosen your platform, click **Build** to trigger a build. Then, Unity will open a file explorer and ask you to select a folder to store your built game. Create a new folder called **Build** inside your the folder that contains your project. Unity will now build your game! It will compress and package all your assets, detect and ignore the ones that aren't used and compile your scripts in an optimized form. When the game is finished building, you can run the executable to try your game. 
