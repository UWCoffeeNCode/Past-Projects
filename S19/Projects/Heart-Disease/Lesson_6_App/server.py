from flask import Flask
from flask import request
from random import randrange

app = Flask(__name__)
import shap
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


@app.route('/forest')
def get_forest_model():

    # Read in Data
    dt = pd.read_csv("./heart_disease.csv")

    # Transform to strings
    dt['sex']= dt['sex'].astype('object')
    dt['chest_pain']= dt['chest_pain'].astype('object')
    dt['blood_sugar']= dt['blood_sugar'].astype('object')
    dt['cardiographic_health']= dt['cardiographic_health'].astype('object')
    dt['exercise_angina']= dt['exercise_angina'].astype('object')
    dt['slope_cardio']= dt['slope_cardio'].astype('object')
    dt['thalassemia']= dt['thalassemia'].astype('object')

    # Transform the 7 fields above into singular fields to put 
    # greater emphasis on values on small scales like 1-3
    dt = pd.get_dummies(dt, drop_first=True)

    # Train the data
    X_train, X_test, y_train, y_test = train_test_split(dt.drop('target', 1), dt['target'], random_state = 42)

    # Fit the data
    model = RandomForestClassifier(max_depth = 7, random_state = 42)
    model.fit(X_train, y_train)

    # function to create shaped plots of heart disease
    def heart_disease_risk_factors(model, patient):
        # Get weights of each feature
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(patient)
        
        # Plot weights
        shap.initjs()
        shap.save_html("./graph.html", shap.force_plot(explainer.expected_value[1], shap_values[1], patient))
        return shap.force_plot(explainer.expected_value[1], shap_values[1], patient)

    # Regularize data for custom override
    data_input = dt.drop('target', 1).mean()

    
    if (request.args.get("override") == "0"):
        # Override with heart disease patient, picks random patient with heart disease and plots it
        data_input = dt.query("target == 1").drop('target', 1).iloc[randrange(dt.query("target == 1").shape[0]), :]

    elif (request.args.get("override") == "1"):
        # Override with healthy patient, picks random healthy patient and plots it
        data_input = dt.query("target == 0").drop('target', 1).iloc[randrange(dt.query("target == 0").shape[0]), :]

    else:
        # Parse request and update the data_input field to create a custom graph
        # Iterate through all keys in the argument
        for key in request.args:
            # Get the value for this key
            val = request.args.get(key)

            # Conditions to modify the result from this key
            if val != "" and key != "override":

                # Special condition since we used the function get_dummies() previously
                if key in ["sex", "chest_pain", "thalassemia"]:
                    data_input.update(pd.Series([0, 0, 0], index=[key+"_1", key+"_2", key+"_3"]))
                    if val != 0:
                        data_input.update(pd.Series([1], index=[key+"_"+val]))
                data_input.update(pd.Series([val], index=[key]))
    
    # Type conversion
    data_for_prediction = data_input.astype(float)

    # Generate the html graph
    heart_disease_risk_factors(model, data_for_prediction)

    # UI interface if accessed via web browser
    return 'Bonjour, World!'