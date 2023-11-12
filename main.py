# bot-icon https://cdn.discordapp.com/attachments/604348596661387303/812661884892872704/istockphoto-1167414558-170667a.jpg

# imports

import discord
import os
from Functions import get_rm_role, change_reset_presence, report, help, verify, customchannels, admin_cmds, afk, \
    custom_json, other, setup, sup, log, music

# definitions
intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
intents.guild_reactions = True
client = discord.Client(intents=intents)
c = 'bot_config.json'
owner_id = custom_json.read_key(c, 'ownerid')
modrole = custom_json.read_key(c, 'modrole')
prefix = custom_json.read_key(c, 'prefix')
presence = custom_json.read_key(c, 'presence')


# on_ready
@client.event
async def on_ready():
    startclock = other.get_time()
    print('')
    print(startclock)
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)

    await client.change_presence(status=discord.Status.online, activity=discord.Game(presence))

    # remove custom channel
    await customchannels.remove(client)


# on_message
@client.event
async def on_message(message):
    blackliston = custom_json.read_key(c, 'blackliston')
    stdpresence = custom_json.read_key(c, 'stdpresence')
    blacklisted = False

    blacklist = custom_json.read('blacklist.json')

    if blackliston == 'True':
        for n in blacklist:
            if message.author.id == n:
                blacklisted = True

    clock = other.get_time()

    if not message.author.id == client.user.id and message.channel not in client.private_channels:

        # log message
        await log.message(message, clock)

        # admin cmds
        await admin_cmds.run(message, modrole, prefix, blackliston, client)

        # help
        await help.run(message, prefix, blacklisted)

        # change/reset presence
        await change_reset_presence.run(message, client, prefix, blacklisted, modrole, stdpresence)

        # closesup
        await sup.closesup(message, prefix, modrole, blacklisted)

        # opensup
        await sup.opensup(message, prefix, modrole, blacklisted)

        # report
        await report.run(message, prefix, blacklisted, clock)

        # afk
        await afk.run(message, prefix, blacklisted, modrole)

        # setup
        await setup.run(message, prefix, modrole, client)

        # sup
        await sup.callsup(message, prefix, modrole)

        # music
        await music.run(client, message, prefix, blacklisted)


# on_raw_reaction_add
@client.event
async def on_raw_reaction_add(payload):

    # verify
    await verify.run(payload, client)

    # get_role
    await get_rm_role.get(payload, client)


# on_raw_reaction_remove
@client.event
async def on_raw_reaction_remove(payload):

    # rm_role
    await get_rm_role.rm(payload, client)


# on_voice_state_update
@client.event
async def on_voice_state_update(member, before, after):
    channel = after.channel
    channel_before = before.channel

    clock = other.get_time()

# channel-join/-left/-move/-sup log

    if channel is not None:
        # move
        if channel is not channel_before and channel_before is not None:

            # log channel move
            await log.chmove(member, channel_before, channel, clock)

            # remove custom channel on move
            await customchannels.remove(client)

        else:
            if channel is not channel_before:

                # log channel move
                await log.chjoin(member, channel, clock)

        supvoicech = custom_json.read_key('ids.json', 'supvoicech')
        if channel.id == supvoicech and channel is not channel_before:

            # call support
            await sup.supinfo(channel, member, modrole)

    if channel is None and channel_before is not None:

        # log channel leave
        await log.chleave(member, channel_before, clock)

        # remove custom channel on leave
        await customchannels.remove(client)

    # create custom channel on join
    await customchannels.create(member, before, after)


# run_bot
token = os.environ.get('BOT_TOKEN')
client.run(token)

# test bot token: TEST_BOT_TOKEN
# main bot token: BOT_TOKEN
