# Lesson 3 
## PlayerMovement Script

    using System.Collections;
    using System.Collections.Generic;
    using UnityEngine;

    public class PlayerMovement : MonoBehaviour
    {
        public float turnSpeed = 20f;

        Animator m_Animator;
        Rigidbody m_Rigidbody;
        Vector3 m_Movement;
        Quaternion m_Rotation = Quaternion.identity;

        void Start ()
        {
            m_Animator = GetComponent<Animator> ();
            m_Rigidbody = GetComponent<Rigidbody> ();
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

            Vector3 desiredForward = Vector3.RotateTowards (transform.forward, m_Movement, turnSpeed * Time.deltaTime, 0f);
            m_Rotation = Quaternion.LookRotation (desiredForward);
        }

        void OnAnimatorMove ()
        {
            m_Rigidbody.MovePosition (m_Rigidbody.position + m_Movement * m_Animator.deltaPosition.magnitude);
            m_Rigidbody.MoveRotation (m_Rotation);
        }
    }


## Environment 
Creating a game environment can be very time-consuming. Unity has already created the environment for this game so all we need to do is instantiate it. 

Go to Project Windows, **Assets > Prefabs** and drag the **Level Prefab** into the Hierarchy. 

Now let's position our player into its starting position. Set Transform component's **Position** property of JohnLemon to **(-9.8, 0, -3.2)**. 

___Adding a Navigation Mesh___

Unity has a built-in system called the **NavMesh**. A Mesh is a collection of triangles that all fit together to define a shape. The mesh enables JohnLemon to be rendered to the screen. The **NavMesh** is an invisible shape over the ground that defines an area within which selected GameObjects can move. 

When a GameObject is identified as **Static**, Unity's navigation systems assume that it will not move. The game environment consists of many GameObjects with Mesh Renderer Components. The combination of all the meshes from the Mesh Renderer Components whose GameObjects are marked as Static form the basis for the NavMesh. Let's mark our environmental GameObject as static by selecting the **Level** GameObject and enabling the **Static** checkbox. When a dialogue box appear asking whether you wish to enable the static flags for all the child objects, select **Yes, change children**. However, we need to set one exception. Find **Ceiling Plane** GameObject under Level > Corridors > Dressing > Ceiling Plane and disable the **Static** checkbox. 

After we have set our environment to Static, it's time to bake (the process of creating a NavMesh) our NavMesh. In the Menu bar, go to **Window > AI > Navigation** to open a Navigation window. Drag and dock the window next to the Inspector Window. Select **Bake** tab. Back settings control the details of how the NavMesh will be constructed. **Agent** refers to the agents that will move around the NavMesh, which are ghosts for our case. Set the **Agent Radius** to **0.25**. Now click the **Bake** button at the bottom and wait a couple minutes until it finishes baking. Once it finishes baking, the part covered in light blue mesh is the area of the environment that ghosts are able to move around. 

## Virtual Camera 
Currently, we have a camera that is fixed to one location, and as the player moves around the Scene, JohnLemon could wander away out of our Game View. To view the Scene, a GameObject in the Scene must have a **Camera Component**. When a new Scene is created, a GameObject is added called Main Camera which has a Camera component. The camera points down the GameObject's **z-axis** and behaves exactly like all other GameObjects. In the Scene view, you can see a gizmo representing the camera's **frustum**. The frustum is a solid shape that looks like a pyramid with the top cut off parallel to the base. This is the shape of the region that can be seen and rendered by a perspective camera. 

There are several ways to get the camera to follow the player character. We will be using Unity's built-in solution: **Cinemachine**. Summary of how Cinemachine works: 

- One or more 'virtual' cameras are created in a Scene.
- These virtual cameras are managed by a component called the Cinemachine Brain. 
- The Cinemachine Brain is attached to the same GameObject as a Camera component - by default this will be the Main Camera GameObject. 
- The Cinemachine Brain manages all of the virtual cameras and decides which virtual camera (or combination of virtual cameras) the actual camera should follow. 

In our game, the camera will only be following our main character, JohnLemon, so we only need one virtual camera. Let's set up our virtual camera. Select JohnLemon GameObject in the Hierarchy and focus on him in the Scene View. In the top menu, go to **Cinemachine > Create Virtual Camera**. Now we have a new GameObject called **CM vcam1** in the Hierarchy. Rename the name of the GameObject to **VirtualCamera**. Virtual camera is created at the point of focus, so it is currently on top of JohnLemon. Let's change the settings to fix this. 

Select **VirtualCamera**. In the inspector find the Cinemachine Virtual Camera component. We will only focus on some sections of this component. The target reference section has two settings **Follow** and **Look At**. These are optional references to the Transform components of GameObjects. For the virtual camera to move, it needs a reference to a Transform that it will follow. The next two sections are **Body** and **Aim**. These are settings for how the camera moves and rotates respectively. You are going to restrict the movement of the virtual camera, so it has JohnLemon in view all the time but doesn't actually look at the character. 

Let's make some changes to our component settings. In the **Aim** section, change the drop-down menu at the top from **Composer** to **Do Nothing**. Then drag and drop JohnLemon GameObject from the Hierarchy window onto the **Follow** property, setting the Follow setting to reference JohnLemon's Transform. In the **Body** section, change the drop-down at the top right of the section from **Transposer** to **Framing Transposer**. This change will allow you to control the virtual camera's position by giving it rules about where on screen it's Follow target has to be. The Game window should now have several red and blue boxes on it. These are guides for where on the screen the target can be. Now let's set the virtual camera to the correct angle. Set the **Rotation** around the x-axis to **45**. Lastly, let's change the **Camera Distance** setting from 10 to **8**. 

If you have more questions or want to know more about it, you can find the Cinemachine documentation in the top menu bar **Cinemachine > About**.  


## UI 
UI stands for User Interface). We are going to set up a UI for game ending, when JohnLemon reaches the exit and the game fades out and quits. First, in the Hierarchy window, let's **Create > UI > Image**. This will create a few new GameObjects to your Scene. First, rename our Canvas to **FaderCanvas**. Then, select **EventSystem** and delete the GameObject. This GameObject allows any UI elements on the screen to interact with user input, however since JohnLemon doesn't need to be able to interact with the UI, we don't need it. 

To edit our image, switch to 2D mode by clicking the 2D button in the top bar of the Scene window. Select the **FaderCanvas** GameObject and focus on it by pressing **F**. Let's zoom in closer. In the inspector, notice how there is a **Rect Transform** component instead of Transform. Rect Transform gives more control over a GameObject's position, thus is normally used for UI objects. The Canvas component controls how UI elements that belong to that Canvas are rendered. The rendering is primarily controlled by the **Render Mode** setting. Render Mode setting has three potential modes: 

- Screen Space - Overlay, where the Canvas fills the screen and all the UI elements of the canvas are rendered on top of everything else 
- Screen Space - Camera, where the Canvas fills the screen but it is rendered to a specific camera and is subject to distance from the camera 
- World Space, where the UI exists in the Scene and is rendered in front or behind other objects (for example, name tags above characters in a 3D world) 

Since we need an Image across the screen and have it rendered over the top of everything, we will be using Render Mode **Screen Space - Overlay**. Next, we have **Canvas Scalar** component. This is used as an easy way of controlling the relative size of UI elements when they are displayed on different screen sizes. Since our image will be stretched across the entire screen, let's remove this component by clicking cog icon in the top right and selecting **Remove Component**. The last component is **Graphic Raycaster**. This is used to detect UI events such as clicks. Since the player won't interact with the UI, we can also remove this component by once again clicking cog icon and selecting **Remove Component**. 

Now, let's adjust the size of the image that will be displayed. Select the image GameObject from the Hierarchy. Now find **Rect Transform** in the Inspector and expand **Anchors** setting. Set the **minimum value for x and y to 0** and **maximum values for x and y to 1**. Anchors are relative to their parents - 0 means far left/bottom of the screen and 1 means far right/top of the screen. Then set **Left, Top, Right,** and **Bottom** properties of Rect Transform to **0**. Next, go to Image component and adjust the color property by setting RGB channels to **0**, and leaving the Alpha(A) at 1. 

Let's add a source image to our Image component. Rename ImageGameObject to **ExitImageBackground**. Right click the **ExitImageBackground** GameObject and select **UI > Image**. Name this GameObject **ExitImage**. Open Inspector of ExitImage and find the Image component and add a **Source Image**, **Won** from the dialogue box. Lastly, find the **Image Type** property and enable the **Preserve Aspect** checkbox. 

Now that we have our ExitImage, let's add a Canvas Group Component. **Canvas Group** allows you to control some aspects of all visible UI elements on a GameObject and all of its children. In the Hierarchy window, select the ExitImageBackground GameObject and add **Canvas Group** component. Set the **Alpha** property to **0**. We are done with making UI, so switch our Scene window back to level and **disable 2D Mode** in the Scene window. 

## Game Ending Trigger 
**Trigger** are Colliders that do not impede movement - instead they allow physical objects to pass through them freely, but report the triggering event so other actions can happen. We need a trigger to detect when JohnLemon has successfully escaped the haunted house. In the Hierarchy, create an empty GameObject and name it **GameEnding**. Set the position of GameEndings Transform to **(20, 1, 1.5)**. Add a **Box Collider** component to GameEnding GameObject and enable **Is Trigger** checkbox. Next, resize the trigger by clicking **Edit Collider**. Set the Size of the Collider to **(1, 1, 3.5)**. 

After this lesson, Transform component's Position of JohnLemon should be at (-9.8, 0, -3.2), Level at (0, 0, 0) and GameEnding at (20, 1, 1.5). 
