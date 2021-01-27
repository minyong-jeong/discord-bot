import discord
from discord.ext import commands

import time
from pytz import timezone
from datetime import datetime


class TimeCheck(commands.Cog, name="timecheck"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="네덜란드시간")
    async def netherland_time(self, ctx):
        now = datetime.now(timezone('Europe/Amsterdam'))
        t = now.strftime('%H시 %M분')
        await ctx.send(t)

    @commands.command(name="한국시간")
    async def korea_time(self, ctx):
        now = datetime.now(timezone('Asia/Seoul'))
        t = now.strftime('%H시 %M분')
        await ctx.send(t)


def setup(bot):
    bot.add_cog(TimeCheck(bot))
