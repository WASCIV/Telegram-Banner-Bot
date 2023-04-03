# Telegram Banner Bot

This Telegram Banner Bot is a simple, yet powerful tool that allows you to generate and display custom banners within your Telegram chats. This repository contains a Python script to help you get started quickly and easily.

[![GitHub license](https://img.shields.io/badge/LICENSE-MIT-orange)](https://github.com/WASCIV/Telegram-Banner-Bot/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/badge/StarME-Star-blue)](https://github.com/WASCIV/Telegram-Banner-Bot/stargazers)

## Table of Contents

1. [Creating a Telegram Bot](#creating-a-telegram-bot)
2. [Replacing the Bot Token](#replacing-the-bot-token)
3. [How to Use the Banner Bot](#how-to-use-the-banner-bot)
4. [Contributing](#contributing)
5. [License](#license)

## Creating a Telegram Bot

To create a Telegram bot, you will need to follow these steps:

1. Open the Telegram app and search for the "BotFather" bot.
2. Start a chat with the BotFather by clicking on the "Start" button.
3. Send the command `/newbot` to create a new bot.
4. Choose a name for your bot (e.g., "My Banner Bot").
5. Choose a unique username for your bot, ending with the word "bot" (e.g., "mybanner_bot").
6. After successfully creating your bot, BotFather will provide you with a bot token. Make sure to save this token, as you will need it later.

## Replacing the Bot Token

To replace the bot token with your own, follow these steps:

1. Open the Python script file named `telegram_banner_bot.py`.
2. Locate the line that says `YOUR_BOT_TOKEN = 'YOUR-BOT-TOKEN-HERE'`.
3. Replace the placeholder text `'YOUR-BOT-TOKEN-HERE'` with the bot token you received from the BotFather.
4. Save the changes to the file.

```python
# Replace this line in telegram_banner_bot.py
YOUR_BOT_TOKEN = 'YOUR-BOT-TOKEN-HERE'
# With your actual bot token
YOUR_BOT_TOKEN = '1234567890:ABCdefGhiJKlmnopQRStuVwxyz'
```

## How to Use the Banner Bot

1. Install the required Python libraries by running the following command:

```bash
pip install -r requirements.txt
```

2. Start the bot by running the following command:

```python
python Banner_bot.py
```

3. Add your bot to a Telegram group or start a chat with it.

4. Send commands and messages to your bot to generate and display custom banners.

For example:

    /addbuttons Hello, World!: Generates a banner with the text "Hello, World!".
	
	Usage: /addbuttons <text1> <URL1> <text2> <URL2> 
	
	Just Forward a message Ensure that it looks like this 
	
	
##	Screenshot 👇👇
	
![Screenshot 1](screenshot/screenshot.jpg)

/start: Displays nothing

## Contributing

We welcome contributions! If you would like to contribute, please feel free to create a pull request or open an issue.

## Follow me on Instagram

Don't forget to follow me on Instagram [@wasiqhatesinsta](https://www.instagram.com/wasiqhatesinsta/) for more projects and updates!


## Join Us On Telegram

Don't forget to follow me on Instagram [@forever_knightss](https://t.me/+iaTYOodcEuU3YjFl) for more projects and updates!


## License

This project is licensed under the [MIT License](https://github.com/WASCIV/Telegram-Banner-Bot/blob/main/LICENSE).

