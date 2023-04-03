import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Updater,
    MessageHandler,
    Filters,
    CallbackContext,
    CommandHandler,
)

TOKEN = "YOUR_BOT_TOKEN"

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def add_buttons(update: Update, context: CallbackContext):
    if len(context.args) < 2 or len(context.args) % 2 != 0:
        update.message.reply_text(
            "Please provide an even number of arguments with button text and URL pairs separated by a space.\nUsage: /addbuttons <text1> <URL1> <text2> <URL2> ..."
        )
        return

    buttons_data = context.args

    keyboard = [[
        InlineKeyboardButton(buttons_data[i], url=buttons_data[i + 1])
        for i in range(0, len(buttons_data), 2)
    ]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    context.user_data["button_markup"] = reply_markup
    update.message.reply_text(
        "The buttons have been created. Now forward a message to add the buttons."
    )

def handle_forwarded(update: Update, context: CallbackContext):
    message = update.message
    if message.forward_from or message.forward_from_chat:
        if "button_markup" in context.user_data:
            reply_markup = context.user_data["button_markup"]

            if message.photo:
                context.bot.send_photo(
                    chat_id=message.chat_id,
                    photo=message.photo[-1].file_id,
                    caption=message.caption or None,  # add `or None` to handle cases where caption is None
                    reply_markup=reply_markup,
                )
            elif message.video:
                context.bot.send_video(
                    chat_id=message.chat_id,
                    video=message.video.file_id,
                    caption=message.caption or None,  # add `or None` to handle cases where caption is None
                    reply_markup=reply_markup,
                )
            else:
                context.bot.send_message(
                    chat_id=message.chat_id,
                    text=message.text,
                    reply_markup=reply_markup if message.caption else None,  # only add reply_markup if caption is present
                )
        else:
            update.message.reply_text(
                "Please create buttons first using the /addbuttons command."
            )
    else:
        update.message.reply_text("Please forward a message to add the buttons.")

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("addbuttons", add_buttons))
    dp.add_handler(MessageHandler(Filters.all & ~Filters.command, handle_forwarded))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
