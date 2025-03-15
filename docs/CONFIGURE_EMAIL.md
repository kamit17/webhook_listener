# 📧 Email Configuration Guide

## 1️⃣ Install `yagmail` and `python-dotenv`
Run the following commands to install the required Python packages:

```sh
pip install yagmail
pip install python-dotenv
```

## 2️⃣ Set Up Gmail App Password (if using Gmail)
- Visit [Google App Passwords](https://myaccount.google.com/apppasswords).
- Generate an app password and **save it securely**.

## 3️⃣ Update the `config/webhook_env` File with Your Email Credentials
Open the configuration file:

```sh
nano config/webhook_env
```

Add the following lines:

```ini
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
EMAIL_RECIPIENT=recipient@example.com
```

🔹 **Note:** Replace `your_email@gmail.com`, `your_app_password`, and `recipient@example.com` with your actual credentials.

💡 **Tip:** Ensure your email provider allows third-party access or use an app password instead of your main password.

