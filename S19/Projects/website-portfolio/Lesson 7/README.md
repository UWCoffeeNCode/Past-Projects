## PUTTING YOUR WEBSITE ONLINE

Onboarding:
+ create a GitHub account

This is gonna involve doing a lot of terminal work now! We are going to get our websites up online, and provide a tutorial for updating your website's online version whenever you change the content. GitHub kindly lets you host free **github pages**, which is what we will be using to host our site, but if you later decide to purchase a URL (details below), you can fairly simply keep the website repository on GitHub and change the URL.

## STEP 0: WHAT IS GITHUB

Three things to note:

**1)Working Directory:** folder where our codes file are present

**2)Local Repository:** This is inside our system. When we first time make COMMIT command then this Local Repository is created. in the same place where is our Working directory ,
Checkit ( .git ) file get created.
After that when ever we do commit , this will store the changes we make in the file of Working Directory to local Repository (.git)

**3)Remote Repository:** This is situated outside our system like on servers located any where in the world . like github. When we make PUSH command then codes from our local repository get stored to this Remote Repository

## STEP 1: CREATE A REPOSITORY AND PUT WEBSITE CODE ON GITHUB
+ Can look <a href="https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line">here</a> for more information, or elsewhere on the web :) 
From the Github interface, we are going to create a new repository with the New button. Our repository has to be called your-username.github.io - this is important!

Now navigate to your website folder on the terminal, and type

```
git init
```
This command initializes the folder as a repository.

Now we will connect it the repository we created on Github. Go back to Github, and copy the address that looks like `github.com/username/repository-name.git`

Now back on the terminal, type

```
git remote add origin your-remote-repository-URL
git remote -v
```
This second line doesn't do anything -> it'll just print to confirm the first step was done successfully!

Now we will add our files to Git, by typing
```
git add .
```
And commit them with
```
git commit -m "First commit"
```
Where the "First commit" is just a comment (use the ```-m``` control for this) - it can say anything you want!

Now by typing
```git push -u origin master```
It will push your changes to the Github website! You can reload it now to see :D

## STEP 2: SETTING UP GH-PAGES

1) Navigate to your repository, where there should be series of tabs at the top.

2) Click on Settings. 

3) Scroll down to GitHub Pages section, and select a source. This is the branch or directory in your repository that you want to be the root of your webpage. We are going to pick the master branch. Click Save.

4) Now scroll back down to that same section, and you will see that your site is now published!!  Click on the link to take a look :)

## MAINTAINING/ UPDATING YOUR CODE

This diagram does a good job of illustrating the commands for git. We will be going over it in class. 

![alt text](https://i.stack.imgur.com/MgaV9.png)

**git commit:** records changes to the local repository (the one on your computer)

**git push:** updates your remote repository (the one on GitHub) by applying changes from local into remote

The syntax of this command is usually ```git push <remote> <branch>```. A remote is the address of a cloned repository. Most projects work with an ```origin``` remote and the ```master``` branch by default.
  
In our above code, we used ```git push -u origin master```. So we PUSHED the content from our LOCAL repository to our REMOTE one (origin is the address, master is the branch). There's also that strange "-u" option. What it does is next time we want to push, we won't need to type the entire thing again. Instead, we just just type ```git push```.

**git pull:** apply changes from remote into local 
