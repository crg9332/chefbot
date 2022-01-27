import discord
import os
from discord.ext.commands import Bot as BotBase
from datetime import datetime
from lib.db import db
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from glob import glob

PREFIX = '-cb '
OWNER_IDS = [318066536180875274]
COGS = [path.split("/")[-1][:-3] for path in glob("./lib/cogs/*.py")]

class MyClient(BotBase):
  def __init__(self):
    self.PREFIX = PREFIX
    self.scheduler = AsyncIOScheduler()
    self.ready = False

    db.autosave(self.scheduler)
    super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)
  
  def setup(self):
    for cog in COGS:
      self.load_extension(f"lib.cogs.{cog}")
      print(f" {cog} cog loaded")
  
  def run(self):
    self.setup()

    self.token = os.environ['TOKEN']
    super().run(self.token, reconnect=True)

  async def on_ready(self):
    self.scheduler.start()
    
    # while not self.cogs_ready.allready():
    #   await sleep(0.5)
    
    self.ready = True
    print('We have logged in as {0.user}'.format(super()))

    embedMessage = discord.Embed(title="Now online!", description="Chef Bot is now online.", color=0x00ff00, timestamp=datetime.utcnow()) #timestamp=datetime.utcnow()
    embedMessage.set_author(name="Chef Bot", icon_url=super().user.avatar_url)
    #embedMessage.add_field(name="Field1", value="hi", inline=True)
    #embedMessage.set_footer(text="this is a footer")
    channel = super().get_channel(916203756851429416)
    await channel.send(embed=embedMessage)

  # async def on_message(self, message):
  #   if message.author == super().user:
  #     return
    
  #   if message.content.startswith(self.PREFIX):
  #     messagedata = message.content
  #     words = messagedata.split()
  #     words.pop(0)
  #     result = commands.process_command(words, message)
      
  #     await message.channel.send(result)

client = MyClient()
client.run()
