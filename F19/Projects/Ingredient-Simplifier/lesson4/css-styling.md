# CSS Styling

This document will outline all the basic CSS styling things that you should know before building your app. Remember that React style names are the same as regular style names, but they use `lowerCamelCaseNames` rather than `dash-separated-names`.

## Colors

[https://www.w3schools.com/css/css3_colors.asp](https://www.w3schools.com/css/css3_colors.asp)

`backgroundColor: "#A2D729"` determines the color of the background.

`color: "blue"` determines the color of the text.

Colors can be specified in RGB, Hex or String (for popular colors).

A nice color picking tool: [https://coolors.co/app](https://coolors.co/app)

You can also use gradients: [https://www.w3schools.com/css/css3_gradients.asp](https://www.w3schools.com/css/css3_gradients.asp)

## Fonts

[https://www.w3schools.com/css/css_font.asp](https://www.w3schools.com/css/css_font.asp)

`fontFamily: "Times New Roman"` sets the font.

`fontSize: 30` determines the size of the font (usually measured in pixels).

## Borders

[https://www.w3schools.com/css/css_border.asp](https://www.w3schools.com/css/css_border.asp)

`borderWidth: 5` sets the width of a box's border.


`borderColor: "green"` sets the color of the box's border.


## Margins & Padding

[https://www.w3schools.com/css/css_boxmodel.asp](https://www.w3schools.com/css/css_boxmodel.asp)

**Margin** deals with the buffer between the container and its parent. **Padding** deals with the buffer between the objects inside the container and the container itself. This is best understood by demonstration.

`marginTop: 5`  sets the top margin

`marginBottom: 2` sets the bottom margin

`margin: 5 6 7 8` sets the top = 5px, right = 6px, bottom = 7px, left = 8px.

`margin: 5 6 7` sets the top = 5px, right & left = 6px, bottom = 7.

`padding` uses the exact same syntax.

## Flexbox

`flexDirection: "column"` says that all the children should be aligned into a column.

`flexDirection: "row"` says that all the children should be aligned into a row.

`justifyContent: "center"` aligns items along the main-axis 
* row = horizontal positioning
* column = vertical positioning
<br/>

`alignItems: "center"` aligns items along the secondary-axis
* row = vertical positioning
* column = horizontal positioning

<br/>
`alignContent` only applies to text that wraps around to the next line.


Use this tool if you're unsure how your code will look: [http://flexbox.buildwithreact.com/](http://flexbox.buildwithreact.com/)
