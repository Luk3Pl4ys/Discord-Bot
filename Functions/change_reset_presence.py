from Functions import custom_json, other
import discord


async def run(message, client, prefix, blacklisted, modrole, stdpresence):
    ch = message.channel
    if message.content.lower().startswith('{0}presence'.format(prefix)):
        await message.delete()
        if not blacklisted:
            cmodrole = other.catch_role(message, modrole)
            global hasperms
            hasperms = False
            error = False
            if message.content.lower().startswith('{0}presence-reset'.format(prefix)):
                for role in message.author.roles:
                    if role == cmodrole:
                        hasperms = True
                        custom_json.edit('bot_config.json', 'presence', stdpresence)
                        await client.change_presence(status=discord.Status.online, activity=discord.Game(stdpresence))
                        print('DEBUG: {0} hat die Presence zum Standardwert "{1}" zurückgesetzt'.format(message.author,
                                                                                                        stdpresence))
                        msg = await ch.send('Die Presence wurde zurückgesetzt!')
                        await msg.delete(delay=3)

            else:
                for role in message.author.roles:
                    if role == cmodrole:
                        hasperms = True
                        presence = message.content[9 + len(prefix):]
                        if not error:
                            custom_json.edit('bot_config.json', 'presence', presence)
                            await client.change_presence(status=discord.Status.online, activity=discord.Game(presence))
                            msg = await ch.send('Die Presence wurde zu: "`{0}`" geändert!'.format(presence))
                            print('DEBUG: {0} hat die Presence erfolgreich zu "{1}" geändert.'.format(message.author,
                                                                                                      presence))
                            await msg.delete(delay=3)

            if not hasperms:
                msg = await ch.send('Du hast keine Rechte um diesen Command auszuführen du brauchst die Rolle: '
                                    '`{0}`!'.format(modrole))
                print('DEBUG: {0} hat versucht den Status zu ändern hatte aber nicht die nötige Berechtigung '
                      'dafür.'.format(message.author))
                await msg.delete(delay=3)
        else:
            msg = await ch.send('Du stehst auf der Blacklist und kannst deswegen keine Commands ausführen!')
            print('DEBUG: Der auf der Blacklist stehende Spieler {0} hat versucht einen Command zu benutzen, '
                  'wurde aber geblockt!'.format(message.author))
            await msg.delete(delay=5)
