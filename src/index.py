import discord
from discord.ext import commands
import time
import threading
import asyncio
import random


bot = commands.Bot(command_prefix='>')
server_list = bot.guilds
phrases_alone = ("{0} está solo solin solito en {1}, esperando a que alguien le de pa' sus chicles",
                 "{0} anda en busca de alguien que le saque la leche, te espera en {1}",
                 "{0} no tiene amigos, lleva un rato solo en {1}",
                 "El {0} quiere a alguien que lo carree en el LOL")
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(server_list)

@bot.event
async def on_connect():
    server_list = bot.guilds
    print(server_list)

@bot.listen()
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    if 'ora' in message.content.lower():
            await message.channel.send('ORA! ORA! ORA!')

    if 'lol' in message.content.lower():
        if message.author.name == 'DigitalRexx':
            await message.channel.send('No vas a llegar a platino :jeje:')
        elif message.author.name == '迪戈加西亞':
            await message.channel.send('Nunu: Campeón de pocos ambiciosos :diego3:')
        elif message.author.name == 'DigitalMorsa':
            await message.channel.send('MA-LO')
        elif message.author.name == 'DigitalScorp1on':
            await message.channel.send('Best Kaisa Ever!')

@bot.listen()
async def on_voice_state_update(member, before, after):
    voice = after.channel
    try:
        print("{0} has join to {1}".format(member.name, voice.name))
        server = bot.get_guild(738893689660637286)
        await asyncio.sleep(5)
        if len(voice.members) == 1:
            await server.text_channels[0].send(random.choice(phrases_alone).format(member.nick, voice.name))

    except(AttributeError):
        print('Users disconnected from the channel')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)



bot.run('NzM4ODg4OTk1NjQzMDY0NDM5.XySeAA.NA5HTgkrpFL_MS_s2SL6nUAFpYU')