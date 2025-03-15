# 🌍 Setting Up GitHub Webhook

## 1️⃣ Get Your ngrok Public URL
Run:
```sh
ngrok http 5000
```
Copy the **ngrok public URL**, e.g.:
```
https://xyz-1234.ngrok-free.app
```

## 2️⃣ Configure GitHub Webhook
1. Go to **GitHub Repository** → **Settings** → **Webhooks**.
2. Click **"Add Webhook"**.
3. **Set the Payload URL**:
   ```
   https://your-ngrok-url/webhook
   ```
4. **Choose `application/json`** as the content type.
5. **Select "Just the push event"**.
6. Click **Save**.

## 3️⃣ Test the Webhook
Push a commit:
```sh
git commit --allow-empty -m "Testing webhook"
git push origin main
```
✅ If successful, the webhook listener should **receive the event** and **send an email**.
```

