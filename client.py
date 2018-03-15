#Anything not working? Report it to Issues and I will help you
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio (remove if not installed)

client = discord.Client()
bot_prefix= "0"
Client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print ("Github https://github.com/JennyDiscord/Client-Discord-Bot/")
   
@client.event
async def on_message(message):
    if message.content == "0test":
        await client.send_message(message.channel, "You are getting real dirty")
    print ("Log: Someone ran 0test on +bot.user.id")
    if message.content == "0emojitest":
        await client.send_message(message.channel, ":middle_finger: :milk: :cookie:")
        print ("Bad-stuff")
    if message.content == "0Spam":
#Take the chances on this raid command and do not complain about the raid command raiding servers
        await client.send_message(message.channel, "Spam")
    if message.content == "0Spam":
        await client.send_message(message.channel, "Spam")
    if message.content == "0help":
        em = discord.Embed(title=':thumbsup: Thank you for using my Github code at https://github.com/JennyDiscord. Now, check your DMS!!!', color=0x00ff00)
        await client.send_message(message.channel, embed=em)
    if message.content == "0help":
        em = discord.Embed(title='Thank you 𝓐𝓻𝓵𝓲𝔁 for this part of the code (Help command)', description='These are the commands **you** can use with the github code you have used at https://github.com/JennyDiscord.', colour=0x00ff00)
        em.add_field(name="0help", value="Shows this command.")
        em.add_field(name="0test", value="A test for the bot.")
        em.add_field(name="0Spam", value="**Raids servers please use at your own risk**.")
        em.add_field(name="0emojitest", value="A test for the bot. It is the **emoji** test. Thank you for using the github code at https://github.com/JennyDiscord")
        await client.send_message(message.author, embed=em)

client.run("Icantbelivethatudownloadedthisinsteadoflookingatitandrewritingitokno")
