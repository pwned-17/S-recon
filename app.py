import slack
import os
from flask import Flask,request
from dotenv import dotenv_values
from slack_bolt.adapter.flask import SlackRequestHandler
from drecon import slack_handler
from slack_bolt import App

# Initialize Dot Env
env = dotenv_values(".env")
# Initialize Flask App
app = Flask(__name__)

# Slack Related Stuff
client = slack.WebClient(token=env.get("SLACK_TOKEN"))
eventHandler = App(signing_secret=env.get("SIGNING_SECRET"), token=env.get("SLACK_TOKEN"))
requestHandler = SlackRequestHandler(app=eventHandler)

@app.route("/slack/events",methods=["POST"])
def slack_events():
    return requestHandler.handle(request)


@eventHandler.event("app_mention")
def message(event):
    print(event)
    slack_handler.SlackHandler(event).parse_event()







if __name__=="__main__":
    app.run(debug=True,port=6789)
