## Setting up Navigation

See this documentation if anything is ambiguous, or just come ask me and I can try to help figure it out.

1. Create two folders in your main project directory: `screens` and `navigation`. Your folder structure should look something like this (ignore the colors for now): 

![example folder structure](https://i.imgur.com/EZ0B5rj.png)

2. Inside your `navigation` folder, create a new file called `AppContainer.tsx`.

3. Inside of your `AppContainer.tsx`, import the necessary libraries, and use `createAppContainer` and `createMaterialTopTabNavigator` in order to export your App Container. (if that was too complicated, just copy the code below and I'll explain later.) This code *will* cause some errors -- we will resolve those in the next few steps.
```
import { createAppContainer } from "react-navigation";
import { createMaterialTopTabNavigator } from "react-navigation-tabs";
import CameraScreen from "../screens/CameraScreen";
import ResultsScreen from "../screens/ResultsScreen";
import AboutScreen from '../screens/AboutScreen';

export default createAppContainer(
  createMaterialTopTabNavigator(
    {
      camera: CameraScreen,
      results: ResultsScreen,
      about: AboutScreen
    },
    {
      initialRouteName: "camera",
      tabBarOptions: {},
      tabBarPosition: "bottom",
      swipeEnabled: true
    }
  )
);
```

also run `yarn add react-navigation`, `yarn add react-navigation-tabs`, `yarn add react-native-gesture-handler`, and `yarn add react-native-reanimated`. **important**

4. In the `screens` folder, create the files `CameraScreen.tsx`, `ResultsScreen.tsx`, and `AboutScreen.tsx`

5. In each of those files, paste the following template code, and fill in the blanks (remove the square brackets):
```
import React from "react";
import { Text, View } from "react-native";

export default function [Blank]Screen() {
  return (
    <View>
      <Text>This is the [blank] screen</Text>
    </View>
  );
}
```

6. Now we just need to connect this to the main component. Firstly, if you have any code from the previous lesson, you can move that into `screens/AboutScreen.tsx`. Once that is moved, in `App.tsx` replace everything with the following code:
```
import React from "react";
import { SafeAreaView } from "react-native";
import AppContainer from "./navigation/AppContainer";

const App = () => (
  <SafeAreaView style={{ flex: 1, backgroundColor: "#ddd" }}>
    <AppContainer />
  </SafeAreaView>
);

export default App;
```

7. You can now run your app with `yarn start` and it should come up with something like this:
![the result of our navigation setup](https://i.imgur.com/BKY0vmI.png)
