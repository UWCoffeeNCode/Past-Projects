# 7. Final Lesson: Deploy!
This lesson will be a short one. These are the steps needed to deploy your web app to a web hosting service, Heroku. This allows for other people to access your web app through their own machine, and not just yours.
You can choose to either 
- Deploy through Github pipeline UI (just clicking buttons)
or
- Deploy through Heroku CLI (you'll have to download the CLI toolbelt for this)

## Deploy through Github pipeline on Heroku interface
1. Create a new Heroku account ([signup link](https://signup.heroku.com/www-header))
2. Your project repo should already exist on GitHub, otherwise create it now. We covered this in [Lesson 1](https://github.com/UWCoffeeNCode/Lessons/tree/master/F18/Projects/rails-app/1).
3. Now on your Heroku dashboard, click **New** to create a new app.

![dashboard](https://github.com/UWCoffeeNCode/Lessons/blob/master/F18/Projects/rails-app/7/1.png)

4. On the next screen you can choose a unique app name, and click **Create**.

![create](https://github.com/UWCoffeeNCode/Lessons/blob/master/F18/Projects/rails-app/7/2.png)

5. Then on the application dashboard under the Deploy tab, you should see some options for you to pick from. In the Deployment method section, click on GitHub.

![deploy tab](https://github.com/UWCoffeeNCode/Lessons/blob/master/F18/Projects/rails-app/7/4.png)

6. Moving on to the Connect to GitHub section, this should prompt you to sign in to GitHub using your email and password.

![connect to github](https://github.com/UWCoffeeNCode/Lessons/blob/master/F18/Projects/rails-app/7/5.png)

7. Choose the project repo on GitHub that you want to deploy, and click **Connect**.

![pick repo](https://github.com/UWCoffeeNCode/Lessons/blob/master/F18/Projects/rails-app/7/6.png)

8. Skip over the section Automatic deploys, we can just manually deploy it ourselves.
9. In the final section, Manual deploy, choose which branch to deploy (it should be *master*) and click **Deploy**.

![deploy!](https://github.com/UWCoffeeNCode/Lessons/blob/master/F18/Projects/rails-app/7/7.png)

10. You should see your app live! Click on **View** to see the live app in the browser.
11. However, you'll notice that Signup and Login don't work. That's no good. Click on the Resources tab in your Heroku dashboard and search for the Postgres add-on. Click to add to your app.
12. In the top right corner click on **More** and click on **Run console**. This should give you a change to type in `rake db:migrate`, and voila! Now the app should be fully working.


## Deploy through Heroku CLI
1. Create a new Heroku account ([signup link](https://signup.heroku.com/www-header))
2. Install the  [Heroku Toolbelt](https://toolbelt.heroku.com/) on your computer.
3. In terminal, first type `heroku login` then log in with your Heroku credentials. 
4. In your Gemfile, add the `pg` gem to the production group, and make sure the sqlite gem is only under development and test :
```ruby
group :development, :test do
  gem 'sqlite3'
...
end
...
group :production do
  gem 'pg'
end
```

5. In terminal, do `bundle install` to install the new gem.
6. Make sure **config/database.yml** is updated to support `postgresql` adapter. 

Change
```yml
production:
  <<: *default
  database: db/production.sqlite3
```
to 
```yml
production:
  <<: *default  
  adapter: postgresql  
  database: db/production.sqlite3
```
7. Commit your changes to git
```bash
git add . 
git commit -m "add Heroku config"
```
8. In terminal, create a new Heroku app with `heroku create`
9. Then push your code to Heroku with `git push heroku master`
10. Make sure you've added the postgres add-on to Heroku to enable the database with the command `heroku addons:create heroku-postgresql`
11. Once that's done, `heroku run rake db:migrate` to apply all the migrations to your database.
12. Get the URL to visit with the command `heroku apps:info` and congrats! You're done!
