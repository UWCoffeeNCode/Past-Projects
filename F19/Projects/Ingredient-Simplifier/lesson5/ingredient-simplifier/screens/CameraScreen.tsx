import React, { useEffect } from "react";
import { Text, View, StyleSheet } from "react-native";
import * as Permissions from 'expo-permissions';
import { Camera } from 'expo-camera';

export default class CameraScreen extends React.Component {
  state = {
    hasCameraPermission: null
  };

  async componentDidMount() {
    const { status } = await Permissions.askAsync(Permissions.CAMERA);
    this.setState({ hasCameraPermission: status === 'granted' });
  }

  render() {
    const { hasCameraPermission } = this.state;
    if(hasCameraPermission === null) {
      return (<Text>Need permission!</Text>);
    } else if(hasCameraPermission === false) {
      return (<Text>Need permission!</Text>);
    } else {
      return <Camera style={{ flex: 1 }} type={ Camera.Constants.Type.back }/>      
    }
  }
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#EDE3E9',
      alignItems: 'center',
      justifyContent: 'center',
      borderWidth: 5,
      borderColor: "orange",
      marginBottom: 50,
      marginTop: 80,
      padding: 50
    },
    mytext: {
        color: "blue",
        fontFamily: "Times New Roman",
        fontSize: 80
    }
  });
  