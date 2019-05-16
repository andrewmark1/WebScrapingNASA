# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:36:03 2019

@author: andrewd
"""

import PyMongo
from scrape_mars import scrape
from flask import Flask, render_template

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():

    # Find one record of data from the mongo database
    mars_data = mongo.db.data.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)

@app.route('/scrape')
def scrapepage():
    # Store the entire team collection in a list
    db = mongo.db.mars_data
    mars_dict = scrape()
    db.mars_data.insert(mars_dict)

    # Return the template with the teams list passed in
    return render_template('index.html', mars_dict=mars_dict)

if __name__ == "__main__":
    app.run(debug=True)
    
