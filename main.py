import conf 
import discord

intense = discord.Intents.default()
intense.members = True
client = discord.Client(intents=intense)

cId = 825309259578474496

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

    if message.channel.id == cId:
        msg = None
        

        ctx = message.content.split(" ", maxsplit=1)
    
        #hello
        if message.content == "!hello":
            msg = f'Ку, {message.author.name}, я {client.user.name}'
        
        
    
        #about_me
        if message.content == "!abme":
            if message.author.nick != None:
                msg = f'Ты {message.author.name}, так же известный, как {message.author.nick}'
            else:
                msg = f'Ты {message.author.name}'
    
        #repeat
        if ctx[0] == "!repeat":
            msg  = ctx[1]
    
        #get_member 
        if ctx[0] == "!get_member":
            pass
    
        #get_members
        if message.content == "!get_members":
            msg = " "
            if message.author.guild.name == "Bots":
                for idx, member in list(enumerate(message.author.guild.members)):
                    msg += f'{idx+1}. {member.name} { f"[{member.nick}]" if member.nick else " "} - {member.id}\n'
                    
        #get_сhannels
    
    
        #goto {id/name}
            
    
    
    
    
    
    
    
    
    
    
        if msg != None:
            await message.channel.send(msg)


client.run(conf.bot_token)



