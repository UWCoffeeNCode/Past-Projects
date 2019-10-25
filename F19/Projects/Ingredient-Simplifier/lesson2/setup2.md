# Setup: Part 2
In the previous setup tutorial, we installed all the required dependencies. Now it's time to get the project running on your phone/laptop :)

> If you have any problems, please message me on Slack or ask me at the next workshop

1. **Open the command line and navigate** to the directory that you would like, using the `cd <folder>` command. If you're unsure which directory you're currently in, run the command `ls` to see what files are in your current directory. 
> Please note: Any instruction that includes angle brackets like `<this>` should **NOT** include angle brackets when you fill it in with a value. 
e.g. `<your name here>` = `David` ≠ `<David>`
```
 ~ $ ls
Applications  Documents  Library  Music  Pictures  dev
Desktop  Downloads  Movies  MyFirstGame  Public  opt
~ $ cd dev
~/dev $
```
I recommend that you make a `/dev` folder if you don't have one already; it's a good way to keep your coding projects organized.

> The `~ $` and `~/dev $` may look slightly different, depending on how your ["PS1"](https://mattmazur.com/2012/01/27/how-to-change-your-default-terminal-prompt-in-mac-os-x-lion/) variable is set up. This won't affect your code, it just looks nice.

2. **Create the template expo project.**
Run the command `expo init ingredient-simplifier`. 
It will prompt you to choose a template, choose the `blank (Typescript)` option. 
It will then ask you to type in a name; you can type in `Ingredient Simplifier`. 
If you have installed Yarn correctly, it will ask if you want to use yarn: type `Y` and then hit `Enter`. 
This should take some time to finish loading...

3. **Run the Bundler.**
If you haven't already, type `cd ingredient-simplifier` -- this is the main project folder where all your code will be stored.
Now run `yarn start` to start the bundler.

4. **Connect your device.**
Normally you would download the Expo app on your mobile device, and scan the QR code to see a live demo of your app -- *this is not possible at Coffee N' Code workshops due to increased latency with so many wi-fi users*. Instead, you should connect your Android/iOS device **by USB cable**, and follow the command line's instructions to run the app on that device.
If this worked, you should be able to see `Open up App.tsx to start working on your app!` on a blank screen. Please don't hesitate to ask me questions in Slack if anything goes wrong.

If for whatever reason you can't connect your device via USB cable, you could also try running it on an emulator/simulator. I recommend installing [Android Studio](https://developer.android.com/studio), and choosing `AVD Manager` from either here: ![accessing avd manager from Android Studio main screen](https://i.imgur.com/qQIlP0u.png) 

or here:![accessing avd manager from Android Studio project screen](https://i.imgur.com/EeRv8Ro.png)

Create whichever modern android device you would like to emulate and download the appropriate version of Android sdk to be installed on that device. 

Alternatively, Mac users can set up an iPhone simulator even easier with XCode -- just download XCode from the App Store, and you can Spotlight Search for "Simulator".
> Note: XCode is a **large** download. Make sure you have enough time to download it, and enough space on your drive.


## Hooray! We're done!

![iPhone Simulator, simulating the empty project](https://i.imgur.com/2ZcIv03.png)

At this point, you should start VSCode, open the `ingredient-simplifier` folder, and start playing around with the code. Just make sure that you save after each code change, and you'll be able to see the changes live on your mobile device.
