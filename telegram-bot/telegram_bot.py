#!/usr/bin/env python

from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

from telegram_bot.config import BOT_TOKEN
from telegram_bot.utils import error_handler, help_command, echo_message


def main():
    """
    Python Telegram Bot
    Usage: Press Ctrl-C on the command line or send a signal to the process to stop the bot
    """

    # Create the Updater and pass it your bot token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    command_handler = {
        'help': help_command
    }
    for command, handler in command_handler.items():
        dp.add_handler(CommandHandler(command, handler, pass_job_queue=True))

    # on non-command i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo_message))

    # log all errors
    dp.add_error_handler(error_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
