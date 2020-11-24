Nic Pittman
# sqlalchemy-challenge

![Screenshot 2020-11-23 194038](https://user-images.githubusercontent.com/69124282/100031536-dd52dd00-2dc3-11eb-8022-a33b52f5eab9.jpg)


# SQLAlchemy Homework - Surfs Up!

![batman](https://user-images.githubusercontent.com/69124282/96508304-65bfea00-1228-11eb-9c60-615edaa649e2.jpg)


Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii! To help with your trip planning, you need to do some climate analysis on the area. The following outlines what you need to do.

# Step 1 - Climate Analysis and Exploration

To begin, use Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.


- Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.


- Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.


- Use SQLAlchemy create_engine to connect to your sqlite database.


- Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.


# Precipitation Analysis

- Design a query to retrieve the last 12 months of precipitation data.


- Select only the date and prcp values.


- Load the query results into a Pandas DataFrame and set the index to the date column.


- Sort the DataFrame values by date.


- Plot the results using the DataFrame plot method.

![pandas_precipitation](https://user-images.githubusercontent.com/69124282/96505629-68b8db80-1224-11eb-86bf-8bfe24987e02.jpg)


- Use Pandas to print the summary statistics for the precipitation data.

![prcp_summary](https://user-images.githubusercontent.com/69124282/96505981-e11f9c80-1224-11eb-9978-14b500c562ee.jpg)


# Station Analysis


- Design a query to calculate the total number of stations.
 
- Design a query to find the most active stations.
 
    -- List the stations and observation counts in descending order.


    -- Which station has the highest number of observations?


    -- Hint: You will need to use a function such as func.min, func.max, func.avg, and func.count in your queries.


- Design a query to retrieve the last 12 months of temperature observation data (TOBS).


    -- Filter by the station with the highest number of observations.


    -- Plot the results as a histogram with bins=12.


![station_analysis](https://user-images.githubusercontent.com/69124282/96506898-69527180-1226-11eb-9b79-00926c898b4a.jpg)




# Step 2 - Climate App

Now that you have completed your initial analysis, design a Flask API based on the queries that you have just developed.

- Use Flask to create your routes.


# Routes


- "/"


    -- Home page.


    -- List all routes that are available.

![available_routes](https://user-images.githubusercontent.com/69124282/96505223-d284b580-1223-11eb-9725-5417ddf37834.jpg)





- "/api/v1.0/precipitation"


    -- Convert the query results to a dictionary using date as the key and prcp as the value.


    -- Return the JSON representation of your dictionary.

![precipitation_results](https://user-images.githubusercontent.com/69124282/96505224-d284b580-1223-11eb-9158-7ada579c68f4.jpg)






- "/api/v1.0/stations"

    -- Return a JSON list of stations from the dataset.

![station_results](https://user-images.githubusercontent.com/69124282/96505221-d284b580-1223-11eb-8b80-5d473b5a8ca4.jpg)





- "/api/v1.0/tobs"


    -- Query the dates and temperature observations of the most active station for the last year of data.


    -- Return a JSON list of temperature observations (TOBS) for the previous year.

![tobs_results](https://user-images.githubusercontent.com/69124282/96505222-d284b580-1223-11eb-9091-f6c691aaf0fa.jpg)






- "/api/v1.0/<start> and /api/v1.0/<start>/<end>"


    -- Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.


    -- When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

![start_results](https://user-images.githubusercontent.com/69124282/96505220-d284b580-1223-11eb-88d6-fccd5e784c7a.jpg)


 
 
 
 -- When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.
   
![start_end_results](https://user-images.githubusercontent.com/69124282/96505218-d284b580-1223-11eb-93bb-e84c3a953f22.jpg)

