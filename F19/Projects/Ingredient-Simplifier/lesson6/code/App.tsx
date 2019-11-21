import React from "react";
import { SafeAreaView } from "react-native";
import AppContainer from "./navigation/AppContainer";

const App = () => (
  <SafeAreaView style={{ flex: 1, backgroundColor: "#ddd" }}>
    <AppContainer />
  </SafeAreaView>
);

export default App;
