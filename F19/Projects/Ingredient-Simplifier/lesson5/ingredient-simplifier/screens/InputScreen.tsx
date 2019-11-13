import React, { FC } from 'react';
import { TextInput, Text, View, TextStyle } from 'react-native';

const TableItem: FC = () => {
    const [input, setInput] = React.useState('hello');

    return (
        <View
        style={{
            flex: 1,
            alignItems: 'stretch',
            padding: 10,
            borderWidth: 0.5,
            borderColor: '#858D99',
            margin: 20
        }}
        >
            <TextInput 
            onChangeText={(newText) => {
                setInput(newText);
            }}
            value={input} 
            editable
            />
        </View>
    );
}


const InputScreen = () => {
    return (
        <View>
            <TableItem />
            <TableItem />
            <TableItem />
            <TableItem />
            <TableItem />
        </View>
    );
}

export default InputScreen;
