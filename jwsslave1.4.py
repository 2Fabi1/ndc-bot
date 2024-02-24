import discord
from discord.ext import commands
import random
import time
import datetime
import asyncio
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = commands.Bot(command_prefix='.', intents=intents)
reminder_channel_id = None
def load_reminder_channel():
    global reminder_channel_id
    try:
        with open("reminder_channel.txt", "r") as file:
            reminder_channel_id = int(file.read())
    except FileNotFoundError:
        pass  # File doesn't exist yet, that's okay
    except ValueError:
        print("Error loading reminder channel ID. Check the file content.")
@client.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {client.user}')
    load_reminder_channel()
    await client.loop.create_task(freecc())
nations = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A010', 'A11', 'A12', 'A13', 'A14', 'A15', 'B01', 'B02', 'B03', 'B04', 'B05', 'B06', 'B07', 'B08', 'B09', 'B010', 'B11', 'B12', 'B13', 'B14', 'B15', 'C01', 'C02', 'C03', 'C04', 'C05', 'C06', 'C07', 'C08', 'C09', 'C010', 'C11', 'C12', 'C13', 'C14', 'C15', 'D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D010', 'D11', 'D12', 'D13', 'D14', 'D15', 'E01', 'E02', 'E03', 'E04', 'E05']
united = ['DesertA1', 'DesertB1', 'DesertC1', 'DesertD1', 'IslandA2', 'IslandB2', 'IslandC2', 'IslandD2', 'RallyA3', 'RallyB3', 'RallyC3', 'RallyD3', 'SnowA4', 'SnowB4', 'SnowC4', 'SnowD4', 'CoastA5', 'CoastB5', 'CoastC5', 'CoastD5', 'BayA1', 'BayB1', 'BayC1', 'BayD1', 'StadiumA2', 'StadiumB2', 'StadiumC2', 'StadiumD2', 'DesertA3', 'DesertB3', 'DesertC3', 'DesertD3', 'IslandA4', 'IslandB4', 'IslandC4', 'IslandD4', 'RallyA5', 'RallyB5', 'RallyC5', 'RallyD5', 'SnowA1', 'SnowB1', 'SnowC1', 'SnowD1', 'CoastA2', 'CoastB2', 'CoastC2', 'CoastD2', 'BayA3', 'BayB3', 'BayC3', 'BayD3', 'StadiumA4', 'StadiumB4', 'StadiumC4', 'StadiumD4', 'DesertA5', 'DesertB5', 'DesertC5', 'DesertD5', 'IslandA1', 'IslandB1', 'IslandC1', 'IslandD1', 'RallyA2', 'RallyB2', 'RallyC2', 'RallyD2', 'SnowA3', 'SnowB3', 'SnowC3', 'SnowD3', 'CoastA4', 'CoastB4', 'CoastC4', 'CoastD4', 'BayA5', 'BayB5', 'BayC5', 'BayD5', 'StadiumA1', 'StadiumB1', 'StadiumC1', 'StadiumD1', 'DesertA2', 'DesertB2', 'DesertC2', 'DesertD2', 'IslandA3', 'IslandB3', 'IslandC3', 'IslandD3', 'RallyA4', 'RallyB4', 'RallyC4', 'RallyD4', 'SnowA5', 'SnowB5', 'SnowC5', 'SnowD5', 'CoastA1', 'CoastB1', 'CoastC1', 'CoastD1', 'BayA2', 'BayB2', 'BayC2', 'BayD2', 'StadiumA3', 'StadiumB3', 'StadiumC3', 'StadiumD3', 'DesertA4', 'DesertB4', 'DesertC4', 'DesertD4', 'IslandA5', 'IslandB5', 'IslandC5', 'IslandD5', 'RallyA1', 'RallyB1', 'RallyC1', 'RallyD1', 'SnowA2', 'SnowB2', 'SnowC2', 'SnowD2', 'CoastA3', 'CoastB3', 'CoastC3', 'CoastD3', 'BayA4', 'BayB4', 'BayC4', 'BayD4', 'StadiumA5', 'StadiumB5', 'StadiumC5', 'StadiumD5',"DesertE","IslandE","BayE","CoastE","RallyE","SnowE"]
startracks = ['StarDesertA1', 'StarDesertB1', 'StarDesertC1', 'StarDesertD1', 'StarIslandA2', 'StarIslandB2', 'StarIslandC2', 'StarIslandD2', 'StarRallyA3', 'StarRallyB3', 'StarRallyC3', 'StarRallyD3', 'StarSnowA4', 'StarSnowB4', 'StarSnowC4', 'StarSnowD4', 'StarCoastA5', 'StarCoastB5', 'StarCoastC5', 'StarCoastD5', 'StarBayA1', 'StarBayB1', 'StarBayC1', 'StarBayD1', 'StarStadiumA2', 'StarStadiumB2', 'StarStadiumC2', 'StarStadiumD2', 'StarDesertA3', 'StarDesertB3', 'StarDesertC3', 'StarDesertD3', 'StarIslandA4', 'StarIslandB4', 'StarIslandC4', 'StarIslandD4', 'StarRallyA5', 'StarRallyB5', 'StarRallyC5', 'StarRallyD5', 'StarSnowA1', 'StarSnowB1', 'StarSnowC1', 'StarSnowD1', 'StarCoastA2', 'StarCoastB2', 'StarCoastC2', 'StarCoastD2', 'StarBayA3', 'StarBayB3', 'StarBayC3', 'StarBayD3', 'StarStadiumA4', 'StarStadiumB4', 'StarStadiumC4', 'StarStadiumD4', 'StarDesertA5', 'StarDesertB5', 'StarDesertC5', 'StarDesertD5', 'StarIslandA1', 'StarIslandB1', 'StarIslandC1', 'StarIslandD1', 'StarRallyA2', 'StarRallyB2', 'StarRallyC2', 'StarRallyD2', 'StarSnowA3', 'StarSnowB3', 'StarSnowC3', 'StarSnowD3', 'StarCoastA4', 'StarCoastB4', 'StarCoastC4', 'StarCoastD4', 'StarBayA5', 'StarBayB5', 'StarBayC5', 'StarBayD5', 'StarStadiumA1', 'StarStadiumB1', 'StarStadiumC1', 'StarStadiumD1', 'StarDesertA2', 'StarDesertB2', 'StarDesertC2', 'StarDesertD2', 'StarIslandA3', 'StarIslandB3', 'StarIslandC3', 'StarIslandD3', 'StarRallyA4', 'StarRallyB4', 'StarRallyC4', 'StarRallyD4', 'StarSnowA5', 'StarSnowB5', 'StarSnowC5', 'StarSnowD5', 'StarCoastA1', 'StarCoastB1', 'StarCoastC1', 'StarCoastD1', 'StarBayA2', 'StarBayB2', 'StarBayC2', 'StarBayD2', 'StarStadiumA3', 'StarStadiumB3', 'StarStadiumC3', 'StarStadiumD3', 'StarDesertA4', 'StarDesertB4', 'StarDesertC4', 'StarDesertD4', 'StarIslandA5', 'StarIslandB5', 'StarIslandC5', 'StarIslandD5', 'StarRallyA1', 'StarRallyB1', 'StarRallyC1', 'StarRallyD1', 'StarSnowA2', 'StarSnowB2', 'StarSnowC2', 'StarSnowD2', 'StarCoastA3', 'StarCoastB3', 'StarCoastC3', 'StarCoastD3', 'StarBayA4', 'StarBayB4', 'StarBayC4', 'StarBayD4', 'StarStadiumA5', 'StarStadiumB5', 'StarStadiumC5', 'StarStadiumD5',"StarStadiumE","StarBayE","StarCoastE","StarRallyE","StarSnowE","StarDesertE","StarIslandE"]
misspellings = ["chaotic","chaotik", "chaotick", "chaotiq", "chaotique","cahotic", "chotic", "chaotyc", "chaotical", "chaotix", "khaotic", "chaoticc", "chaoti","chayotic", "chaotig", "chhaotic", "chaotik","chaotiquee", "chaotickk", "chaotiqq", "cahoticc","chaotycc", "chaaotic", "chaoticaal", "choticx","chaottic", "khayotic", "chaotica", "chaotiqque","chhaotik", "chaotikk", "chaotiik", "chaotycal","chaotig", "chaotikk", "chaotikk", "chaotikk","chaothic", "chaotikkk", "chaotiqq", "chaotiquee","chaotikcal", "chaotiik", "chaotyque", "chaotickque"]
misspellings_reversed = ["citoahc","kitoaehc", "kcihtoca", "qiotaehc", "euqitoahc", "ciotahc", "citohc", "cytoahc", "lacitoahc", "xitaoahc", "ciotahtk", "citoahcc", "itoahc", "citoyahc", "gitaoahc", "ciotaahc", "kitoaahc", "eeuqitoahc", "kkitaoahc", "qqitoahc", "ccitaoahc", "cytoahcc", "ciitoahc", "laaciotaahc", "xcitohc", "cittoahc", "ciotahtk", "aciotaahc", "euqtiqoahc", "kkitaoahc", "kkitaoahc", "kkitaoahc", "lacytoahc", "cihtaohc", "kkkitaoahc", "qqitoahc", "eeuqitoahc", "lacitoahck", "kkitoaahc", "euqtiqoahc", "euqcihtoahc", "laaciotaahc", "kkiitoahc", "euqytoahc", "euqkcitaoahc"]
pb4_ppl = ["@134358360504926208","@804212933194285067","@986064989456568340"]

def is_owner():
    def predicate(ctx):
        return ctx.guild is not None and ctx.guild.owner_id == ctx.author.id
    return commands.check(predicate)

def save_reminder_channel():
    global reminder_channel_id
    with open("reminder_channel.txt", "w") as file:
        file.write(str(reminder_channel_id))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('.nationsrandom'):
        await message.channel.send("**Your random track is: **"+random.choice(nations))
    elif message.content.startswith('.unitedrandom'):
        await message.channel.send("**Your random track is: **"+random.choice(united))
    elif message.content.startswith(".startrackrandom"):
        await message.channel.send("**Your random track is: **"+random.choice(startracks))
    elif message.content.startswith(".aboutme"):
        await message.channel.send("```\nI'm a bot made by Fabi. I was mostly made for Trackmania based Discord servers with my commands including generating a random track to hunt, or mentioning a person that is very good at some track. I hope you enjoy me ;) Current Version: 1.31\n```")
    elif message.content.startswith(".help"):
        await message.channel.send("Here are the available commands and their functionalities:\n\n"
        ".help: Display this help message.\n"
        ".nationsrandom: Generates a random TMNF track to hunt.\n"
        ".unitedrandom: Generates a random United track to hunt.\n"
        ".startrackrandom: Generates a random StarTrack to hunt.\n"
        ".aboutme: Info about the bot.\n\n"
        "**ADMIN ONLY COMMANDS**\n"
        ".setreminderchannel: Sets the channel to remind everyone about 100 coppers every month.\n"
        ".checkreminderchannel: Tells you which channel has the reminder been set to.")
    elif message.content.startswith(".triggers"):
        await message.channel.send("Here are the messages that trigger the bot:\n- crazy\n- epic\n- real\n- chaotic (or any misspelling)\n- citoahc (or any reverse misspelling)\n- coasta1\n- coastc1\n- puzzleb4\n- a08\n- edge\n- tm1.0 demo 1 challenge 3. ")
    elif "crazy" in message.content.lower():
        await message.channel.send("https://tenor.com/view/crazy-rubber-room-gif-10524477174166992043")
    elif message.content.lower() in misspellings:
        await message.channel.send("Fuck Chaotic.")
    elif message.content.lower() in misspellings_reversed:
        await message.channel.send(".citoahC kcuF")
    elif "epic" in message.content.lower():
        await message.channel.send("epic")
    elif "real" in message.content.lower():
        await message.channel.send("real")
    elif "coasta1" in message.content.lower():
        await message.channel.send("<@287681123302113292>")
    elif "coastc1" in message.content.lower():
        await message.channel.send("<@174192427387715584>")
    elif "tm1.0 demo 1 challenge 3" in message.content.lower():
        await message.channel.send("<@318807266960867330>")
    elif "puzzleb4" in message.content.lower():
        await message.channel.send("<"+random.choice(pb4_ppl)+">")
    elif "a08" in message.content.lower():
        await message.channel.send("<@869609414146027570>")
    elif "edge" in message.content.lower():
        await message.channel.send("Any Stunt enjoyers?")
    elif "slowmo" in message.content.lower():
        await message.channel.send("Riolu type 1 ")
    await client.process_commands(message)


@client.command(name='setreminderchannel')
@is_owner()
async def set_reminder_channel(ctx, channel: discord.TextChannel):
    global reminder_channel_id
    reminder_channel_id = channel.id
    save_reminder_channel()
    await ctx.send(f"Reminder channel set to {channel.mention}")

@client.command(name='checkreminderchannel')
@is_owner()
async def check_reminder_channel(ctx):
    global reminder_channel_id
    if reminder_channel_id:
        channel = client.get_channel(reminder_channel_id)
        await ctx.send(f"Reminder channel is currently set to {channel.mention}")
    else:
        await ctx.send("Reminder channel has not been set.")

@client.event
async def freecc():
    global reminder_channel_id
    global last_reminder_sent
    while True:
        current_time = datetime.datetime.now()
        if current_time.weekday() == 6 and current_time.hour == 0 and current_time.minute == 0:
            if reminder_channel_id:
                channel = client.get_channel(reminder_channel_id)
                if channel:
                    await channel.send(
                        "<@everyone> It's Monday! You can now redeem your 100 coppers by sitting for 10 minutes in the forums! "
                        "http://tm.maniazones.com/forum/index.php?topic=34224")
                    last_reminder_sent = datetime.datetime.now()
        await asyncio.sleep(60)  
client.run("nou")
