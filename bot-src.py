import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()
import os

class MainClient(discord.Client):
	
# Command prefix (DOESN'T WORK - MUST BE FIXED)
#	bot = commands.Bot(command_prefix='>')
	
# Bot's name and ID, can be viewed in a command line interface
	async def on_ready(self):
		print("")
		print("Logged in as:")
		print(self.user.name)
		print(self.user.id)
		print("------")


# Various messages
	async def on_message(self, message):
		
		if message.author.id == self.user.id:
			return
		
# Hello Lain 1 - English	
		if message.content.find("Hello Lain") != -1:
			await message.channel.send("Hello {0.author.mention}!".format(message))
		
# Hello Lain 2 - English
		if message.content.find("Hi Lain") != -1:
			await message.channel.send("https://raw.githubusercontent.com/getimiskon/lainbot/master/assets/lain-wave.png")			
		
# Hello Lain 3 - Japanese
		if message.content.find("こんにちは玲音") != -1:
			await message.channel.send("こんにちは{0.author.mention}さん！".format(message))

# Ping command - useful for troubleshooting purposes			
		if message.content.find("Ping") != -1:
			await message.channel.send("Pong!")
		
# Various references to Serial Experiments Lain	
		if message.content.find("play track 44") != -1:
			await message.channel.send("https://www.youtube.com/watch?v=w_wx2jag7xI")
			
		if message.content.find("What is memory?") != -1:
			await message.channel.send("A memory is only a record. You just have to rewrite that record.")
						
		if message.content.find("Present day!") != -1:
			await message.channel.send("Present time!")
			await message.channel.send("HAHAHAHAHAHA!")
		
		if message.content.find("プレゼント・デイ") != -1:
			await message.channel.send("プレゼント・タイム")
			await message.channel.send("はははははは！")
		
# "How are you?" question	
#		if message.content.find("How are you, Lain?") != -1:
#			await message.channel.send("I'm fine. How about you?")
		
# "I'm fine" reply - to be removed
#		if message.content.find("I'm fine") != -1:
#			await message.channel.send("That's good")
		
# Help command	
#		if message.content.find("Help me Lain") != -1:
#			await message.channel.send("For any help, contact @getimiskon#7962.")
		
# reference to "nobody here video" from YouTube	
		if message.content.find("anybody here") != -1:
			await message.channel.send("https://www.youtube.com/watch?v=-RFunvF0mDw")
			
# Swear words
#		if message.content.find("fuck") != -1:
#			await message.channel.send("Calm down, {0.author.mention}.".format(message))

# "Dead chat" reply
		if message.content.find("dead chat") != -1:
			await message.channel.send("https://discord.com/channels/270375970706423808/796889008524230698/808370338923544587")
			
		if message.content.find("dead chat xD") != -1:
			await message.channel.send("https://discord.com/channels/270375970706423808/796889008524230698/808370338923544587")

#Welcome message for new members (BROKEN - MUST BE FIXED)
#	async def on_member_join(self, member):
#		guild = member.guild
#		if guild.system_channel is not None:
#			to_send = "Welcome to the {0.name}, {1.mention}.".format(guild, member)
#			await guild.system_channel.send(to_send)
			
# Client-specific data
client = MainClient()
TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
