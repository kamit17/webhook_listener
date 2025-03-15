```md
# 🛠 Troubleshooting Guide

### ❌ Webhook Listener Not Running?
Check logs:
```sh
sudo systemctl status webhook
journalctl -u webhook --no-pager --lines=20
```
If not running, restart:
```sh
sudo systemctl restart webhook
```

---

### ❌ ngrok Not Starting?
Check if ngrok is installed:
```sh
which ngrok
```
Check logs:
```sh
sudo systemctl status ngrok
journalctl -u ngrok --no-pager --lines=20
```
If ngrok isn't authenticated, re-run:
```sh
ngrok config add-authtoken YOUR_NGROK_AUTH_TOKEN
```

---

### ❌ Webhook Request Not Received?
1. **Check GitHub Webhook Delivery Logs** (GitHub → Settings → Webhooks).
2. Ensure the ngrok URL is correct:
   ```sh
   curl http://127.0.0.1:4040/api/tunnels
   ```
3. Restart webhook listener:
   ```sh
   sudo systemctl restart webhook
   ```

✅ **If you still face issues, check `logs/webhook.log` for errors!**
```
