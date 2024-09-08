import discord
from discord.ext import commands
from datetime import datetime
import os
from myserver import server_on

intents = discord.Intents.all()
intents.voice_states = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_voice_state_update(member, before, after):
    # Get the channel by ID
    channel = bot.get_channel(1282300370915299348)

    # Get the current time in formatted string
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # When member joins a voice channel
    if before.channel is None and after.channel is not None:
        embed = discord.Embed(
            title="📥 เข้าช่องเสียง",
            description=f"{member.name} ได้เข้าช่องเสียง **{after.channel.name}**",
            color=discord.Color.green(),
            timestamp=datetime.now()
        )
        embed.set_footer(text=f"เวลา: {current_time}")
        await channel.send(embed=embed)

    # When member leaves a voice channel
    elif before.channel is not None and after.channel is None:
        embed = discord.Embed(
            title="📤 ออกจากช่องเสียง",
            description=f"{member.name} ได้ออกจากช่องเสียง **{before.channel.name}**",
            color=discord.Color.red(),
            timestamp=datetime.now()
        )
        embed.set_footer(text=f"เวลา: {current_time}")
        await channel.send(embed=embed)


server_on()

bot.run(os.getenv('Token'))
