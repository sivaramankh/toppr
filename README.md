# Toppr

Sample Flask Bootstrap app amde for a Hackathon.

# Deploying the App
For deploying the app in your local machine, setup a virtualenv using Python 3.5. If inside the folder containing requirements.txt, run – "pip install –r requirements.txt". If want to replicate the MongoDB db collection, run csv_to_db.py after changing the connection and csv file path details. MongoDB database url for the app can be setup in the __init__.py file inside the app. 
To run the app run command – python run.py

# REST API Documentation
i.	/api/count
Returns the number of records in the database.

ii.	/api/list
Returns all the records in the database.

iii.	/api/list/<battle_number>
Returns the battle record corresponding to the battle number.

iv.	/api/search?<parameter>=value&<parameter2>=value2
Returns battle records corresponding to the parameters. Multiple parameters supplied for the same field will be exclusive search and different field .

v.	/api/stats
Returns the battle statistics for the whole dataset. 

vi.	/api/<values>
Values in [active, largest, year]. Returns the corresponding statistics.

If any query didn’t match the any of the records, an error response is send.
