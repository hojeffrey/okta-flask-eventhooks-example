from flask import abort, Flask, make_response, redirect, url_for, render_template, logging, session, flash, jsonify, request
import logging
import sys
import json
import requests

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def event_hook():
    # One Time Token Verification
    if request.method == "GET":
        headers = request.headers
        verification_challenge_token = request.headers['x-okta-verification-challenge']
        return_response_body = f'{{ "verification": "{verification_challenge_token}" }}'
        print(headers)
        print(verification_challenge_token)
        return (return_response_body).encode()
    # Handling Event Delivery Requests
    if request.method == "POST":
        data = request.get_json()
        json_data = json.dumps(data)

        # Values Parsed out to variables
        actor_okta_id = data["data"]["events"][0]["actor"]["id"]
        actor_email = data["data"]["events"][0]["actor"]["alternateId"]
        actor_name = data["data"]["events"][0]["actor"]["displayName"]
        target_okta_id = data["data"]["events"][0]["target"][0]["id"]
        target_email = data["data"]["events"][0]["target"][0]["alternateId"]
        target_name = data["data"]["events"][0]["target"][0]["displayName"]
        group_okta_id = data["data"]["events"][0]["target"][1]["id"]
        group_name = data["data"]["events"][0]["target"][1]["displayName"]
        published_time = data["data"]["events"][0]["published"]


if __name__ == "__main__":
    app.run(debug=True, port=80)