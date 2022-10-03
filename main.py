from pathlib import Path
import logging
import asyncio

import pytomlpp as toml
import pendulum
import discord

logging.basicConfig(
  filename = "main.log",
  format = "{asctime} {name} {levelname}: {message}",
  style = "{",
  level = logging.DEBUG,
  encoding = "utf8"
)
logger = logging.getLogger("main")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

@client.event
async def on_ready():
  logging.info(f"We have logged in as {client.user}")
  # await client.change_presence(activity = discord.CustomActivity("Blah"))
  await client.change_presence(activity = discord.Game(name = "Selecting a quote!"))

if __name__ == "__main__":
  client.run(Path("token.txt").read_text())
