# Lesson 6: Microposts
Today's lesson will focus on making the Micropost object and model. This is the main post object that users will be contributing to the rails app. We split this into some main chunks:
1. Defining the model
2. Model associations
3. Showing posts
4. Creating posts

## 6.1 Defining the model
We want to create something that has content, that can be displayed. We'll call it a post, but a micro one since it'll be smol.

Micropost object | type
------|-------
id | integer
content | string
user_id | integer
created_at | datetime
updated_at | datetime

### 6.1.1 Generate the model
Generate the Micropost model with the terminal command:
```
rails generate model Micropost content:text user:references
```

After running the command, the generated micropost.rb file looks like 
```ruby
# app/models/micropost.rb

class Micropost < ApplicationRecord
   belongs_to :user
end
```
### 6.1.2 Make an edit to our migration file
Now that we generated the model, we do what we always do: we run the migration. BUT beware, this time we want to make an edit before we run the migration:
```ruby
# db/migrate/[timestamp]_create_microposts.rb

class CreateMicroposts < ActiveRecord::Migration[5.0]
  def change
    create_table :microposts do |t|
      t.text :content
      t.references :user, foreign_key: true

      t.timestamps
    end
 # add the next line to the migration file
 add_index :microposts, [:user_id, :created_at]  end
end
```
### 6.1.3  Run the migration
Now with our migration file good to go, go ahead and run `rails db:migrate` in terminal.

### 6.1.4 Validation
We want to validate that each micropost comes from a user, with a valid user id.

**Objective 1**: Write the line of code in `micropost.rb` that would check this.

As well, make sure that each micropost has content, and isn't just a blank post with nothing. 

**Objective 2**: Make sure the content isn't too much, and set a limit that you think is appropriate. You can do this all with `validates` statements, like in [Lesson 3, Section 2.4](https://github.com/UWCoffeeNCode/Lessons/tree/master/F18/Projects/rails-app/3#24-validation).

## 6.2 Model associations
```ruby
# app/models/micropost.rb

class Micropost < ApplicationRecord
  belongs_to :user # add this line to your file
  validates :user_id, presence: true
  validates :content, presence: true, length: { maximum: 140 }
end
```
```ruby
# app/models/user.rb

class User < ApplicationRecord
  has_many :microposts # add this line to your file
  .
  .
  .
end
```

### Generate the MicropostsController

To generate the controller, as always, run `rails generate controller Microposts` in terminal.


## 6.3 Showing posts
We'll display posts alongside a user profile. Since there can be more posts that can load or fit on one page, we introduce some new gems that we use to paginate our posts. As well, 

### 6.3.1 Setup with some exciting gems
Add the following gems to your `Gemfile` and run `bundle install` to get the gems loaded.
```ruby
gem 'will_paginate',           '3.1.6' 
gem 'bootstrap-will_paginate', '1.0.0'
```

### 6.3.2 Render and display posts
```ruby
# app/controllers/users_controller.rb

class UsersController < ApplicationController
  .
  .
  .
  def show
    @user = User.find(params[:id])
    # add the next line to show microposts
    @microposts = @user.microposts.paginate(page: params[:page])
  end
  .
  .
  .
end
```

Now add the partial to render posts, which we'll reference wherever we want to display the posts. Make this new partial under `app/views/microposts/_microposts.html.erb`.
```html.erb
<!-- app/views/microposts/_micropost.html.erb -->

<li id="micropost-<%= micropost.id %>">
  <span class="user"><%= link_to micropost.user.name, micropost.user %></span>
  <span class="content"><%= micropost.content %></span>
  <span class="timestamp">
    Posted <%= time_ago_in_words(micropost.created_at) %> ago.
  </span>
</li>
```
### 6.3.3 Add styling
To add styling to display the posts, feel free to use the styling provided below, and add it to the existing `custom.scss` file. However, I encourage you to try your own style!!! Styling is where you can really make your web app unique from all the others, and show some personality.
```scss
...
/* microposts */

.microposts {
  list-style: none;
  padding: 0;
  li {
    padding: 10px 0;
    border-top: 1px solid #e8e8e8;
  }
  .user {
    margin-top: 5em;
    padding-top: 0;
  }
  .content {
    display: block;
    margin-left: 60px;
    img {
      display: block;
      padding: 5px 0;
    }
  }
  .timestamp {
    color: $gray-light;
    display: block;
    margin-left: 60px;
  }
  .gravatar {
    float: left;
    margin-right: 10px;
    margin-top: 5px;
  }
}

aside {
  textarea {
    height: 100px;
    margin-bottom: 5px;
  }
}

span.picture {
  margin-top: 10px;
  input {
    border: 0;
  }
}
...
```

### 6.3.4 Add the right routing
Add the correct routes to `routes.rb` to get the following routes in the chart below:

|**HTTP request**|**URL**|**Action**|**Named route**|
|--|--|--|--|
|`POST` | /microposts | `create` | `microposts_path` |
|`DELETE` | /microposts/1 | `destroy` | `micropost_path(micropost)` |

### 6.3.5 Make the logged_in_user method
This new method is to check that the user is logged in before we perform any actions. The `logged_in?` method is the same one that we made in [last week's lesson](https://github.com/UWCoffeeNCode/Lessons/tree/master/F18/Projects/rails-app/5).
```ruby
# app/controllers/application_controller.rb

class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  include SessionsHelper

  private

    # Confirms a logged-in user.
    def logged_in_user
      unless logged_in?
        store_location
        flash[:danger] = "Please log in."
        redirect_to login_url
      end
    end
end
```
And now add the check on the second line under the UsersController
```ruby
class UsersController < ApplicationController
  before_action :logged_in_user, only: [:index, :edit, :update, :destroy]
  ...
```
and the MicropostsController
```ruby
# app/controllers/microposts_controller.rb
class MicropostsController < ApplicationController
  before_action :logged_in_user, only: [:create, :destroy]
  ...
```

## 6.4 Creating posts
Now that the model is all set up, we can do stuff with it! First step is to help users create their own posts. We do the setup with the `create` function and also the post submission form partial.
### 6.4.1 Creating the `create` function
In order to create posts, we have to have the function in the MicropostsController:
```ruby
# app/controllers/microposts_controller.rb
...
def create
    @micropost = current_user.microposts.build(micropost_params)
    if @micropost.save
      flash[:success] = "Micropost created!"
      redirect_to root_url
    else
      render 'static_pages/home'
    end
  end
...
private

    def micropost_params
      params.require(:micropost).permit(:content)
    end
...
```
Notice, the `flash[:success]` line is a notification that appears on the web app, and we create this hash ourselves, giving it both `:success` and `:danger` messages. 

I've uploaded the main `application.html.erb` file in the lesson folder for everyone to have access to this.
### 6.4.2 The post partial
Now we can create a partial with a form to help users create their own posts. The `f.text_area` creates a text window that users can type in, and the `placeholder` is the text that shows up in that window before the user types anything. Again, once the user hits `f.submit`, the form object will be sent with its text content.

Create this file under `app/views/microposts/_micropost_form.html.erb`
```html.erb
<!-- app/views/microposts/_micropost_form.html.erb -->

<%= form_for(@micropost) do |f| %>
  <div class="field">
    <%= f.text_area :content, placeholder: "Compose new micropost..." %>
  </div>
  <%= f.submit "Post", class: "btn btn-primary" %>
<% end %>
```
### 6.4.3 Display on the homepage
Add the following to `home.html.erb`, leaving the original code under the else statement. This will display the logged-in user info and a post form IF there is a user logged in, otherwise it will display the usual home screen.
```html.erb
...
<% if logged_in? %>
  <div class="row">
    <aside class="col-md-4">
      <section class="user_info">
        <h1><%= current_user.name %></h1>
        <p><%= current_user.email %></p>
        <span><%= link_to "view my profile", current_user %></span>
      </section>
      <section class="micropost_form">
        <%= render 'microposts/micropost_form' %>
      </section>
    </aside>
  </div>
<% else %>
...
<% end %>
```
In the end, it should look something like:


## Extra Resources

Here are some extra links and external resources to read up on, since we covered a lot of content in this less.

- Rails migration files: https://www.tutorialspoint.com/ruby-on-rails/rails-migrations.htm
- ActiveRecord associations: https://guides.rubyonrails.org/association_basics.html
- More info on will_paginate: https://github.com/mislav/will_paginate
- More info on bootstrap-will_paginate: https://github.com/yrgoldteeth/bootstrap-will_paginate
