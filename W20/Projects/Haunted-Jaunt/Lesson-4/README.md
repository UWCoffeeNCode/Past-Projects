# Lesson 4
## UI 
Expand **FaderCanvas** GameObject in the Hierarchy. Duplicate **ExitImageBackground** by pressing Ctrl/Cmd + D. Rename the copy to **CaughtImageBackground** and ExitImage copy GameObject to **CaughtImage**. In the Inspector window of CaughtImage, switch the **Source Image** property to sprite called **Caught**. 

## GameEnding Script 

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
        public CanvasGroup caughtBackgroundImageCanvasGroup;

        bool m_IsPlayerAtExit;
        bool m_IsPlayerCaught;
        float m_Timer;

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
                EndLevel (exitBackgroundImageCanvasGroup, false);
            }
            else if (m_IsPlayerCaught)
            {
                EndLevel (caughtBackgroundImageCanvasGroup, true);
            }
        }

        void EndLevel (CanvasGroup imageCanvasGroup, bool doRestart)
        {
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
    
Go back to Unity Editor and let's finish our UI. We need to assign a reference to the Exit and Caught Background Image Canvas Group on the Game Ending script. Drag **ExitImageBackground** GameObject from the Hierarchy onto the Exit Background Image Canvas Group field on the Game Ending and do the same for CaughtImageBackground to Caught Background Image Canvas Group field. 

## Setting up Gargoyle Prefab 
Let's bring in our Gargoyle model into the Scene. Go to **Assets > Models** and drag **Gargoyle** asset into the Hierarchy. Create Gargoyle prefab in the **Assets > Prefabs** folder. Select **Original Prefab** when dialogue box appears. Open prefab editor. 

Let's start by animating our gargoyle. In the Project window, go to **Assets > Animation > Animators** and create an **Animator Controller** and name it **"Gargoyle"**. Next, navigate to **Assets > Animation > Animations** and expand **Gargoyle@Idle**. Drag the **Idle** animation from the Project window into the Animator window. Now let's assign our animator to our Gargoyle GameObject. Select Gargoyle GameObject and drag the Gargoyle animator onto the **Controller** property of the Gargoyle's Animator Component in the Inspector. 

We need to make sure JohnLemon can bump into Gargoyle GameObject and Gargoyle can spot JohnLemon. We'll achieve this by using colliders. First add **Capsule Collider Component** to our GameObject and set it's value to: **Center** to **(0, 0.9, 0)**, **Radius** to **0.3**, and **Height** to **1.8**. Next, we will use another collider and use it as a Trigger to simulate Gargoyle's line of sight. Create an Empty GameObject under GargoyleModel and name it **PointOfView**. This GameObject will act as our Gargoyle's line of sight. Set the **Transform** component's **Position** to **(0, 1.4, 0.4)** and **Rotation** to **(20, 0, 0)**. Add a **Capsule Collider** component to PointOfView and check off **Is Trigger**. Adjust the collider settings: **Center** property to **(0, 0, 0.95)**, **Radius** to **0.7**, **Height** to **2** and **Direction** property from Y-Axis to **Z-Axis**. 

Exit prefab editor and let's set our first Gargoyle's **Transform** component's **Position** to **(-15.2, 0, 0.8)** and **Rotation** to **(0, 135, 0)**. 

## Observer Script 
    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;

    public class Observer : MonoBehaviour
    {
        public Transform player;
        public GameEnding gameEnding;

        bool m_IsPlayerInRange;

        void OnTriggerEnter (Collider other)
        {
            if (other.transform == player)
            {
                m_IsPlayerInRange = true;
            }
        }

        void OnTriggerExit (Collider other)
        {
            if (other.transform == player)
            {
                m_IsPlayerInRange = false;
            }
        }

        void Update ()
        {
            if (m_IsPlayerInRange)
            {
                Vector3 direction = player.position - transform.position + Vector3.up;
                Ray ray = new Ray(transform.position, direction);
                RaycastHit raycastHit;

                if(Physics.Raycast(ray, out raycastHit))
                {
                    if (raycastHit.collider.transform == player)
                    {
                        gameEnding.CaughtPlayer(); 
                    }
                }
            }
        }
    }
    
## Setting Up Ghost Prefab 
Same with the Gargoyle, go to **Assets > Models > Characters** and drag **Ghost** asset into the Hierarchy. Turn it into a prefab and open the Prefab for editing. Create **Animator Controller** inside **Assets > Animation > Animators** and name it **"Ghost"**. Double click to open the Animator window. From **Assets > Animation > Animations** expand **Ghost@Walk** and drag **Walk** animation into the Animator window. Finally assign the animator controller to ghost prefab in the Inspector window **Controller** property. 

We want our ghosts to have physical presence like JohnLemon and Gargoyle prefab. Let's go ahead and add **Capsule Collider** to Ghost GameObject. Adjust the settings to: **Center** to **(0, 0.6, 0)**, **Radius** to **0.25**, and **Height** to **1.2**. Just like Gargoyles, we want Ghosts to spot JohnLemon. We will achieve this by adding **PointOfView** GameObject to our Ghost prefab as well. From the Hierarchy, find **PointOfView** GameObject and drag it into the Project window to make it a prefab. Now, add **PointOfView** prefab to Ghost prefab. In the Inspector, adjust the Transform component's **Position** to **(0, 0.75, 0.4)** and **Rotation** to **(0, 0, 0)**. 

For our ghost prefab, we also want **Rigidbody** component because it is moving. However, because we don't want collision with JohnLemon to create any movement in the Ghost, we will enable **Is Kinematic** checkbox in the Rigidbody component. If "Is Kinematic" is enabled, Rigidbody cannot be affected by external forces such as collision, but it can still collide with other GameObjects. 
