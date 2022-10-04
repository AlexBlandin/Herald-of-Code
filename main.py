from pathlib import Path
from problem_handler import Problem, parse_problem_from_file

import logging
import asyncio

import pytomlpp as toml
import pendulum
import discord
import interactions

setup = toml.load(Path("setup.toml"))
assert ("servers" in setup)
assert (len(setup.servers) == 1)
assert (isinstance(setup.servers[0], int))
assert ("token" in setup)
assert (isinstance(setup.token, str))

logging.basicConfig(
  filename = "main.log",
  format = "{asctime} {name} {levelname}: {message}",
  style = "{",
  level = logging.DEBUG,
  encoding = "utf8"
)
logger = logging.getLogger("main")

bot = discord.Bot()

@bot.event
async def on_ready():
  logging.info(f"We have logged in as {bot.user}")
  await bot.change_presence(activity = discord.Game(name = "Heralding the Code!"))

@bot.slash_command(guild_only = True, guild_ids = setup.servers)
async def hello(ctx: discord.ApplicationContext):
  await ctx.respond("Hello!")

# I don't know if you want snake_case or camelCase
# (or indeed if it even affects the command)

@bot.slash_command(guild_only = True, guild_ids = setup.servers)
async def list_problems(ctx = discord.ApplicationContext):
  """Returns a list of all promblems in ./problems"""
  pass

@bot.slash_command(guild_only = True, guild_ids = setup.servers)
@interactions.option() # I dunno ?
async def get_problem(problem_name: str, ctx = discord.ApplicationContext):
  """Returns an embed containing the name, content, and question, for a specified problem"""
  problem_object = parse_problem_from_file(f"{problem_name}.toml") # probably need an actual filter
  embed = discord.Embed(title = problem_object.name, description = problem_object.content)
  # colour = some orange for halloween?
  embed.set_footer(text = "Problem for dd/mm/yy ") # ?
  await ctx.send(embed = embed)

# This one probably needs to be obfuscated?
# To prevent other people seeing answers, I don't know..

@bot.slash_command(guild_only = True, guild_ids = setup.servers)
@interactions.option()
async def attempt_problem(problem: str, answer: str, ctx = interactions.CommandContext):
  """Allows a user to attempt a specific problem"""
  problem_object = parse_problem_from_file(f"{problem_name}.toml") # probably need an actual filter
  embed = discord.Embed(title = problem_object.name, description = problem_object.content)
  # colour = some orange for halloween?
  result = answer == problem_object.answer # but better
  embed.add_field(text = f"Your answer is {'correct!' if result else 'wrong :('}") # but also better
  embed.set_footer(text = "Problem for dd/mm/yy ") # ?
  # Then save something to a database I guess?
  pass

# Also the above should probably lie in their own file, problem_handler.py or something?

if __name__ == "__main__":
  bot.run(setup.token)
