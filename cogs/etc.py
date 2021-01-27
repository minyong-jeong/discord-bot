import discord
from discord.ext import commands


class Etc(commands.Cog, name="etc"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="한강수온")
    async def temperature_of_hanriver(self, ctx):
        await ctx.send('https://hangang.life/')


def setup(bot):
    bot.add_cog(Etc(bot))
