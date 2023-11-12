import discord
from Functions import custom_json


async def create(member, before, after):
    chid = custom_json.read_key('ids.json', 'createvoicech')
    if after.channel is None:
        return
    if after.channel.id == chid and before.channel is not after.channel:
        category = after.channel.category
        name = '{0}\'s Channel'.format(member.name)
        overwrite = discord.PermissionOverwrite(manage_channels=True, manage_roles=True, view_channel=True)
        ch = await category.create_voice_channel(name=name)
        await ch.set_permissions(member, overwrite=overwrite)
        await member.move_to(ch)
        custom_channels = custom_json.read('custom_channels.json')
        custom_channels.append(ch.id)
        custom_json.write('custom_channels.json', custom_channels)


async def remove(client):
    custom_channels = custom_json.read('custom_channels.json')
    for chid in custom_channels:
        ch = client.get_channel(chid)
        if ch.members == []:
            await ch.delete()
            custom_channels.remove(chid)
            custom_json.write('custom_channels.json', custom_channels)
            await remove(client)
            break
