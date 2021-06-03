import discord
from discord.ext import commands
from pathlib import Path
from utils import get_discord_key
import logging
import logging.handlers

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.handlers.TimedRotatingFileHandler(
    'discord.log', "midnight", 1)
handler.suffix = "%Y%m%d"
handler.setFormatter(logging.Formatter(
    '[%(asctime)s][%(processName)-10s][%(levelname)s] - %(message)s'))
logger.addHandler(handler)

COMMAND_PREFIX = '!'
COGS = [
    "cogs.timecheck",
    "cogs.server",
    "cogs.finance"
]


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=self.prefix)
        self.loop.create_task(self.load_all_extensions())

    async def on_ready(self):
        logger.info(f'Logged in as name: {bot.user.name}, id: {bot.user.id}')

    async def on_connect(self):
        logger.info("Client has successfully connected to Discord.")

    async def on_disconnect(self):
        logger.info("Client has disconnected from Discord.")

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found.")
        logger.info(error)

    async def load_all_extensions(self):
        for extension in COGS:
            try:
                self.load_extension(extension)
                extension = extension.replace("cogs.", "")
                logger.info(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                extension = extension.replace("cogs.", "")
                logger.info(
                    f"Failed to load extension {extension}\n{exception}")

    async def prefix(self, bot, msg):
        return commands.when_mentioned_or(COMMAND_PREFIX)(bot, msg)


if __name__ == "__main__":
    bot = MyBot()
    bot.run(get_discord_key("config/discordkey.json"))
