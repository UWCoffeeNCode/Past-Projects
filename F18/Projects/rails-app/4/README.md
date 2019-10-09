
# Lesson 4: Signup and Login

Last lesson, we added styling and made Users, as well as added encryption to user passwords. This lesson will add on top of the User model we created last time and extend our app functionality.

We'll be covering
1. Showing Users
- Learn about resources in routes
2. Signup

## 1. Showing Users
So, we have users from last lesson. However, in real life platforms the users can only be gained through signup. We'll build that functionality this week.

### 1.1 Rails Resources
So at this point your routes.rb file should look something like this:
```ruby
# config/routes.rb
Rails.application.routes.draw do
  root 'static_pages#home'
  get  '/help',    to: 'static_pages#help'
  get  '/about',   to: 'static_pages#about'
  get  '/contact', to: 'static_pages#contact'
  get  '/signup',  to: 'users#new'
```
We're going to add what's known as a `resource` to the routes file just at the very end, so that we can start doing things with Users.
```ruby
 resources :users
 ```
 Remember what REST is? Yeah, REpresentational State Transfer! By adding this users resource, we have automatically enabled the following endpoints to be hit (although they shouldn't do anything at the moment):
 

| **HTTP request** | **URL** (added to the base URL) | **Action** | **Named route** | **Purpose**|
|-----------|-------------|-------|------|-----|
| `GET` | /users | `index` | `users_path` | page to list all users |
| `GET` | /users/1 | `show` | `user_path(user)` | page to show user |
| `GET` | /users/new | `new` | `new_user_path` | page to make a new user (signup) |
| `POST` | /users | `create` | `users_path` | create a new user |
| `GET` | /users/1/edit | `edit` | `edit_user_path(user)` | page to edit user with id  `1` |
| `PATCH` | /users/1 | `update` | `user_path(user)` | update user |
| `DELETE` | /users/1 | `destroy` | `user_path(user)` | delete user |

<<<<<<< HEAD
 Notice, if you run your rails server and try to navigate to localhost, you see an error page.
 ![no good](https://github.com/UWCoffeeNCode/Lessons/blob/master/F18/Projects/rails-app/4/unknown_action_show.png)
 That's no good. We'll have to show our users to the view in the next step.
=======

 Notice, if you run your rails server and try to navigate to localhost, you see an error page. That's no good. We'll have to show our users to the view in the next step.

![alt text](https://github.com/UWCoffeeNCode/Lessons/blob/master/F18/Projects/rails-app/4/unknown_action_show.png)
>>>>>>> 6fe9c0a4c37aa0407e75cf808644a7dc74849588

### 1.2 The show.html.erb view
Unlike the app/views/users/new.html.erb file that was generated when we generated the User controller, we will create a show.html.erb file under the same directory. Go ahead and do that now, and the below line of embedded ruby code. This is just showing the user's name and user's email in the webpage.
```ruby
# app/views/users/show.html.erb
<%= @user.name %>, <%= @user.email %>
```
And now we add the show() function in the UsersController. This is how the user view (show.html.erb) will be able to grab the name and email from the user, by us providing the @user variable from the backend.
```ruby
# app/controllers/users_controller.rb

class UsersController < ApplicationController

  def show
   @user = User.find(params[:id])  
  end

end
```
## 2. Signup
Now, we get users to actually signup.
### 2.1 Signup Form
The signup form is something we'll have to build out for the users to user. We currently have a blank signup form as per last lesson, but we'll make the full one today. 
### 2.2 Using form_for
Remember that the signup page /signup is routed to the `new` action in the Users controller (the `get  '/signup',  to: 'users#new'` line in our routes.rb file). We have to again create that User argument which gets passed to `form_for` which is a built-in helper method and builds out a form.
### 2.3 The Users#new function
Try adding the `new` function to your users controller.
```ruby
# app/controllers/users_controller.rb

class UsersController < ApplicationController

  def show
    @user = User.find(params[:id])
  end

  def new
    @user = User.new
  end
end
```
Now, the `new` view should contain something too:
```html.erb
# app/views/users/new.html.erb

<h1>Sign up</h1>

<div class="row">
  <div class="col-md-6 col-md-offset-3">
    <%= form_for(@user) do |form| %>
      <%= form.label :name %>
      <%= form.text_field :name %>

      <%= form.label :email %>
      <%= form.email_field :BLANK %>

      <%= form.label :BLANK %>
      <%= form.password_field :password %>

      <%= form.label :password_confirmation, "Confirmation" %>
      <%= form.password_field :password_confirmation %>

      <%= form.submit "Create my account", class: "btn btn-primary" %>
    <% end %>
  </div>
</div>
```
**NOTICE** that there's code missing from above. **Objective 1** of this lesson is to fill in the missing code blocks with what you think should go there. Also add in the following styling after you're done that to make it pretty:
```scss
# app/assets/stylesheets/custom.scss
.
.
.
/* forms */

input, textarea, select, .uneditable-input {
  border: 1px solid #bbb;
  width: 100%;
  margin-bottom: 15px;
  @include box_sizing;
}

input {
  height: auto !important;
}
```
If you add the code and `Inspect Element` in your browser, you can see that the embedded ruby code block:
```html
<%= f.label :name %>
<%= f.text_field :name %>
```
produces the HTML:
```html
<label for="user_name">Name</label>
<input id="user_name" name="user[name]" type="text" />
```
and you will see something similar for user email as well.


### 2.4 Creating the User
If we inspect more of the HTML, we can see that the code
```html
<form action="/users" class="new_user" id="new_user" method="post">
```
which submits the user form performs a POST request to /users, which relates to the #create function in our UsersController. After hitting the submit button, we should be creating the user in the database within our `create` function.
```ruby
def create
  @user = User.new(params[:user])
  if @user.save
      redirect_to user_url(@user)
  else
    render 'new'
  end
end
```
### 2.5 Verifying Valid Users
We want to make sure that what our users are submitting is valid information. So, we do that by defining a new method in our controller to do that error check. 

**Objective 2**: see if you can place the code below in the proper place within the UsersController.
```ruby
.
.
.
@user = User.new(user_params)
.
.
.
private
  def user_params
    params.require(:user).permit(:name, :email, :password, :password_confirmation)
  end
.
.
.
```
### 2.6 Managing Errors
So, your user submitted invalid items to the web form. Now what? We want to handle the case where the invalid information comes through to us. 
**Objective 3**: handle the error case by displaying error messages.
Hint: you can access errors with `user.errors.full_messages` in Rails, given the user object.
