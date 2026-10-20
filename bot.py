import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command()
async def play(ctx, url):
    # Play music logic
    pass

@bot.command()
async def pause(ctx):
    # Pause music logic
    pass

@bot.command()
async def resume(ctx):
    # Resume music logic
    pass

@bot.command()
async def stop(ctx):
    # Stop music logic
    pass

bot.run(TOKEN)