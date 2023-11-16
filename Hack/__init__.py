import env
import sys
from logger import LOGGER
import asyncio

from telethon import TelegramClient

loop = asyncio.get_event_loop()
botname = ""
botusername = ""

bot = TelegramClient('Hack', env.API_ID,
                     env.API_HASH).start(bot_token=env.BOT_TOKEN)


async def initiate_bot():
    global botname, botusername
    LOGGER(__name__).info('STARTING BOT⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️')
    try:
        await bot.start()
    except Exception as e:
        LOGGER(__name__).error(f'\033[31m{e}')
        sys.exit(0)
    getme = await bot.get_me()
    botusername = (getme.username).lower()
    if getme.last_name:
        botname = getme.first_name + " " + getme.last_name
    else:
        botname = getme.first_name
    if env.LOG_GROUP_ID:
        try:
            await bot.send_message(env.LOG_GROUP_ID, f'{botname} has started⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️')
        except Exception as e:
            LOGGER(__name__).error(
                f'\033[31mBot Is Unable To Send Message In Log Group Please Check⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️\n{e}'
            )
            sys.exit(0)
    LOGGER(__name__).info(f'BOT STARTED AS {botname}⚡️𝐒 𝐘 𝐍 𝐀 𝐗⚡️')

loop.run_until_complete(initiate_bot())
