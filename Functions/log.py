from Functions import custom_json, other
import discord
from discord.utils import get


async def message(msg, clock):
    ch = msg.channel
    cont = msg.content
    auth = msg.author
    logchid = custom_json.read_key('ids.json', 'logch')
    logch = other.catch_channel(msg, logchid)

    logmsg = '{0} hat die Naricht "{1}" in {2} geschrieben.'.format(auth, cont, ch)
    print('')
    print(clock)
    print(logmsg)

    log = discord.Embed(description=clock, color=0x0000a0)
    log.set_author(name='Gamezone Bot Logsystem', icon_url='https://cdn.discordapp.com/attachments/604348596661387303/812661884892872704/istockphoto-1167414558-170667a.jpg')
    log.add_field(name='Aktion:', value='Nachricht')
    log.add_field(name='Member:', value=auth, inline=True)
    log.add_field(name='Channel:', value=ch, inline=True)
    log.add_field(name='Inhalt:', value=cont, inline=True)
    log.set_footer(text='Gamezone Bot by Lukeplays#1187')
    try:
        await logch.send(embed=log)
    except discord.errors.HTTPException:
        try:
            await logch.send(clock)
            await logch.send('Die Folgende geloggte Nachricht ist zu lang um in einem Embed dargestellt zu werden: {0}'.format(logmsg))
        except discord.errors.HTTPException:
            await logch.send('Die Folgende geloggte Nachricht ist zu lang um in einer Discord Nachricht dargestellt zu werden. {0} hat folgende Nachricht in {1} geschrieben:'.format(auth, ch.name))
            await logch.send(cont)


async def chleave(member, channel_before, clock):
    logchid = custom_json.read_key('ids.json', 'logch')
    logch = get(member.guild.channels, id=logchid)

    logmsg = '{0} hat den Kanal "{1}" verlassen.'.format(member, channel_before)
    print('')
    print(clock)
    print(logmsg)

    log = discord.Embed(description=clock, color=0x0000a0)
    log.set_author(name='Gamezone Bot Logsystem', icon_url='https://cdn.discordapp.com/attachments/604348596661387303/812661884892872704/istockphoto-1167414558-170667a.jpg')
    log.add_field(name='Aktion:', value='Channel-Leave')
    log.add_field(name='Channel:', value=channel_before, inline=True)
    log.add_field(name='Member:', value=member)
    log.set_footer(text='Gamezone Bot by Lukeplays#1187')
    await logch.send(embed=log)


async def chjoin(member, channel, clock):
    logchid = custom_json.read_key('ids.json', 'logch')
    logch = get(member.guild.channels, id=logchid)

    logmsg = '{0} ist dem Kanal "{1}" beigetreten.'.format(member, channel)
    print('')
    print(clock)
    print(logmsg)

    log = discord.Embed(description=clock, color=0x0000a0)
    log.set_author(name='Gamezone Bot Logsystem', icon_url='https://cdn.discordapp.com/attachments/604348596661387303/812661884892872704/istockphoto-1167414558-170667a.jpg')
    log.add_field(name='Aktion:', value='Channel-Join')
    log.add_field(name='Channel:', value=channel, inline=True)
    log.add_field(name='Member:', value=member)
    log.set_footer(text='Gamezone Bot by Lukeplays#1187')
    await logch.send(embed=log)


async def chmove(member, channel_before, channel, clock):
    logchid = custom_json.read_key('ids.json', 'logch')
    logch = get(member.guild.channels, id=logchid)

    logmsg = '{0} hat vom Kanal "{1}" zum Kanal "{2}" gewechselt.'.format(member, channel_before, channel)
    print('')
    print(clock)
    print(logmsg)

    log = discord.Embed(description=clock, color=0x0000a0)
    log.set_author(name='Gamezone Bot Logsystem', icon_url='https://cdn.discordapp.com/attachments/604348596661387303/812661884892872704/istockphoto-1167414558-170667a.jpg')
    log.add_field(name='Aktion:', value='Channel-Move')
    log.add_field(name='Channel(vorher):', value=channel_before, inline=True)
    log.add_field(name='Channel(nachher):', value=channel, inline=True)
    log.add_field(name='Member:', value=member)
    log.set_footer(text='Gamezone Bot by Lukeplays#1187')
    await logch.send(embed=log)
