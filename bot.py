# Loading Environment File
from dotenv import load_dotenv
load_dotenv()

# Importing Packages
import os
import disnake
from disnake.ext import commands
import tabulate

# Main Variables
TOKEN = os.getenv('BOT_TOKEN')
PREFIX = "_"

bot = commands.Bot(command_prefix=PREFIX, intents=disnake.Intents.all(), case_insensitive=True, help_command=None)

# Notify When The Bot Is Ready & Loading Cogs

@bot.event
async def on_ready():
    for cog in os.listdir(r"cogs"):
        if cog.endswith(".py"):
            try:
                cog = f"cogs.{cog.replace('.py', '')}"
                bot.load_extension(cog)
                print(tabulate([[cog, "Loaded"]], tablefmt='orgtbl'))
            except Exception as e:
                print(tabulate([[cog, e]], tablefmt='orgtbl'))

        print(tabulate([['Username', bot.user], ['ID', bot.user.id]], headers=["Loggeed", "In!"], tablefmt='orgtbl'))

bot.run(TOKEN)