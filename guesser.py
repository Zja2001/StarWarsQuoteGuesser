from discord.ext import commands
import discord
BOT_TOKEN = "MTIxOTg0Mjg4Mzk0MzkyNzg1OQ.GzleY4.STAwWc9zFdVdCNBiOEWWjn8zdaRYkbjZ6sCHr4"
Channel_ID = 1219845695918440571

Bot = commands.Bot(command_prefix="!", intents= discord.intents.all())


@Bot.Command()
async def characters():
    print("/n Qui Gon Gin /n Obi wan Kenobi /n Aniken Skywalker /n Padme /n Darth Maul ")

    bot.run(BOT_TOKEN)