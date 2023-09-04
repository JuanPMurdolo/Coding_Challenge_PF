# Coding_Challenge_PF
Coding Challenge software
Python (3.9+) or Typescript Backend Challenge

Task:
•	Build a RESTful api that services requests for sprocket factory data and sprockets.
•	The app should be built using either Python (3.9+) or Typescript.
•	For data retention, a database or cache can be used.
•	Ideally, use docker/docker-compose for standing up the datastore.
•	The code should be on a github repository that should be shared with your engineering contact.

Requirements:
•	RESTful Endpoints
o	An endpoint that returns all sprocket factory data ✓
o	An endpoint that returns factory data for a given factory id ✓
o	An endpoint that returns sprockets for a given id ✓
o	An endpoint that will create new sprocket ✓
o	An endpoint that will update sprocket for a given id ✓
   -  Seed data/examples of the factory and sprocket are in the attached JSON files
   -  Include a README with instructions on how to stand up the database and application

Notes:
The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories. A virtual environment is created on top of an existing Python installation, known as the virtual environment’s “base” Python, and may optionally be isolated from the packages in the base environment, so only those explicitly installed in the virtual environment are available.


For runing the app on a test environment: create a new python venv, use pip for installation of the requirements, run the flask app and then test using swagger endpoints.

- run the command on the root directory: python -m venv .venv (The .venv is for the creation of venv on this directory)
- Close the terminal you were using and open a new one for the venv to load you should see the (.venv) line in the new command line.
- cd RestApi
- run pip install -r requirements.txt
- use: flask run
- open http://127.0.0.1:5000/swagger-ui on your desired browser
- then you will have a swagger GUI to test the RestAPI endpoints
   - for testing the factory one use the factory endpoints
   - for testing the sprocket one use the sprocket endpoint 
