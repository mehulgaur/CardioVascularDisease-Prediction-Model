# -*- coding: utf-8 -*-
"""

@author: Mehul
"""
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server

import pickle
import numpy as np

model = pickle.load(open('CVDPredictionModel.pkl', 'rb'))
app = Flask(__name__)


def predict():
    age = input("Enter your age in years：", type=NUMBER)
    age = age*365
    
    gender = select("Select your Gender", ['Male','Female'])
    if (gender == 'Male'):
        gender = 1

    elif (gender == 'Female'):
        gender = 2
    
    height = input("Enter the Height(in cm)", type=FLOAT)
    height = np.log(height)
    
    weight = input("Enter the weigth(in Kg)：", type=FLOAT)
    weight = np.log(weight)
    
    ap_hi = input("Enter the Systolic Blood Pressure(in mmHG)", type=NUMBER)
    
    
    ap_lo = input('Enter the Diastolic Blood Pressure(in mmHG)', type=NUMBER)
    
    cholesterol = select('Cholestrol Level', ['Normal', 'Above Normal', 'Well Above Normal'])
    if (cholesterol == 'Normal'):
        cholesterol = 1
    
    elif(cholesterol == 'Above Normal'):
        cholesterol = 2
        
    else:
        cholesterol = 3
        
    
    gluc = select('Glucose Level', ['Normal', 'Above Normal', 'Well Above Normal'])
    if (gluc == 'Normal'):
        gluc = 1
    
    elif(gluc == 'Above Normal'):
        gluc = 2
        
    else:
        gluc = 3
    
    smoke = select('Do you Smoke?', ['Yes', 'No'])
    if (smoke == 'No'):
        smoke = 0
    
    else:
        smoke = 1
        
    alco = select('Do you consume Alcohol?', ['Yes', 'No'])
    if (alco == 'No'):
        alco = 0
    
    else:
        alco = 1
    
    
    active = select('Are you Physically Active?', ['Yes', 'No'])
    if (active == 'No'):
        active = 0
    
    else:
        active = 1
    
    
    bmi = weight/((height/100))**2
    
    
    
    
    

    prediction = model.predict([[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active,bmi]])
    

    if prediction == 0:
        put_text("You dont have CVD!! Congrats")

    else:
        put_text('You have CVD!! Please visit the doctor ASAP!!')

    


app.add_url_rule('/', 'webio_view', webio_view(predict),
            methods=['GET', 'POST', 'OPTIONS'])

app.run(host='localhost', port=80)