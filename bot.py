import os
import subprocess
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Use hardcoded token for now (recommend env variable for production)
TOKEN = "7434729169:AAET2qNJNLTzl5OdXjlbzWgS7QTQ1mCL-xI"

def start(update, context):
    update.message.reply_text("👋 Send me a phone number (e.g. +919876543210) and I’ll run Maigret for you.")

def handle_message(update, context):
    phone_number = update.message.text.strip()
    
    if not phone_number.startswith('+'):
        update.message.reply_text("⚠️ Please send phone number in international format (e.g. +91xxxxxx).")
        return

    update.message.reply_text("🔍 Running Maigret... Please wait ⏳")

    try:
        output_file = f"maigret_report.json"
        command = f"maigret {phone_number} --json {output_file}"
        subprocess.run(command, shell=True, timeout=180)

        with open(output_file, 'rb') as f:
            context.bot.send_document(chat_id=update.effective_chat.id, document=f)

        os.remove(output_file)

    except Exception as e:
        update.message.reply_text(f"❌ Error: {str(e)}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
