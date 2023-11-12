from Functions import other, custom_json


async def run(payload, client):

    verifymsgid = custom_json.read_key('ids.json', 'verifymsg')
    maintenance = custom_json.read_key('bot_config.json', 'maintenance')

    c_id = payload.channel_id
    m_id = payload.message_id
    g_id = payload.guild_id
    u_id = payload.user_id

    channel = client.get_channel(c_id)
    message = await channel.fetch_message(m_id)
    guild = client.get_guild(g_id)
    member = guild.get_member(u_id)

    if m_id == verifymsgid:

        await message.remove_reaction('✅', member)
        if maintenance == 'False':
            crole = other.catch_role(message, 'Mitglied')
            await member.add_roles(crole)
            await member.send('Du bist nun verifiziert! Viel Spaß auf Gamezone!')
