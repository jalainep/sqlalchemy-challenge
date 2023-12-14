# Import the dependencies.

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np
from flask import Flask , jsonify
#################################################
# Database Setup
#################################################


# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect the tables
Base = automap_base()

Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

#################################################
# Flask Setup
#################################################


app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return (f"/api/v1.0/precipitation"
            f"/api/v1.0/stations"
            f"/api/v1.0/tobs"
            f" /api/v1.0/<start>"
            f"/api/v1.0/<start>/<end>"
           )
             
@app.route("/api/v1.0/precipitation")
def precipitation():    
    results = session.query(Base.classes.measurement.date, Base.classes.measurement.prcp).\
    filter(Base.classes.measurement.date >= last_year).\
    order_by(Base.classes.measurement.date).all()
    
    prcp_dict = []
    for date, prcp in last_year_data:
        date_dict = {}
        date_dict["Date"] = date
        date_dict["Precipitation"] = prcp
        prcp_dict.append(date_dict)
    
     return jsonify(prcp_dict)
        
@app.route("/api/v1.0/stations")
def stations():
    stations_list= session.query(Station.station, Station.name).all()
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def most_active():
    temp_results = session.query(Measurement.tobs).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= last_year).all()
    return jsonify(temp_results)
    

    
@app.route("/api/v1.0/<start>")
def start_day():
    
@app.route("/api/v1.0/<start>/<end>")  
def end_day():            
            
            