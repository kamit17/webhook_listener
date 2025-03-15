```md
# 🚀 Running Webhook & ngrok as Systemd Services

## 1️⃣ Set Up Environment Variables
Create `/etc/default/webhook_env`:
```sh
sudo nano /etc/default/webhook_env
```
Add:
```ini
PROJECT_PATH=<your_project_path>/webhook_listener
```

## 2️⃣ Configure systemd Services
Copy service files:
```sh
sudo cp services/webhook.service /etc/systemd/system/
sudo cp services/ngrok.service /etc/systemd/system/
```

## 3️⃣ Reload and Start Services
```sh
sudo systemctl daemon-reload
sudo systemctl enable webhook ngrok
sudo systemctl start webhook ngrok
```

## 4️⃣ Check Service Status
```sh
sudo systemctl status webhook
sudo systemctl status ngrok
```
✅ If both say **"active (running)"**, the setup is complete!
```
