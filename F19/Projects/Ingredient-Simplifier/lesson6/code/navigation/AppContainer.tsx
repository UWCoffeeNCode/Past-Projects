import { createAppContainer } from "react-navigation";
import { createMaterialTopTabNavigator } from "react-navigation-tabs";
import CameraScreen from "../screens/CameraScreen";
import ResultsScreen from "../screens/ResultsScreen";
import AboutScreen from '../screens/AboutScreen';
import InputScreen from '../screens/InputScreen';

export default createAppContainer( 
  createMaterialTopTabNavigator( 
    {
      camera: CameraScreen,
      results: ResultsScreen,
      about: AboutScreen,
      input: InputScreen
    },
    {
      initialRouteName: "camera",
      tabBarOptions: {},
      tabBarPosition: "bottom",
      swipeEnabled: true
    }
  )
);