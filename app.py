# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:36:03 2019

@author: andrewd
"""

from scrape_mars import scrape
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/weather_app")

@app.route("/")
def index():

    # Find one record of data from the mongo database
    mars_data = mongo.db.mars_data.find_one()

    # Return template and data
    return render_template("index.html", mars=mars_data)

@app.route('/scrape')
def scrapepage():
    # Store the entire team collection in a list
    db = mongo.db.mars_data
    mars_dict = scrape()
    db.update({}, mars_dict, upsert=True)

    # Return the template with the teams list passed in
    return render_template('index.html', mars=mars_dict)

if __name__ == "__main__":
    app.run(debug=True)
    
