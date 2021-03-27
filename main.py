import conf 
import discord

client = discord.Client()

@client.event
async def on_message(message):

    # <Message id=825338578766266389 channel=<TextChannel id=822806350886207542 name='флудильня' position=0 nsfw=False news=False category_id=822806350886207539> type=<MessageType.default: 0> 
    # author=<Member id=353837163529502720 name='hbjuo' discriminator='6923' bot=False nick='Сергей Жуков' guild=<Guild id=822806350886207538 name='Bots' shard_id=None chunked=False 
    # member_count=29>>
    #  flags=<MessageFlags value=0>>
    if message.author == client.user:
        return
    
    if message.author.bot:
        return

    if message.channel.id == 825309259578474496 or message.channel.id == 749622584659935285:
        msg = None
        

    if message.content == "!hello":
        msg = f'Hello, {message.author.name}, i am {client.user.name}'
    
    if message.content == "!abme":
        if message.author.nick != None:
        msg = f'Ты {message.author.name}, так же известный, как {message.author.nick}'
        else:
        msg = f'Ты {message.author.name}'



    if msg != None:
        await message.channel.send(msg)


client.run(conf.bot_token)



