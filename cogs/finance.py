import discord
from discord.ext import commands

from utils import MongoController


class Finance(commands.Cog, name="finance"):
    def __init__(self, bot):
        self.bot = bot
        self.db = MongoController('config/database.json', 'exchange')

    @commands.command(name="환율")
    async def exchange(self, ctx):
        result = self.db.get_exchange()
        if result:
            text = "+" + ("-" * 25) + "+\n"
            text = text + "| %-10s | %-10s |\n" % ("Currency", "Value(₩)")
            text = text + "|" + ("-" * 25) + "|\n"
            for key in result['exchange'].keys():
                text = text + \
                    "| %-10s | %-10s |\n" % (key, result['exchange'][key])
            text = text + "+" + ("-" * 25) + "+\n"

            t = '```\n' + text + '```'
            await ctx.send(t)
        else:
            await ctx.send("환율조회 시스템 이상")


def setup(bot):
    bot.add_cog(Finance(bot))
