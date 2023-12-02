from pathlib import Path
import logging

import pytomlpp as toml
import discord

# this file is where we do the actual plumbing of Herald

setup = toml.load(Path("setup.toml"))
assert "servers" in setup
assert len(setup.servers) == 1
assert isinstance(setup.servers[0], int)
assert "token" in setup
assert isinstance(setup.token, str)

logging.basicConfig(filename="main.log", format="{asctime} {name} {levelname}: {message}", style="{", level=logging.DEBUG, encoding="utf8")
logger = logging.getLogger("herald")

bot = discord.Bot()


@bot.event
async def on_ready():
  logging.info(f"We have logged in as {bot.user}")
  await bot.change_presence(activity=discord.Game(name="Heralding the Code!"))


@bot.slash_command(guild_only=True, guild_ids=setup.servers)
async def hello(ctx: discord.ApplicationContext):
  await ctx.respond("Hello!")


if __name__ == "__main__":
  bot.run(setup.token)
