```md
# 🛠 Installation Guide

## 1️⃣ Install Python Dependencies
Ensure you have **Python 3** installed, then run:
```sh
pip install -r requirements.txt
```

## 2️⃣ Install & Configure ngrok
- **Download and install ngrok**:
  ```sh
  wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-amd64.zip
  unzip ngrok-stable-linux-amd64.zip
  sudo mv ngrok /usr/local/bin/
  ```
- **Authenticate ngrok**:
  ```sh
  ngrok config add-authtoken YOUR_NGROK_AUTH_TOKEN
  ```

## 3️⃣ Clone the Project (If Not Done Already)

## 4️⃣ Verify Installation
Check if everything is installed:
```sh
python3 --version
ngrok --version
pip freeze | grep flask
```
✅ If you see **valid versions**, installation is successful!
```
