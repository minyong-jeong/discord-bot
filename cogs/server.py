import discord
from discord.ext import commands

import time
from pytz import timezone
from datetime import datetime


class Server(commands.Cog, name="server"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx):
        latency = self.bot.latency
        await ctx.send(latency)


def setup(bot):
    bot.add_cog(Server(bot))
