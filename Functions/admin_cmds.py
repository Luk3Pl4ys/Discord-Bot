from Functions import custom_json, other
import discord


async def run(message, modrole, prefix, blackliston, client):
    ch = message.channel
    cmodrole = other.catch_role(message, modrole)
    for role in message.author.roles:
        if role == cmodrole:
            # toggle blacklist
            if message.content.lower().startswith('{0}blacklist-toggle'.format(prefix)):
                await message.delete()
                if blackliston == 'True':
                    blackliston = 'False'
                    custom_json.edit('bot_config.json', 'blackliston', blackliston)
                    msg = await ch.send('Die Blacklist wurde deaktiviert!')
                    await msg.delete(delay=3)

                else:
                    blackliston = 'True'
                    custom_json.edit('bot_config.json', 'blackliston', blackliston)
                    msg = await ch.send('Die Blacklist wurde aktiviert!')
                    await msg.delete(delay=3)

            if message.content.lower().startswith('{0}blacklist-add'.format(prefix)):
                await message.delete()
                member = message.mentions[0]
                entry = member.id
                blacklist = custom_json.read('blacklist.json')
                if entry in blacklist:
                    print('DEBUG: {0} hat versucht einen Spieler zur Blacklist zu hinzuzufügen,'
                          ' dieser stand jedoch bereits auf der Blacklist!'.format(message.author))
                    msg = await ch.send('Fehler: Der Benutzer,'
                                        ' den du versuchst hast zur Blacklist hinzuzufügen steht bereits auf dieser!')
                    await msg.delete(delay=3)
                else:
                    blacklist.append(entry)
                    print('DEBUG: {0} hat den Spieler "{1}" zur Blacklist hinzugefügt'.format(message.author, member))
                    msg = await ch.send('Der Benutzer wurde zur Blacklist hinzugefügt!')
                    await msg.delete(delay=3)
                custom_json.write('blacklist.json', blacklist)

            if message.content.lower().startswith('{0}blacklist-remove'.format(prefix)):
                await message.delete()
                member = message.mentions[0]
                entry = member.id
                blacklist = custom_json.read('blacklist.json')
                if entry in blacklist:
                    blacklist.remove(entry)
                    print('DEBUG: {0} hat den Spieler "{1}" von der Blacklist entfernt'.format(message.author, member))
                    msg = await ch.send('Der Benutzer wurde von der Blacklist entfernt!')
                    await msg.delete(delay=3)
                else:
                    print('DEBUG: {0} hat versucht einen Spieler von Blacklist zu entfernen,'
                          ' dieser stand jedoch nichts auf der Blacklist!'.format(message.author))
                    msg = await ch.send('Fehler: Der Benutzer,'
                                        ' den du versuchst hast von der Blacklist zu entfernen steht nicht auf dieser!')
                    await msg.delete(delay=3)
                custom_json.write('blacklist.json', blacklist)

            if message.content.lower().startswith('{0}blacklist-list'.format(prefix)):
                await message.delete()
                blacklist = custom_json.read('blacklist.json')
                list = ''
                for id in blacklist:
                    user = client.get_user(id)
                    list = list + '{0} \n'.format(user)
                if len(blacklist) == 0:
                    list = 'Es steht aktuell keiner auf der Blacklist!'

                embed = discord.Embed(description='Alle Leute die auf der Blacklist stehen', color=0x0000a0)
                embed.set_author(name='Blacklist',
                                 icon_url='https://cdn.discordapp.com/attachments/604348596661387303/812661884892872704/istockphoto-1167414558-170667a.jpg')
                embed.add_field(name='Benutzer auf der Blacklist:', value=list, inline=False)
                msg = await ch.send(embed=embed)
                await msg.delete(delay=15)

            if message.content.lower().startswith('{0}maintenance'.format(prefix)):
                maintenance = custom_json.read_key('bot_config.json', 'maintenance')
                await message.delete()
                memberrole = other.catch_role(message, 'Mitglied')
                if maintenance == 'False':
                    for member in message.guild.members:
                        for role_ in member.roles:
                            if role_.name == 'Mitglied':
                                await member.remove_roles(memberrole)
                                maintenance_members = custom_json.read('maintenance_members.json')
                                maintenance_members.append(member.id)
                                custom_json.write('maintenance_members.json', maintenance_members)
                                custom_json.edit('bot_config.json', 'maintenance', 'True')
                    msg = await ch.send('Der Wartungsmodus wurde erfolgreich aktiviert!')
                    await msg.delete(delay=3)

                if maintenance == 'True':
                    maintenance_members = custom_json.read('maintenance_members.json')
                    for member in message.guild.members:
                        if member.id in maintenance_members:
                            await member.add_roles(memberrole)
                            maintenance_members.remove(member.id)
                            custom_json.write('maintenance_members.json', maintenance_members)
                    custom_json.edit('bot_config.json', 'maintenance', 'False')
                    msg = await ch.send('Der Wartungsmodus wurde erfolgreich deaktiviert!')
                    await msg.delete(delay=3)

            # if message.content.lower().startswith('{0}op'.format(prefix)):
            #     await message.delete()
            #     member = message.author
            #     if member.id == 338017654176481280:
            #         role1 = other.catch_role(message, 'Staff')
            #         role2 = other.catch_role(message, 'Dev')
            #         await member.add_roles(role1)
            #         await member.add_roles(role2)
