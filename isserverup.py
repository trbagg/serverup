import os
import time
import discord
from dotenv import load_dotenv
from discord import app_commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = int(os.getenv('DISCORD_GUILD')) # 1361461683649904650
ADDRESS = os.getenv('ADDRESS')

class MyClient(discord.Client):
    user: discord.ClientUser

    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=discord.Object(id=GUILD))
        await self.tree.sync(guild=discord.Object(id=GUILD)) 

intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

@client.tree.command()
async def status(interaction: discord.Interaction):
    """Is the server up?"""
    url = f"https://api.mcstatus.io/v2/widget/java/{ADDRESS}?t={int(time.time())}"
    embed = discord.Embed(title=f"Server Status")
    embed.set_image(url=None)
    embed.set_image(url=url)
    await interaction.response.send_message(embed=embed)

@client.tree.command()
async def request(interaction: discord.Interaction):
    """Why isn't the server up?"""
    await interaction.response.send_message(content="<@209065283317530624>\nhttps://klipy.com/gifs/megamind-17")

@client.tree.command()
async def thank(interaction: discord.Interaction):
    """Server is up."""
    await interaction.response.send_message(content="https://klipy.com/gifs/yippee-creature-funny-dance")

@client.tree.command()
async def code(interaction: discord.Interaction):
    """Print bot code"""
    code = open("isserverup.py")
    await interaction.response.send_message(content=code.read())
    code.close()


intents.presences = False
client.run(TOKEN)