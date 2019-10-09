# Setup
Follow the instructions below to setup all the tools you need for the Ingredient Simplifier App :smile:

## NodeJS & npm
Almost all modern javascript development happens with NodeJS in some way. This will lay the foundation for the other tools we're about to install.

1. Install this: [https://nodejs.org/en/](https://nodejs.org/en/)

2. When it's done, open Command Prompt (Windows), or Terminal (Mac) and run the command `npm -v`. If it gives you a version number (e.g. `6.9.0`), then everything worked!

## Visual Studio Code (VSCode)
This is a text editor, which we will be using for most of the project. It comes with a lot of handy tools to help you write better code.

1. Install it here: [https://code.visualstudio.com/download](https://code.visualstudio.com/download)
2. Open it to see if it works

## Expo
This is a library built on top of *React Native*, which greatly simplifies the app development process.

1. Create a free account here: [https://expo.io/](https://expo.io/)
2. Download the Android/iOS app on your phone (just look up `Expo` in the App Store/Google Play Store)
3. Run the command `npm install -g expo-cli` from the command line (Terminal/Command Prompt)
> *Note: NodeJS & npm must already be installed before you run this command*

## Yarn
This is a package manager that is *faster* than the default **n**odejs **p**ackage **m**anager (npm). It will help us download and organize all the code libraries that our project requires in order to run.

1. For Mac users, you will first need to install Homebrew: [https://brew.sh/](https://brew.sh/)
2. See installation instructions here: [https://yarnpkg.com/en/docs/install](https://yarnpkg.com/en/docs/install)

### If you have setup everything thus far, you're doing good! This is all that we need for the first 1 or 2 lessons

## Git (CLI) [Recommended]
This is a version control software, which allows for easy collaboration in teams. Depending on time, we may or may not cover how to use Git. 

> *Note: This is **not** the same as the "GitHub client".*
1. Install this: [https://git-scm.com/downloads](https://git-scm.com/downloads)

2. When it's done, restart Command Prompt or Terminal and run the command `git --version`. If it gives you a version number, then everything worked!

## Github [Recommended]
This is a platform that connects with Git, allowing you to share your code with the world. It also plays a part in allowing teams of programmers to collaborate on a project. We may or may not cover how to use Github, depending on time.

1. Create an account if you don't already have one: [https://github.com](https://github.com/)

## Firebase [For Later Use]
This is a suite of cloud tools that will help us manage the *backend* aspect of our app. Any kind of database access, user logins, or machine learning algorithms will somehow be related to Firebase.

1. Go to this site: [https://console.firebase.google.com](https://console.firebase.google.com/). Sign in using your Google Account, and click `Create a Project`. Choose an appropriate project name, and select all the default (free) options. After this, you can close that tab -- that's all the web setup we need for now :)

2. Now, in order to set up the CLI interface, open Terminal/Command Prompt and run `npm install -g firebase-tools`
> *Note: NodeJS & npm must already be installed before you run this command*
