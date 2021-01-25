from random import randint
from string import printable
from aiogram import Bot, Dispatcher, executor, types


printable = printable[0:-9]
printable.replace(" ", '')

MIN = 0
MAX = len(printable) - 1


API_TOKEN = 'BOT_APT_KEY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    start_message = """
This bot will help you generate really secure password of anylength

send /help command to see list of commands
"""

    await message.reply(start_message)


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):

    help_message = """
/start : to see the welcome message.
/gen : to generate a 32 chatacter length password.
/gen num : to generate a num character length password.

example: /gen 8
         /gen 10
         /gen 16
         /gen 64

passwords generated using /gen command are very strong but are not
easy to remember. You should have guts to remember such 
passwords.

it's better if you use a pass phrase if you want to remember.
A pass phrase is a password which is made of several different words
like as shown bellow.

passphrase: absentee afternoon plus repackagelong
/phrase num : to generate a pass phrase with num words

example: /phrase 4
         /phrase 8
         /phrase 12
         /phrase 20
    """

    await message.reply(help_message)


@dp.message_handler(commands=['gen'])
async def inp(message: types.Message):
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

            await message.reply(passwords)

        else:
            await message.reply("Send a number between 4 and 256")

    except:
        await message.reply("Please send a number!")


@dp.message_handler(commands=['phrase'])
async def phrase(message: types.Message):
    from wordlist import wordlist

    length = message.text.replace('/phrase', '').strip()
    try:
        if len(length) == 0:
            length = 8
        else:
            try:
                length = int(length.strip())
                if 4 <= length <= 100:
                    phrases = ""
                    for _ in range(5):
                        phrase = ""
                        for _ in range(length):
                            phrase += " " + wordlist[randint(0,len(wordlist)-1)]
                        phrases += "\n\n" + phrase
                    await message.reply(phrases)
        
                elif length <= 3:
                    await message.reply("Too short...")

                elif length > 100:
                    await message.reply("Too long...")
            except:
                await message.reply("Please provide a number!")
        
    except Exception as e:
        await message.reply("Please provide a valid command!")


def generate(length):
    password = ""

    for _ in range(length):
        password += printable[randint(MIN, MAX)]
    
    return password


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
