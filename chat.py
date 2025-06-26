import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import openai

# Replace with your keys
TELEGRAM_TOKEN = '6436450622:AAEEBhg4dRpQlpbPNHtrth-545ch0tq0MFs'
OPENAI_API_KEY = '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'

openai.api_key = OPENAI_API_KEY

# Logging (for debugging)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Function to get response from ChatGPT
async def chat_with_gpt(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Or "gpt-4" if you have access
        messages=[
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message['content'].strip()

# Handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    gpt_reply = await chat_with_gpt(user_text)
    await update.message.reply_text(gpt_reply)

# Start bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I'm your AI chatbot. Ask me anything."_
