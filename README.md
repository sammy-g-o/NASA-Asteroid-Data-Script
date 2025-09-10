# NASA-Asteroid-Data-Script
This Python script retrieves data from NASA's NeoWS (Near Earth Object Web Service) API. It fetches information for a specific asteroid by its ID and also gets a list of all near-earth objects, saving the latter to a JSON file.
## Prerequisites
Python installed on your system.
The requests library:
pip install requests


## How to Use
Make sure the requests library is installed.
Run the script from your terminal:
python "get asteroid data from nasa's api.txt"


The script will print the name, hazardous status, and orbiting body of a specific asteroid to the console.
It will also create a file named allasteroiddata.json containing a list of all near-earth objects from the API.
Note: The script uses a hard-coded API key. For production applications, you should handle API keys more securely (e.g., using environment variables).
