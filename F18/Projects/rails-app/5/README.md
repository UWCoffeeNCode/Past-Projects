# Lesson 5: Login and Sessions
Welcome back! This lesson we'll be learning about sessions and building a login system for our app.
Things we'll be covering:
1. What are sessions?
2. Create a SessionsController
3. Building a login page
4. Logging in
5. Logging out

## 5.1 What are sessions?
[HTTP](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) is a stateless protocol, meaning it does not require the HTTP server to remember things such as user sessions or login. So, web developers work around this with "sessions". 

Most commonly in Rails, we see this being implemented with cookies, which are small pieces of text that sits in the user's browser. We can think of sessions from a RESTful standpoint: 
- the login form will render a *new* sessions form
- logging in *creates* a new session
- logging out will *destroy* the session.

Unlike users, which uses a database to store data about each user, cookies are a different mechanic that we'll build out in the next few sections.

## 5.2 Create a SessionsController
Using a Rails command, generate a SessionsController and add the proper code to the routes file to create the following routes:

| **HTTP request** | **URL** | **Named route** | **Action** | **Purpose** |
|------------------|---------|-----------------|------------|-------------|
| `GET` | /login | `login_path` | `new` | page for a new session (login) |
| `POST` |/login | `login_path` | `create` | create a new session (login)|
| `DELETE` | /logout | `logout_path` | `destroy` | delete a session (log out) |

## 5.3 Building a login page
Recall that we used `form_for` in our previous lesson when creating a signup page. We'll be creating a similar form with the same built-in method, but this time for the Sessions object instead of Users. 
### 5.3.1 The new.html.erb form
Notice in the code snippet we're using `form_for(:session, url: login_path)` to create a form that will submit the `email` and `password` parameters upon the user hitting "Log in".
``` html.erb
<!--app/views/sessions/new.html.erb-->

<% provide(:title, "Log in") %>
<h1>Log in</h1>

<div class="row">
  <div class="col-md-6 col-md-offset-3">
    <%= form_for(:session, url: login_path) do |f| %>

      <%= f.label :email %>
      <%= f.email_field :email, class: 'form-control' %>

      <%= f.label :password %>
      <%= f.password_field :password, class: 'form-control' %>

      <%= f.submit "Log in", class: "btn btn-primary" %>
    <% end %>

    <p>New user? <%= link_to "Sign up now!", signup_path %></p>
  </div>
</div>
```
Next up we need to add to our controller to provide the proper controller methods.
```ruby
# app/controllers/sessions_controller.rb

class SessionsController < ApplicationController

  def new
  end

  def create
    render 'new'  # renders the new.html.erb view for Sessions
  end

  def destroy
  end
end
```
### 5.3.2 Params
As touched on before, the **params** hash is something that is stored on the user browser, and its data comes from three main sources:
- string GET requests
- form POST requests
- the path of the URL.

In our case, we're submitting data to the [params hash](https://gorails.com/episodes/the-params-hash) through our POST request when submitting the login form. The `sessions` key in our **params** has will contain a nested hash with data such as email and password, which are needed to login.
```ruby
# this hash resides within the params hash
{ session: { password: "foobar", email: "user@example.com" } }
```
### 5.3.3 Finding and logging in our user
Assuming the user presses the submit button and the browser has sent the POST request, we must now pass information to the SessionsController to authenticate the submitted user information.
**Objective 1**: under the `create` function in your SessionsController, add the logic to find the user based off the unique user email retrieved from params. Then, authenticate the user if found.

In the end, your `create` method should look like this:
```ruby
def create
    user = User.find_by(???)# find user somehow
    if user and ??? # user exists AND has the correct login password
      # Log the user in and redirect to the user's show page.
    else
	  # error handling, display error message
	  render 'new'
	end
end
 ```

## 5.4 Logging in
So, now assuming the user has inputted correct information, the next step is to handle valid logins. We'll need coordination between multiple controllers to pull this off, so we're adding our first `include` statement in ruby. This essentially means we can use all the functions in the SessionsHelper where we have that line of code, and reduces redundant code!
```ruby
# found in app/controllers/application_controller.rb

class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  include SessionsHelper # Add this line
end
```
### 5.4.1 Add the log_in method
Now, let's add the actual log_in method in our SessionsHelper in order for other controllers to use it. We use a convenient `session` method defined by Ruby, which we can treat as a has to store the user id, like below:
```ruby
# app/helpers/sessions_helper.rb
module SessionsHelper
  # Logs in the given user.
  def log_in(user)
    session[:user_id] = user.id
  end
end
```
**Objective 2**: think about where else users need to log in, and implement the `log_in` method.

### 5.4.2 Defining the current_user
We need a way of keeping track who the logged in user at a given time is. This is helped with our own `current_user` method, defined below.
```ruby
# Returns the current logged-in user (if any).
def current_user
  if session[:user_id] 
    @current_user ||= User.find_by(id: session[:user_id])
  end
end
```

**Objective 3**: define your own method called `logged_in?` which checks if there's someone logged in (if there's a current_user). You can define the method in the SessionsHelper.

### 5.4.3 Conditional layouts for logged in users
Now that we have a logged in user, they should be able to access their profile and such. We do this with conditional formatting. I've uploaded the needed files within this lesson folder, titled `header.html.erb`.  We'll also need to include `jquery` and `bootstrap` in order to enable some drop-down menu actions. 

## 5.5 Logging out
In order to log out, we must delete the user id from the session and set the current_user to `nil` (learn more about the [ruby nil type](https://www.rubyguides.com/2018/01/ruby-nil/)), which means we "forget" the user.
**Objective 4**: implement the `log_out` function in the sessions helper.

### 5.5.1 Destroy
Now that we can use our `log_out` function, let's use it in the SessionsController `destroy` action. 
```ruby
def destroy
  log_out
  redirect_to root_url  
end
 ```
