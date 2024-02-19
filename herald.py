"""
A Discord Bot for setting up your own https://adventofcode.com styled events!

Copyright 2022 Alex Blandin
"""

import logging
from pathlib import Path

import discord
import pytomlpp as toml

# this file is where we do the actual plumbing of Herald

setup = toml.load(Path("setup.toml"))

logging.basicConfig(
  filename="main.log", format="{asctime} {name} {levelname}: {message}", style="{", level=logging.DEBUG, encoding="utf8"
)
logger = logging.getLogger("herald")

bot = discord.Bot()


@bot.event
async def on_ready() -> None:  # noqa: D103
  logging.info(f"We have logged in as {bot.user}")  # noqa: G004
  await bot.change_presence(activity=discord.Game(name="Heralding the Code!"))


@bot.slash_command(guild_only=True, guild_ids=setup.servers)
async def hello(ctx: discord.ApplicationContext) -> None:  # noqa: D103
  await ctx.respond("Hello!")


if __name__ == "__main__":
  bot.run(setup.token)
