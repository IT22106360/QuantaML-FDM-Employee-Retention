import pickle 
import numpy as np 

import pickle

# Load the model from the file
with open('static/model/selected_model.pkl', 'rb') as file:
    model = pickle.load(file)

def get_predictions(city_development_index, relevant_experience, education_level, experience, last_new_job_gap):
    #relevant experience encoding
    relevant_experience = 1 if relevant_experience == 'Yes' else 0

    #education level encoding
    education_encoding = {
        'Graduate':0,
        'Masters':1,
        'High School':2,
        'PhD':3,
        'Primary School':4
    }

    education_level = education_encoding.get(education_level, 0)

    #prepare inputs to send to the model

    input_features = np.array([[
            city_development_index,
            relevant_experience,
            education_level,
            experience,
            last_new_job_gap
        ]])

    prediction = model.predict_proba(input_features)
    output = round(prediction[0][1], 2)

    binary_prediction = 1 if output >= 0.5 else 0

    return binary_prediction

