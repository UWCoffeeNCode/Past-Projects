# Lesson #1 Agenda:

**Objectives**: 
- join our [Slack](https://uwcoffeencode.slack.com)
- follow us on [GitHub](https://github.com/UWCoffeeNCode/Lessons)
- collect group names & emails
- install technologies & tools and learn about them
- write "Hello World, my name is [name]!" with HTML
- share your first webpage on GitHub Pages

## 1. Installing and Explaining our Tools

### 0. Sublime Text Editor
In this project, we will only require one text editor and any text editor will be suitable for this proejct (eg. Notepad, Notepad++, etc.). We will specifically working with [Sublime Text 3](https://www.sublimetext.com/3)

<img src="https://upload.wikimedia.org/wikipedia/en/d/d2/Sublime_Text_3_logo.png" alt="Sublime Text logo" width="300px"/>

### 1. HTML
HTML stands for Hyper Text Markup Language. HTML is the language we will use to structure and define our web page. 

Each HTML file is one web page and vice versa.

HTML by itself looks bland, but we can fix that with CSS.

There is no installation required for HTML, CSS, or JavaScript. 

<img src="https://www.planet-source-code.com/vb/2010Redesign/images/LangugeHomePages/HTML5_CSS_JavaScript.png" alt="HTML, CSS, JS logos" width="500px"/>

### 2. CSS
CSS stands for Cascading Style Sheets. CSS is the language we use to style our HTML to make it look more interesting.

CSS allows you to make your web page less boring by adding colours, adjusting text sizes, moving pictures, and more!

Writing HTML and CSS all by yourself is time-consuming, but we can speed things up with Bootstrap 4.

### 3. Bootstrap 4
Bootstrap 4 is a styling framework, meaning Bootstrap is a lot of HTML and CSS bundled together for easier use. Think of Bootstrap as "HTML and CSS but with shortcuts", except you need to understand the basics of HTML and CSS in order to use the shortcuts properly.

Bootstrap 4 allows you to make responsive web pages more easily, meaning the web pages will look good on different screen sizes such as your phone, tablet, laptop, or TV.

We will install Bootstrap 4 in a future lesson.

### 4. JavaScript
JavaScript is a programming language that allows you to add behaviour to your website.

We will use JavaScript to make buttons that will filter our side projects based on categories.

JavaScript is powerful, but most of our web site will be using HTML, CSS, and Bootstrap.

### 5. jQuery
jQuery is a JavaScript library, meaning jQuery is a lot of JavaScript bundled together for easier use, just like how Bootstrap is a lot of HTML and CSS bundled together.

jQuery makes it easier to update your web page contents by modifying HTML.

We will install jQuery in a future lesson. 

## 3. Coding

### 1. "Hello World" with HTML
**Objective**: write our first webpage

**Hints & Resources**: If you get stuck at any point at this part, [visit w3schools](https://www.w3schools.com/html/default.asp) for more instructions or ask one of us for help! Googling is always a good option too!

**Instructions**:
1. make a text file on your desktop named "index.html"
2. edit the textfile and write the code snippet below but with your name instead of "NAME"
```html
<html>
	<h1>hello world, my name is NAME!</h1>
</html>
```
3. open index.html with any web browser you want (eg. chrome, firefox, internet explorer,etc.); you can do this by dragging and dropping index.html onto your browser icon on your desktop
4. you should see "hello world, my name is NAME!" at the top of your web page, but with your name instead of "NAME"

### 2. "Hello World" on GitHub
**Objective**: share our first webpae on GitHub pages to share with each other

**Hints & Resources**: If you get stuck at any point at this part, [go here for more instructions](https://pages.github.com/) or ask one of us for help! Googling is always a good option too!

**Instructions**:
1. create a GitHub account (ask Ahrar if you need help!)
2. go to "your profile" by clicking in the top right
3. click "Repositories"; you shouldn't have any yet if you just made an account
4. click "New" in green to make a new repository
5. enter "profileName.github.io" as your repository name, but with your profile name instead of "profileName"
6. click "create repository" in green at the bottom
7. go back to your github profile and click the repository we just made
8. click "upload files" on the right and select "index.html"
9. press "commit changes" at the bottom
10. while still looking at your repository, click "settings" on the top right
11. scroll down to "GitHub Pages" and select "master branch" under "source" and click save
12. go to "http://profileName.github.io/repository" but with your actual profile name instead of "profileName"
13. you should see the same web page you saw in part 1, but now it is being hosted on github pages instead of your laptop
14. share the link to your webpage with other people in your group via slack!

## 4. Optional Homework, Excellent for Practice & Learning!
- Check out w3schools and their awesome HTML/CSS tutorials!
[HTML Tutorial](https://www.w3schools.com/html/default.asp)
[CSS Tutorial](https://www.w3schools.com/css/default.asp)
- Watch some of this [HTML/CSS tutorial video playlist](https://www.youtube.com/watch?v=pm5OVxpul48&list=PL0eyrZgxdwhwNC5ppZo_dYGVjerQY3xYU&index=2) to get ahead!
- Try [changing the text colour and background colour](https://www.w3schools.com/html/html_colors.asp)
- Try [inserting pictures onto your web page](https://www.w3schools.com/html/html_images.asp)

## 5. Homework Solutions
Adding text colour:
```html
<html>
	<h1 style="color: green">hello world, my name is Michael!</h1>
</html>
```

Adding background colour:
```html
<html>
	<h1 style="color: green; background-color: pink">hello world, my name is Michael!</h1>
</html>
```

Inserting a picture onto your web page:
```html
<html>
	<h1>hello world, my name is Michael!</h1>
	<img src="https://i.ytimg.com/vi/wRx3Uvcktm8/maxresdefault.jpg">
</html>
```