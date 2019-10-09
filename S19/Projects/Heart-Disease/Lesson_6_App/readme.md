# Heart Disease Classifier with UI

## Getting started
1. To run this you need Python3 and Pip3 installed
2. Install all dependencies with Pip3

The HTML page generates a graph.html file that visualizes the risk of heart disease from a RandomForest classifier. This file is generated via our server.py file that runs a Flask-Python server locally.<br />
Navigate to the app directory and run
```
pip3 install pandas
pip3 install numpy
pip3 install flask
pip3 install shap
pip3 install sklearn
```

This should enable our server to start running (Please reinstall if any dependencies are missing). 

## Run the server
Navigate to the app directory and run
```
export FLASK_APP=hello.py
flask run
```
http://flask.pocoo.org/docs/1.0/quickstart/

## HTML
Now making POST request calls to http://127.0.0.1:5000/forest will also generate a graph locally. A POST request is sent via the form button "Classify Risk". Our custom commands and user-inputed data is also sent from this POST request and will be processed in Flask.