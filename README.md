Flask Twitter API
This Flask application serves as a simple API to retrieve Twitter data from a provided JSON file. It exposes several endpoints to retrieve tweets, extract external links, fetch details of a specific tweet by its ID, and obtain detailed profile information about a specific Twitter user by their screen name.

Installation
Clone this repository to your local machine:

bash
Copy code
git clone <repository-url>
Navigate to the project directory:

bash
Copy code
cd flask-twitter-api
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Flask application:

bash
Copy code
python app.py
Once the server is running, you can access the API endpoints using the following base URL:

arduino
Copy code
http://localhost:5000
API Endpoints
Get All Tweets
URL: /tweets
Method: GET
Description: Retrieves all tweets from the JSON file.
Sample Response:
json
Copy code
[
{
"Created at": "Wed Mar 13 23:01:36 +0000 2013",
"Tweet ID": 311975360667459585,
"Text": "Was wondering why @billgates cc'd me on story abt @MSFTResearch cool viral search tool; discovered I'm featured in it http:\/\/t.co\/g6oSeEIEUr"
},
...
]
Get All External Links
URL: /external_links
Method: GET
Description: Extracts all external links from the tweets.
Sample Response:
json
Copy code
{
"311975360667459585": [
"http:\/\/t.co\/g6oSeEIEUr"
],
...
}
Get Tweet Details by ID
URL: /tweet_details/<tweet_id>
Method: GET
Description: Retrieves details of a specific tweet by its ID.
Sample Response:
json
Copy code
{
"Created at": "Wed Mar 13 23:01:36 +0000 2013",
"Text": "Was wondering why @billgates cc'd me on story abt @MSFTResearch cool viral search tool; discovered I'm featured in it http:\/\/t.co\/g6oSeEIEUr",
"User's screen name": "timoreilly"
}
Get User Profile by Screen Name
URL: /user_profile/<screen_name>
Method: GET
Description: Retrieves detailed profile information about a specific Twitter user by their screen name.
Sample Response:
json
Copy code
{
"Location": "Sebastopol, CA",
"Description": "Founder and CEO, O'Reilly Media. Watching the alpha geeks, sharing their stories, helping the future unfold.",
"Followers count": 1679016,
"Friends count": 1012
}
Testing with Postman
Download and install Postman.

Open Postman and import the provided collection: Flask Twitter API.postman_collection.json.

Once imported, you will find the collection containing requests for each API endpoint.

Click on the desired request, then click "Send" to execute the request and view the response.
