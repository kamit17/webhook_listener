Webhook Automation with Flask & ngrok 


# Webhook Automation with Flask & ngrok 

## Overview
This project listens for **GitHub webhook events** and **sends email notifications** for every new commit.

Features
1. Listens for webhook events from GitHub  
2. Runs as a **systemd service** on Linux  
3. Uses **ngrok** to expose local server  
4. Sends **email notifications** when a push occurs 

How It Works
1. Flask app listens for webhook events.
2. ngrok exposes the local server to the internet.
3. GitHub sends webhook events to the listener.
4. The script processes the webhook & sends an email.(pending)

Technologies Used
- Python (`Flask`)
- ngrok (exposes local server)
- systemd (runs service in background)

Installation & Setup
1. Install Dependencies
Refer to 📄 INSTALLATION.md for detailed installation steps.

2. Start ngrok
Refer to 📄 SETUP_WEBHOOK.md for webhook setup.

3. Configuring GitHub Webhook
Follow 📄 SETUP_WEBHOOK.md for full instructions.

3. Running the Service
Refer to 📄 RUNNING_SERVICE.md for detailed steps.

4. Troubleshooting
 For common issues and solutions, refer to 📄 TROUBLESHOOTING.md.

