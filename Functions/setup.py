from Functions import other, custom_json


async def run(message, prefix, modrole, client):

    if message.content.lower().startswith('{0}setup'.format(prefix)):

        ch = message.channel
        member = message.author
        cmodrole = other.catch_role(message, modrole)
        await message.delete()

        def pred(m):
            return m.author == member and m.channel == ch

        for role in member.roles:
            if role == cmodrole:

                msg = await ch.send('Bitte gebe die id des "#verify" Channels ein!')
                response = await client.wait_for('message', check=pred)
                verifychid = int(response.content)
                await response.delete()
                await msg.delete()

                msg = await ch.send('Bitte gebe die id des "#rollen-zuweisung" Channels ein!')
                response = await client.wait_for('message', check=pred)
                rolechid = int(response.content)
                await response.delete()
                await msg.delete()

                msg = await ch.send('Bitte gebe die id des "#support" Channels ein!')
                response = await client.wait_for('message', check=pred)
                supchid = int(response.content)
                await response.delete()
                await msg.delete()

                msg = await ch.send('Bitte gebe die id des "#reports" Channels ein!')
                response = await client.wait_for('message', check=pred)
                repchid = int(response.content)
                await response.delete()
                await msg.delete()

                msg = await ch.send('Bitte gebe die id des "AFK" VoiceChannels ein!')
                response = await client.wait_for('message', check=pred)
                afkvoicechid = int(response.content)
                await response.delete()
                await msg.delete()

                msg = await ch.send('Bitte gebe die id des "Support Warteraum" VoiceChannels ein!')
                response = await client.wait_for('message', check=pred)
                supvoicechid = int(response.content)
                await response.delete()
                await msg.delete()

                msg = await ch.send('Bitte gebe die id des "#teamchat" Channels ein!')
                response = await client.wait_for('message', check=pred)
                teamchid = int(response.content)
                await response.delete()
                await msg.delete()

                msg = await ch.send('Bitte gebe die id des "Channel erstellen" VoiceChannels ein!')
                response = await client.wait_for('message', check=pred)
                createvoicech = int(response.content)
                await response.delete()
                await msg.delete()

                msg = await ch.send('Bitte gebe die id des "#logs" Channels ein!')
                response = await client.wait_for('message', check=pred)
                logch = int(response.content)
                await response.delete()
                await msg.delete()

                custom_json.edit('ids.json', 'verifych', verifychid)
                custom_json.edit('ids.json', 'rolech', rolechid)
                custom_json.edit('ids.json', 'supch', supchid)
                custom_json.edit('ids.json', 'repch', repchid)
                custom_json.edit('ids.json', 'teamch', teamchid)
                custom_json.edit('ids.json', 'afkvoicech', afkvoicechid)
                custom_json.edit('ids.json', 'supvoicech', supvoicechid)
                custom_json.edit('ids.json', 'createvoicech', createvoicech)
                custom_json.edit('ids.json', 'logch', logch)

                async def question():
                    msg = await ch.send('Sollen die Narichten in "#verify" und "#rollen-zuweisung" erstellt werden?(J/N)')
                    response = await client.wait_for('message', check=pred)
                    response_ = response.content
                    await response.delete()
                    await msg.delete()
                    if not response_ == 'J' and not response_ == 'N':
                        msg = await ch.send('Fehler: Ungültige Antwort!')
                        await msg.delete(delay=3)
                        response_ = await question()
                        return response_
                    return response_

                answer = await question()
                print(answer)

                if answer.lower().startswith('j'):

                    verifych = other.catch_channel(message, verifychid)
                    msg = await verifych.send('Klicke auf die Reaktion um dich zu verifizieren und die Regeln anzunehmen')
                    await msg.add_reaction('✅')

                    verifymsgid = msg.id

                    rolech = other.catch_channel(message, rolechid)
                    msg = await rolech.send('Reagier auf das Emote um die entsprechende Rolle zu erhalten oder zu entfernen!\n'
                                            '1️⃣ <@&700691126658793552>\n'
                                            '2️⃣ <@&700686467999072277>\n'
                                            '3️⃣ <@&700686635896930346>\n'
                                            '4️⃣ <@&812670506758569995>\n'
                                            '5️⃣ <@&744903409513005067>')
                    await msg.add_reaction('1️⃣')
                    await msg.add_reaction('2️⃣')
                    await msg.add_reaction('3️⃣')
                    await msg.add_reaction('4️⃣')
                    await msg.add_reaction('5️⃣')

                    rolemsgid = msg.id

                    custom_json.edit('ids.json', 'verifymsg', verifymsgid)
                    custom_json.edit('ids.json', 'rolemsg', rolemsgid)

                msg = await ch.send('Setup abgeschlossen!')
                await msg.delete(delay=3)
