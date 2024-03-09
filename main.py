from flask import Flask, jsonify, request
import json
import re
import requests

app = Flask(__name__)

# Load JSON data from the provided URL
def load_json_data():
    # Send GET request to the provided URL
    response = requests.get("https://foyzulhassan.github.io/files/favs.json")
    # Check if the response status code is 200 (OK), and if so, return the data
    if response.status_code == 200:
        return response.json()
    else:
        return None 

# Endpoint to get all tweets
@app.route('/tweets', methods=['GET'])
def get_all_tweets():
    # Load JSON data
    data = load_json_data()
    if data:
        # Extract required information from each tweet and create a list of dictionaries
        tweets = [{"Created at": tweet['created_at'], "Tweet ID": tweet['id'], "Text": tweet['text']} for tweet in data]
        return jsonify(tweets)
    else:
        return jsonify({"message": "Failed to load tweets"}), 500

# Endpoint to get all external links
@app.route('/external_links', methods=['GET'])
def get_external_links():
    # Load JSON data
    data = load_json_data()
    if data:
        external_links = {}
        # Iterate through each tweet to extract external links using regex
        for tweet in data:
            tweet_id = str(tweet['id'])
            text = tweet['text']
            urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
            external_links[tweet_id] = urls
        return jsonify(external_links)
    else:
        return jsonify({"message": "Failed to load tweets"}), 500

# Endpoint to get details of a specific tweet by its ID
@app.route('/tweet_details/<tweet_id>', methods=['GET'])
def get_tweet_details(tweet_id):
    # Load JSON data
    data = load_json_data()
    if data:
        for tweet in data:
            # Find the tweet with the specified ID and extract required details
            if str(tweet['id']) == tweet_id:
                tweet_details = {
                    "Created at": tweet['created_at'],
                    "Text": tweet['text'],
                    "User's screen name": tweet['user']['screen_name']
                }
                return jsonify(tweet_details)
        return jsonify({"message": "Tweet not found"}), 404
    else:
        return jsonify({"message": "Failed to load tweets"}), 500

# Endpoint to get detailed profile information about a specific Twitter user by screen name
@app.route('/user_profile/<screen_name>', methods=['GET'])
def get_user_profile(screen_name):
    # Load JSON data
    data = load_json_data()
    if data:
        for tweet in data:
            # Find the tweet with the specified screen name and extract user profile details
            if tweet['user']['screen_name'] == screen_name:
                user_profile = {
                    "Location": tweet['user']['location'],
                    "Description": tweet['user']['description'],
                    "Followers count": tweet['user']['followers_count'],
                    "Friends count": tweet['user']['friends_count']
                }
                return jsonify(user_profile)
        return jsonify({"message": "User not found"}), 404
    else:
        return jsonify({"message": "Failed to load tweets"}), 500

if __name__ == '__main__':
    app.run(debug=True)
