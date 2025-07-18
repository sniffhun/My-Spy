# MY SPY Telegram Bot

This Telegram bot lets you send a phone number and receive an OSINT report.

## 🚀 How to Deploy on Render

1. Fork or clone this repo.
2. Push to your own GitHub.
3. Go to https://render.com and create a new **Web Service**.
4. Connect your GitHub repo.
5. Set build and start commands:

**Build Command:**
```
pip install -r requirements.txt
```

**Start Command:**
```
./start.sh
```

## 🔐 Environment Variables (Recommended)

Instead of hardcoding, set this on Render:

```
Key: BOT_TOKEN
Value: your-telegram-bot-token
```

And modify `bot.py` like:
```python
TOKEN = os.getenv("BOT_TOKEN")
```

## 📝 Notes

- Only works with international format numbers (e.g. `+14155552671`).
- Make sure `maigret` is available on system path (Render handles this if installed via pip).
