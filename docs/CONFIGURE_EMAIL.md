1. Install yagmail and python-dotenv
pip install yagmail
pip install python-dotenv

2.Set up Gmail App Password (if using Gmail):
Visit Google App Passwords.
Generate an app password and save it.
3.Update the config/webhook_env file with your email credentials
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECIPIENT=recipient@example.com

