# Lesson 1: Getting to know Unity, building our player

This lesson we will be installing our key tools and learning a bit more about the engine.

## Installing Unity

Start by making a [Unity ID](https://id.unity.com/), you will need this later to use the tool

 heading to the [Unity Download Page](https://unity3d.com/get-unity/download) and click the "choose your unity + download" button.

<p align="center">
  <img src="https://i.imgur.com/wMBbRHA.png" width="650"/>
</p>

At the next page, please select "personal edition"

<p align="center">
  <img src="https://i.imgur.com/lFZBq8v.png" width="650"/>

Once the installer is done downloading, open it and begin the installation process by following the instructions on screen.
When prompted with the **Components** page, please select **Unity**, **Mac Build Support**, **Visual Studio** (if you don't already have it) and **Windows Build Support**. You may now proceed with the rest of the installation.

<p align="center">
  <img src="https://i.imgur.com/Fnl3He0.png" width="400"/>
</p>

## Importing our project

Once Unity is done installing, please open it and sign in with your Unity ID.
You will need to create a new project to work with our assets. You will find the tutorial project in the **Learn** tab under **Tutorial Projects**. Select this tab and scroll down until you find the **Space Shooter** project, and click **Download**.

<p align="center">
  <img src="https://i.imgur.com/12lOFec.png" width="650"/>
</p>

Once the download is complete, please click start, and wait for Unity to load.

When the project is open, please **immediately** attempt to close the window, and this will prompt a dialogue box indicating whether or not you want to keep the project. Please select **Keep** and save the project to a location of your choice with a good name.

Re-open Unity and you should see your project now in the **Projects** tab, click it and it should open.

**Now you're ready to rock n' roll!!!**

## Creating a new scene

Do your friends always give you s#!t for making a scene? Well joke's on them, we are about to give that phrase a whole new meaning.

Now that you have the project and Unity set up, the first thing we want to do is create a new **Scene**. Scenes are like a snapshot of a game world we want to work in; there can be many scenes in one game! (similar to how there may be many levels in a game)

Click on your Assets folder to select it, and right click to hover over **Create**. From here a menu should appear, and you should be able to select **Folder**. Name the new folder *Scenes*

<p align="center">
  <img src="https://i.imgur.com/1Bs1LOk.jpg" width="650"/>
</p>

Now look in the top left corner of the editor for the **File** dropdown, and within it select **New Scene**. This will open a new scene and view it in Scene view right away.

<p align="center">
  <img src="https://i.imgur.com/fyNgA5y.png" width="650"/>
</p>

Now that we have created the new scene, open the **File** dropdown again and select **Save**, NOT Save Project. This Save will save the *currently open scene*. Give the scene a pretty new name and save it to our newly created scenes folder!

## Constructing our Player GameObject

Some say "Don't hate the player, hate the game", but I believe that we don't have to hate either.

To make the spaceship our player will control, navigate to the **Project View** and find the **Models** folder. Within this folder you should be able to find the *vehicle_playerShip* model. Click on the model once to select it, and drag n' drop it over to the **Hierarchy**.

<p align="center">
  <img src="https://i.imgur.com/IVW8lnZ.png" width="650"/>
</p>

Once the new GameObject is in the Hierarchy, click it to select it. You should see the **Inspector** on the right hand side change to show you the components of the GameObject. Components are the features we give to our GameObjects, they can be from Unity or we can make them ourselves! Locate the **Transform** component, and click the little gear icon to the right of the component. This will bring up a menu and you should be able to select **Reset** to recenter the GameObject to the world origin.

Scroll down the Inspector to find the **Add Component** button, and click it once to bring up the search bar. Search for **Rigidbody** (NOT Rigidbody 2D) and click it to add it.

You should now see a new component in the Inspector! Within the Rigidbody component there should be a checkmark next to **Use Gravity**, please **UNSELECT** this. We will be moving the player GameObject with our onw forces, not gravity.

Perform the same steps using the Inspector and the Add Component button to add a **Mesh Collider** component. There are many kinds of collider components, but we will be using the Mesh Collider. To keep physics calculations simple and our performance good, we will be providing a much similar mesh compared to the one Unity uses for our player. Click the little tiny circle next to the **Mesh** field on the Mesh Collider component. This will bring up a menu with all possible meshes we can use for our Mesh Collider, so select *player_ship_collider*. You will notice the green mesh that shows our collider becomes a much more simple shape.

<p align="center">
  <img src="https://i.imgur.com/IUpDBq8.png" width="650"/>
</p>

Finally, what's a spaceship without some rockets?! We will add some particles to show our rocket trail, and you can find them in the folder Assets/Prefabs/VFX/Engines. The GameObject you are looking for is called *engines_player*. Drag and drop this GameObject **ON TOP OF** the player GameObject we made earlier. You should see a little arrow appear next to the player GameObject after, and if you expand this arrow you will see the engine effects are **Parented** to the player GameObject. This means they will now stick to the player and follow them, as all good rockets do.

<p align="center">
  <img src="https://i.imgur.com/YzmlvjT.png" width="650"/>
</p>
