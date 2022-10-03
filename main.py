from pathlib import Path
import asyncio

import pytomlpp as toml
import pendulum
import discord

# Variables and stuff
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents = intents)

if __name__ == "__main__":
  client.run(Path("token.txt").read_text())
