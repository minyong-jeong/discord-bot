import discord
from discord.ext import commands
from pathlib import Path
from utils import get_discord_key

COMMAND_PREFIX = '!'
COGS = [
    "cogs.greetings",
    "cogs.timecheck",
    "cogs.server",
    "cogs.etc",
]


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=self.prefix)
        self.loop.create_task(self.load_all_extensions())

    async def on_ready(self):
        print('Logged in as')
        print(f'name: {bot.user.name}')
        print(f'id: {bot.user.id}')
        print('---------------')

    async def on_connect(self):
        print("Client has successfully connected to Discord.")
        print('---------------')

    async def on_disconnect(self):
        print("Client has disconnected from Discord.")
        print('---------------')

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Command not found.")
        raise error

    async def load_all_extensions(self):
        for extension in COGS:
            try:
                self.load_extension(extension)
                extension = extension.replace("cogs.", "")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                extension = extension.replace("cogs.", "")
                print(f"Failed to load extension {extension}\n{exception}")
        print('---------------')

    async def prefix(self, bot, msg):
        return commands.when_mentioned_or(COMMAND_PREFIX)(bot, msg)


if __name__ == "__main__":
    bot = MyBot()
    bot.run(get_discord_key())
