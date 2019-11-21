import React, { FC, useState } from 'react';
import { TextInput, Text, View, StyleSheet, Keyboard, Button } from 'react-native';

interface InputBoxProps {
    input: string;
    setInput(newText: string): void;
}

const InputBox: FC<InputBoxProps> = ({ input, setInput }) => {
    return (
        <View
        style={{
            alignItems: 'stretch',
            borderWidth: 0.5,
            borderColor: '#858D99',
            padding: 10,
            marginHorizontal: 20,
            marginVertical: 5,
            borderRadius: 12

        }}
        >
            <TextInput 
            onChangeText={(newText) => {
                setInput(newText);
            }}
            value={input} 
            returnKeyType="done"
            blurOnSubmit={true}
            onSubmitEditing={() => {Keyboard.dismiss}}
            placeholder="Type ingredient here"
            />
        </View>
    );
}

const InputScreen = ({ navigation }) => {
    const ingredients = navigation.getParam('words', ['', '', '']);
    const setIngredients = (words: string[]) => navigation.setParams({words: words});

    return (
        <View>
            <View style={styles.titleContainer}>
                <Text style={styles.title}>Ingredient Input</Text>
            </View>
            {ingredients.map((ingr, idx) => (
                <InputBox 
                    key={idx}
                    input={ingr}
                    setInput={(newIngr) => {
                        setIngredients([
                            ...ingredients.slice(0,idx), 
                            newIngr, 
                            ...ingredients.slice(idx+1)
                        ]);
                    }}
                />
            ))}
            <Button 
                title="Add ingredient"
                onPress={() => {
                    setIngredients([...ingredients, '']);
                }}
            />
            <Button 
                title="Submit"
                onPress={() => {
                    navigation.navigate('results', { ingredients: ingredients });
                }}
            />
        </View>
    );
}

const styles = StyleSheet.create({
    title: {
        fontSize: 20,
        fontWeight: 'bold'
    },
    titleContainer: {
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        margin: 20
    }
});

export default InputScreen;
