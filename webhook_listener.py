from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Webhook Listener is Running!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Received Webhook Data:", data)
    return jsonify({"message": "Webhook received successfully"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

