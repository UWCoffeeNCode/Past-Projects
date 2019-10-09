# Lesson 2: Ruby and Embedded Ruby
So as a refresh, in Lesson 1 we covered: setup, app creation, overview of parts of a Rails app, and made some static pages (Home and Help). If you haven't done these things please take a look at Lesson 1: https://github.com/UWCoffeeNCode/Lessons/tree/master/F18/Projects/rails-app/1.

In this lesson, we'll be covering
1. Ruby
	- Interactive ruby
	- Ruby syntax basics
	- Functions
2. Embedded Ruby
	- Three objectives to do

## Main Objectives:
These objectives are to be completed by the end of the session. This is meant to keep adding onto your app when you learn new concepts!
### Objective 1: Create an About page
### Objective 2: Display different titles on our different pages
### Objective 3: Add a picture in embedded ruby
### Objective 4: Use a loop in embedded ruby

## 1. Ruby
Ruby is an intuitive programming language that has syntax similar to that of Python if you're familiar with that language. The main differences are in iteration and class definition. 


### 1.1 Interactive Ruby / Rails console
Since you already have ruby installed, you'll have irb (interactive ruby). Interactive ruby is a quick way to access the ruby programming language without creating a new file. To launch irb, go to your (bash) terminal and type "irb".

Alternatively, you could also access rails console, which is a powerful tool when creating your app. It's built on irb, which allows playing around with ruby but it does much more than just that. Once we have our database set up, we can play around with our objects and things on the rails console, which we can't do from irb. To launch, go to your app folder in terminal and type "rails console".
### 1.2 Ruby syntax basics
So now that we're in an interactive ruby terminal, we're going to go over strings, numbers, and loops. 
#### Strings
Strings are a basic ruby type. They look like `'this is a string'` in ruby, but there are double-quoted strings and multi-line strings as well.
#### Numbers 
Numbers in ruby are just that: numbers. Try typing in the following and pressing enter in irb or rails console:
```ruby
1 + 6 / 2
```
#### Loops
Loops in ruby look like any other language: you have your condition, executing block, and end. In the case below, **loop** is a special ruby method that keeps looping until you stop it (by hitting CTRL + C). Try it out by typing the below code block into irb.
```ruby
loop do 
puts "This will keep printing until you hit Ctrl + c"  
end
```
Below is a more complex example, with some actual conditions. The `break` keyword stops execution of the loop and exits when invoked.
```ruby
i =  0 
loop do i +=  1 
puts i 
break  # this will cause execution to exit the loop  
end
```
#### While loops
While loops look pretty much the same. In the code below we are creating a variable x, which is an instance of the ruby class Fixnum (https://ruby-doc.org/core-2.2.0/Fixnum.html). We check if x is odd with`x.odd?` (which is a handy public method defined in the Fixnum class) and if it is, we print it out. Try the code!
```ruby
x = 0
while x <=  10  
if x.odd? # checking if x is odd
puts x 
end 
x +=  1  
end
```
#### For loops 
For loops are basically while loops, but they specifically iterate over objects. Example of iterating over a range (instantiated by 1 . . x) and printing all numbers in the range.
```ruby
x = 5
for i in  1..x do 
puts i 
end
```
Another for loop, iterating over a list:
```ruby
x =  [1,  2,  "three",  4,  5.0]  
for i in x do 
puts i 
end
```
### 1.3 Functions (aka Methods)
Bless functions for making programming easier. Functions or methods contain lines of code that can be called with a simpler invocation. If you have a block of code that gets called over and over and over again, it's much easier to run that block of code by typing `my_function()` and letting the function (which contains the block of code) handle things.

Try defining your own functions below:
```ruby
def  hello_world # prints hello world
puts "hello, world!"
end

def hello(name) # prints a personalized hello message
puts "hello, " + name
end
```
### 1.4 Explore!
To explore ruby on your own, I recommend the following resources to get more familiar with the language:
- Codecademy: https://www.codecademy.com/learn/learn-ruby
- Learn Ruby in 20 minutes: https://www.ruby-lang.org/en/documentation/quickstart/
- More comprehensive guide to Ruby: https://launchschool.com/books/ruby/read/basics#strings

## 2. Embedded Ruby
Embedded Ruby is a special type of ruby that can be injected into documents that aren't ruby files.
For example, in our use cases, we will be using HTML documents that have ruby code. These files will have the extension `*.html.erb`. The example below shows a standard html document that has a paragraph containing the user's first name, provided by the ruby backend.
```html.erb
<!DOCTYPE html>
<html>
  <body>
    <p>Hello, <%= user.first_name %>.</p>
  </body>
</html>
```

An example of a simple for loop using .html.erb
```html.erb
...
<tbody>
  <% for @user in @user_list %>
    <tr> User: <%= @user %></tr>
  <% end %>
</tbody>
...
```
You can see the familiar HTML tags, but also some new notation: `<%` and `%>` which are the opening and closing braces to embedded ruby. Notice, when there's an extra equals sign on the opening brace `<%=` it means the front-end actually receives the ruby data being injected, whereas without it the ruby code simply executes.

**Fun fact**: in addition to HTML files, we can also add embedded ruby to *.js files (JavaScript) or *.css files (but we won't need that for our application purposes).

### Objective 1:
Create another page called About, and add the route to routes.rb and add the corresponding method to app/controllers/static_pages_controller.rb.

### Objective 2: 
Since our static pages currently have different titles (i.e. Home, Help, About) we want this to display on our HTML pages. Use Ruby to tell the HTML page which title to use on which page.

We do this by providing a title on a given page:

**app/views/static_pages/home.html.erb**
```html.erb
<% provide(:title, "Home") %>
<body>
<h1>Home Page</h1>
  <p>
    This is my home page. Welcome.
  </p>
</body>
```
and in our application.html.erb page, we provide the general title:
```html
<!DOCTYPE html>
<html>
  <head>
    <title><%= yield(:title) %> | Bloggster</title>
    <%= csrf_meta_tags %>

    <%= stylesheet_link_tag    'application', media: 'all', 'data-turbolinks-track': 'reload' %>
    <%= javascript_include_tag 'application', 'data-turbolinks-track': 'reload' %>
  </head>

  <body>
    <%= yield %>
  </body>
</html>
```
### Objective 3:
Add a picture to your homepage! Try and customize your app the way you want it to look, and go ahead and add styling! If you're not sure how, we'll cover this next week. Hint: you'll want to use the built in image_tag method in your layout (in the *.html.erb files)
```html.erb
<%= image_tag("my_image.jpg", :alt => "my image") %>
```
### Objective 4:
Use a for loop in embedded ruby! You can use it however you like, whether to print some numbers or make that picture show up multiple times.
### Next Week
Since next week might be really busy in terms of midterms, the lesson will be fairly straight-forward and voluntary. We'll be covering styling such as css and bootstrap which is not always necessary for an app to work (BUT it is kinda important imo, you want things to look pretty).
