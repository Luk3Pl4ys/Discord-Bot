from Functions import other, custom_json
import discord
from discord.utils import get


async def callsup(message, prefix, modrole):
    if message.content.lower().startswith('{0}sup'.format(prefix)):
        ch = message.channel
        await message.delete()

        msg = await ch.send('Du hast erfolgreich Support angefordert! Ein Teammitglied wird sich gleich um dich kümmern.')
        await msg.delete(delay=3)

        membername = message.author.name
        channelid = custom_json.read_key('ids.json', 'teamch')
        cchannel = other.catch_channel(message, channelid)
        cmodrole = other.catch_role(message, modrole)
        await cchannel.send('{0} Das Mitglied {1} benötigt Hilfe!'.format(cmodrole.mention,membername))


async def opensup(message, prefix, modrole, blacklisted):

    ch = message.channel
    if message.content.lower().startswith('{0}opensup'.format(prefix)):
        await message.delete()
        if not blacklisted:
            cmodrole = other.catch_role(message, modrole)
            noperms = True
            for role in message.author.roles:
                if role == cmodrole:
                    voicechannelid = custom_json.read_key('ids.json', 'supvoicech')
                    voicechannel = other.catch_channel(message, voicechannelid)
                    textchannelid = custom_json.read_key('ids.json', 'supch')
                    textchannel = other.catch_channel(message, textchannelid)
                    target = other.catch_role(message, 'Mitglied')
                    await voicechannel.edit(name='⏳Support Warteraum')
                    await voicechannel.set_permissions(target=target, overwrite=discord.PermissionOverwrite(connect=True))
                    await textchannel.edit(topic='Support Geöffnet! (wenn du Support benötigst dann gebe /sup ein)')
                    await textchannel.set_permissions(target=target, overwrite=discord.PermissionOverwrite(send_messages=True))
                    noperms = False
                    break

            if noperms:
                msg = await ch.send('Du hast keine Rechte um diesen Command auszuführen du brauchst die Rolle: `{0}`!'.format(modrole))
                await msg.delete(delay=3)
                print('DEBUG: {0} hat versucht den support zu öffnen, hatte aber keine Berechtigung dazu.'.format(message.author))

            elif not noperms:
                msg = await ch.send('Der Support wurde erfolgreich geöffnet!')
                await msg.delete(delay=3)
                print('DEBUG: {0} hat den Support geöffnet.'.format(message.author))
        else:
            msg = await ch.send('Du stehst auf der Blacklist und kannst deswegen keine Commands ausführen!')
            print('DEBUG: Der auf der Blacklist stehende Spieler {0} hat versucht einen Command zu benutzen, wurde aber geblockt!'.format(message.author))
            await msg.delete(delay=5)


async def closesup(message, prefix, modrole, blacklisted):
    ch = message.channel
    if message.content.lower().startswith('{0}closesup'.format(prefix)):
        await message.delete()
        if not blacklisted:
            cmodrole = other.catch_role(message, modrole)
            noperms = True
            for role in message.author.roles:
                if role == cmodrole:
                    voicechannelid = custom_json.read_key('ids.json', 'supvoicech')
                    voicechannel = other.catch_channel(message, voicechannelid)
                    textchannelid = custom_json.read_key('ids.json', 'supch')
                    textchannel = other.catch_channel(message, textchannelid)
                    target = other.catch_role(message, 'Mitglied')
                    await voicechannel.edit(name='🚫Support Geschlossen')
                    await voicechannel.set_permissions(target=target, overwrite=discord.PermissionOverwrite(connect=False))
                    await textchannel.edit(topic='Support Geschlossen!')
                    await textchannel.set_permissions(target=target, overwrite=discord.PermissionOverwrite(send_messages=False))
                    noperms = False
                    break

            if noperms:
                msg = await ch.send('Du hast keine Rechte um diesen Command auszuführen du brauchst die Rolle: `{0}`!'.format(modrole))
                await msg.delete(delay=3)
                print('DEBUG: {0} hat versucht den support zu schließen, hatte aber keine Berechtigung dazu.'.format(message.author))

            elif not noperms:
                msg = await ch.send('Der Support wurde erfolgreich geschlossen!')
                await msg.delete(delay=3)
                print('DEBUG: {0} hat den Support geschlossen.'.format(message.author))
        else:
            msg = await ch.send('Du stehst auf der Blacklist und kannst deswegen keine Commands ausführen!')
            print('DEBUG: Der auf der Blacklist stehende Spieler {0} hat versucht einen Command zu benutzen, wurde aber geblockt!'.format(message.author))
            await msg.delete(delay=5)


async def supinfo(channel, member, modrole):
    teamchatid = custom_json.read_key('ids.json', 'teamch')
    teamchat = get(channel.guild.channels, id=teamchatid)
    mod = get(channel.guild.roles, name=modrole)
    for role in member.roles:
        if role == mod:
            print('DEBUG: {0} ist dem Support Warteraum beigetreten'.format(member))
            await teamchat.send('<@&{0}>  Der Spieler "{1}" wartet im Supportwarteraum auf ein Teammitglied!'.format(mod.id, member))
            await member.send('''
[ Gamezone ]
Du befindest dich nun in der Supportwarteschlange.
Einen Moment bitte, ein Teammitglied wird sich gleich um dich kümmern.''')
