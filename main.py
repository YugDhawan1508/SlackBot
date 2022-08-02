from http import client
from unicodedata import name
import requests
from pprint import pprint
import slack
import os
import requests
from pprint import pprint
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, Response 
from slackeventsapi import SlackEventAdapter

env_path = Path('.') / '.env'

app=Flask(__name__)
load_dotenv(dotenv_path=env_path)
slack_event_adapter = SlackEventAdapter(os.environ['SECRET'], '/slack/events', app)

client = slack.WebClient(token=os.environ['TOKEN'])

API_URL = "https://api.github.com"
payload = '{"name": "Testname"}'




headers={
    "Authorization": "token "+ os.environ['GIT_TOKEN'],
    "Accept": "application/vnd.github+json"
}


@app.route('/create-repo', methods=['POST'])
def create_repo():
    r=requests.post(API_URL+"/user/repos", data=payload, headers=headers)
    client.chat_postMessage(channel='#general', text='Created Repo TestName')


client.chat_postMessage(channel='#general', text='I Am Online')





if __name__ == "__main__":
    app.run()
