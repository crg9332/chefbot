from discord.ext.commands import Cog
from discord.ext.commands import command

class Fun(Cog):
  def __init__(self, bot):
    self.bot = bot
  
  # @Cog.listener()
  # async def on_ready(self):
  #   if not self.bot.ready:
  #     self.bot.cogs_ready.ready_up("help")

  # @Cog.listener()
  # async def on_message(self, message):
  #   print("Message detected within Fun")

  @command(name="Hello", aliases=["hi", "hey"], hidden=True)
  async def hello(self, ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

def setup(bot):
    bot.add_cog(Fun(bot))