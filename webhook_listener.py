import os
import yagmail
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables from config/webhook_env
load_dotenv("config/webhook_env")

# Flask App Initialization
app = Flask(__name__)

# Email Configuration from Environment Variables
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECIPIENT = os.getenv("EMAIL_RECIPIENT")

# Validate that email credentials are set
if not EMAIL_SENDER or not EMAIL_PASSWORD or not EMAIL_RECIPIENT:
    raise ValueError("❌ Missing email configuration. Check config/webhook_env")

@app.route('/')
def home():
    return "✅ Webhook Listener is Running!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("📩 Received Webhook Data:", data)

    # Extract relevant details from the webhook payload
    if 'pusher' in data and 'repository' in data and 'head_commit' in data:
        sender = data['pusher']['name']
        repo = data['repository']['name']
        commit_message = data['head_commit']['message']
        commit_url = data['head_commit']['url']

        subject = f"🔔 New Commit in {repo} by {sender}"
        body = f"""
        A new commit was pushed to **{repo}** by **{sender}**.

        📌 **Commit Message:**
        ```
        {commit_message}
        ```

        🔗 [View Commit]({commit_url})
        """

        # Send email notification
        send_email(subject, body)

    return jsonify({"message": "Webhook processed"}), 200

def send_email(subject, body):
    """Function to send email using yagmail"""
    try:
        yag = yagmail.SMTP(EMAIL_SENDER, EMAIL_PASSWORD)
        yag.send(EMAIL_RECIPIENT, subject, body)
        print("✅ Email sent successfully")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

