from flask import Flask, request, jsonify
import yagmail

app = Flask(__name__)

# Email Configuration
EMAIL_SENDER = ""  # Change this to your email
EMAIL_PASSWORD = ""  # Use an App Password (Recommended)
EMAIL_RECIPIENT = ""  # Email that receives notifications

SMTP_SERVER = "smtp.gmail.com"  # Use "smtp.gmail.com" for Gmail
SMTP_PORT = 587  # Use 465 for SSL

@app.route('/')
def home():
    return "Webhook Listener is Running!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received Webhook Data:", data)

    if 'pusher' in data:
        sender = data['pusher']['name']
        repo = data['repository']['name']
        commit_message = data['head_commit']['message']

        subject = f"New Commit in {repo} by {sender}"
        body = f"""
        A new commit was pushed to {repo} by {sender}.

        Commit Message:
        "{commit_message}"

        View Commit: {data['head_commit']['url']}
        """

        # Send email notification
        send_email(subject, body)

    return jsonify({"message": "Webhook processed"}), 200

def send_email(subject, body):
    try:
        yag = yagmail.SMTP(EMAIL_SENDER, EMAIL_PASSWORD, host=SMTP_SERVER, port=SMTP_PORT, smtp_starttls=True, smtp_ssl=False)
        yag.send(EMAIL_RECIPIENT, subject, body)
        print("✅ Email sent successfully")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

