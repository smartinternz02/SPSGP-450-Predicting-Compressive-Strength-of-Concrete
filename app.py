# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 19:01:30 2021

@author: suresh
"""


from flask import Flask, request, render_template

import pickle 
import numpy as np

model=pickle.load(open('cement.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/index.html')
def inputs():
    return render_template('index.html')
@app.route('/login',methods=['POST'])
def login():
    cement=(float)(request.form['cement'])
    blast=(float)(request.form['blast'])
    flyash=(float)(request.form['flyash'])
    superplasticiser=(float)(request.form['super'])
    water=(float)(request.form['water'])
    coarse=(float)(request.form['coarse'])
    fine=(float)(request.form['fine'])
    age=(float)(request.form['age'])
    t=[[cement,blast,flyash,superplasticiser,water,coarse,fine,age]]
    y_pred=model.predict(t)
    result="Strength of the cement is "+(str)(y_pred)
    return render_template("result.html",showcase=result)

if __name__ == "__main__":
    app.run(debug=True)