from datetime import datetime
from random import randint
from string import printable

from aiogram import Bot, Dispatcher, executor, types

from database_class import Database
from encryption import EncryptionManager
from wordlist import wordlist

printable = printable[0:-9]
printable.replace(" ", '')

MIN = 0
MAX = len(printable) - 1
API_TOKEN = 'BOT_API_KEY'


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db = Database()


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    check = db.insert_user(message["from"]["id"], message["from"]["first_name"])
    start_message = f"""
Hello {message["from"]["username"]} 😀,
This bot will help you generate really 🔐 SECURE passwords and passphrases of lengths between 4 to 256 and 4 to 100 respectively.

/help command to see list of commands
"""

    await message.reply(start_message)


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):

    db.insert_user(message["from"]["id"], message["from"]["first_name"])

    help_message = """
/start : to see the welcome message.
/gen : to generate a 32 chatacter length password.
/gen num : to generate a num character length password.

example:

/gen 8
/gen 10
/gen 16
/gen 64

🔑 passwords generated using /gen command are very strong 💪 but are not easy to remember. You should have some amount of guts to remember such passwords.

it's better if you use a pass phrase if you want to remember. A pass phrase is a kind of password which is a combination of several `n` different words like as shown bellow.

pass-phrase: absentee afternoon plus repackage long

/phrase : to generate 8 words length pass-phrase
/phrase num : to generate a pass phrase with num words

example: 

/phrase 4
/phrase 8
/phrase 12
/phrase 20

SMALL FEATURES:

----------------------
/save: to save any notes or passwords

note: all the saved notes are encrypted and no one without a valid decryption key can read the notes. keys are unique to each user. read more about it on my github page. try /dev

example:

/save I need to meet a friend @12:30 pm today!
/save My amazon pass is AmAsOnPaSz
---------------------

/get: to retrive or get all saved notes

OTHER COMMANDS:

/stat: to see you statistics
/gstat: to see global statistics

/dev: to see info about this bot's developer
    """

    await message.reply(help_message)


@dp.message_handler(commands=['gen'])
async def gen(message: types.Message):

    length = message.text.replace("/gen", '').strip()

    try:
        if len(length) == 0:
            length = 16
        else:
            length = int(length)

        if 4 <= length <= 256:

            passwords = ""
            for _ in range(5):
                passwords += "\n\n" + (generate(length))

            db.increase_password_count(message["from"]["id"], 5)
            msg = f"""Your generated strong 🔐 passwords are:
{passwords[1:]}
                """
            await message.reply(msg)
        elif length <= 3:
                await message.reply("Too short... 🤏")
        elif length > 256:
                await message.reply("Too long... 🤥")
    except:
        await message.reply("Please send a number! 🔢")


@dp.message_handler(commands=['phrase'])
async def phrase(message: types.Message):

    length = message.text.replace('/phrase', '').strip().replace(" ", '')

    try:
        if len(length) == 0:
            length = 8
        
        try:

            if length != 8:
    
                length = int(length)
            if 4 <= length <= 100:

                phrases = ""

                for _ in range(5):
                    phrase = ""
                    for _ in range(length):

                        phrase += " " + wordlist[randint(0,len(wordlist)-1)]

                    phrases += "\n\n" + phrase
                msg = f"""Your generated pass phrases 👍 are:
{phrases[1:]}
                """
                db.increase_passphrase_count(message["from"]["id"], 5)
                await message.reply(msg)

            elif length <= 3:
                await message.reply("Too short... 🤏")

            elif length > 100:
                await message.reply("Too long... 🤥")
    
        except:
            await message.reply("Please provide a number! 🔢")
    
    except Exception as e:
        await message.reply("Please provide a valid command! 📔")


@dp.message_handler(commands=['stats', 'stat', 'statistics'])
async def user_stat(message):

    stats = db.user_stat(message["from"]["id"])
    passwords_generated = stats[0]
    passphrases_generated = stats[1]
    msg = f"You have generated {passwords_generated} strong 🔐 passwords and {passphrases_generated} easy to remember passphrases."
    
    del stats
    del passphrases_generated
    del passwords_generated

    await message.reply(msg)


@dp.message_handler(commands=['gstats', 'gstat', 'gstatistics'])
async def global_stat(message):

    stats = db.global_stat()
    passwords_generated = stats[0]
    passphrases_generated = stats[1]

    msg = f"Users have generated {passwords_generated} strong passwords 🔐 and {passphrases_generated} 🔐 easy to remember passphrases."
    
    del stats
    del passphrases_generated
    del passwords_generated
    
    await message.reply(msg)


@dp.message_handler(commands=['dev', 'developer', 'builder'])
async def dev(message):
    msg = f"""Hi! {message["from"]["first_name"]} 😀.
I am a @BeastImran. You can ping me if you want something from me!
you can see my projects at: https://github.com/BeastImran
    """
    await message.reply(msg)


@dp.message_handler(commands=['save'])
async def save_notes(message):
    msg = message["text"].replace('/save', '', 1).strip()
    if len(msg) > 0:
        msg = EncryptionManager(message["from"]["id"]).encrypt_data(msg)

        db.save_notes(message["from"]["id"], msg, datetime.now().strftime("%y-%m-%d %H:%M:%S"))
        await message.reply("Saved 👍")
    else:
        await message.reply("SEND SOMETHING TO SAVE! 😕")


@dp.message_handler(commands=['get'])
async def get_saved_notes(message):
    
    data = db.get_notes(message["from"]["id"])

    if len(data) > 0:
        msg = '''Your saved notes 📖 are:'''
        enc = EncryptionManager(message["from"]["id"])
        for i in data:
            msg += "\n\n" + enc.decrypt_data(i[0])
        await message.reply(msg)
        del enc
    else:
        await message.reply("YOU HAVE NOT SAVED ANYTHING YET! 😕")


@dp.message_handler()
async def same_reply(message):
    db.insert_user(message["from"]["id"], message["from"]["first_name"])
    await message.reply(f"HEY {message['from']['username']}!\nDO YOU MIND SENDING SOMETHING MEANINGFUL! 😅")


def generate(length):
    password = ""
    for _ in range(length):
        password += printable[randint(MIN, MAX)]
    return password


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
