import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")
# reflect an existing database into a new model 
Base = automap_base()
# reflect the tables 
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def home_page():
#List all routes that are available.
    return (
		f"Available Routes:<br>"
		f"/api/v1.0/precipitation<br>"
		f"/api/v1.0/stations<br>"
		f"/api/v1.0/tobs<br>"
		f"/api/v1.0/<start><br>"
		f"/api/v1.0<start>/<end><br>"
	)

##################___Precipitation___#################

# Convert the query results to a dictionary using date as the key and prcp as the value.
# Return the JSON representation of your dictionary

##################___Precipitation___#################

@app.route("/api/v1.0/precipitation")
def precipitation():
    
	# Query all Measurment
	results = session.query(Measurement).all()
	# Close the Query
	session.close()

	# Create a dictionary using 'date' as the key and 'prcp' as the value.
	prcp_list = []
	for result in results:
		prcp_dict = {}
		prcp_dict["date"] = result.date
		prcp_dict["prcp"] = result.prcp
		prcp_list.append(prcp_dict)

	# Jsonify summary
	return jsonify(prcp_list)


##################___Stations___#################

# Return a JSON list of stations from the dataset.

##################___Stations___#################

@app.route("/api/v1.0/stations")
def stations():
# Create session 
    session = Session(engine)

# query for all stations
    results = session.query(Station.station).all()
    
# close session
    session.close()

# Convert list of tuples into normal list
    station_list = list(np.ravel(results))

    return jsonify(station_list)


##################___TOBS___#################

#Query the dates and temperature observations of the most active station for the last year of data.
#Return a JSON list of temperature observations (TOBS) for the previous year.

##################___TOBS___#################

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # query for station activity order
    station_order = session.query(Measurement.station,func.count(Measurement.station)) \
                 .group_by(Measurement.station) \
                 .order_by(func.count(Measurement.station).desc()).all()
    
    # set most active station to variable
    most_active_station=station_order[0][0] 

# query of the most active station for the last year of data
    results = session.query(Measurement.date, Measurement.tobs) \
        .filter(Measurement.station == most_active_station) \
        .filter(Measurement.date >= "2016-08-23") \
        .group_by(Measurement.date).all()

    # close session
    session.close()
    
    date_tobs = []
    for result in results:
        tobs_dict = {}
        tobs_dict["date"] = result.date
        tobs_dict["tobs"] = result.tobs
        date_tobs.append(tobs_dict)
        
    return jsonify(date_tobs)


##################___<start>/<end><br>___#################

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

##################___<start>/<end><br>___#################

# This function called `calc_temps` will accept start date and end date in the format '%Y-%m-%d' 
# and return the minimum, average, and maximum temperatures for that range of dates
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVG, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()


@app.route("/api/v1.0/<start>")
def start(start):
    #session open
    session = Session(engine)
    
    # calc_temps second argument from start date to the max date
    max_date_query = session.query(func.max(func.strftime("%Y-%m-%d", Measurement.date))).all()
    max_date = max_date_query[0][0]
    
    tobs = calc_temps(start, max_date)
    
    # close session
    session.close()

    # min, avg, max list 
    tobs_list = []
    start_date_dict = {'start_date': start, 'end_date': max_date}
    tobs_list.append(start_date_dict)
    tobs_list.append({'Hawaii': 'Minimum', 'Temperature': tobs[0][0]})
    tobs_list.append({'Hawaii': 'Average', 'Temperature': tobs[0][1]})
    tobs_list.append({'Hawaii': 'Maximum', 'Temperature': tobs[0][2]})

    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
   
    #calc_temps tobs to start / end
    tobs = calc_temps(start, end)

    # min, avg, max list 
    tobs_list = []
    start_date_dict = {'start_date': start, 'end_date': end}
    tobs_list.append(start_date_dict)
    tobs_list.append({'Hawaii': 'Minimum', 'Temperature': tobs[0][0]})
    tobs_list.append({'Hawaii': 'Average', 'Temperature': tobs[0][1]})
    tobs_list.append({'Hawaii': 'Maximum', 'Temperature': tobs[0][2]})

    return jsonify(tobs_list)




if __name__ == "__main__":
	app.run(debug=True)