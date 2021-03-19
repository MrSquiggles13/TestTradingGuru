# import discord
# import os
# import time

# discordClient = discord.Client()

# @discordClient.event
# async def on_ready():
#   print("Watsup Bitches!!!")

# @discordClient.event
# async def on_message(message):
#   if message.author == discordClient.user:
#     return
#   if message.content.startswith('$joke'):
#     await message.channel.send('Fuck off')
#   if message.content.startswith('$why'):
#     await message.channel.send('Cuz you a bitch')

#   if message.content.startswith('$data'):
#     await message.channel.send('')

# discordClient.run(os.getenv('DISCORD_TOKEN'))