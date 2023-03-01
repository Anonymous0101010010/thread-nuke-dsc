import discord
import asyncio

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

async def create_thread(channel):
    await channel.create_thread(name='name', type=discord.ChannelType.public_thread)
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    while True:
        for guild in client.guilds:
            for channel in guild.text_channels:
                await create_thread(channel)
                await asyncio.sleep(1)

client.run('OTgwMDc5NDIyMTY4MjYwNjM5.GGXu_N.B9uqb-8RrNmL_s9bA8odHJdHCQg17QxHqVFUVM')



