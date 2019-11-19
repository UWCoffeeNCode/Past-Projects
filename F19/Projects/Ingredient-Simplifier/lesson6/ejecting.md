
# Ejecting

We need more functionality than Expo can provide, so we're going to convert to a "pure" react native project (which is called "ejecting").

### app.json
In `app.json`, find the part that says
```
"ios": {
	"supportsTablet": true
}
```
and modify it to this:
```
"ios": {
	"supportsTablet": true,
	"bundleIdentifier": "com.yournamewithoutspaces.ingredientsimplifier"
},
"android": {
	"package": "com.yournamewithoutspaces.ingredientsimplifier"
}
```
*this is a very sensitive file -- be sure to match the brackets, commas, and quotation marks __exactly__.* If there is any red (error) underlining from your editor, you have probably done something wrong.

### Optional: Save your progress with git

Just in case something goes wrong, you might want to be able to revert back to your working project. If you don't have git installed (you can check by running `git -v`), you can download it [here](https://git-scm.com/downloads)

In your root director, run:
`git init`
`git add .`
`git commit -m "initial commit"`

if everything went well, you should be able to run `git log --oneline` and see something like this:
```
bca6850 (HEAD -> master) initial commit
```
If you ever want to revert back to that state, take the "hash" code on the far left (in my case it's `bca6850`) and run the command `git reset bca6850`.

### Run `expo eject`

Run `expo eject` and it will prompt you to select a few options.
Choose:
```
? How would you like to eject your app?
❯ Bare: I'd like a bare React Native project.
```

```
? What should your app appear as on a user's home screen? (Ingredient Simplifier)
❯ Ingredient Simplifier
```

```
? What should your Android Studio and Xcode projects be called?
❯ ingredientsimplifier
```

### Change to `react-native-camera`
We can no longer use `expo-camera` or `expo-permissions` because we have ejected from expo. Instead we're going to be using `react-native-camera`.

First, uninstall the old modules.
```
yarn remove expo-camera expo-permissions
```
Now install react-native-camera:
```
yarn add react-native-camera
npx react-native link react-native-camera
```

But react-native-camera works a bit differently from expo-camera: it doesn't request permissions within your react-native code: it only asks for permissions when the app is launched. 

Open up `android/app/build.gradle` and `Ctrl+F` to search for the keyword `defaultConfig`. You should see a block of code that looks something like this:
```
defaultConfig {
	applicationId "com.ingredientsimplifier"
	minSdkVersion rootProject.ext.minSdkVersion
	targetSdkVersion rootProject.ext.targetSdkVersion
	versionCode 1
	versionName "1.0"
}
```
Add in the line `missingDimensionStrategy 'react-native-camera', 'general'` such that it looks like this:
```
defaultConfig {
	applicationId "com.ingredientsimplifier"
	minSdkVersion rootProject.ext.minSdkVersion
	targetSdkVersion rootProject.ext.targetSdkVersion
	versionCode 1
	versionName "1.0"
	missingDimensionStrategy 'react-native-camera', 'general'
}
```

Lastly, we need to modify `screens/CameraScreen.tsx` so that it uses `react-native-camera` rather than `expo-camera`. Just change the import line at the top from this:
```
import { Camera } from  'expo-camera';
```
to this:
```
import { RNCamera  as  Camera } from  'react-native-camera';
```

### Test It!

With your android emulator running, you should be able to run `npx react-native run-android`, which will:
1) Open a new window called `Metro Bundler`. **Do not close this window**, or else your code won't load onto the device.
2) Start building your app -- this will be a long process the first time (2-3 minutes), but it will be a lot quicker for subsequent builds.

If it gives you an error, call me over (or DM me on slack). Otherwise, you're ready to move on to 
implementing text recognition.
