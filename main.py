from config import Config
from pyrogram import Client as bot, idle
import asyncio
import logging

logging.basicConfig(
    level=logging.INFO,    
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
LOGGER = logging.getLogger(__name__)
LOGGER.info("Live log streaming to telegram.")

plugins = dict(root="plugins")

if __name__ == "__main__":
    bot = bot(
        "Bot",
        bot_token=Config.7565091501:AAEBHeV2F30qZ46Ol4bXN1JX0qQLZ5P1_uA,
        api_id=Config.28021723,
        api_hash=Config.f6b0736c56e8544e6d55b7c4ef169a68,
        sleep_threshold=120,
        plugins=plugins,
        workers=10,
    )
    async def main():
        await bot.start()
        bot_info = await bot.get_me()
        LOGGER.info(f"<--- @{bot_info.Txtuploader2_bot} Started --->")
        for user_id in Config.AUTH_USERS:6312174113
            try:
                await bot.send_message(chat_id=6312174113, text=f"__Congrats! You Are DRM member ... if You get any error then contact me -  {Config.CREDIT}__ ")
            except Exception as e:
                LOGGER.error(f"Failed to send message to user {6312174113}: {e}")
                continue
        await idle()
    asyncio.get_event_loop().run_until_complete(main())
    LOGGER.info("<--- Bot Stopped --->")
