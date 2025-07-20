# 🔔 Telegram Bot Notifier for Long-Running Code

Tired of waiting around for your code to finish running? Get a Telegram notification when it’s done — straight to your phone, no refreshing required.

This simple Python script uses the **Telegram Bot API** to notify you once your long-running task or notebook cell finishes execution.

---

## 🚀 Quick Setup

### 1. Create Your Telegram Bot

No coding needed — just follow these easy steps inside the Telegram app:

1. **Open Telegram** and search for **[@BotFather](https://t.me/BotFather)**.
2. Send `/newbot` and follow the prompts to:
   - Choose a name and username (e.g. `MyNotifyBot`)
   - Get your **API Token** (you’ll need this later)
3. Save your token somewhere safe!

> 💡 Tip: You can get help anytime by sending `/help` to BotFather.

---

### 2. Get Your Chat ID

1. Search for **[@userinfobot](https://t.me/userinfobot)** in Telegram.
2. Send it any message — it will reply with your **User ID** (aka Chat ID).

---

### 3. Plug It into Your Code

Add the code snippet to the end of your Python script or notebook
