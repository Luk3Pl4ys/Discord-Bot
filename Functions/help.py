import discord


async def run(message, prefix, blacklisted):
    ch = message.channel
    if message.content.lower().startswith('{0}help'.format(prefix)):
        await message.delete()
        if blacklisted:
            msg = await ch.send('Du stehst auf der Blacklist und kannst deswegen keine Commands ausführen!')
            print('DEBUG: Der auf der Blacklist stehende Spieler {0} hat versucht einen Command zu benutzen,'
                  ' wurde aber geblockt!'.format(message.author))
            await msg.delete(delay=5)
            return

        msg = await ch.send('Du stehst auf der Blacklist und kannst deswegen keine Commands ausführen!')
        print('DEBUG: Der auf der Blacklist stehende Spieler {0} hat versucht einen Command zu benutzen,'
                ' wurde aber geblockt!'.format(message.author))
        await msg.delete(delay=5)
        print('DEBUG: {0} hat {1}help benutzt.'.format(message.author,prefix))

        help1 = discord.Embed(description='Hilfe Seite 1/1 Alle Commands können Groß, Klein oder als Mischformen von beidem geschrieben werden.',
                                color=0x0000a0)
        help1.set_author(name='Gamezone Bot Hilfe 1/1', icon_url='https://cdn.discordapp.com/attachments/604348596661387303/812661884892872704/istockphoto-1167414558-170667a.jpg')
        help1.add_field(name='{0}help'.format(prefix), value='Zeigt diese Seite an.', inline=False)
        help1.add_field(name='{0}report [@Nutzer] [Grund]'.format(prefix), value='Reportet einen Spieler.', inline=False)
        help1.add_field(name='{0}afk'.format(prefix), value='Verschiebt dich in den AFK Channel.',inline=False)
        #help1.add_field(name='{0}Minecraft'.format(prefix), value='Gibt/entfernt dir die Rolle Minecraft.', inline=False)
        help1.set_footer(text='Gamezone Bot by Lukeplays#1187')

        help2 = discord.Embed(description='Hilfe Seite 2/3. Alle Commands können Groß, Klein oder als Mischformen von beidem geschrieben werden.',
                                  color=0x0000a0)
        help2.set_author(name='Gamezone Bot Hilfe 2/3', icon_url='https://cdn.discordapp.com/attachments/604348596661387303/812661884892872704/istockphoto-1167414558-170667a.jpg')
        help2.add_field(name='{0}ETS'.format(prefix), value='Gibt/entfernt dir die Rolle Euro Truck Simulator.', inline=False)
        help2.add_field(name='{0}CS-GO'.format(prefix), value='Gibt/entfernt dir die Rolle CS-GO.', inline=False)
        help2.add_field(name='{0}CoD'.format(prefix), value='Gibt/entfernt dir die Rolle CoD.', inline=False)
        help2.add_field(name='{0}GTA'.format(prefix), value='Gibt/entfernt dir die Rolle GTA.', inline=False)
        help2.set_footer(text='Gamezone Bot by Lukeplays#1187')

        help3 = discord.Embed(description='Hilfe Seite 3/3. Alle Commands können Groß, Klein oder als Mischformen von beidem geschrieben werden.',
                                  color=0x0000a0)
        help3.set_author(name='Gamezone Bot Hilfe 3/3', icon_url='https://cdn.discordapp.com/attachments/604348596661387303/812661884892872704/istockphoto-1167414558-170667a.jpg')
        help3.add_field(name='{0}RDR2'.format(prefix), value='Gibt/entfernt dir die Rolle Red Dead Redemption 2.',inline=False)
        help3.add_field(name='{0}Overwatch'.format(prefix), value='Gibt/entfernt dir die Rolle Owerwatch.', inline=False)
        help3.add_field(name='{0}Hogwarts Mystery'.format(prefix), value='Gibt/entfernt dir die Rolle Hogwarts Mystery.', inline=False)
        help3.add_field(name='{0}Garrysmod'.format(prefix), value='Gibt/entfernt dir die Rolle Garrysmod.',inline=False)
        help3.set_footer(text='Gamezone Bot by Lukeplays#1187')

        help1 = await ch.send(embed=help1)
        #help2 = await ch.send(embed=help2)
        #help3 = await ch.send(embed=help3)
        await help1.delete(delay=15)
        #await help2.delete(delay=30)
        #await help3.delete(delay=45)
