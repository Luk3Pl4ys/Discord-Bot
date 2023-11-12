from Functions import other, custom_json


async def move(member_, message_, mode):
    ch = message_.channel
    channelid = custom_json.read_key('ids.json', 'afkvoicech')
    cchannel = other.catch_channel(message_, channelid)
    if member_.voice is None:
        if mode == 'self':
            msg = await ch.send('Du befindest dich in keinem Channel!')
            await msg.delete(delay=3)
        if mode == 'other':
            msg = await ch.send('Der Benutzer befindet sich in keinem Channel!')
            await msg.delete(delay=3)
        return None

    await member_.move_to(cchannel)
    if mode == 'self':
        msg = await ch.send('Du wurdest in den AFK Channel verschoben!')
        await msg.delete(delay=3)
    if mode == 'other':
        msg = await ch.send('Der Benutzer "{0}" wurde in den AFK Channel verschoben!'.format(member_.name))
        await msg.delete(delay=3)


async def run(message, prefix, blacklisted, modrole):
    if message.content.lower().startswith('{0}afk'.format(prefix)):
        ch = message.channel
        await message.delete()

        if blacklisted:
            msg = await ch.send('Du stehst auf der Blacklist und kannst deswegen keine Commands ausführen!')
            print('DEBUG: Der auf der Blacklist stehende Spieler {0} hat versucht einen Command zu benutzen,'
                  ' wurde aber geblockt!'.format(message.author))
            await msg.delete(delay=5)
            return None

        if message.mentions.__len__() > 0:
            member = message.mentions[0]
            cmodrole = other.catch_role(message, modrole)
            for role in message.author.roles:
                if role == cmodrole:
                    await move(member, message, 'other')
                    return None

        else:
            member = message.author
            await move(member, message, 'self')
            return None

        msg = await ch.send('Du hast keine Berechtigung für diesen Befehl!')
        await msg.delete(delay=3)
