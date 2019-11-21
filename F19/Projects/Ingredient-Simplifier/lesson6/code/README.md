# Lesson 6

In this week's final workshop, we ejected from Expo into a bare React-Native project. Although we had some technical difficulties at the end of the class, all of the code necessary to fix those issues should be provided here. You can also access all of my project files, and see if your code looks similar (your code doens't need to be *exactly* the same as mine, just make sure that it runs).

In addition, while we do have some basic styling built into our app, I'm going to publish another version of the project with some more styling that you can look over as an example or copy if you'd like -- nothing that we haven't already covered. 

## Corrections

Two small (but crucial) corrections that I have made from the code that we used in the workshop:

`screens/InputScreen.tsx`
old:
```
  const setIngredients = (words: string[]) => navigation.setParams('words', words);
```
new:
```
  const setIngredients = (words: string[]) => navigation.setParams({words: words});
```


`screens/CameraScreen.tsx`
old:
```
  const words = this.state.textBlocks.map(({word}) => word);
```
new:
```
  const words = this.state.textBlocks.map(({value}) => value);
```

## Running on iOS

In class, we built our app on an Android emulator; 
for Mac users who want to test on iPhone, you first need to install cocoapods with `sudo gem install cocoapods`.
You can then run the commands `cd ios` and `pod install`, before returning to your main project
directory (i.e. `cd ..`) and running `npx react-native run-ios` (this takes a looooong time to build).


## Future Resources

If you like React Native, you might want to try out [ReactJS (for web)](https://reactjs.org/) -- a popular way to build highly-responsive web apps. And now that you've used React Native, you will already be a pro with ReactJS!

Although we didn't end up using firebase mlkit as expected, you could still take a look at the [`react-native-camera` documentation](https://github.com/react-native-community/react-native-camera); they have a slightly-more-complicated setup that [uses firebase mlkit](https://github.com/react-native-community/react-native-camera/tree/master/examples/mlkit) for text recognition rather than their default text recognition. The advantage is that firebase mlkit has slightly better quality text-recognition algorithms, so it will be able to detect more than the standard algorithms.

It's been great coding with you guys. I hope to see you at the CoffeeNCode EOT event this Wednesday, Nov 27, and you can always chat with me in Slack. Thanks for being a part of CoffeeNCode! :)

