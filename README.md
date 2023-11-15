This Python script implements a Telegram bot that sends "romantic compliments" to specific users. The bot uses the _python-telegram-bot_ library to interact with the Telegram API.

# Features
/start: Command that welcomes the user to the bot.

/compliment: Command that sends random romantic compliments to specific users.

/id: Command that returns the user ID of the sender.

/whois: Command that returns the ID of another user by replying to their message or forwarding it.

# Configuration
Before running the bot, make sure to follow these steps:

### Get Telegram Token:
Get a token for your Telegram bot by following the instructions on BotFather.

Replace ‘YOUR_TELEGRAM_TOKEN’ with your bot’s token in the script.

### Define User List:
In the ‘user_list’ variable, add the real IDs of the users you want to send compliments to.

### Install Dependencies:
Install the dependencies ```pip install python-telegram-bot```

### Run the Script:
Run the script to start the bot.

```python3 CrazyLover.py```

# Compliments
The ‘random_compliment()’ function randomly chooses a compliment from the predefined list. You can customize the list according to your preferences. and send a pull request.
