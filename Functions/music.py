import discord
import youtube_dl
import os


async def run(client, message, prefix, blacklisted):

    channel = message.channel
    guild = message.guild
    author = message.author

    if blacklisted:
        msg = await channel.send('Du stehst auf der Blacklist und kannst deswegen keine Commands ausführen!')
        print('DEBUG: Der auf der Blacklist stehende Spieler {0} hat versucht einen Command zu benutzen,'
              ' wurde aber geblockt!'.format(message.author))
        await msg.delete(delay=5)
        return None

    if message.content.lower().startswith('{0}play'.format(prefix)):
        await message.delete()

        args = str(message.content[5 + len(prefix):])

        await play(client, prefix, channel, guild, author, args)

    if message.content.lower().startswith('{0}leave'.format(prefix)):
        await message.delete()
        await leave(client, channel, guild)

    if message.content.lower().startswith('{0}pause'.format(prefix)):
        await message.delete()
        await pause(client, channel, guild)

    if message.content.lower().startswith('{0}resume'.format(prefix)):
        await message.delete()
        await resume(client, channel, guild)

    if message.content.lower().startswith('{0}stop'.format(prefix)):
        await message.delete()
        await stop(client, guild)


async def play(client, prefix, ch, guild, author, args):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        msg = await ch.send(f'Bitte Warte bis der aktuelle Song vorbei ist oder benutze den {prefix}stop command um einen neuen Song abspielen zu können!')
        await msg.delete(delay=3)

    if args == "":
        msg = await ch.send('Fick dich Boss!')
        await msg.delete(delay=3)
        return

    voiceChannel = author.voice.channel

    if voiceChannel is None:
        msg = await ch.send('Du musst dich in einem Voice Channel befinden um diesen Command ausführen zu können!')
        await msg.delete(delay=3)
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    if args.lower().startswith('http'):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(args, download=True)
        title = meta['title']
        uploader = meta['uploader']
        duration = meta['duration']

    else:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(f'ytsearch:{args}', download=True)
        entries = meta['entries'][0]
        title = entries['title']
        uploader = entries['uploader']
        duration = entries['duration']

    duration = int(duration)
    hours = divmod(duration, 3600)
    minutes = divmod(hours[1], 60)
    seconds = minutes[1]

    hours = str(hours[0])
    minutes = str(minutes[0])
    seconds = str(seconds)

    if len(hours) == 1:
        hours = f'0{hours}'

    if len(minutes) == 1:
        minutes = f'0{minutes}'

    if len(seconds) == 1:
        seconds = f'0{seconds}'

    if hours == '00':
        time = f'{minutes}:{seconds}'
    else:
        time = f'{hours}:{minutes}:{seconds}'

    await ch.send(f'Spiele "{title}"[{time}] von {uploader} ab!')

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")

    try:
        await voiceChannel.connect()
    except AttributeError:
        pass

    voice = discord.utils.get(client.voice_clients, guild=guild)

    voice.play(discord.FFmpegPCMAudio("song.mp3"))


async def leave(client, ch, guild):
    voice = discord.utils.get(client.voice_clients, guild=guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        msg = await ch.send("Der Bot befindet sich in keinem Voice Channel")
        await msg.delete(delay=3)


async def pause(client, ch, guild):
    voice = discord.utils.get(client.voice_clients, guild=guild)
    if voice.is_playing():
        voice.pause()
    else:
        msg = await ch.send("Es wird gerade nichts gespielt!")
        await msg.delete(delay=3)


async def resume(client, ch, guild):
    voice = discord.utils.get(client.voice_clients, guild=guild)
    if voice.is_paused():
        voice.resume()
    else:
        msg = await ch.send("Der Song ist gerade nicht pausiert!")
        await msg.delete(delay=3)


async def stop(client, guild):
    voice = discord.utils.get(client.voice_clients, guild=guild)
    voice.stop()
