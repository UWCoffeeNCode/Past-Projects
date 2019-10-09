
# Lesson 3. Styling, Creating Users
Hey! Welcome to lesson 3. This one's a fun one. We'll be learning about:
1. Styling

	**Objective 1**: Simplify the given code using SCSS nesting
	
2. Create our Users

	2.1. Create our UserController
	
	2.2 Generate our User model
	
	2.3 Create sample users
	
	**Objective 2**: play around with the User object in rails console
	
	2.4 Validation
	
	**Objective 3**: validate that users have proper names and emails
	
	**Objective 4**: extend what needs to be validated and make sure everything is being checked.
	
	2.5 User passwords
	
	2.6 Add password hashing
	
	2.7 Play around with users one more time in rails console
	
3. Extra Resources


## 1 Styling
Nobody likes an ugly website. Let's make ours pretty! We'll be using bootstrap and SCSS. If you know CSS, you're basically know SCSS as well. For the basics on SCSS, please check out https://sass-lang.com/guide. We'll see below that it's pretty straight-forward.
### 1.1 Add the bootstrap gem to the Gemfile.
```ruby
gem 'bootstrap-sass', '3.3.7'
```
After adding the gem to your Gemfile and saving, make sure to run a `bundle install` to get the gem contents.
### 1.2 Create your .scss file
Add your own custom.scss file under *app/assets/stylesheets*. I've given you the base code for what we'll need below, try reading through it:
```scss
@import "bootstrap-sprockets";
@import "bootstrap";

/* mixins, variables, etc. */
$gray-medium-light: #eaeaea;

/* universal */

body {
  padding-top: 60px;
}

section {
  overflow: auto;
}

textarea {
  resize: vertical;
}

.center {
  text-align: center;
}

.center h1 {
margin-bottom: 10px;
}

/* typography */

h1, h2, h3, h4, h5, h6 {
  line-height: 1;
}

h1 {
  font-size: 3em;
  letter-spacing: -2px;
  margin-bottom: 30px;
  text-align: center;
}

h2 {
  font-size: 1.2em;
  letter-spacing: -1px;
  margin-bottom: 30px;
  text-align: center;
  font-weight: normal;
  color: $gray-light;
}

p {
  font-size: 1.1em;
  line-height: 1.7em;
}

/* header */

#logo {
  float: left;
  margin-right: 10px;
  font-size: 1.7em;
  color: $gray-light;
  text-transform: uppercase;
  letter-spacing: -1px;
  padding-top: 9px;
  font-weight: bold;
}

#logo &:hover {
  color: $gray-light;
  text-decoration: none;
}

/* image styling and layout */

#my_image {
    height: auto; 
    width: auto; 
    max-width: 300px; 
    max-height: 300px;
}

#my_image .center{
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
```

### 1.3 Use nesting
One of the wonderful things about SCSS is nesting. Let's use it to simplify the following code snippet from your .scss file.
```scss
.center {
  text-align: center;
}

.center h1 {
  margin-bottom: 10px;
}
```
... which seems redundant, into the below code:
```scss
.center {
  text-align: center;
  h1 {
    margin-bottom: 10px;
  }
}
```
... much better :)
Let's do it again for the following examples too, in your same .scss file. Before:
```scss
#logo {
  float: left;
  margin-right: 10px;
  font-size: 1.7em;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: -1px;
  padding-top: 9px;
  font-weight: bold;
}

#logo &:hover {
  color: $gray-light;
  text-decoration: none;
}
```
After:
```scss
#logo {
  float: left;
  margin-right: 10px;
  font-size: 1.7em;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: -1px;
  padding-top: 9px;
  font-weight: bold;
  &:hover {
    color: #fff;
    text-decoration: none;
  }
}
```
### Objective 1: Simplify the given code using SCSS nesting

### 1.4 Partials
Another cool rails functionality. Partials allow you to render a view within a view, which can be useful if you have redundant code.
## 2 Create our Users
Users are the ones who will be on the application, and we must create the User object and its controller before letting them post on the site in the future. To store users, we'll also need a database for that.
### 2.1 Create the UsersController
Alright. We're going to need a UsersController to control our users. Run the rails command in terminal:
```bash
rails generate controller Users new
```
The generated files we'll be using:
```ruby
# Found in app/controllers/users_controller.rb
class UsersController < ApplicationController

  def new
  end
end
```

```html
# Found in app/views/users/new.html.erb
<h1>Users#new</h1>
<p>Find me in app/views/users/new.html.erb</p>
```
You can go ahead and change the new.html.erb file to something more meaningful:
```html
<h1>Sign up</h1>
<p>This will be a signup page for new users.</p>
```
### 2.2 Generate the User model
Remember in lesson 1 how I talked about the model as part of the MVC-architecture? Here we are. Run the following command in terminal to generate the User model:
```bash
rails generate model User name:string email:string
```
Then run the migration:
```bash
rails db:migrate
```
This creates the following table model for our Users, where the id is uniquely generated and assigned to every user object.

| id | name | email |
| -------- | ------ | ------------- |
| 1 | first last | first.last@email.com |
| 2 | Annie Zhang | annie.zhang@email.com |

### 2.3 Create sample users 
We're gonna try faking some data! Remember how we played around with the rails console last lesson? We're gonna do more of that! This time, in terminal, type the following to create a one-off instance of rails console that won't save anything after you're done with it (hence the "sandbox" option).
```
 rails console --sandbox
```
Once you're in, try this out (notice `>>` is just part of the console, don't type it out):
```
>> User.new
```
What do you see? It should be the default configuration of a User object. Now try making your own new user, and defining it as a variable:
```
>> user = User.new(name: "Han Solo", email: "han@solo.com")
```
Check if the user is valid:
```
>> user.valid?
```
Then save it! (don't worry, sandboxing will still prevent any real changes)
```
>> user.save
```
**Objective 2**: play around with the User object in rails console
Try out more stuff on your own!
### 2.4 Validation
Now, something we should check for before saving a user is validity. If you played around in rails console more, you'd notice that it's possible to save a user with no name! That's wack. Check that name is present in the User model, and that the length is under a certain maximum:
```ruby
class User < ApplicationRecord
  validates :name,  presence: true, length: { maximum: 50 }
end
```
**Objective 3**: validate that users have proper names and emails.
What else needs to be checked before a User is actually created?

**Objective 4**: extend what needs to be validated and make sure everything is being checked.

### 2.5 User passwords
Great. We created Users, but we also should add one more thing to the model: passwords. This is because each user will be needing a unique password in order to log on. 
| id | name | email | password|
| -------- | ------ | ------------- |-----|
| 1 | first last | first.last@email.com | (some encryption) |
| 2 | Annie Zhang | annie.zhang@email.com | (some encryption) |

#### Migrations
Migrations are how we handle any model changes, and each one is generated with a command like the following:
```
rails generate migration add_password_digest_to_users password_digest:string
```
This rails command will generate a file like the following:
```ruby
# File found at db/migrate/[timestamp]_add_password_digest_to_users.rb

class AddPasswordDigestToUsers < ActiveRecord::Migration[5.0]
  def change
    add_column :users, :password_digest, :string
  end
end
```
Now, to apply it, we use the following command:
```
rails db:migrate
```
### 2.6 Add password hashing
As you may have guessed, we're not just going to store passwords in a string in our database. So to help us better encrypt our user data, we use a gem called `bcrypt`. Read more about bcrypt: https://en.wikipedia.org/wiki/Bcrypt

Add the following gem to your Gemfile:
```ruby
gem 'bcrypt',         '3.1.12'
```
And as always, run `bundle install` to install the gem.
Now, we're ready to start using bcrypt. Luckily rails has a built in function called `has_secure_password`, which we can tack onto the user validation.
```ruby
# Found in app/controllers/users_controller.rb
class User < ApplicationRecord
  validates :name,  presence: true, length: { maximum: 50 }
  ... # stuff you added to validate the user
  ...
   has_secure_password
   validates :password, presence: true, length: { minimum: 6 }
end
```
### 2.7 Play around with users one more time in rails console
Now that we've added passwords and checks, try creating a new user on rails console like we did before, and try to make it break. We can see the new password_digest attribute as a part of our new user. 
```
>> User.create(name: "Han Solo", email: "han@solo.com", password: "hansolo", password_confirmation: "hansolo")
>> user = User.find_by(email: "han@solo.com")
>> user.password_digest
```
Check out the `authenticate` function, which compares the digest of strings to validate them. 
```
>> user.authenticate("not_the_right_password")
```
This should return false. We'll be using this later on when we add signup / login to our app!
## 3 Extra Resources
- Learn Sass on on Codecademy: https://www.codecademy.com/learn/learn-sass
- SCSS cheatsheet: https://devhints.io/sass
- Ruby migrations: https://edgeguides.rubyonrails.org/active_record_migrations.html
- Bcrypt Encryption: http://dustwell.com/how-to-handle-passwords-bcrypt.html
