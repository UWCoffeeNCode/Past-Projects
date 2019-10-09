# This file should be found under your project directory
# under APP-FOLDER/config/routes.rb, where APP-FOLDER is 
# the name of your application
Rails.application.routes.draw do
  get 'static_pages/home'

  get 'static_pages/help'

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  root 'application#hello'
end
