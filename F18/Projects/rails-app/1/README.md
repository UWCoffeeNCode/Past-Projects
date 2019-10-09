# Lesson 1: Intro to Ruby on Rails
Welcome! In the first lesson we'll go through the following:
1. Setup
2. Creating a new rails app
3. Parts of the app
4. Try to make some static pages!
5. Resources

## 1. Setup
First, you'll need your development environment set up. Some things you'll need: 
- Ruby and Rails (both: http://railsinstaller.org/en for Windows, Homebrew for Mac)
- some IDE / text editor of your choice (I recommend Sublime: https://www.sublimetext.com/3)
- Git (https://git-scm.com/downloads)
- Git Bash (needed if you have Windows only)


## 2. Creating a new rails app
To create a new rails app, change directory (cd) into your specified folder (in this case it's called workspace), run the rails command, and cd into the newly created app folder:
```bash
$ cd ~/FOLDER_WHERE_YOU_WANT_TO_PUT_THE_APPLICATION
$ rails new YOUR_APP_NAME_HERE
$ cd YOUR_APP_NAME_HERE/
```
Rails will generate a bunch of things in creating the app, including a Gemfile. To install all the gems in the Gemfile without production gems, run:
```bash
$ bundle install --without production
```

To see your app in a local server, go to terminal and type:
```bash
$ rails server
```
Then navigate to http://localhost:3000/. You should see something!!!

To init Git tracking, type:
```bash
$ git init
$ git add -A
$ git commit -m "Initialize repository"
```
Next, create a GitHub repository (fancy word for master folder type thing) and then "push" all your changes. Note: in between this step, you may need to set up your SSH key. Read more here: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/
```bash
$ git remote add origin git@github.com:YOUR_USERNAME/YOUR_APP_NAME_HERE.git
$ git push -u origin --all
```
You should see stuff on GitHub now!!! On the website under your profile your repo should now have populated files.

## 3. Parts of the app
Rails generates a bunch of stuff for you when you first create an app. This really simplifies things for the developer gets the ball rolling. We'll talk about a few of those generated files below.
### 3.1 Gemfile
Rails generates a new Gemfile when you run rails new. You should have this file directly under the project directory. This is where the gems are stored. Each gem is a ruby library that extends functionality.
```ruby
source 'https://rubygems.org'

gem 'rails',        '5.1.6'
gem 'puma',         '3.9.1'
gem 'sass-rails',   '5.0.6'
gem 'uglifier',     '3.2.0'
gem 'coffee-rails', '4.2.2'
gem 'jquery-rails', '4.3.1'
gem 'turbolinks',   '5.0.1'
gem 'jbuilder',     '2.7.0'

group :development, :test do
  gem 'sqlite3', '1.3.13'
  gem 'byebug',  '9.0.6', platform: :mri
end

group :development do
  gem 'web-console',           '3.5.1'
  gem 'listen',                '3.1.5'
  gem 'spring',                '2.0.2'
  gem 'spring-watcher-listen', '2.0.1'
end

group :test do
  gem 'rails-controller-testing', '1.0.2'
  gem 'minitest',                 '5.10.3'
  gem 'minitest-reporters',       '1.1.14'
  gem 'guard',                    '2.13.0'
  gem 'guard-minitest',           '2.4.4'
end

group :production do
  gem 'pg', '0.18.4'
end

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: [:mingw, :mswin, :x64_mingw, :jruby]
```

### 3.2 app/controllers/application_controller.rb
The controller for the application. Rails uses a Model-View-Controller (MVC) architechture to organize things. (Read more: https://medium.com/the-renaissance-developer/ruby-on-rails-http-mvc-and-routes-f02215a46a84)
```ruby
class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception

  def hello # added our own function to say something friendly
    render html: "hello, world!"
  end
end
```

### 3.3 app/views/layouts/application.html.erb
An embedded Ruby file for the main application page. Looks like HTML for the most part, but you can also add ruby to the page! This would be the "View" in our MVC application. Again, you should already have the below code thanks to Rails generating it!!!
```html.erb
<!DOCTYPE html>
<html>
  <head>
    <title>TestApp</title>
    <%= csrf_meta_tags %>

    <%= stylesheet_link_tag    'application', media: 'all', 'data-turbolinks-track': 'reload' %>
    <%= javascript_include_tag 'application', 'data-turbolinks-track': 'reload' %>
  </head>

  <body>
    <%= yield %>
  </body>
</html>
```

### 3.4 The non-existent model
Hold up. We don't have the Model part of our Model-View-Controller app yet. But stay tuned! This requires creating a database table with attributes and such. If you're really interested and want to try this on your own, go right ahead! We'll be doing this next week along with adding styling.

### 3.5 config/routes.rb
Routes are a Rails concept that map URLs to controls that can do things. Below is an example of directing the root (the main directory) to the hello method in the application controller.
```ruby
Rails.application.routes.draw do
  root 'application#hello'
end
```

#### Side note about RESTful Routes
REpresentational State Transfer (REST) is an architectural style defined for providing standards between computer systems on the web, making it easier for systems to communicate with each other.

| HTTP Method	| What it's used for      | Examples  |
|-------------|-------------------------|-----------|
| GET	        | Retrieving a resource.	| Any time you navigate directly to a page or use google to navigating the page, you use the GET http method. |
| POST	      | Creating a resource	| Older web applications used POST for everything. |
| PUT	        | Used to completely update a resource.	| Updating your user profile on some website would typically use patch with web frameworks that support it. |
| PATCH	      | Used to partially update a resource.	| An example of this would be where you are just updating the password for your user profile. |

Source: https://richonrails.com/articles/understanding-rails-routing

## 4. Try to make some static pages!!!
Alright. Now it's your turn to explore! Your objective is to create a few static pages on your website. This could include a *Help* page and an *About* page.

### 4.1 Create a branch
To get started, create a "branch" which is a local copy of your workspace/files that can keep track of changes to the original files.
```bash
$ git checkout -b static-pages
```

### 4.2 Generate a controller
The StaticPages controller file will be generated with the below command, along with two empty methods, home and help:
```bash
$ rails generate controller StaticPages home help
```
This generates the file at app/controllers/static_pages_controller.rb in your project! Go check it out and see what was generated.

### 4.3 Your turn to add stuff!
Now, add stuff to provide something at the directory http://localhost:3000/static_pages/home and http://localhost:3000/static_pages/help!!! Currently if you navigate to those directories, you'll see something but it might not be what you want. 

#### Objective 1: add a title and text describing each page of your own.
(Hint: this is where some trusty HTML is useful! Remember how those `.html.erb` files were where our webpage styling is hosted?)

#### Objective 2: add an About page to go along with your Home and Help pages. 
(Hint: you've already created the StaticPages controller, which should host all your pages! Your *About* page should be at the directory http://localhost:3000/static_pages/about)

## 5. Resources
### 5.1 Learn Ruby!
Codecademy: https://www.codecademy.com/learn/learn-ruby

Online interactive Ruby tutorial: https://www.learnrubyonline.org/en/Welcome

### 5.2 Learn Git!
Codecademy: https://www.codecademy.com/learn/learn-git

Online interactive Git branching tutorial: https://learngitbranching.js.org/
