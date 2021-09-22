#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import socket
import time

import logging

from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    # update.message.reply_text(update.message.text)
    UDP_IP = "169.254.1.116" # set it to destination IP.. RPi in this case
    UDP_PORT = 12345

    print("UDP target IP:", UDP_IP)
    print("UDP target port:", UDP_PORT)
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    sock.sendto(update.message.text.encode('utf_8'), (UDP_IP, UDP_PORT))


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("Bot-Token")
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()