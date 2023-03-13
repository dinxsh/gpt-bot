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

@bot.slash_command(name="ask-gpt", description="Ask gpt a prompt", guild_ids=[1059369565068476478])
async def askgpt(interaction: nextcord.Interaction, prompt:str):
    response = openai.Completion.create(engine="text-davinci-002",prompt=f"{prompt}",max_tokens=2048,temperature=0.5)
    await interaction.channel.send(response.choices[0].text)

@bot.slash_command(name="ask-a-tsundere", description="ask tsundere a prompt", guild_ids=[1059369565068476478])
async def asktsundere(interaction: nextcord.Interaction, prompt:str):
    await interaction.response.defer()
    response = openai.Completion.create(engine="text-davinci-002",prompt=f"refer to me as oni-chan, {prompt}",max_tokens=2048,temperature=0.5)
    await interaction.followup.send(content=str(response.choices[0].text)[:1999])

@bot.command()
async def ask(ctx, *, prompt):
    response = openai.Completion.create(engine="text-davinci-002",prompt=f"{prompt}",max_tokens=2048,temperature=0.5)
    await ctx.reply(content=str(response.choices[0].text)[:1999])
    
bot.run(TOKEN)