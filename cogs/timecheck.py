import discord
from discord.ext import commands

import time
from pytz import timezone
from datetime import datetime


class TimeCheck(commands.Cog, name="timecheck"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="시간확인")
    async def check_time(self, ctx):
        tz_list = [
            'America/New_York',
            'Europe/London',
            'Europe/Amsterdam',
            'Asia/Seoul'
        ]
        t = "```\n"
        for tz in tz_list:
            now = datetime.now(timezone(tz))
            t = t + "%-20s ==> %s\n" % (tz, now.strftime('%Y/%m/%d %H:%M'))
        t = t + "```"
        await ctx.send(t)


def setup(bot):
    bot.add_cog(TimeCheck(bot))
