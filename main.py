import discord

# Please create a token file if it does not exist
token_file = open('token', 'r')

TOKEN = token_file.read()

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)

# Add bot.load_extension(path) for whatever cog you want to use.
bot.load_extension('cogs.fjf')
bot.load_extension('cogs.fun')


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} successfully!")


bot.run(TOKEN)
