#!/bin/bash

# Navigate to the project directory
cd "$(dirname "$0")/.."

# Start the Flask Webhook Listener
echo "Starting Webhook Listener..."
nohup python3 webhook_listener.py > logs/webhook.log 2>&1 &

# Start ngrok to expose the webhook publicly
echo "Starting ngrok..."
nohup ngrok http 5000 > logs/ngrok.log 2>&1 &

echo "Webhook listener and ngrok started successfully!"

