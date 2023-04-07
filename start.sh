#!/bin/bash

# Install project dependencies
# pip install -r requirements.txt

# moving files to /usr/bin/chatbot
mkdir -p /usr/bin/chatbot
chmod +x main.py
cp main.py /usr/bin/chatbot/
cp chatbot.py /usr/bin/chatbot/

# add a place for api key and add it to .env file in /usr/bin/chatbot
echo "API_KEY=" >/usr/bin/chatbot/.env
