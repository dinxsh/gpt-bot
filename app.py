import openai
import discord
from dotenv import load_dotenv
import os
import nextcord
from nextcord.ext import commands
TESTING_GUILD_ID = 1059369565068476478  # Replace with your guild ID
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')
openai.api_key = OPENAI_KEY
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def ask(ctx, *, prompt):
    response = openai.Completion.create(engine="text-davinci-002",prompt=f"{prompt}",max_tokens=2048,temperature=0.5)
    await ctx.reply(content=str(response.choices[0].text)[:1999])
    
bot.run(TOKEN)