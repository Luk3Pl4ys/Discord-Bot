import discord
from Functions import other, custom_json


async def run(message, prefix, blacklisted, clock):
    ch = message.channel
    if message.content.lower().startswith('{0}report'.format(prefix)):
        if not blacklisted:
            await message.delete()
            error = False
            if (message.mentions.__len__() > 0):
                user = message.mentions[0]
            else:
                error = True
                msg = await ch.send('Fehler: Du musst angeben wen du reporten möchtest!')
                await msg.delete(delay=3)
            if not error:
                space = 8 + int(len(message.mentions[0].mention)) + len(prefix)
                reportcontent = str(message.content[space:])
                if len(reportcontent) == 0:
                    error = True
                    msg = await ch.send('Fehler: Du musst einen Reportgrund angeben!')
                    await msg.delete(delay=3)
                if not error:
                    if message.content[8] == '<':
                        report = discord.Embed(description='Ein neuer Report wurde erstellt',color=0x0000a0)
                        report.set_author(name='Gamezone Bot Reportsystem', icon_url='https://cdn.discordapp.com/attachments/604348596661387303/812661884892872704/istockphoto-1167414558-170667a.jpg')
                        report.add_field(name='Zeit:', value=clock, inline=True)
                        report.add_field(name='Von Benutzer:', value='{0}'.format(message.author), inline=True)
                        report.add_field(name='Gegen Benutzer:', value='{0}'.format(user), inline=True)
                        report.add_field(name='Grund:', value=reportcontent, inline=True)
                        report.set_footer(text='Gamezone Bot by Lukeplays#1187')
                        channel = custom_json.read_key('ids.json', 'repch')
                        cchannel = other.catch_channel(message, channel)
                        await cchannel.send(embed=report)
                        msg = await ch.send('Dein Report wurde erfolgreich gesendet! Eine Kopie deines Reports wurde an dich zugeschickt.')
                        await message.author.send(embed=report)
                        await msg.delete(delay=3)
                    else:
                        msg = await ch.send('Fehler: Du musst erst den Benutzer, dann den Reportgrund angeben!')
                        await msg.delete(delay=3)

        else:
            msg = await ch.send('Du stehst auf der Blacklist und kannst deswegen keine Commands ausführen!')
            print('DEBUG: Der auf der Blacklist stehende Spieler {0} hat versucht einen Command zu benutzen, wurde aber geblockt!'.format(message.author))
            await msg.delete(delay=5)
