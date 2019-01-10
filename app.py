import json
import pandas as pd
import numpy as np
import os
import sqlalchemy

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, render_template
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///UberPrices.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
UberPrices = Base.classes.uberPrices

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///UberPrices.sqlite'
#db = SQLAlchemy(app)

# Define our pet table
#class UberPrices(db.Model):
    #__tablename__ = 'uberPrices'
    #id = db.Column(db.Integer, primary_key=True)
    #place = db.Column(db.String)
    #lat = db.Column(db.Integer)
    #lon = db.Column(db.Integer)
    #dist = db.Column(db.Integer)
    #display_name = db.Column(db.String)
    #product_id = db.Column(db.String)
    #duration = db.Column(db.Integer)
    #estimate = db.Column(db.String)

#################################################
# Flask Routes
#################################################

#@app.route("/")
#def welcome():
 #   """List all available api routes."""
 #   return (
 #       f"Available Routes:<br/>"
 #       f"/api/v1.0/names<br/>"
 #       f"/api/v1.0/passengers"
 #   )


#@app.route("/api/v1.0/names")
#def names():
   # """Return a list of all passenger names"""
    # Query all passengers
    #results = session.query(UberPrices.place, UberPrices.lat, UberPrices.lon, UberPrices.dist, UberPrices.display_name, 
    #                        UberPrices.product_id, UberPrices.duration, UberPrices.estimate).all()

    # Convert list of tuples into normal list
    #all_names = list(np.ravel(results))

    #return jsonify(results)


#@app.route("/api/v1.0/passengers")
#def passengers():
    #"""Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    #results = session.query(Passenger).all()

    # Create a dictionary from the row data and append to a list of all_passengers
    #all_passengers = []
    #for passenger in results:
    #    passenger_dict = {}
    #    passenger_dict["name"] = passenger.name
     #   passenger_dict["age"] = passenger.age
    #    passenger_dict["sex"] = passenger.sex
    #    all_passengers.append(passenger_dict)

    #return jsonify(all_passengers)

results = session.query(UberPrices.place, UberPrices.lat, UberPrices.lon, UberPrices.dist, UberPrices.display_name, 
                           UberPrices.product_id, UberPrices.duration, UberPrices.estimate).all()
    
    
@app.route("/data")
def data():
    
    #results = session.query(UberPrices.place, UberPrices.lat, UberPrices.lon, UberPrices.dist, UberPrices.display_name, 
    #                       UberPrices.product_id, UberPrices.duration, UberPrices.estimate).all()
    data = jsonify(results)
    
    # data = db.session.query(uberPrices).all()
    return jsonify(results)
    #return render_template("index.html")

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)