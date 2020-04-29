import discord

class MyClient(discord.Client):

    async def on_ready(self):

        print("")
        print("Logged in as:")
        print(self.user.name)
        print(self.user.id)
        print("------")

    async def on_message(self, message):

        if message.author.id == self.user.id:
            return

        if message.content.find("Hello Lain") != -1:
            await message.channel.send("Hello {0.author.mention}!".format(message))

        elif message.content.find("こんにちは玲音") != -1:
            await message.channel.send("こんにちは{0.author.mention}さん！".format(message))

        elif message.content.find("play track 44") != -1:
            await message.channel.send("https://www.youtube.com/watch?v=w_wx2jag7xI")

        elif message.content.find("What is memory?") != -1:
            await message.channel.send("A memory is only a record. You just have to rewrite that record.")

        elif message.content.find("Hi Lain") != -1:
            await message.channel.send("https://media.discordapp.net/attachments/661242158745124864/691612106553819176/D_cnjqiUEAE9MLS.png?width=331&height=287")
        
        elif message.content.find("Present day!") != -1:
            await message.channel.send("Present time!")
            await message.channel.send("HAHAHAHAHAHA!")

        elif message.content.find("プレゼント・デイ") != -1:
            await message.channel.send("プレゼント・タイム")
            await message.channel.send("はははははは！")

        elif message.content.find("How are you, Lain?") != -1:
            await message.channel.send("I'm fine. How about you?")

        elif message.content.find("I'm fine.") != -1:
            await message.channel.send("That's good")


    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = "Welcome to the {0.name}, {1.mention}.".format(guild, member)
            await guild.system_channel.send(to_send)

client = MyClient()
client.run("")
