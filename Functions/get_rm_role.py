from Functions import custom_json, other


# '1️⃣'
# '2️⃣'
# '3️⃣'
# '4️⃣'
# '5️⃣'

async def get(payload, client):

    rolemsgid = custom_json.read_key('ids.json', 'rolemsg')

    c_id = payload.channel_id
    m_id = payload.message_id
    g_id = payload.guild_id
    u_id = payload.user_id
    emoji = payload.emoji.name

    channel = client.get_channel(c_id)
    message = await channel.fetch_message(m_id)
    guild = client.get_guild(g_id)
    member = guild.get_member(u_id)

    if m_id == rolemsgid:

        if emoji == '1️⃣':
            role = other.catch_role(message, 'Events')
            await member.add_roles(role)

        if emoji == '2️⃣':
            role = other.catch_role(message, 'Bot-Rechte')
            await member.add_roles(role)

        if emoji == '3️⃣':
            role = other.catch_role(message, 'Announcements')
            await member.add_roles(role)

        if emoji == '4️⃣':
            role = other.catch_role(message, 'Karaoke')
            await member.add_roles(role)

        if emoji == '5️⃣':
            role = other.catch_role(message, 'Osu!')
            await member.add_roles(role)


async def rm(payload, client):

    rolemsgid = custom_json.read_key('ids.json', 'rolemsg')

    c_id = payload.channel_id
    m_id = payload.message_id
    g_id = payload.guild_id
    u_id = payload.user_id
    emoji = payload.emoji.name

    channel = client.get_channel(c_id)
    message = await channel.fetch_message(m_id)
    guild = client.get_guild(g_id)
    member = guild.get_member(u_id)

    if m_id == rolemsgid:

        if emoji == '1️⃣':
            role = other.catch_role(message, 'Events')
            await member.remove_roles(role)

        if emoji == '2️⃣':
            role = other.catch_role(message, 'Bot-Rechte')
            await member.remove_roles(role)

        if emoji == '3️⃣':
            role = other.catch_role(message, 'Announcements')
            await member.remove_roles(role)

        if emoji == '4️⃣':
            role = other.catch_role(message, 'Karaoke')
            await member.remove_roles(role)

        if emoji == '5️⃣':
            role = other.catch_role(message, 'Osu!')
            await member.remove_roles(role)
