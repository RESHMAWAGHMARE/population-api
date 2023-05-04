# population-api

#World Population API
This is a Django project that provides an API to retrieve population data for countries from the World Bank API.

Installation
Clone this repository:



git clone https://github.com/your-username/world-population-api.git
Install the project dependencies:


pip install -r requirements.txt
Create a local_settings.py file in the myproject directory with the following contents:



SECRET_KEY = '<your_secret_key>'
DEBUG = True
Replace <your_secret_key> with a secret key for your Django project.

Apply database migrations:


python manage.py migrate
Run the development server:


python manage.py runserver
The API will be available at http://localhost:8000/api/.

API Endpoints
The following API endpoints are available:

/api/countries/: Returns a list of all countries in the World Bank API.
/api/population/<iso2code>/: Returns the population data for the given country code (e.g. /api/population/US/ for the United States).
Web Interface
A web interface is available at http://localhost:8000/ that displays a list of all available countries. Clicking on a country will display the population data for that country.