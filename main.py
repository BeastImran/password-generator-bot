from random import randint
from string import printable
from aiogram import Bot, Dispatcher, executor, types


printable = printable[0:-9]
printable.replace(" ", '')

MIN = 0
MAX = len(printable) - 1


API_TOKEN = 'YOUR_BOT_API'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """

    start_message = """
This bot will help you generate really secure password of any length

send /help command to see list of commands
"""

    await message.reply(start_message)


@dp.message_handler(commands=['help'])
async def echo(message: types.Message):

    help_message = """
/start : to see the welcome message.
/gen : to generate a 32 chatacter length password.
/gen num : to generate a num character length password.

example:

/gen 8
/gen 10
/gen 16
/gen 64

passwords generated using /gen command are very strong but are not easy to remember. You should have some amount of guts to remember such passwords.

it's better if you use a pass phrase if you want to remember. A pass phrase is a kind of password which is a combination of several `n` different words like as shown bellow.

pass-phrase: absentee afternoon plus repackage long

/phrase : to generate 8 words length pass-phrase
/phrase num : to generate a pass phrase with num words

example: 

/phrase 4
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
                    phrases += "\n\n" + '`' + phrase + '`'
                await message.reply(phrases)
    
            elif length <= 3:
                await message.reply("Too short...")

            elif length > 100:
                await message.reply("Too long...")
    
        except:
            await message.reply("Please provide a number!")
    
    except Exception as e:
        await message.reply("Please provide a valid command!")


@dp.message_handler()
async def same_reply(message):
    await message.reply(message)


def generate(length):
    password = ""

    for _ in range(length):
        password += printable[randint(MIN, MAX)]
    
    return '`' + password + '`'


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
