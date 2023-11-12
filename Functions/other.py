import datetime
from discord.utils import get


def get_time():
    now = datetime.datetime.now()
    hours = str(now.hour)
    if len(hours) == 1:
        hours = '0' + hours
    minutes = str(now.minute)
    if len(minutes) == 1:
        minutes = '0' + minutes
    seconds = str(now.second)
    if len(seconds) == 1:
        seconds = '0' + seconds
    day = str(now.day)
    if len(day) == 1:
        day = '0' + day
    month = str(now.month)
    if len(month) == 1:
        month = '0' + month
    year = str(now.year)
    clock = '[{0}.{1}.{2} {3}:{4}:{5}]'.format(day, month, year, hours, minutes, seconds)
    return clock


def catch_role(message, rolename):
    member = message.author
    catchedrole = get(member.guild.roles, name=rolename)
    return catchedrole


def catch_channel(message, channelid):
    member = message.author
    catchedchannel = get(member.guild.channels, id=channelid)
    return catchedchannel
