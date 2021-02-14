# PASSWORD GENERATOR TELEGRAM BOT

This bot will help you generate some **random, strong** *passwords* and *passphrases* as your requested length.

This mini-project was started by me as a fun project but it gained over [250+](https://t.me/BotsArchive/1786 "BotsArchive post link") users and [3.8 / 5](https://t.me/BotsArchive/1786 "BotsArchive post link") score in [BotsArchive channel](https://t.me/BotsArchive "BotsArchive channel"). So I am continuing to improve it furthur.
Please ping me in telegram [@BeastImran](https://t.me/BeastImran) if you want to use this code or files in your project in anyway or need to query something or you want to involve in this project in any manner.



## Prerequisite

You will need to have [python3](https://www.python.org/ "python official site") language and [aiogram](https://pypi.org/project/aiogram/ "pip site for aiogram") library or API installed.

You can install aiogram library using pip.
```bash
  pip install aiogram
```
## Installation and running

The installation is straight forward.

  1. Download and satisfy the [prerequisite](#prerequisite "prerequisite").
  
  2. Download this repository.
  
  3. Get a BOT API KEY from [BOT FATHER](https://t.me/botfather) in telegram.
  
  4. If you have a BOT API KEY you can replace text "BOT_API_KEY" with your valid key in [main.py](https://github.com/BeastImran/password-generator-bot/blob/main/main.py "main.py file") file.
  
  5. Open a terminal in the downloaded directory and type the following command.
  
  ```bash
    python main.py
  ```
  
  6. The bot should be up and running by now if everything is done right.

## How to use this bot in telegram

**Start a chat with this [bot](https://t.me/SimpleStrongPasswordGeneratorBot "bot telegram link")**

  `/start` : to see the welcome message.
  
  `/gen` : to generate a 32 chatacter length password.
  
  `/gen num` : to generate a num character length password.
  
  **example:**

  `/gen 8` `/gen 10` `/gen 16` `/gen 64`

  passwords generated using `/gen` command are very strong but are not easy to remember. You should have some amount of guts to remember such passwords.
  It's better if you use a pass phrase if you want to remember. A pass phrase is a kind of password which is a combination of several `n` different words like as shown bellow.
  
  pass-phrase: absentee afternoon plus repackage long
  
  `/phrase` : to generate 8 words length pass-phrase

  `/phrase num` : to generate a pass phrase with num words
  
  **example:**
  
  `/phrase 4` `/phrase 8` `/phrase 12` `/phrase 20`
    
  **OTHER COMMANDS:**
  
  `/stat`: to see your statistics
  
  `/gstat`: to see global statistics
  
  `/dev`: to see info about this bot's developer
