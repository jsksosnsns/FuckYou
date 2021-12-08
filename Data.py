from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hello {}

welcome {}

If you don't trust this bot,
 1) don't read this message
 2) block bot or delete chat

This Bot Works To Help You Get Session String Via Bot.  Recommendations If You Want To Take String Use Another Account, So As Not To Delay. Thank you
 By @DEXDECRYPT_MUSIC
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ Maintaned By ✨", url="https://t.me/NIKHILOWNER")],
        [
            InlineKeyboardButton("How to Use Me ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Info Bot Other ♥", url="https://t.me/DEXDECRYPT_MUSIC")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/about - About this Bot
/help - This Message
/start - Start Bot
/generate - Start Generating Session
/cancel - Cancels process
/restart - Abort the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to retrieve pyrograms and telethon string sessions by @DEXDECRYPT_MUSIC_STRING_BOT

Group Support : [Gabung](https://t.me/DEXDECRYPT_MUSIC)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @NIKHILOWNER
    """
