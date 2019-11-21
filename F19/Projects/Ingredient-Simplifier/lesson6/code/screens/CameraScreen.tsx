import React, { useEffect } from "react";
import { Text, View, StyleSheet } from "react-native";
import * as Permissions from 'expo-permissions';
import { RNCamera as Camera, TrackedTextFeature } from 'react-native-camera';
import { Icon } from 'react-native-elements';

interface CameraScreenProps {
  navigation: any
}

interface CameraScreenState {
  hasCameraPermission: boolean | null;
  textBlocks: TrackedTextFeature[];
}

export default class CameraScreen extends React.Component<CameraScreenProps> {
  state: CameraScreenState = {
    hasCameraPermission: null,
    textBlocks: []
  };

  async componentDidMount() {
    const { status } = await Permissions.askAsync(Permissions.CAMERA);
    this.setState({ hasCameraPermission: status === 'granted' });
  }

  renderBoxes() {
    if(this.state.textBlocks == []) {
      return <></>;
    }
    return this.state.textBlocks.map((textBlock) => {
      const left = textBlock.bounds.origin.x;
      const top = textBlock.bounds.origin.y;
      const width = textBlock.bounds.size.width;
      const height = textBlock.bounds.size.height;
      return (
        <View key={left + " " + top} style={{
          position: 'absolute',
          left: left,
          top: top,
          height: height,
          width: width,
          borderColor: 'green',
          borderWidth: 2
        }} />
      );
    });
  }

  render() {
    const { hasCameraPermission } = this.state;
    if(hasCameraPermission === null) {
      return (<Text>Need permission!</Text>);
    } else if(hasCameraPermission === false) {
      return (<Text>Need permission!</Text>);
    } else {
      return (
        <>
        <Camera 
          style={{ flex: 1, justifyContent: 'flex-end' }} 
          type={ Camera.Constants.Type.back }
          onTextRecognized={(textBlocks) => {
            this.setState({ textBlocks: textBlocks });
          }}
        >
          <Icon 
            name='camera'
            type='font-awesome'
            color='green'
            onPress={() => {
              const words = this.state.textBlocks.map(({value}) => value);
              this.props.navigation.navigate('input', { words: words });
            }}
          />
        </Camera>
        {this.renderBoxes()}
        </>
      );
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
  