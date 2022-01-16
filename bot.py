import discord
import random
import asyncio
import json
import os
from discord.ext import commands, tasks
from discord.mentions import AllowedMentions
import dislash
from dislash import InteractionClient, Option, OptionType, SlashInteraction, ActionRow, Button, ButtonStyle, SelectMenu, SelectOption, OptionChoice

#Note: There's cringe variable names

lelnums = {}

print('started lelnumsssssssssss')

lelnum_filename = 'lelnums.json'

try:
    file_yey = open(lelnum_filename)
    lelnums = json.load(file_yey)
    print('loaded data!')
except IOError:
    print(f'lelnums.json dont exist...')

if not os.path.isfile("users.txt"):
    file = open("users.txt", 'w+')
    file.write("nothing lol xd")
    file.close()
if not os.path.isfile("cookis.txt"):
    file = open("cookis.txt", 'w+')
    file.write("0")
    file.close()
if not os.path.isfile("items.txt"):
    file = open("items.txt", 'w+')
    file.write("Cooki&&5&&Cooki :D&&:cookie:\nLinux&&129&&Linux&&:penguin:\nLelcube plushie&&180&&Lelcube plushie uwu&&<:lelcube:811058465383514132>\nWindows Vista&&299&&Super stable OS.&&:window:\nTerrible laptop&&399&&Dis laptop trash&&:computer:\nFree bobux&&500&&Use this item to get free bobux :eyes::eyes::eyes:&&:money_mouth:\nTop secret lelcube images&&1000&&:eyes:&&:card_box:")
    file.close()
if not os.path.isfile("facts.txt"):
    file = open("facts.txt", 'w+')
    file.write("1&&C is a programming language, and B is a programming language too!&&hellory4n\n2&&Windows 7 version is actually 6.1, 8 is 6.2 and 8.1 is 6.3, but Windows 10 is really Windows 10&&hellory4n\n3&&You are seeing millions of small squares with different colors shown in a thing we call \"screen\"&&hellory4n\n4&&You are cook :)&&hellory4n\n5&&\"Racecar\" is a palidrome&&MrXCube\n6&&If you are not rich you still can buy apple products, such as apple juice, apple ,apple pie, etc&&Rubi\n7&&If you explore the internet, then you are an Internet Explorer&&i forgor\n8&&Windows 10 has a very ||in||consistent design!&&hellory4n\n9&&||***KAMANDTSNEAHNLABDNPISCOIR3S1O8HRCBTNOVXULAEMEOAIA4RDRFHEYNWVEPCOHCAYWIOOERNTLHEXOTABODTIUEYORUSXRYU4ZP1LMWTBGTMHMUNTLILWMNESOOEYFTA4IMSRTLUOTMPWRHIB3BLLS1TENMOESTTHHIEAPCEEOIPTLNEW3DSGLR1RAAEWCTRORYTBRIULAQIAOL5XTYALFORBIAAIDAGEDITLCSDBLDTAYSOEBNILFENTATOLSAOLNX8VSLIBANDDTREYOFEOAPHRLLANATBRHALNGB0RCEARBRLJIRCTTOELRYEJAIIRTOU2C5NRKATAASWUAOLTMVFOPY6RI4YEOAYNAVEEDCXECPX***||&&hellory4n\n10&&Lists are lists, cameras are cameras, and objects are objects :thumbsup:&&hellory4n\n11&&Yuo Stlil Cna Raed Thsi Meyss Mesaseg.&&Miftah\n12&&To make cookies you need an oven. Get inside the oven, now wait 5-8 minutes, and you will no more need to make cookis cuz, ***you are the cookis now***&&SrMuffin136\n13&&Having 300,000,000 bobux is not required to get a cookie.&&hellory4n\n14&&Calculator is a very good game&&hellory4n\n15&&Speedrunners spend all of their time trying to spend the least of their time&&MrXCube\n16&&Many french people don't say \"I love you!\", that is because they don't speak english&&Rubi\n17&&M isn't the 3rd letter of the alphabet&&Rubi\n18&&1 + 1 isn't 13&&hellory4n\n19&&Your age is the age you has today.&&hellory4n\n20&&Pancakes are not made to be used to remove dust.&&hellory4n\n21&&You only have 1 birthday, the other ones are congratulations for surviving&&Rubi\n22&&If you say #NonsenseAlwaysDie 69 times in a row, someone from Makesense Dimension will slap you and said \"Nice\". Then it will suck you like a vacuum and bring you to a place near giant incinerator. It will ask you some questions. If you can't answer them, you'll be incinerated and die forever.&&R3DZ3R\n23&&This server has more than 1 member! :sunglasses:&&hellory4n\n24&&Christmas trees aren't made out of Christmas&&alex343xd\n25&&Hello guys! Today I'm gonna say an **EPIC** fact! But before we continue, today's fact is sponsored by Nonsense, one of the most innovative Fancade puzzle games of 2021 and it's totally free! Currently almost 1 million users have joined Nonsense over the last 6 months, and it's one of the most impressive games in its class with simple models, cringy texts, and smooth 60 frames per second animations! The game is called Nonsense because you can nonsense someone with this cuz ues im crazy lol waea. Nonsense has 4.0 score on the Fancade Spotlight! So what are you waiting for? Go to the Fancade Discord Server, click on the game link and you'll get the game ready to play! Fact: You are you.&&R3DZ3R + hellory4n (R3DZ3R made the ad, hellory4n made the rest)\n26&&This text wasn't written in 1970.&&hellory4n\n27&&No matter how far you rotate it, a sphere is still a sphere&&R3DZ3R\n28&&Technically, a space suit protacts an astronaut from nothing&&MrXCube\n29&&Discord Nitro has no speed change to the app&&alex343xd\n30&&It's kinda rude when you go to your best friend's funeral, but he doesn't go to yours&&Rubi")
    file.close()

client = commands.Bot(command_prefix = 'l!')

client.remove_command('help')

inter_client = InteractionClient(client)

@tasks.loop(seconds = 3600)
async def cook_loop():
    statuses = ['/',
    'Me has cook slash commands',
    'Hey do you want free B O b u X?',
    'Beep boop',
    'Beep boop me is a bot and me don\'t breathe air cuz bots don\'t breathe air',
    'lel',
    'This text was written on 11/03/2021',
    'I need potatos. Can you give me potatos?',
    'Me likes potatos',
    'Potatos are cook',
    'There\'s so many good things you can do on your life, why you are reading this?',
    'h uwu',
    'Hello! My token is [REDACTED].',
    'hgsfvusdijfv',
    'You are cook :)',
    'Type "/slash" to see a butiful message',
    'Never gonna give you up',
    'Are you reading this?',
    'h',
    'Did you know that your age is your age + 3 - 3?',
    'I want a really fancy coffee maker',
    'I love SandwichXP, it\'s just so well made!']
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(f'Type l!help for help! {random.choice(statuses)}'))

@client.event
async def on_ready():
    #Only remove the "#" from the line below if you don't have to restart the bot many times
    #cook_loop.start()
    print('Im online EEEEEEEE')

@client.event
async def on_command_error(ctx, error):
    await ctx.send(f'```o\n{error}```\nIf it wasn\'t you, report it to hellory4n')

@client.event
async def on_slash_command_error(interaction, error):
    await interaction.send(f"```o\n{error}```\nIf it wasn't you, report it to hellory4n")

@client.command(aliases=['hello'])
async def hello2(ctx, *, someone=""):
    hello = ["Hello", "Hi", "Helo", "Henlo", "Yo", "Hellooo", "Helooo", "Henlooo", "Hi hello", "Hello hi", "Hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo", "***Hej***", "Hola", "Hewwo"]
    await ctx.send(f"{random.choice(hello)} {someone}")

@client.command(aliases=['ping'])
async def ping2(ctx):
    await ctx.send(f':ping_pong: Pong! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ['yes', 'probably yes', 'yes?', 'definitely', 'idk lol', 'Hi', 'no', 'probably not', 'no?', 'definitely not']
    eightball_embed=discord.Embed(title=f'{question}', description=f'{random.choice(responses)}', color=0xFECC4D)
    eightball_embed.set_footer(text=ctx.author.id)
    await ctx.send(embed=eightball_embed)

@client.command(aliases=['explode', 'explosion', 'boom'])
async def boom2(ctx, *, exploded_lol):
    boom_embed=discord.Embed(title="Boom!", description=f'{exploded_lol} exploded!\nDamage: {random.randint(1,100)}', color=0xFECC4D)
    boom_embed.set_footer(text=f'Exploded by {ctx.message.author}')
    await ctx.send(embed=boom_embed)

@client.command(aliases=['commands'])
async def help(ctx):
    embed = discord.Embed(title="Help", description="\n`<>` means required argument, `[]` means optional argument\nDon't include `<>` or `[]`\nMost commands are available in slash commands!", color=0xFECC4D)
    embed.add_field(name="Very random", value="`bobux`, `dostuff [index]`, `hello [something]`, `morecookis`, `randomsandwich`, `randomstory`, `sandwich <size>`, `name`", inline=False)
    embed.add_field(name="Random", value="`bam <someone>`, `boom <something>`, `fact [index]`, `hack <something>`, `sweatsmile`, `yesorno <question>`, `chat <something>`, `sentence`, `who <someone>`", inline=False)
    embed.add_field(name="Not so random", value="`attack <someone>`, `hug <someone>`, `say <something>`, `8ball <question>`, `when <question>`, `weirdtext`, `text_to_wotcode`, `wotcode_to_text`", inline=False)
    embed.add_field(name="Economy",value="`work`, `bal [user]`, `dep <amount>`, `with <amount>`, `lb`, `shop`, `buy [amount]`, `inv [user]`, `use [amount]`, `give_money <user> <amount>`, `reset_money`, `give_item <user> <amount>`, `rob <user> <amount>`")
    embed.add_field(name="Bot stuff", value="`ping`, `invite`, `aboutme`, `server`, `help`, `classic_help`", inline=False)
    embed.add_field(name="Stuff that isn't really for fun", value="`embed <title> | <description>`, `math <expression>`, `poll <text>`, `randnum <min> <max>`, `suggest <suggestion>`, `roll`", inline=False)
    await ctx.reply(embed=embed)

@client.command()
async def invite(ctx):
    embed = discord.Embed(title="Invite", description="Click [here](https://discord.com/api/oauth2/authorize?client_id=822199023636709456&permissions=8&scope=bot%20applications.commands) to invite lelbot on your cook server!", color=0xFECC4D)
    embed.set_footer(text=":)")
    await ctx.send(embed=embed)

@client.command(aliases=['chat'])
async def chat2(ctx, *, chat):
    chatresponses = ['njfk',
                'Ye',
                'Okie',
                'Okay',
                'Oke',
                'OISUGIAEODFIJUHYSEIUODUGY',
                'nice',
                'oh noes!',
                'me too!',
                'ooh',
                'ok, but i have the ~~worst~~ best ai',
                'i dont like lolbot',
                'sandwich. **sandwich...** SANDWICH!!!!!!! GIMME SANDWICH!!!!',
                'OwO',
                'UwU',
                'a?',
                'h']
    
    await ctx.send(f'{random.choice(chatresponses)}')

@client.command()
async def funfact(ctx):
    funfacts = ['**Fun Fact #1**:\nI liek hugs (/･ω･(-ω-) *(fact by SrMuffin136)*',
                '**Fun Fact #2**:\nyou breathe air *(fact by Senjienji)*',
                '**Fun Fact #3**:\nThis is a text message *(fact by Dylan Brew)*',
                '**Fun Fact #4**:\nA tsunami can travel as fast as a jet plane. *(fact by shartok)*',
                '**Fun Fact #5**:\nU are *alive (fact by SrMuffin136)*',
                '**Fun Fact #6**:\nThere is a 50% chance that in a group of 23 people, two will share the same birthday.  In a group of 367 people, it is a 100% chance.  But only 70 people are required for a 99.9% chance. *(fact by shartok)*',
                '**Fun Fact #7**:\nLelbot is sweatsmile but smugging instead *(fact by Nextie)*',
                '**Fun Fact #8**:\nSandwich are cool *(fact by SrMuffin136)*',
                '**Fun Fact #10**:\nTheres no fun fact #9 lel',
                '**Fun Fact #11**:\nI have [too lazy to update this lol]KB!',
                '**Fun Fact #12**:\nThe python version i used in this code is 3.9.2/3.9.7!',
                '**Fun Fact #13**:\nThe best letter is Æ!',
                '**Fun Fact #14**:\nI like potatos',
                '**Fun Fact #15**:\nleft handed people can finish a test faster than a tiger *(fact by Rubi)*']

    await ctx.send(f'{random.choice(funfacts)}')

@client.command(aliases=['randomstory'])
async def randomstory2(ctx):
    storywords = ['in',
                'a',
                'random',
                'village',
                '.',
                'that',
                'will',
                'be',
                'walking',
                'on',
                'cliffside',
                'little',
                'man',
                'called',
                'lelbot',
                'has',
                'builder',
                'friend',
                'for',
                'the',
                'leader',
                'of',
                'where',
                'magic',
                'happens',
                'then',
                'it',
                'goes',
                'to',
                'so',
                'banana',
                'walked',
                'potatopatata']
    
    await ctx.send(f'*{random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)}*')

@client.command()
async def aboutme(ctx):
        embed=discord.Embed(title=f'About lelbot', description=f"Hello! I'm lelbot, the smartest AI in the universe, created by hellory5n, a very evil guy with very dumb plans!\nBy the way this is hellory5n: <:hellory5n:915028960604200982>", color=0xFECC4D)
        embed.set_footer(text="Version 1.3.1")
        embed.add_field(name="Credits",value="Developed by hellory4n\nMany facts from `fact`: The credits are in the command itself\nArnold cooki ad from super snowman item: JustYellow\nThanks for using me!",inline=False)
        await ctx.send(embed=embed)

@client.command(aliases=['when'])
async def when2(ctx, *, whenn):
    whentype = random.randint(1,8)

    if whentype == 1:
        await ctx.send(f'After {random.randint(1,60)} seconds.')
    if whentype == 2:
        await ctx.send(f'After {random.randint(1,60)} minutes.')
    if whentype == 3:
        await ctx.send(f'After {random.randint(1,24)} hours.')
    if whentype == 4:
        await ctx.send(f'After {random.randint(1,31)} days.')
    if whentype == 5:
        await ctx.send(f'After {random.randint(1,12)} months.')
    if whentype == 6:
        await ctx.send(f'After {random.randint(1,100)} years.')
    if whentype == 7:
        await ctx.send(f'After {random.randint(1,10000)} milleniums.')
    if whentype == 8:
        await ctx.send(f'After {random.randint(1,100000000000000000)} milleniums... Thats too much!')

@client.command(aliases=['yesorno'])
async def helloyesorno(ctx, *, question):
    helloyesorno = ['https://media.discordapp.net/attachments/806308041115959377/911742147655508038/hellono_but_big.png',
            'https://media.discordapp.net/attachments/806308041115959377/911742147999445052/helloyes_but_big.png']
    embed=discord.Embed(title=question, description="", color=0xFECC4D)
    embed.set_footer(text=ctx.author.id)
    embed.set_image(url=random.choice(helloyesorno))
    await ctx.send(embed=embed)

@client.command(aliases=['say'])
async def say2(ctx, *, sandwich_owo):
    if '@everyone' in sandwich_owo or '@here' in sandwich_owo:
        await ctx.send(f'{ctx.author.mention} no mass ping here >:c')
    else:
        await ctx.send(f'{sandwich_owo}\n\n**- {ctx.message.author} ({ctx.author.id})**')

@client.command(aliases=['hug'])
async def hug2(ctx, *, never_gonna_give_you_up):
    if '@everyone' in never_gonna_give_you_up or '@here' in never_gonna_give_you_up:
        await ctx.send(f'{ctx.author.mention} no mass ping here >:c')
    else:
        await ctx.send(f'{ctx.author.mention} hugged {never_gonna_give_you_up}! <:Hello_UwU:822546152402321428>')

@client.command(aliases=['attack'])
async def attack2(ctx, *, never_gonna_let_you_down):
    if '@everyone' in never_gonna_let_you_down or '@here' in never_gonna_let_you_down:
        await ctx.send(f'{ctx.author.mention} no mass ping here >:c')
    else:
        await ctx.send(f'{ctx.author.mention} attacked {never_gonna_let_you_down}! <:Gun:816099538619072553> <:Hello_Angry:822546148534386699>')

@client.command(aliases=['bam'])
async def bam2(ctx, *, bammed):
    if '@everyone' in bammed or '@here' in bammed:
        await ctx.send(f'{ctx.author.mention} no mass ping here >:c')
    else:
        await ctx.send(f'{bammed} has (not) been banned by {ctx.author.mention}. ')

@client.command()
async def roll(ctx):
    await ctx.send(f':game_die: {random.randint(1,6)}')

@client.command(aliases=['hack'])
async def hack2(ctx, *, something):
    yo = await ctx.send(f"Getting access to {something}...")
    await asyncio.sleep(5)
    await yo.edit(content=f"Found email! ({something}{str(random.randint(10000000,99999999))}@lelmail.com)")
    await asyncio.sleep(2.5)
    await yo.edit(content="Found emojis from their phone cuz why not <:lelcube:811058465383514132>")
    await asyncio.sleep(3)
    await yo.edit(content="Drinking coffee... :coffee:")
    await asyncio.sleep(3.1)
    await yo.edit(content="Exploding my own database lol <:lelcube:811058465383514132>")
    await asyncio.sleep(4)
    await yo.edit(content="Selling their data to a random person...")
    await asyncio.sleep(3.5)
    await yo.edit(content=f"{ctx.author.mention} Hacked {something} successfully!")

@client.command()
async def server(ctx):
    await ctx.send('This is ma cook server\nhttps://discord.gg/JUYGFDavj6')

@client.command(aliases=['randomsandwich'])
async def randomsandwich2(ctx):
    randsandwich = ['sandwich',
                'sandwich OwO',
                'sandwich UwU',
                'sandwich 2',
                'fanmade sandwich',
                'super sandwich',
                'coolio sandwich',
                'sandwich god',
                'sandwich EEEEEEEE',
                'sandwich plus',
                'big sandwich',
                'tiny sandwich',
                'normal sandwich',
                'sandwich fans',
                'sandwich 95',
                'sandwich speed',
                'sandwich 98',
                'sandwich 2000',
                'sandwich 2009',
                'sandwich 2012',
                'sandwich 10',
                'next sandwich',
                'sandwich hd',
                'retro sandwich',
                'sandwich pro',
                'sandwich gold',
                'sandwich spam',
                'sandwich online',
                'sandwich x',
                'sandwich xl',
                'sandwich xz',
                'free sandwich',
                'sandwich multiplayer',
                'sandwich cube',
                'sandwich ball',
                'sandwich ooooooo',
                'sandwich smart',
                'sandwich camera',
                'sandwich light',
                'sandwich stop']
    await ctx.send(f'You got... **{random.choice(randsandwich)}**!')

@client.command(aliases=['poll'])
async def poll2(ctx, *, owopoll):
    pou_embed=discord.Embed(title=f'Poll by {ctx.message.author}', description=f'{owopoll}', color=0xFECC4D)
    pou_embed.set_footer(text=f'lel')
    Poll = await ctx.send(embed=pou_embed)
    await Poll.add_reaction('<:checkmark:828495515423080448>')
    await Poll.add_reaction('<:crossmark:828495571240747018>')

@client.command(aliases=['suggest','suggestion'])
async def suggest2(ctx, *, suggestiondiewatflooshed):
    susggestion_embed=discord.Embed(title=f'{ctx.message.author} suggestion', description=f'{suggestiondiewatflooshed}', color=0xFECC4D)
    susggestion_embed.set_footer(text=f'lel')
    susmsg = await ctx.send(embed=susggestion_embed)
    await susmsg.add_reaction('✅')
    await susmsg.add_reaction('❎')
    await susmsg.add_reaction('🤔')
    await susmsg.add_reaction('❓')

@client.command(aliases=['weirdtext'])
async def weirdtext2(ctx):
    a_lot_of_characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']

    await ctx.send(f'{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}')

@client.command(aliases=['dostuff'])
async def dostuff2(ctx,index="random"):
    no_NOOOOO = False
    
    try:
        int_index = int(index)
    except:
        index = "random"

    if index == "random":
        lelbot_tasks_index = random.randint(1,65)
        no_NOOOOO = True
    else:
        if int_index < 1 or int_index > 65:
            await ctx.send("Invalid index! Please enter something between 1 and 65.")
        else:
            lelbot_tasks_index = int_index
            no_NOOOOO = True

    #choices = [':microphone2: <:lelcube:811058465383514132>&&He sings',':frame_photo: :paintbrush: <:lelcube:811058465383514132>&&He paints',':computer: <:lelcube:811058465383514132>&&He codes',':video_game: <:lelcube:811058465383514132>&&He play games',':potato: <:Gun:816099538619072553> <:lelcube:811058465383514132>',':tv: <:lelcube:811058465383514132>&&He watches tv',':hammer: <:lelcube:811058465383514132>&&He destroy stuff',':shower:\n<:lelcube:811058465383514132>&&He showers','<:lelcube:811058465383514132> :shopping_cart:&&He goes shopping',':balloon: <:lelcube:811058465383514132>&&He plays with balloon',':wastebasket: :newspaper2: <:lelcube:811058465383514132>&&He doesnt like to read cuz reading is boring and i just noticed that to use discord you have to read which is boring so technicly using discord is boring but is not eeeeeeeeeeeee',':video_camera: <:lelcube:811058465383514132>&&He records a video',':pencil: <:lelcube:811058465383514132>&&He writes a text','<:Nextie:835598971518189621> :mag: <:lelcube:811058465383514132>&&He is trying to see nextie *but nextie has the size of a __pixel__*','<:lelcube:811058465383514132> :loudspeaker:&&He says potatopatata very loud',':cake: :fork_and_knife: <:lelcube:811058465383514132>&&He eats a cake',':iphone: <:lelcube:811058465383514132>&&He uses the phone',':pizza: <:lelcube:811058465383514132>&&He is 101% sure that pizza is pizza','<:clapping:811058070843162686> <:lelcube:811058465383514132>&&He claps','<:lelcube:811058465383514132> :vs: <:sweatsmile:811059266806480916>&&He fights',':telephone_receiver: <:lelcube:811058465383514132>&&He calls people','<:lelcube:811058465383514132> :tent:&&He goes camping',':ballet_shoes: <:lelcube:811058465383514132>&&He uses a ballet shoes','<:lelcube:811058465383514132> :toothbrush: :toilet:&&He uses a ballet shoes',':tophat:\n<:lelcube:811058465383514132> :magic_wand:&&He magic man',':saxophone: <:lelcube:811058465383514132>&&He plays the saxophone cuz saxophones are cool','<:lelcube:811058465383514132> ']
    if no_NOOOOO == True:
        if lelbot_tasks_index == 1:
            await ctx.send(f'🎙 <:lelcube:811058465383514132>')
            await ctx.send(f'He sings')
        if lelbot_tasks_index == 2:
            await ctx.send(f':frame_photo: :paintbrush: <:lelcube:811058465383514132>')
            await ctx.send(f'He paints')
        if lelbot_tasks_index == 3:
            await ctx.send(f':computer: <:lelcube:811058465383514132>')
            await ctx.send(f'He codes')
        if lelbot_tasks_index == 4:
            await ctx.send(f':video_game: <:lelcube:811058465383514132>')
            await ctx.send(f'He play games')
        if lelbot_tasks_index == 5:
            await ctx.send(f':potato: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
            await ctx.send(f'He kills potatos')
        if lelbot_tasks_index == 6:
            await ctx.send(f':tv: <:lelcube:811058465383514132>')
            await ctx.send(f'He watches tv')
        if lelbot_tasks_index == 7:
            await ctx.send(f':hammer: <:lelcube:811058465383514132>')
            await ctx.send(f'He destroy stuff')
        if lelbot_tasks_index == 8:
            await ctx.send(f':shower:\n<:lelcube:811058465383514132>')
            await ctx.send(f'He showers')
        if lelbot_tasks_index == 9:
            await ctx.send(f'<:lelcube:811058465383514132> :shopping_cart:')
            await ctx.send(f'He goes shopping')
        if lelbot_tasks_index == 10:
            await ctx.send(f':balloon: <:lelcube:811058465383514132>')
            await ctx.send(f'He plays with balloon')
        if lelbot_tasks_index == 11:
            await ctx.send(f':wastebasket: :newspaper2: <:lelcube:811058465383514132>')
            await ctx.send(f'He doesnt like to read cuz reading is boring and i just noticed that to use discord you have to read which is boring so technicly using discord is boring but is not eeeeeeeeeeeee')
        if lelbot_tasks_index == 12:
            await ctx.send(f':video_camera: <:lelcube:811058465383514132>')
            await ctx.send(f'He records a video')
        if lelbot_tasks_index == 13:
            await ctx.send(f':pencil: <:lelcube:811058465383514132>')
            await ctx.send(f'He writes a text')
        if lelbot_tasks_index == 14:
            await ctx.send(f'<:Nextie:835598971518189621> :mag: <:lelcube:811058465383514132>')
            worstjokeever = await ctx.send(f'He is trying to see nextie *but nextie have the size of a __pixel__*')
            await worstjokeever.add_reaction('<:bassrolf:821948606701371462>')
        if lelbot_tasks_index == 15:
            await ctx.send(f'<:lelcube:811058465383514132> :loudspeaker:')
            await ctx.send(f'He says potatopatata very loud')
        if lelbot_tasks_index == 16:
            await ctx.send(f':cake: :fork_and_knife: <:lelcube:811058465383514132>')
            await ctx.send(f'He eats a cake')
        if lelbot_tasks_index == 17:
            await ctx.send(f':iphone: <:lelcube:811058465383514132>')
            await ctx.send(f'He uses the phone')
        if lelbot_tasks_index == 18:
            await ctx.send(f':pizza: <:lelcube:811058465383514132>')
            await ctx.send(f'He is 101% sure that pizza is pizza')
        if lelbot_tasks_index == 19:
            await ctx.send(f'<:clapping:811058070843162686> <:lelcube:811058465383514132>')
            await ctx.send(f'He claps')
        if lelbot_tasks_index == 20:
            await ctx.send(f'<:lelcube:811058465383514132> :vs: <:sweatsmile:811059266806480916>')
            await ctx.send(f'He fights')
        if lelbot_tasks_index == 21:
            await ctx.send(f':telephone_receiver: <:lelcube:811058465383514132>')
            await ctx.send(f'He calls people')
        if lelbot_tasks_index == 22:
            await ctx.send(f'<:lelcube:811058465383514132> :tent:')
            await ctx.send(f'He goes camping')
        if lelbot_tasks_index == 23:
            await ctx.send(f':ballet_shoes: <:lelcube:811058465383514132>')
            await ctx.send(f'He uses a ballet shoes')
        if lelbot_tasks_index == 24:
            await ctx.send(f'<:lelcube:811058465383514132> :toothbrush: :toilet:')
            await ctx.send(f'He clean the toilet')
        if lelbot_tasks_index == 25:
            await ctx.send(f":tophat:\n<:lelcube:811058465383514132> :magic_wand:")
            await ctx.send(f'He magic man')
        if lelbot_tasks_index == 26:
            await ctx.send(f':saxophone: <:lelcube:811058465383514132>')
            await ctx.send(f'He plays the saxophone cuz saxophones are cool')
        if lelbot_tasks_index == 27:
            await ctx.send(f'<:lelcube:811058465383514132> <:okhand:811059019828428821>')
            await ctx.send(f'He likes *something*')
        if lelbot_tasks_index == 28:
            await ctx.send(f'<:sweatwide1:818622702574632970><:lelcube:811058465383514132><:sweatwide2:818622715815526481>')
            await ctx.send(f'He uses a disguise')
        if lelbot_tasks_index == 29:
            await ctx.send(f':sweat_smile: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
            await ctx.send(f'He kills')
        if lelbot_tasks_index == 30:
            await ctx.send(f'<:maum1:778489567036178464> <:lelcube:811058465383514132> <:maum2:778489689014403072>')
            await ctx.send(f'He will catch you')
        if lelbot_tasks_index == 31:
            await ctx.send(f'<:lelcube:811058465383514132> :dash:')
            await ctx.send('He fards')
        if lelbot_tasks_index == 32:
            await ctx.send(f'<:lelcube:811058465383514132>\n:blue_car:')
            await ctx.send('He drives a car')
        if lelbot_tasks_index == 33:
            await ctx.send(':boom: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
            await ctx.send('He commits war crimes')
        if lelbot_tasks_index == 34:
            await ctx.send(':wolf: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
            await ctx.send('He hunts')
        if lelbot_tasks_index == 35:
            await ctx.send(':cloud_rain:\n:umbrella:\n<:lelcube:811058465383514132>')
            await ctx.send('He is on rain')
        if lelbot_tasks_index == 36:
            await ctx.send('<:lelcube:811058465383514132>\n:sailboat: :island:')
            await ctx.send('He escapes island')
        if lelbot_tasks_index == 37:
            await ctx.send(':cooking: <:lelcube:811058465383514132>')
            await ctx.send('He cooks')
        if lelbot_tasks_index == 38:
            await ctx.send(':ping_pong: <:lelcube:811058465383514132>')
            await ctx.send('He plays ping pong')
        if lelbot_tasks_index == 39:
            await ctx.send(':guitar: <:lelcube:811058465383514132>')
            await ctx.send('He plays guitar')
        if lelbot_tasks_index == 40:
            await ctx.send('<:blushing:821505454361935902> :heart: <:lelcube:811058465383514132>')
            await ctx.send('He finds love')
        if lelbot_tasks_index == 41:
            await ctx.send(':desktop: :hammer: <:lelcube:811058465383514132>')
            await ctx.send('He hacks')
        if lelbot_tasks_index == 42:
            await ctx.send(':telescope: <:lelcube:811058465383514132>')
            await ctx.send('He sees the space')
        if lelbot_tasks_index == 43:
            await ctx.send(':microscope: <:lelcube:811058465383514132>')
            await ctx.send('He finds the close ad button')
        if lelbot_tasks_index == 44:
            await ctx.send(':desktop: <:lelcube:811058465383514132>')
            await ctx.send('He works on the computer')
        if lelbot_tasks_index == 45:
            await ctx.send(':moneybag: <:lelcube:811058465383514132>')
            await ctx.send('He gets paid')
        if lelbot_tasks_index == 46:
            await ctx.send(':chart_with_upwards_trend: <:lelcube:811058465383514132>')
            await ctx.send('He stonks')
        if lelbot_tasks_index == 47:
            await ctx.send(':house_with_garden: :money_with_wings: <:lelcube:811058465383514132>')
            await ctx.send('He buys house')
        if lelbot_tasks_index == 48:
            await ctx.send('<:sweatsmile:811059266806480916> :gift: <:lelcube:811058465383514132>')
            await ctx.send('He gets gift')
        if lelbot_tasks_index == 49:
            await ctx.send('🥳 🥳 🥳 🥳 <:lelcube:811058465383514132> 🥳 🥳 🥳')
            await ctx.send('He goes to party')
        if lelbot_tasks_index == 50:
            await ctx.send(':airplane_departure: <:lelcube:811058465383514132>')
            await ctx.send('He flies')
        if lelbot_tasks_index == 51:
            await ctx.send(':book: <:lelcube:811058465383514132>')
            await ctx.send('He reads books')
        if lelbot_tasks_index == 52:
            await ctx.send(':mag: <:lelcube:811058465383514132>')
            await ctx.send('He searches')
        if lelbot_tasks_index == 53:
            await ctx.send(':broom: <:lelcube:811058465383514132>')
            await ctx.send('He does chores')
        if lelbot_tasks_index == 54:
            await ctx.send(':jack_o_lantern: :skull: <:lelcube:811058465383514132>')
            await ctx.send('He is on spooky month')
        if lelbot_tasks_index == 55:
            await ctx.send('<:maum1:778489567036178464> :gem: <:lelcube:811058465383514132> <:maum2:778489689014403072>')
            await ctx.send('He steals')
        if lelbot_tasks_index == 56:
            await ctx.send('<:lelcube:811058465383514132> :arrows_counterclockwise:')
            await ctx.send('He spins')
        if lelbot_tasks_index == 57:
            await ctx.send('<:lelcube:811058465383514132> :zzz:\n:bed:')
            await ctx.send('He sleeps')
        if lelbot_tasks_index == 58:
            await ctx.send('<:lelcube:811058465383514132>\n:bus:')
            await ctx.send('He is on a bus')
        if lelbot_tasks_index == 59:
            await ctx.send(':placard: <:lelcube:811058465383514132>')
            await ctx.send('He reads a sign')
        if lelbot_tasks_index == 60:
            await ctx.send(':bulb:\n<:lelcube:811058465383514132>')
            await ctx.send('He gets an idea')
        if lelbot_tasks_index == 61:
            await ctx.send(':watch: <:lelcube:811058465383514132>')
            await ctx.send('He watches a watch')
        if lelbot_tasks_index == 62:
            await ctx.send(':electric_plug: <:lelcube:811058465383514132>')
            await ctx.send('He starts his new time machine')
        if lelbot_tasks_index == 63:
            await ctx.send(':test_tube: <:lelcube:811058465383514132>')
            await ctx.send('He scientist')
        if lelbot_tasks_index == 64:
            await ctx.send('<:lelcube:811058465383514132>\n:couch:')
            await ctx.send('He is on a couch')
        if lelbot_tasks_index == 65:
            await ctx.send('He flipped the messages')
            await ctx.send(':level_slider: <:lelcube:811058465383514132>')

@client.command(aliases=['embed'])
async def embed2(ctx, *, embedsay):
    embedsay2 = embedsay.split('| ')

    if '| ' not in embedsay:
        await ctx.send(f'You need a `|`!\nExample: Title | Description')
    else:
        SASBED_embed=discord.Embed(title=f'{embedsay2[0]}', description=f'{embedsay2[1]}', color=0xFECC4D)
        SASBED_embed.set_footer(text=f'Embed by {ctx.message.author}')
        webhook = await ctx.channel.create_webhook(name="Lelbot webhook", reason=f"{ctx.author} used the embed command")
        msg = await webhook.send(embed=SASBED_embed, username=ctx.author.name, avatar_url=ctx.author.avatar_url)
        await webhook.delete()

@client.command()
async def math(ctx, *, expression:str):
    expression = "".join(filter(lambda i: i in "9876543210+-×÷^*/()", expression))
    expression = expression.replace("^", "**").replace("÷", "/").replace("×", "*")
    await ctx.reply(f"Math: {expression}\nResults: {float(eval(expression))}")

@client.command(aliases=['sweatsmile'])
async def sweatsmile2(ctx):
    sweatversions = ['The classic sweatsmile https://cdn.discordapp.com/attachments/805879110848348191/834176321722122260/sweatsmile.png',
                'SweatsmileX Blue by hellory4n: https://cdn.discordapp.com/attachments/805879110848348191/834176159851479041/sweatsmilexblue.png',
                'SweatsmileX by hellory4n: https://cdn.discordapp.com/attachments/805879110848348191/834176188699770901/sweatsmilex.png',
                'Sweatsmile HD Blue by hellory4n: https://cdn.discordapp.com/attachments/805879110848348191/834176229757157417/sweatsmileHDblue.png',
                'Sweatsmile HD by hellory4n: https://cdn.discordapp.com/attachments/805879110848348191/834176256786432080/sweatsmileHD.png',
                'Sweatsmile blue: https://cdn.discordapp.com/attachments/805879110848348191/834176285776936960/sweatsmileblue.png',
                'Sweatcookie by TheXtremeCrafter: https://cdn.discordapp.com/attachments/805879110848348191/834176362716987405/sweatcookie.png',
                'Squaresmile by Rubi: https://cdn.discordapp.com/attachments/805879110848348191/834176392303214612/squaresmile.png',
                'Lelcube by hellory4n: https://cdn.discordapp.com/attachments/805879110848348191/834176440970772510/lelcubie.png',
                'Lelbot by hellory4n: https://cdn.discordapp.com/attachments/805879110848348191/834176485567758336/lelbot.png',
                'elimstaewS: https://cdn.discordapp.com/attachments/805879110848348191/834176565994192966/elimstaews.png',
                'Choccy Sweat by SrMuffin136: https://cdn.discordapp.com/attachments/833534015755517965/834178902834413578/Tak_berjudul91_20210414114335.png',
                'Blocksmile by hellory4n: https://cdn.discordapp.com/attachments/833532807531331606/833550167881547817/sketch-1618796790604.png',
                'Sweatbutton by hellory4n: https://cdn.discordapp.com/attachments/833532807531331606/833735786524180520/sweatbutton.gif',
                'Longsweat by hellory4n: https://cdn.discordapp.com/attachments/833532807531331606/833766604009242664/longsweat.png',
                'Drive Sweat by hellory4n: https://cdn.discordapp.com/attachments/833532807531331606/833771226504888340/drivesweat.png',
                'SweatKing by SrMuffin136: https://cdn.discordapp.com/attachments/833532807531331606/834178265702203422/1618953954517.png',
                'Sweatxie by Nextie: https://cdn.discordapp.com/attachments/833532807531331606/834179515613839411/Untitled4_20210421003117.png']

    await ctx.send(f'{random.choice(sweatversions)}')

@client.command()
async def house(ctx):
    HOUSEthings = ['<:table:834902103172055051>',
                '<:chest:834909482143318056>',
                '<:void:834904392008335360>',
                '<:Hello_OwO:822546151010074694>',
                ':sandwich:']
    
    await ctx.send(f'<:wall:834902110168416278><:wall:834902110168416278><:wall:834902110168416278><:wall:834902110168416278><:wall:834902110168416278><:wall:834902110168416278>\n<:wall:834902110168416278><:void:834904392008335360><:void:834904392008335360><:void:834904392008335360><:void:834904392008335360><:wall:834902110168416278>\n<:wall:834902110168416278>{random.choice(HOUSEthings)}{random.choice(HOUSEthings)}{random.choice(HOUSEthings)}{random.choice(HOUSEthings)}<:wall:834902110168416278>')

@client.command()
async def everyone(ctx, *, everyoni):
    if '@everyone' in everyoni or '@here' in everyoni:
        await ctx.send(f'{ctx.author.mention} no mass ping here >:c')
    else:
        await ctx.send(f'{ctx.message.author} {everyoni}')

@client.command()
async def hidden(ctx):
    await ctx.send(f'```These are the hidden/unused commands:\nl!house - terrible command\nl!everyone <text> - command to test the "dont make mass ping when theres everyone on command" thing```')

@client.command()
async def randnum(ctx, num1, num2):
    await ctx.send(f':game_die: {random.randint(int(num1), int(num2))}')

@client.command(aliases=['bobux'])
async def bobux2(ctx):
    BOBUX1 = ['b','*b*','**b**','***b***','__b__','__*b*__','__**b**__','__***b***__','B','*B*','**B**','***B***','__B__','__*B*__','__**B**__','__***B***__']
    BOBUX2 = ['o','*o*','**o**','***o***','__o__','__*o*__','__**o**__','__***o***__','O','*O*','**O**','***O***','__O__','__*O*__','__**O**__','__***O***__']
    BOBUX3 = ['u','*u*','**u**','***u***','__u__','__*u*__','__**u**__','__***u***__','U','*U*','**U**','***U***','__U__','__*U*__','__**U**__','__***U***__']
    BOBUX4 = ['x','*x*','**x**','***x***','__x__','__*x*__','__**x**__','__***x***__','X','*X*','**X**','***X***','__X__','__*X*__','__**X**__','__***X***__']

    await ctx.send(f'{random.choice(BOBUX1)} {random.choice(BOBUX2)} {random.choice(BOBUX1)} {random.choice(BOBUX3)} {random.choice(BOBUX4)}')

def lelnum_save():
    with open(lelnum_filename, 'w') as lelnum_file:
        json.dump(lelnums, lelnum_file)

@client.command()
async def set_num(ctx, lelnum_input):
    lelnums[str(ctx.author.id)] = {'num by ' + str(ctx.message.author): str(lelnum_input)}
    lelnum_save()
    await ctx.send(f'done!')

@client.command()
async def all_nums(ctx):
    file = open(lelnum_filename)
    data = json.load(file)

    await ctx.send(f'i know, this is weird, im just too lazy to make this more butiful <:sweatsmile:811059266806480916>')
    await ctx.send(data)
    
    file.close()

@client.command()
async def my_num(ctx):
    file = open(lelnum_filename)
    data = json.load(file)

    await ctx.send(f'{ctx.author.mention} your number is {data[ctx.author.id]}')

    file.close()

@inter_client.slash_command(description="Says \"/\" for no reason lol (why i even added this)")
async def slash(inter):
    await inter.reply("/")

@inter_client.slash_command(description="Pong :)")
async def ping(inter):
    await inter.reply(f"{inter.author.mention} :ping_pong: Pong! {round(client.latency * 1000)}ms")

@inter_client.slash_command(description="Get an answer to a random question", options=[Option('question', 'Ask a question :)', OptionType.STRING, required=True)])
async def eightball(inter, question="yes"):
    options = ['yes', 'probably yes', 'yes?', 'definitely', 'idk lol', 'Hi', 'no', 'probably not', 'no?', 'definitely not']
    embed=discord.Embed(title=question, description=f'{random.choice(options)}', color=0xFECC4D)
    embed.set_footer(text=inter.author.id)
    await inter.reply(embed=embed)

@inter_client.slash_command(description="The good old help command")
async def help(inter):
    embed = discord.Embed(title="Help", description="\n`<>` means required argument, `[]` means optional argument\nDon't include `<>` or `[]`\nMost commands are available in slash commands!", color=0xFECC4D)
    embed.add_field(name="Very random", value="`bobux`, `dostuff [index]`, `hello [something]`, `morecookis`, `randomsandwich`, `randomstory`, `sandwich <size>`, `name`", inline=False)
    embed.add_field(name="Random", value="`bam <someone>`, `boom <something>`, `fact [index]`, `hack <something>`, `sweatsmile`, `yesorno <question>`, `chat <something>`, `sentence`, `who <someone>`", inline=False)
    embed.add_field(name="Not so random", value="`attack <someone>`, `hug <someone>`, `say <something>`, `8ball <question>`, `when <question>`, `weirdtext`, `text_to_wotcode`, `wotcode_to_text`", inline=False)
    embed.add_field(name="Economy",value="`work`, `bal [user]`, `dep <amount>`, `with <amount>`, `lb`, `shop`, `buy [amount]`, `inv [user]`, `use [amount]`, `give_money <user> <amount>`, `reset_money`, `give_item <user> <amount>`, `rob <user> <amount>`")
    embed.add_field(name="Bot stuff", value="`ping`, `invite`, `aboutme`, `server`, `help`, `classic_help`", inline=False)
    embed.add_field(name="Stuff that isn't really for fun", value="`embed <title> | <description>`, `math <expression>`, `poll <text>`, `randnum <min> <max>`, `suggest <suggestion>`, `roll`", inline=False)
    await inter.reply(embed=embed)

@inter_client.slash_command(description="Chat with lelbot! But, his replies won't make any sense! Best idea!", options=[Option('message', 'Message :thumbsup:', OptionType.STRING, required=True)])
async def chat(inter):
    chatresponses = ['njfk',
                'Ye',
                'Okie',
                'Okay',
                'Oke',
                'OISUGIAEODFIJUHYSEIUODUGY',
                'nice',
                'oh noes!',
                'me too!',
                'ooh',
                'ok, but i have the ~~worst~~ best ai',
                'i don\'t like lolbot',
                'sandwich. **sandwich...** SANDWICH!!!!!!! GIMME SANDWICH!!!!',
                'OwO',
                'UwU',
                'a?',
                'h']
    await inter.reply(random.choice(chatresponses))

@inter_client.slash_command(description="Create a butiful story.")
async def randomstory(inter):
    storywords = ['in',
                'a',
                'random',
                'village',
                '.',
                'that',
                'will',
                'be',
                'walking',
                'on',
                'cliffside',
                'little',
                'man',
                'called',
                'lelbot',
                'has',
                'builder',
                'friend',
                'for',
                'the',
                'leader',
                'of',
                'where',
                'magic',
                'happens',
                'then',
                'it',
                'goes',
                'to',
                'so',
                'banana',
                'walked',
                'potatopatata']
    
    await inter.reply(f'*{random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)}*')

@inter_client.slash_command(description="Ask when something will happen", options=[Option('question', 'yes', OptionType.STRING, required=True)])
async def when(inter):
    whentype = random.randint(1,8)

    if whentype == 1:
        await inter.reply(f'After {random.randint(1,60)} seconds.')
    if whentype == 2:
        await inter.reply(f'After {random.randint(1,60)} minutes.')
    if whentype == 3:
        await inter.reply(f'After {random.randint(1,24)} hours.')
    if whentype == 4:
        await inter.reply(f'After {random.randint(1,31)} days.')
    if whentype == 5:
        await inter.reply(f'After {random.randint(1,12)} months.')
    if whentype == 6:
        await inter.reply(f'After {random.randint(1,100)} years.')
    if whentype == 7:
        await inter.reply(f'After {random.randint(1,10000)} milleniums.')
    if whentype == 8:
        await inter.reply(f'After {random.randint(1,100000000000000000)} milleniums... That\'s too much!')

@inter_client.slash_command(description="I don't know what i can put here :D", options=[Option('question','ahbgjivker', OptionType.STRING, required=True)])
async def yesorno(inter, question):
    helloyesorno = ['https://media.discordapp.net/attachments/806308041115959377/911742147655508038/hellono_but_big.png',
            'https://media.discordapp.net/attachments/806308041115959377/911742147999445052/helloyes_but_big.png']
    embed=discord.Embed(title=question, description="", color=0xFECC4D)
    embed.set_footer(text=inter.author.id)
    embed.set_image(url=random.choice(helloyesorno))
    await inter.reply(embed=embed)

@inter_client.slash_command(description="Make lelbot say something", options=[Option('message', 'message lol', OptionType.STRING, required=True)])
async def say(inter, message):
    await inter.reply(f"{message}\n\n**- {inter.author} ({inter.author.id})**", allowed_mentions = discord.AllowedMentions(everyone = False))

@inter_client.slash_command(description="Hug someone :)", options=[Option('someone','uwu', OptionType.STRING)])
async def hug(inter, someone="**literally no one**"):
    await inter.reply(f"{inter.author.mention} hugged {someone}! <:Hello_UwU:822546152402321428>", allowed_mentions = discord.AllowedMentions(everyone = False))

@inter_client.slash_command(description="Attack someone :)", options=[Option('someone','unu', OptionType.STRING)])
async def attack(inter, someone="**literally no one**"):
    await inter.reply(f"{inter.author.mention} attacked {someone}! <:Gun:816099538619072553> <:Hello_Angry:822546148534386699>", allowed_mentions = discord.AllowedMentions(everyone = False))

@inter_client.slash_command(description="Bam someone!", options=[Option('someone','>:c', OptionType.STRING, required=True), Option('reason','Why you want to bam someone',OptionType.STRING)])
async def bam(inter, someone, reason='None'):
    await inter.reply(f"{someone} has (not) been banned by {inter.author.mention} (Reason: {reason})")

@inter_client.slash_command(description="Explode something!", options=[Option('something', 'Yes', OptionType.STRING, required=True)])
async def boom(inter, something):
    embed=discord.Embed(title="Boom!", description=f'{something} exploded!\nDamage: {random.randint(1,100)}', color=0xFECC4D)
    embed.set_footer(text=f'Exploded by {inter.author}')
    await inter.reply(embed=embed)

@inter_client.slash_command(description="Hackn't something!", options=[Option('something','hejusidghjk',OptionType.STRING,required=True)])
async def hack(inter, something):
    yo = await inter.reply(f"Getting access to {something}...")
    await asyncio.sleep(5)
    await yo.edit(content=f"Found email! ({something}{str(random.randint(10000000,99999999))}@lelmail.com)")
    await asyncio.sleep(2.5)
    await yo.edit(content="Found emojis from their phone cuz why not <:lelcube:811058465383514132>")
    await asyncio.sleep(3)
    await yo.edit(content="Drinking coffee... :coffee:")
    await asyncio.sleep(3.1)
    await yo.edit(content="Exploding my own database lol <:lelcube:811058465383514132>")
    await asyncio.sleep(4)
    await yo.edit(content="Selling their data to a random person...")
    await asyncio.sleep(3.5)
    await yo.edit(content=f"{inter.author.mention} Hacked {something} successfully!")

@inter_client.slash_command(description="Get a random sandwich lol")
async def randomsandwich(inter):
    randsandwich = ['sandwich',
                'sandwich OwO',
                'sandwich UwU',
                'sandwich 2',
                'fanmade sandwich',
                'super sandwich',
                'coolio sandwich',
                'sandwich god',
                'sandwich EEEEEEEE',
                'sandwich plus',
                'big sandwich',
                'tiny sandwich',
                'normal sandwich',
                'sandwich fans',
                'sandwich 95',
                'sandwich speed',
                'sandwich 98',
                'sandwich 2000',
                'sandwich 2009',
                'sandwich 2012',
                'sandwich 10',
                'next sandwich',
                'sandwich hd',
                'retro sandwich',
                'sandwich pro',
                'sandwich gold',
                'sandwich spam',
                'sandwich online',
                'sandwich x',
                'sandwich xl',
                'sandwich xz',
                'free sandwich',
                'sandwich multiplayer',
                'sandwich cube',
                'sandwich ball',
                'sandwich ooooooo',
                'sandwich smart',
                'sandwich camera',
                'sandwich light',
                'sandwich stop']
    await inter.reply(f'You got... **{random.choice(randsandwich)}**!')

@inter_client.slash_command(description="Make a cook poll", options=[Option('text','Text :D',OptionType.STRING,required=True), Option('option1','Don\'t include an emoji here',OptionType.STRING,required=True), Option('option2','Don\'t include an emoji here²',OptionType.STRING,required=True)])
async def poll(inter, text, option1, option2):
    embed=discord.Embed(title=text, description=f':one: = {option1}\n:two: = {option2}', colot=0xFECC4D)
    embed.set_footer(text=f'Poll by {inter.author} ({inter.author.id})')
    Poll = await inter.reply(embed=embed)
    await Poll.add_reaction('1️⃣')
    await Poll.add_reaction('2️⃣')

@inter_client.slash_command(description="Suggest something, nice", options=[Option('suggestion','text lol',OptionType.STRING,required=True)])
async def suggest(inter, suggestion):
    embed=discord.Embed(title=f"{inter.author} suggestion", description=suggestion, color=0xFECC4D)
    embed.set_footer(text=inter.author.id)
    msg = await inter.reply(embed=embed)
    await msg.add_reaction('✅')
    await msg.add_reaction('❎')
    await msg.add_reaction('🤔')
    await msg.add_reaction('❓')

@inter_client.slash_command(description="A weird text")
async def weirdtext(inter):
    a_lot_of_characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    await inter.reply(f'{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}')

@inter_client.slash_command(description="See lelcube doing a random task",options=[Option("index","If you don't put anything here, the index will be random",OptionType.INTEGER,required=False)])
async def dostuff(ctx,index="random"):
    no_NOOOOO = False
    
    try:
        int_index = int(index)
    except:
        index = "random"

    if index == "random":
        lelbot_tasks_index = random.randint(1,65)
        no_NOOOOO = True
    else:
        if int_index < 1 or int_index > 65:
            await ctx.send("Invalid index! Please enter something between 1 and 65.")
        else:
            lelbot_tasks_index = int_index
            no_NOOOOO = True

    #choices = [':microphone2: <:lelcube:811058465383514132>&&He sings',':frame_photo: :paintbrush: <:lelcube:811058465383514132>&&He paints',':computer: <:lelcube:811058465383514132>&&He codes',':video_game: <:lelcube:811058465383514132>&&He play games',':potato: <:Gun:816099538619072553> <:lelcube:811058465383514132>',':tv: <:lelcube:811058465383514132>&&He watches tv',':hammer: <:lelcube:811058465383514132>&&He destroy stuff',':shower:\n<:lelcube:811058465383514132>&&He showers','<:lelcube:811058465383514132> :shopping_cart:&&He goes shopping',':balloon: <:lelcube:811058465383514132>&&He plays with balloon',':wastebasket: :newspaper2: <:lelcube:811058465383514132>&&He doesnt like to read cuz reading is boring and i just noticed that to use discord you have to read which is boring so technicly using discord is boring but is not eeeeeeeeeeeee',':video_camera: <:lelcube:811058465383514132>&&He records a video',':pencil: <:lelcube:811058465383514132>&&He writes a text','<:Nextie:835598971518189621> :mag: <:lelcube:811058465383514132>&&He is trying to see nextie *but nextie has the size of a __pixel__*','<:lelcube:811058465383514132> :loudspeaker:&&He says potatopatata very loud',':cake: :fork_and_knife: <:lelcube:811058465383514132>&&He eats a cake',':iphone: <:lelcube:811058465383514132>&&He uses the phone',':pizza: <:lelcube:811058465383514132>&&He is 101% sure that pizza is pizza','<:clapping:811058070843162686> <:lelcube:811058465383514132>&&He claps','<:lelcube:811058465383514132> :vs: <:sweatsmile:811059266806480916>&&He fights',':telephone_receiver: <:lelcube:811058465383514132>&&He calls people','<:lelcube:811058465383514132> :tent:&&He goes camping',':ballet_shoes: <:lelcube:811058465383514132>&&He uses a ballet shoes','<:lelcube:811058465383514132> :toothbrush: :toilet:&&He uses a ballet shoes',':tophat:\n<:lelcube:811058465383514132> :magic_wand:&&He magic man',':saxophone: <:lelcube:811058465383514132>&&He plays the saxophone cuz saxophones are cool','<:lelcube:811058465383514132> ']
    if no_NOOOOO == True:
        if lelbot_tasks_index == 1:
            await ctx.send(f'🎙 <:lelcube:811058465383514132>')
            await ctx.send(f'He sings')
        if lelbot_tasks_index == 2:
            await ctx.send(f':frame_photo: :paintbrush: <:lelcube:811058465383514132>')
            await ctx.send(f'He paints')
        if lelbot_tasks_index == 3:
            await ctx.send(f':computer: <:lelcube:811058465383514132>')
            await ctx.send(f'He codes')
        if lelbot_tasks_index == 4:
            await ctx.send(f':video_game: <:lelcube:811058465383514132>')
            await ctx.send(f'He play games')
        if lelbot_tasks_index == 5:
            await ctx.send(f':potato: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
            await ctx.send(f'He kills potatos')
        if lelbot_tasks_index == 6:
            await ctx.send(f':tv: <:lelcube:811058465383514132>')
            await ctx.send(f'He watches tv')
        if lelbot_tasks_index == 7:
            await ctx.send(f':hammer: <:lelcube:811058465383514132>')
            await ctx.send(f'He destroy stuff')
        if lelbot_tasks_index == 8:
            await ctx.send(f':shower:\n<:lelcube:811058465383514132>')
            await ctx.send(f'He showers')
        if lelbot_tasks_index == 9:
            await ctx.send(f'<:lelcube:811058465383514132> :shopping_cart:')
            await ctx.send(f'He goes shopping')
        if lelbot_tasks_index == 10:
            await ctx.send(f':balloon: <:lelcube:811058465383514132>')
            await ctx.send(f'He plays with balloon')
        if lelbot_tasks_index == 11:
            await ctx.send(f':wastebasket: :newspaper2: <:lelcube:811058465383514132>')
            await ctx.send(f'He doesnt like to read cuz reading is boring and i just noticed that to use discord you have to read which is boring so technicly using discord is boring but is not eeeeeeeeeeeee')
        if lelbot_tasks_index == 12:
            await ctx.send(f':video_camera: <:lelcube:811058465383514132>')
            await ctx.send(f'He records a video')
        if lelbot_tasks_index == 13:
            await ctx.send(f':pencil: <:lelcube:811058465383514132>')
            await ctx.send(f'He writes a text')
        if lelbot_tasks_index == 14:
            await ctx.send(f'<:Nextie:835598971518189621> :mag: <:lelcube:811058465383514132>')
            worstjokeever = await ctx.send(f'He is trying to see nextie *but nextie have the size of a __pixel__*')
            await worstjokeever.add_reaction('<:bassrolf:821948606701371462>')
        if lelbot_tasks_index == 15:
            await ctx.send(f'<:lelcube:811058465383514132> :loudspeaker:')
            await ctx.send(f'He says potatopatata very loud')
        if lelbot_tasks_index == 16:
            await ctx.send(f':cake: :fork_and_knife: <:lelcube:811058465383514132>')
            await ctx.send(f'He eats a cake')
        if lelbot_tasks_index == 17:
            await ctx.send(f':iphone: <:lelcube:811058465383514132>')
            await ctx.send(f'He uses the phone')
        if lelbot_tasks_index == 18:
            await ctx.send(f':pizza: <:lelcube:811058465383514132>')
            await ctx.send(f'He is 101% sure that pizza is pizza')
        if lelbot_tasks_index == 19:
            await ctx.send(f'<:clapping:811058070843162686> <:lelcube:811058465383514132>')
            await ctx.send(f'He claps')
        if lelbot_tasks_index == 20:
            await ctx.send(f'<:lelcube:811058465383514132> :vs: <:sweatsmile:811059266806480916>')
            await ctx.send(f'He fights')
        if lelbot_tasks_index == 21:
            await ctx.send(f':telephone_receiver: <:lelcube:811058465383514132>')
            await ctx.send(f'He calls people')
        if lelbot_tasks_index == 22:
            await ctx.send(f'<:lelcube:811058465383514132> :tent:')
            await ctx.send(f'He goes camping')
        if lelbot_tasks_index == 23:
            await ctx.send(f':ballet_shoes: <:lelcube:811058465383514132>')
            await ctx.send(f'He uses a ballet shoes')
        if lelbot_tasks_index == 24:
            await ctx.send(f'<:lelcube:811058465383514132> :toothbrush: :toilet:')
            await ctx.send(f'He clean the toilet')
        if lelbot_tasks_index == 25:
            await ctx.send(f":tophat:\n<:lelcube:811058465383514132> :magic_wand:")
            await ctx.send(f'He magic man')
        if lelbot_tasks_index == 26:
            await ctx.send(f':saxophone: <:lelcube:811058465383514132>')
            await ctx.send(f'He plays the saxophone cuz saxophones are cool')
        if lelbot_tasks_index == 27:
            await ctx.send(f'<:lelcube:811058465383514132> <:okhand:811059019828428821>')
            await ctx.send(f'He likes *something*')
        if lelbot_tasks_index == 28:
            await ctx.send(f'<:sweatwide1:818622702574632970><:lelcube:811058465383514132><:sweatwide2:818622715815526481>')
            await ctx.send(f'He uses a disguise')
        if lelbot_tasks_index == 29:
            await ctx.send(f':sweat_smile: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
            await ctx.send(f'He kills')
        if lelbot_tasks_index == 30:
            await ctx.send(f'<:maum1:778489567036178464> <:lelcube:811058465383514132> <:maum2:778489689014403072>')
            await ctx.send(f'He will catch you')
        if lelbot_tasks_index == 31:
            await ctx.send(f'<:lelcube:811058465383514132> :dash:')
            await ctx.send('He fards')
        if lelbot_tasks_index == 32:
            await ctx.send(f'<:lelcube:811058465383514132>\n:blue_car:')
            await ctx.send('He drives a car')
        if lelbot_tasks_index == 33:
            await ctx.send(':boom: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
            await ctx.send('He commits war crimes')
        if lelbot_tasks_index == 34:
            await ctx.send(':wolf: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
            await ctx.send('He hunts')
        if lelbot_tasks_index == 35:
            await ctx.send(':cloud_rain:\n:umbrella:\n<:lelcube:811058465383514132>')
            await ctx.send('He is on rain')
        if lelbot_tasks_index == 36:
            await ctx.send('<:lelcube:811058465383514132>\n:sailboat: :island:')
            await ctx.send('He escapes island')
        if lelbot_tasks_index == 37:
            await ctx.send(':cooking: <:lelcube:811058465383514132>')
            await ctx.send('He cooks')
        if lelbot_tasks_index == 38:
            await ctx.send(':ping_pong: <:lelcube:811058465383514132>')
            await ctx.send('He plays ping pong')
        if lelbot_tasks_index == 39:
            await ctx.send(':guitar: <:lelcube:811058465383514132>')
            await ctx.send('He plays guitar')
        if lelbot_tasks_index == 40:
            await ctx.send('<:blushing:821505454361935902> :heart: <:lelcube:811058465383514132>')
            await ctx.send('He finds love')
        if lelbot_tasks_index == 41:
            await ctx.send(':desktop: :hammer: <:lelcube:811058465383514132>')
            await ctx.send('He hacks')
        if lelbot_tasks_index == 42:
            await ctx.send(':telescope: <:lelcube:811058465383514132>')
            await ctx.send('He sees the space')
        if lelbot_tasks_index == 43:
            await ctx.send(':microscope: <:lelcube:811058465383514132>')
            await ctx.send('He finds the close ad button')
        if lelbot_tasks_index == 44:
            await ctx.send(':desktop: <:lelcube:811058465383514132>')
            await ctx.send('He works on the computer')
        if lelbot_tasks_index == 45:
            await ctx.send(':moneybag: <:lelcube:811058465383514132>')
            await ctx.send('He gets paid')
        if lelbot_tasks_index == 46:
            await ctx.send(':chart_with_upwards_trend: <:lelcube:811058465383514132>')
            await ctx.send('He stonks')
        if lelbot_tasks_index == 47:
            await ctx.send(':house_with_garden: :money_with_wings: <:lelcube:811058465383514132>')
            await ctx.send('He buys house')
        if lelbot_tasks_index == 48:
            await ctx.send('<:sweatsmile:811059266806480916> :gift: <:lelcube:811058465383514132>')
            await ctx.send('He gets gift')
        if lelbot_tasks_index == 49:
            await ctx.send('🥳 🥳 🥳 🥳 <:lelcube:811058465383514132> 🥳 🥳 🥳')
            await ctx.send('He goes to party')
        if lelbot_tasks_index == 50:
            await ctx.send(':airplane_departure: <:lelcube:811058465383514132>')
            await ctx.send('He flies')
        if lelbot_tasks_index == 51:
            await ctx.send(':book: <:lelcube:811058465383514132>')
            await ctx.send('He reads books')
        if lelbot_tasks_index == 52:
            await ctx.send(':mag: <:lelcube:811058465383514132>')
            await ctx.send('He searches')
        if lelbot_tasks_index == 53:
            await ctx.send(':broom: <:lelcube:811058465383514132>')
            await ctx.send('He does chores')
        if lelbot_tasks_index == 54:
            await ctx.send(':jack_o_lantern: :skull: <:lelcube:811058465383514132>')
            await ctx.send('He is on spooky month')
        if lelbot_tasks_index == 55:
            await ctx.send('<:maum1:778489567036178464> :gem: <:lelcube:811058465383514132> <:maum2:778489689014403072>')
            await ctx.send('He steals')
        if lelbot_tasks_index == 56:
            await ctx.send('<:lelcube:811058465383514132> :arrows_counterclockwise:')
            await ctx.send('He spins')
        if lelbot_tasks_index == 57:
            await ctx.send('<:lelcube:811058465383514132> :zzz:\n:bed:')
            await ctx.send('He sleeps')
        if lelbot_tasks_index == 58:
            await ctx.send('<:lelcube:811058465383514132>\n:bus:')
            await ctx.send('He is on a bus')
        if lelbot_tasks_index == 59:
            await ctx.send(':placard: <:lelcube:811058465383514132>')
            await ctx.send('He reads a sign')
        if lelbot_tasks_index == 60:
            await ctx.send(':bulb:\n<:lelcube:811058465383514132>')
            await ctx.send('He gets an idea')
        if lelbot_tasks_index == 61:
            await ctx.send(':watch: <:lelcube:811058465383514132>')
            await ctx.send('He watches a watch')
        if lelbot_tasks_index == 62:
            await ctx.send(':electric_plug: <:lelcube:811058465383514132>')
            await ctx.send('He starts his new time machine')
        if lelbot_tasks_index == 63:
            await ctx.send(':test_tube: <:lelcube:811058465383514132>')
            await ctx.send('He scientist')
        if lelbot_tasks_index == 64:
            await ctx.send('<:lelcube:811058465383514132>\n:couch:')
            await ctx.send('He is on a couch')
        if lelbot_tasks_index == 65:
            await ctx.send('He flipped the messages')
            await ctx.send(':level_slider: <:lelcube:811058465383514132>')

@inter_client.slash_command(description="Builds a custom embed", options=[Option('title', 'Embed title', OptionType.STRING, required=True),Option('description', 'Embed description', OptionType.STRING,required=True),Option('color', 'Embed color', OptionType.STRING),Option('footer','Embed footer',OptionType.STRING),Option('url','Embed image url',OptionType.STRING)])
async def embed(inter, title, description, color=0xFECC4D, footer="Super cook embed", url=None):
    if color != 0xFECC4D:
        try:
            color = await commands.ColorConverter().convert(inter, color)
        except:
            color = await commands.ColorConverter().convert(inter, color)
    if color is None:
        color = discord.Color.default()
    embed=discord.Embed(title=title, description=description, color=color)
    embed.set_footer(text=f"{footer} • {inter.author} ({inter.author.id})")
    if url is not None:
        embed.set_image(url=url)
    webhook = await inter.channel.create_webhook(name="Lelbot webhook", reason=f"{inter.author} used the embed command")
    await webhook.send(embed=embed, username=inter.author.name, avatar_url=inter.author.avatar_url)
    await webhook.delete()
    await inter.reply("Posted embed!", ephemeral=True)

@inter_client.slash_command(description="Get a random sweatsmile")
async def sweatsmile(inter):
    sweatversions = ['The classic sweatsmile https://cdn.discordapp.com/attachments/805879110848348191/834176321722122260/sweatsmile.png',
                'SweatsmileX Blue by hellory4n: https://cdn.discordapp.com/attachments/805879110848348191/834176159851479041/sweatsmilexblue.png',
                'SweatsmileX by hellory4n: https://cdn.discordapp.com/attachments/805879110848348191/834176188699770901/sweatsmilex.png',
                'Sweatsmile HD Blue by hellory4n: https://cdn.discordapp.com/attachments/805879110848348191/834176229757157417/sweatsmileHDblue.png',
                'Sweatsmile HD by hellory4n: https://cdn.discordapp.com/attachments/805879110848348191/834176256786432080/sweatsmileHD.png',
                'Sweatsmile blue: https://cdn.discordapp.com/attachments/805879110848348191/834176285776936960/sweatsmileblue.png',
                'Sweatcookie by TheXtremeCrafter: https://cdn.discordapp.com/attachments/805879110848348191/834176362716987405/sweatcookie.png',
                'Squaresmile by Rubi: https://cdn.discordapp.com/attachments/805879110848348191/834176392303214612/squaresmile.png',
                'Lelcube by hellory4n: https://cdn.discordapp.com/attachments/805879110848348191/834176440970772510/lelcubie.png',
                'Lelbot by hellory4n: https://cdn.discordapp.com/attachments/805879110848348191/834176485567758336/lelbot.png',
                'elimstaewS: https://cdn.discordapp.com/attachments/805879110848348191/834176565994192966/elimstaews.png',
                'Choccy Sweat by SrMuffin136: https://cdn.discordapp.com/attachments/833534015755517965/834178902834413578/Tak_berjudul91_20210414114335.png',
                'Blocksmile by hellory4n: https://cdn.discordapp.com/attachments/833532807531331606/833550167881547817/sketch-1618796790604.png',
                'Sweatbutton by hellory4n: https://cdn.discordapp.com/attachments/833532807531331606/833735786524180520/sweatbutton.gif',
                'Longsweat by hellory4n: https://cdn.discordapp.com/attachments/833532807531331606/833766604009242664/longsweat.png',
                'Drive Sweat by hellory4n: https://cdn.discordapp.com/attachments/833532807531331606/833771226504888340/drivesweat.png',
                'SweatKing by SrMuffin136: https://cdn.discordapp.com/attachments/833532807531331606/834178265702203422/1618953954517.png',
                'Sweatxie by Nextie: https://cdn.discordapp.com/attachments/833532807531331606/834179515613839411/Untitled4_20210421003117.png']
    await inter.reply(random.choice(sweatversions))

@inter_client.slash_command(description="Get a random number", options=[Option('min','min',OptionType.INTEGER,required=True),Option('max','max',OptionType.INTEGER,required=True)])
async def random_number(inter, min, max):
    await inter.reply(str(random.randint(min,max)))

@inter_client.slash_command(description="i don't know anymore")
async def bobux(inter):
    BOBUX1 = ['b','*b*','**b**','***b***','__b__','__*b*__','__**b**__','__***b***__','B','*B*','**B**','***B***','__B__','__*B*__','__**B**__','__***B***__']
    BOBUX2 = ['o','*o*','**o**','***o***','__o__','__*o*__','__**o**__','__***o***__','O','*O*','**O**','***O***','__O__','__*O*__','__**O**__','__***O***__']
    BOBUX3 = ['u','*u*','**u**','***u***','__u__','__*u*__','__**u**__','__***u***__','U','*U*','**U**','***U***','__U__','__*U*__','__**U**__','__***U***__']
    BOBUX4 = ['x','*x*','**x**','***x***','__x__','__*x*__','__**x**__','__***x***__','X','*X*','**X**','***X***','__X__','__*X*__','__**X**__','__***X***__']

    await inter.reply(f'{random.choice(BOBUX1)} {random.choice(BOBUX2)} {random.choice(BOBUX1)} {random.choice(BOBUX3)} {random.choice(BOBUX4)}')

@inter_client.slash_command(description="Get a random hello version", options=[Option('someone','e',OptionType.STRING)])
async def hello(inter, someone=""):
    hello = ["Hello", "Hi", "Helo", "Henlo", "Yo", "Hellooo", "Helooo", "Henlooo", "Hi hello", "Hello hi", "Hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo", "***Hej***", "Hola", "Hewwo"]
    await inter.reply(f"{random.choice(hello)} {someone}")

@inter_client.slash_command(description="Get the bot invite!")
async def invite(inter):
    embed = discord.Embed(title="Invite", description="Click [here](https://discord.com/api/oauth2/authorize?client_id=822199023636709456&permissions=8&scope=bot%20applications.commands) to invite lelbot on your cook server!", color=0xFECC4D)
    embed.set_footer(text=":)")
    await inter.reply(embed=embed)

@inter_client.slash_command(description="About me 😉")
async def aboutme(inter):
    ABOTME_embed=discord.Embed(title=f'About lelbot', description=f"Hello! I'm lelbot, the smartest AI in the universe, created by hellory5n, a very evil guy with very dumb plans!\nBy the way this is hellory5n: <:hellory5n:915028960604200982>", color=0xFECC4D)
    ABOTME_embed.set_footer(text="Version 1.3.1")
    ABOTME_embed.add_field(name="Credits",value="Developed by hellory4n\nMany facts from `fact`: The credits are in the command itself\nArnold cooki ad from super snowman item: JustYellow\nThanks for using me!",inline=False)
    await inter.send(embed=ABOTME_embed)

@client.command(aliases=['morecookis','morecookies'])
async def morecookis2(ctx):
    with open('cookis.txt','r') as f:
        txt = f.read()
    cookis = int(txt) + 1
    with open('cookis.txt','w') as f:
        f.write(str(cookis))
    
    if cookis == 69 or cookis == 420:
        ok = "(nice)"
    elif cookis == 100 or cookis == 200 or cookis == 300 or cookis == 400 or cookis == 500 or cookis == 600 or cookis == 700 or cookis == 800 or cookis == 900:
        ok = "(wowww!)"
    elif cookis == 1000 or cookis == 2000 or cookis == 3000 or cookis == 4000 or cookis == 5000 or cookis == 6000 or cookis == 7000 or cookis == 8000 or cookis == 9000:
        ok = "(oh ma gawd!)"
    else:
        ok = ""

    await ctx.send(f'Now we have **{str(cookis)}** cookis! :cookie: {ok}')

@inter_client.slash_command(description="Increase a cooki counter!")
async def morecookis(inter):
    with open('cookis.txt','r') as f:
        txt = f.read()
    cookis = int(txt) + 1
    with open('cookis.txt','w') as f:
        f.write(str(cookis))
    
    if cookis == 69 or cookis == 420:
        ok = "(nice)"
    elif cookis == 100 or cookis == 200 or cookis == 300 or cookis == 400 or cookis == 500 or cookis == 600 or cookis == 700 or cookis == 800 or cookis == 900:
        ok = "(wowww!)"
    elif cookis == 1000 or cookis == 2000 or cookis == 3000 or cookis == 4000 or cookis == 5000 or cookis == 6000 or cookis == 7000 or cookis == 8000 or cookis == 9000:
        ok = "(oh ma gawd!)"
    else:
        ok = ""

    await inter.reply(f'Now we have **{str(cookis)}** cookis! :cookie: {ok}')

def create_user_if_it_dont_exist(user_id):
    filename = str(user_id) + ".json"
    filename2 = str(user_id) + "_items.json"
    
    if not os.path.isfile(filename):
        f = open(filename, 'w+')
        ae = {'cash':0, 'bank':0}
        json.dump(ae, f)
        f.close()
        
        with open("users.txt",'r') as file:
            txt = file.read()
        
        txt = txt + "\n" + str(user_id)
        
        with open("users.txt",'w') as file:
            file.write(txt)

    if not os.path.isfile(filename2):
        cook_file = open(f"{str(user_id)}_items.json", 'w+')
        ae2loluwu = {}
        json.dump(ae2loluwu, cook_file)

@inter_client.slash_command(description="Get money :)")
@dislash.cooldown(1, 60, commands.BucketType.user)
async def work(inter):
    filename = str(inter.author.id) + '.json'
    
    create_user_if_it_dont_exist(inter.author.id)
    
    with open(filename, 'r') as f:
        ok = json.load(f)
    
    cash = ok['cash']
    ok['cash'] = cash + random.randint(10,75)

    with open(filename, 'w') as f:
        json.dump(ok, f)
    
    replies=['You helped hellory4n explode his super boom machine.',
    'You was using your PC like a normal person and then somehow suddenly many moneys started appearing from the screen.',
    'You made a ｔａｃｏ ｉｃｅ ｃｒｅａｍ.',
    'You exploded your house.(wait how this can give money)',
    'You bought a sandwich.',
    'You used `/work`.',
    'You helped some people make an ultra boom machine.',
    'You found money in your toilet.',
    'You made a Fancade game.',
    'You.',
    'Your opinion is invalid.',
    'hellory4n joined the server.',
    'You hacked UES GAMEPLAYS\' PC and selled their data.',
    'You made a YouTube channel and started spamming videos that are exactly the same thing.',
    'You made 42 games and published all of them once.',
    'You [Message only available for WhatsApp 2 users].']

    await inter.reply(f"{random.choice(replies)} Your cash is now {ok['cash']} <:lelgold:888933451410075689>")

@inter_client.slash_command(description="See your money", options=[Option("user","If you don't put anything here, I'll use you!",OptionType.USER)])
async def balance(inter, user=None):
    if user==None:
        filename = str(inter.author.id) + '.json'
        user=inter.author
    else:
        filename = str(user.id) + '.json'
    
    create_user_if_it_dont_exist(inter.author.id)

    with open(filename, 'r') as f:
        ok = json.load(f)
    
    embed = discord.Embed(title=f"{user}'s balance", description="", color=0xFECC4D)
    embed.add_field(name="Cash", value=f"{ok['cash']} <:lelgold:888933451410075689>", inline=True)
    embed.add_field(name="Bank",value=f"{ok['bank']} <:lelgold:888933451410075689>", inline=True)
    embed.add_field(name="Total",value=f"{ok['cash'] + ok['bank']} <:lelgold:888933451410075689>", inline=True)
    embed.set_footer(text=str(inter.author.id))
    await inter.reply(embed=embed)

@inter_client.slash_command(description="Deposit your money", options=[Option("value","The value you want to deposit",OptionType.INTEGER,required=True)])
async def deposit(inter, value):
    filename = str(inter.author.id) + '.json'

    create_user_if_it_dont_exist(inter.author.id)
    
    with open(filename, 'r') as f:
        ok = json.load(f)
    
    if value > 0 and value < ok['cash'] + 1:
        ok['cash'] -= value
        ok['bank'] += value

        with open(filename, 'w') as f:
            json.dump(ok, f)
    
        await inter.reply("Boom")
    else:
        await inter.reply("Lol no")

@inter_client.slash_command(description="Withdraw your money", options=[Option("value","The value you want to withdraw",OptionType.INTEGER,required=True)])
async def withdraw(inter, value):
    filename = str(inter.author.id) + '.json'

    create_user_if_it_dont_exist(inter.author.id)
    
    with open(filename, 'r') as f:
        ok = json.load(f)
    
    if value > 0 and value < ok['bank'] + 1:
        ok['cash'] += value
        ok['bank'] -= value

        with open(filename, 'w') as f:
            json.dump(ok, f)
    
        await inter.reply("Boom")
    else:
        await inter.reply("Lol no")

@inter_client.slash_command(description="See the leaderboard")
async def leaderboard(inter):
    page = 0
    lb_uwu = ""
    cook_list = {}
    when_the = []

    with open("users.txt",'r') as f:
        txt = f.read()

    t_x_t = txt.split("\n")
    t_x_t.remove("nothing lol xd")

    for i in t_x_t:
        with open(f"{i}.json",'r') as f:
            ok = json.load(f)
        when_the.append(ok['cash'] + ok['bank'])

        for i_ in when_the:
            cook_list[i] = i_

    def split_dict_into_chunks(input_dict, chunk_size):
        res = []
        new_dict = {}
        for k, v in input_dict.items():
            if len(new_dict) < chunk_size:
                new_dict[k] = v
            else:
                res.append(new_dict)
                new_dict = {k: v}
        res.append(new_dict)
        return res

    cook_list = dict(sorted(cook_list.items(), key=lambda item: item[1]))
    cook_list = dict(reversed(list(cook_list.items())))

    users_chunks = split_dict_into_chunks(cook_list,10)

    for key,value in users_chunks[page].items():
        lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

    embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
    embed.set_footer(text=str(inter.author.id))

    can_go_back = True
    can_go_forward = True

    if page+1 == 1:
        can_go_back = False

    if page+1 == len(users_chunks):
        can_go_forward = False

    row = ActionRow(
        Button(
            style=ButtonStyle.blurple,
            label="Previous page",
            custom_id="prev_button",
            disabled=not can_go_back
        ),
        Button(
            style=ButtonStyle.blurple,
            label="Next page",
            custom_id="next_button",
            disabled=not can_go_forward
        )
    )
    msg = await inter.reply(embed=embed, components=[row])

    on_click = msg.create_click_listener(timeout=120)

    @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
    async def on_wrong_user(inter):
        await inter.reply("You're not the author :P", ephemeral=True)

    @on_click.matching_id("prev_button")
    async def on_prev_button(inter):
      nonlocal page
      can_go_back = True
      can_go_forward = True
      page -= 1

      if page == 0:
        can_go_back = False

      if page == len(users_chunks)-1:
        can_go_forward = False

      newrow = ActionRow(
        Button(
          style=ButtonStyle.blurple,
          label="Previous page",
          custom_id="prev_button",
          disabled=not can_go_back
        ),
        Button(
          style=ButtonStyle.blurple,
          label="Next page",
          custom_id="next_button",
          disabled=not can_go_forward
          )
        )

      lb_uwu = ""

      for key,value in users_chunks[page].items():
        lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

      embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
      embed.set_footer(text=str(inter.author.id))

      await msg.edit(embed=embed, components=[newrow])

    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])
    
    @on_click.matching_id("next_button")
    async def on_next_button(inter):
      nonlocal page
      can_go_back = True
      can_go_forward = True
      page += 1

      if page == 0:
        can_go_back = False

      if page == len(users_chunks)-1:
        can_go_forward = False

      newrow = ActionRow(
        Button(
          style=ButtonStyle.blurple,
          label="Previous page",
          custom_id="prev_button",
          disabled=not can_go_back
        ),
        Button(
          style=ButtonStyle.blurple,
          label="Next page",
          custom_id="next_button",
          disabled=not can_go_forward
          )
        )

      lb_uwu = ""

      for key,value in users_chunks[page].items():
        lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

      embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
      embed.set_footer(text=str(inter.author.id))

      await msg.edit(embed=embed, components=[newrow])

    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])

@inter_client.slash_command(description="See all of the shop items!")
async def shop(inter):
    items = ""

    with open("items.txt", 'r') as f:
        txt = f.read()
    
    txt2 = txt.split("\n")

    for i in txt2:
        item_info = i.split("&&")
        items = items + item_info[3] + " `" + item_info[0] + "` (" + item_info[1] + " <:lelgold:888933451410075689>)" + "\n" + item_info[2] + "\n\n"
    
    await inter.reply(items)

@inter_client.slash_command(description="Buy something :)", options=[Option("item",description="The item you want to buy",type=OptionType.STRING,required=True,choices=[OptionChoice("Void","Void"),OptionChoice("Cooki","Cooki"),OptionChoice("Arnold cooki","Arnold cooki"),OptionChoice("Linux","Linux"),OptionChoice("Lelcube plushie","Lelcube plushie"),OptionChoice("Windows Vista","Windows Vista"),OptionChoice("Terrible laptop","Terrible laptop"),OptionChoice("Free bobux","Free bobux"),OptionChoice("Top secret lelcube images","Top secret lelcube images"),OptionChoice("Internet Explorer 12","Internet Explorer 12"),OptionChoice("Clippy","Clippy"),OptionChoice("Illegal DVD","Illegal DVD"),OptionChoice("eyePhone","eyePhone"),OptionChoice("iMark","iMark"),OptionChoice("Super snowman","Super snowman"),OptionChoice("Metal cake","Metal cake")]),Option("amount","The amount that you want to buy",OptionType.INTEGER,required=False)])
async def buy(inter: SlashInteraction, item: str, amount=1):
    oh_nice = False

    create_user_if_it_dont_exist(inter.author.id)

    if not amount < 1:
        with open("items.txt") as f:
            txt = f.read()
        
        txt2 = txt.split("\n")

        for i in txt2:
            txt3 = i.split("&&")

            if txt3[0] == item:
                with open(f"{inter.author.id}.json", 'r') as f:
                    ok = json.load(f)
                
                if ok['cash'] > int(txt3[1]) * amount - 1:
                    ok['cash'] -= int(txt3[1]) * amount
                    
                    with open(f"{inter.author.id}.json", 'w') as f:
                        json.dump(ok, f)

                    oh_nice = True
        
        if oh_nice == True:
            with open(f"{inter.author.id}_items.json", 'r') as file:
                ues = json.load(file)
            
            try:
                ues[item] = ues[item] + amount
            except:
                ues[item] = amount
            
            with open(f"{inter.author.id}_items.json", 'w') as file:
                json.dump(ues, file)

            await inter.reply("Boom")
        else:
            await inter.reply("Lol you can't buy this")
    else:
        await inter.reply("Lol wot")

@inter_client.slash_command(description="See your items", options=[Option("user", "If you don't put something here, I'll use you!", OptionType.USER)])
async def inventory(inter, user=None):
    if user==None:
        filename = str(inter.author.id) + '_items.json'
        user=inter.author
    else:
        filename = str(user.id) + '_items.json'

    try:
        super_cook_text = ""

        create_user_if_it_dont_exist(inter.author.id)
        create_user_if_it_dont_exist(user.id)

        with open(filename, 'r') as f:
            items = json.load(f)
        
        for value, key in items.items():
            if not key < 1:
                super_cook_text = super_cook_text + str(value) + " (" + str(key) + ")\n"

        embed=discord.Embed(title=f"{user}'s inventory", description=super_cook_text, color=0xFECC4D)
        embed.set_footer(text=str(inter.author.id))
        await inter.reply(embed=embed)
    except:
        await inter.reply("It looks like you don't have items. (If you actually have then this is a bug)")

@inter_client.slash_command(description="Use an item that you have", options=[Option("item",description="The item you want to use",type=OptionType.STRING,required=True,choices=[OptionChoice("Void","Void"),OptionChoice("Cooki","Cooki"),OptionChoice("Arnold cooki","Arnold cooki"),OptionChoice("Linux","Linux"),OptionChoice("Lelcube plushie","Lelcube plushie"),OptionChoice("Windows Vista","Windows Vista"),OptionChoice("Terrible laptop","Terrible laptop"),OptionChoice("Free bobux","Free bobux"),OptionChoice("Top secret lelcube images","Top secret lelcube images"),OptionChoice("Internet Explorer 12","Internet Explorer 12"),OptionChoice("Clippy","Clippy"),OptionChoice("Illegal DVD","Illegal DVD"),OptionChoice("eyePhone","eyePhone"),OptionChoice("iMark","iMark"),OptionChoice("Super snowman","Super snowman"),OptionChoice("Metal cake","Metal cake")]),Option("amount","The amount that you want to use",OptionType.INTEGER,required=False)])
async def use(inter, item, amount=1):
    create_user_if_it_dont_exist(inter.author.id)

    ono = False

    with open(f"{str(inter.author.id)}_items.json", 'r') as f:
        items = json.load(f)
    
    if item not in items or items[item] < amount:
        ono = True
        await inter.reply("Lol you don't have this item")

    if ono == False:
        items[item] = items[item] - amount

        with open(f"{str(inter.author.id)}_items.json", 'w') as f:
            json.dump(items, f)
        
        if item == "Cooki":
            await inter.reply(":yum:")
        elif item == "Linux":
            await inter.reply("Congratulations you was scammed :clap: <:lelcube:811058465383514132>")
        elif item == "Lelcube plushie":
            row = ActionRow(
                Button(
                    style=ButtonStyle.green,
                    label="Hug it :)",
                    custom_id="hug"
                ),
                Button(
                    style=ButtonStyle.green,
                    label="Play with it :)",
                    custom_id="play"
                ),
                Button(
                    style=ButtonStyle.red,
                    label="Explode it",
                    custom_id="boom"
                )
            )
            msg = await inter.reply("What you want to do with the lelcube plushie?", components=[row])

            on_click = msg.create_click_listener(timeout=120)

            @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
            async def on_wrong_user(inter):
                await inter.reply("You're not the author :P", ephemeral=True)

            @on_click.matching_id("hug")
            async def on_hug(inter):
                await msg.edit(content="You hugged the plushie! <:Hello_UwU:822546152402321428>")
            
            @on_click.matching_id("play")
            async def on_play(inter):
                await msg.edit(content="You played with the plushie! <:Hello_OwO:822546151010074694>")
            
            @on_click.matching_id("boom")
            async def on_boom(inter):
                await msg.edit(content="You exploded the plushie, no buttons for you >:(", components=[])

            @on_click.timeout
            async def on_timeout():
                await msg.edit(components=[])

        elif item == "Windows Vista":
            msg = await inter.reply("Starting Windows...")
            await asyncio.sleep(30)
            await msg.edit(content="Still starting Windows...")
            await asyncio.sleep(30)
            choices = ['Why you bought Windows Vista in the first place?',
            'STILL STARTING WINDOWS...',
            'What you expected',
            '1 minute left lol',
            'A NASA PC is required to run Windows Vista properly',
            'lol',
            'You are quite patient, huh?',
            '"While Windows Vista is starting, I think you should buy Microsoft 365, Office, Microsoft Surface, and Windows 11!" - Microsoft, 100% True',
            'Go get something to eat or something, idk, Windows Vista still needs one more minute...',
            'One more thing...',
            'Such speed.',
            'Such good OS',
            '10/10 best OS',
            '**ｂｅｓｔ ｏｓ ｅｖｅｒ**']
            await msg.edit(content=random.choice(choices))
            await asyncio.sleep(60)
            await msg.edit(content="https://cdn.discordapp.com/attachments/778461818686406678/903425146990247966/unknown.png")
        elif item == "Terrible laptop":
            row = ActionRow(
                Button(
                    style=ButtonStyle.green,
                    label="Use its OS (Which is Windows 10)",
                    custom_id="use"
                ),
                Button(
                    style=ButtonStyle.green,
                    label="Show its specifications",
                    custom_id="specs"
                ),
                Button(
                    style=ButtonStyle.red,
                    label="Destroy it lol",
                    custom_id="boom"
                )
            )
            msg = await inter.reply("What you want to do with the ~~terrible~~ laptop", components=[row])

            on_click = msg.create_click_listener(timeout=120)

            @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
            async def on_wrong_user(inter):
                await inter.reply("You're not the author :P", ephemeral=True)

            @on_click.matching_id("use")
            async def on_use(inter):
                await msg.edit(content="https://cdn.discordapp.com/attachments/778461818686406678/903431704197337178/unknown.png")
            
            @on_click.matching_id("specs")
            async def on_specs(inter):
                await msg.edit(content="RAM: 2GB RAM\nHDD: 32GB\nCPU: Intel Atom\nGPU: Nonexistent\nOthers: Its design was made in 3 minutes :thumbsup:")
            
            @on_click.matching_id("boom")
            async def on_boom(inter):
                await msg.edit(content="That's a good choice", components=[])

            @on_click.timeout
            async def on_timeout():
                await msg.edit(components=[])
        elif item == "Free bobux":
            row = ActionRow(
                Button(
                    style=ButtonStyle.green,
                    label="CONFIRM FREE BOBUX 🤑🤑🤑🤑🤑🤑🤑🤑🤑",
                    custom_id="hax"
                )
            )
            msg = await inter.reply("CLICK IN \"CONFIRM FREE BOBUX\" TO CONFIRM FREE BOBUX :money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth:", components=[row])

            on_click = msg.create_click_listener(timeout=120)

            @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
            async def on_wrong_user(inter):
                await inter.reply("You're not the author :P", ephemeral=True)

            @on_click.matching_id("hax")
            async def on_hax(inter):
                await hack(inter, inter.author.name)

            @on_click.timeout
            async def on_timeout():
                await msg.edit(components=[])
        elif item == "Top secret lelcube images":
            await inter.reply(":soap: <:lelcube:811058465383514132>")
            await inter.send("You know what this means?????????? It means Lelcube has soap!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111111111111111111!!1!!1!!!1!")
        elif item == "Void":
            await inter.reply("** **")
        elif item == "Internet Explorer 12":
            await inter.reply("Starting Internet Explorer...\n\nTip: Get a better browser")
        elif item == "Clippy":
            row = ActionRow(
                Button(
                    style=ButtonStyle.blurple,
                    label="Get help with writing the letter",
                    custom_id="help"
                ),
                Button(
                    style=ButtonStyle.blurple,
                    label="Write the letter without help",
                    custom_id="nohelp"
                )
            )

            row2 = ActionRow(
                Button(
                    style=ButtonStyle.blurple,
                    label="More useful tips with Clippy!",
                    custom_id="more"
                )
            )
            msg = await inter.reply("It looks like you're writing a letter.", components=[row])

            on_click = msg.create_click_listener(timeout=120)

            @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
            async def on_wrong_user(inter):
                await inter.reply("You're not the author :P", ephemeral=True)

            @on_click.matching_id("help")
            async def on_help(inter):
                await msg.edit(content="To write letters, it's very easy! You just press a letter, or any character, and boom!", components=[row2])

            @on_click.matching_id("nohelp")
            async def on_nohelp(inter):
                await msg.edit(content="unu",components=[])

            @on_click.matching_id("more")
            async def on_more(inter):
                await msg.edit(content="Failed to load more useful tips.",components=[])

            @on_click.timeout
            async def on_timeout():
                await msg.edit(components=[])
        elif item == "Illegal DVD":
            await inter.reply(":police_car:")
            await asyncio.sleep(5)
            await inter.reply("The police is here, and you will be bammed!")
            await asyncio.sleep(5)
            await bam(inter, inter.author.name, "Buying illegal DVDs")
        elif item == "Arnold cooki":
            await inter.reply(":yum::yum:")
        elif item == "eyePhone":
            await inter.reply("Move your eye to use your eyePhone.")
            await asyncio.sleep(1)
            await inter.reply("*phone explodes cuz the sensor thinks you want to explode the phone*")
        elif item == "iMark":
            await inter.reply(":apple:")
            await asyncio.sleep(3)

            ues = ['Wait das not a mac >:ccccc',
            '*iMark explodes*',
            'iMark: I don\'t want to start today >:c',
            'Uh oh. Looks like this hardware is from 1982.',
            'Windows: Oh, is that a Windows computer?',
            'https://cdn.discordapp.com/attachments/877602677394124820/877603176138817556/Welcome.mp4',
            '*burns*',
            '*screen shoots laser*',
            '*iMark becomes an egg*']
            lol_wot = await inter.reply(random.choice(ues))
            await asyncio.sleep(3)
            await lol_wot.edit(content="https://cdn.discordapp.com/attachments/811051812638556221/928413032634257428/unknown.png")
        elif item == "Super snowman":
            ads = ['**[AD] - Oreo**\nSTOP WHAT ARE YOU DOING!!!!!!!!!!\nSAY IMMA BUY AN OREO NOWWWWWWWWWWWWWW',
            '**[AD] - Void**\nWant nothing? Then I can help you! Buy a void today! It\'s free!!!!',
            '**[AD] - Cookis**\nWe all love cookis. But what if you could get a cooki now? Get a cooki now then, but, get our deliciously delicious cookis made by my mom!',
            '**[AD] - Arnold cookis**\nThis is a very cook cooki made by the snake himself, Arnold!\n\nWhich is :\n• Super cook stuff for you!\n• Delicious! Everyone likes it!\n• Its also looks very good!\n\nLook what other people said 🤔\n> 🟧 Harold said : it\'s so cook! Even Jeremy likes it!\n>👩‍🦲 Mark said : A really nice cooki! It makes me fell so good!',
            '**[AD] - Linux**\ndis os prety cook uwu pls by me',
            '**[AD] - Lelcube plushie**\nLelcube, now as a marketable plushie!\nHug it! Punch it! Burn it! The possibilities aren\'t endless!',
            '**[AD] - Windows Vista**\nThe wow starts now.\n\nMany new technologies, that will help build the future of Windows. There\'s the new Aero theme, which looks so good, that it makes you say "wow" 50 times. The start menu has been improved, and now it has a search bar, which you can use to find all of your stuff easily. We added gadgets, an incredible way of getting info, like the weather, or maybe a bunch of photos you have! Multitasking was taken to the next level. Imagine if all of your apps were on a 3D space, and you could switch between them. That\'s possible with Windows Vista. Office 2007 is here, and it is beautiful, and has a lot of new stuff. Easier. Safer. Better connected. More entertaining. Wow.',
            '**[AD] - Terrible laptop**\n"Terrible" laptop? NO IT ACTUALLY IS GOOD IT HAS FANCY SUTFF WE USED A TABLET BOARD BUT TBATSOK EVERYONE DOE S THAT WHAT ARE Y OU DOING NOOOOOOO TRDUST ME THSI AGOOD',
            '**[AD] - Free bobux**\nAlways wanted bobux, but you don\'t have money to buy it? Don\'t worry! Free bobux allows you get a lot of bobux, with just a couple of clicks.',
            '**[AD] - eyePhone**\nWell it\'s an iPhone, but, with revolutionary eye trackers.\nNow you can use your phone, making weird eye gestures!\nEven tho no one asked for this feature, we decided to set new industry standards.\n\n:apple:\nThink different.',
            '**[AD] - Top secret lelcube images**\nGIMME BOBUX :rage:',
            '**[AD] - Internet Explorer 12**\nThe next evolution of the internet. Internet Explorer is back, more revolutionary than ever. Here\'s a list of the new features that will completely change everything.\n- Fluent Design theme\n- Removed many features\n- Browser is slower',
            '**[AD] - Clippy**\nHello! I\'m clippy! I can help you! Ask anything to me, I have an answer!',
            '**[AD] - Illegal DVD**\nwh-',
            '**[AD] - iMark**\nSay hello to the new iMark.\nInspired by the best of apples (literally, apples). Transformed by the MM1 chip. Stands out in any space. Fits perfectly into your life.\n\nOne boring color.\nYou do boring silver\nOnly 10m. Now that\'s thin.\nAnd more than 1,000 pounds. Abracadabra.\nBrilliant 240p retina display.\n144p FaceTime HD camera.\nStudio-quality mic. (if that studio is garbage)\nNo speaker, who needs sounds\nThere are less apps for iMark than ever before.\niMark + eyePhone. Quite the pair.',
            '**[AD] - Super snowman**\nHigh quality ad machine',
            '**[AD] - Metal cake**\nWe love cakes, and we love metal, so we made a metal cake! It\'s extremely tasty, and it\'s good for the environment!']
            await inter.reply(random.choice(ads))
        elif item == "Metal cake":
            await inter.reply("Hmm, metal tastes so good! I love it! Tasty! Delicious! Incredible!")
            await asyncio.sleep(3)
            await inter.reply("*explodes*")

@inter_client.slash_command(description="Give money to another person", options=[Option("user","The user that will get your money",OptionType.USER,required=True),Option("amount","The amount of money that you will give",OptionType.INTEGER,required=True)])
async def give_money(inter, user, amount):
    problems_ono = False

    if user.id == inter.author.id:
        problems_ono = True
        await inter.reply("You can't give money for yourself", ephemeral=True)
    
    input = f"{str(inter.author.id)}.json"
    output = f"{str(user.id)}.json"

    with open(input, 'r') as f_i:
        ok_i = json.load(f_i)
    
    if amount < 1 or not ok_i['cash'] > amount - 1:
        problems_ono = True
        await inter.reply("You can't lol")
    
    if problems_ono == False:
        with open(output, 'r') as f_o:
            ok_o = json.load(f_o)
        
        ok_i['cash'] -= amount
        ok_o['cash'] += amount

        with open(input, 'w') as f_i:
            json.dump(ok_i, f_i)
        
        with open(output, 'w') as f_o:
            json.dump(ok_o, f_o)
        
        await inter.reply("Boom")

@inter_client.slash_command(description="Reset YOUR money")
async def reset_money(inter):
    input_received = False

    filename = str(inter.author.id) + ".json"

    create_user_if_it_dont_exist(inter.author.id)

    row = ActionRow(
        Button(
            style=ButtonStyle.red,
            label="Yes, reset my money!",
            custom_id="yes_button"
        ),
        Button(
            style=ButtonStyle.blurple,
            label="Nevermind.",
            custom_id="no_button"
        )
    )
    msg = await inter.reply("Are you sure you want to reset your money??", components=[row])

    on_click = msg.create_click_listener(timeout=120)

    @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
    async def on_wrong_user(inter):
        await inter.reply("You're not the author :P", ephemeral=True)

    @on_click.matching_id("yes_button")
    async def on_yes_button(inter):
        with open(filename, 'r') as f:
            ok = json.load(f)

        ok['cash'] = 0
        ok['bank'] = 0

        with open(filename, 'w') as f:
            json.dump(ok, f)

        await msg.edit(content="Successfully reseted.", components=[])
        input_received = True
    
    @on_click.matching_id("no_button")
    async def on_no_button(inter):
        await msg.edit(content="Ok", components=[])
        input_received = True

    @on_click.timeout
    async def on_timeout():
        if input_received == False:
            await msg.edit(components=[])
        else:
            pass

@inter_client.slash_command(description="Give an item to someone", options=[Option("user","The user that will get the item",OptionType.USER,required=True),Option("item","The item that you will give", OptionType.STRING, required=True, choices=[OptionChoice("Void","Void"),OptionChoice("Cooki","Cooki"),OptionChoice("Arnold cooki","Arnold cooki"),OptionChoice("Linux","Linux"),OptionChoice("Lelcube plushie","Lelcube plushie"),OptionChoice("Windows Vista","Windows Vista"),OptionChoice("Terrible laptop","Terrible laptop"),OptionChoice("Free bobux","Free bobux"),OptionChoice("Top secret lelcube images","Top secret lelcube images"),OptionChoice("Internet Explorer 12","Internet Explorer 12"),OptionChoice("Clippy","Clippy"),OptionChoice("Illegal DVD","Illegal DVD"),OptionChoice("eyePhone","eyePhone"),OptionChoice("iMark","iMark"),OptionChoice("Super snowman","Super snowman"),OptionChoice("Metal cake","Metal cake")]), Option("amount","The amount that you will give",OptionType.INTEGER,required=False)])
async def give_item(inter, user, item, amount=1):
    problems_ono = False
    
    input = f"{str(inter.author.id)}_items.json"
    output = f"{str(user.id)}_items.json"

    with open(input, 'r') as f_i:
        ok_i = json.load(f_i)
    
    if amount < 1 or not ok_i[item] > amount - 1:
        problems_ono = True
        await inter.reply("You can't lol")
    
    if problems_ono == False:
        with open(output, 'r') as f_o:
            ok_o = json.load(f_o)
        
        ok_i[item] -= amount

        if item in ok_o:
            ok_o[item] += amount
        else:
            ok_o[item] = amount

        with open(input, 'w') as f_i:
            json.dump(ok_i, f_i)
        
        with open(output, 'w') as f_o:
            json.dump(ok_o, f_o)
        
        await inter.reply("Boom")

@inter_client.slash_command(description="Math", options=[Option("expression","Ues",OptionType.STRING,required=True)])
async def math(ctx, *, expression:str):
    expression = "".join(filter(lambda i: i in "9876543210+-×÷^*/()", expression))
    expression = expression.replace("^", "**").replace("÷", "/").replace("×", "*")
    await ctx.reply(f"Math: {expression}\nResults: {float(eval(expression))}")

@client.command()
async def not_say(ctx, *, msg):
    if ctx.author.id == 748560377763201185:
        await ctx.send(msg)
    else:
        await ctx.send("You can't use this command lol")

@inter_client.slash_command(description="Steal someone's money (don't do that, das bad >:c)", options=[Option("amount","The amount that you want to steal",OptionType.INTEGER,required=True),Option("user","The user that you will steal",OptionType.USER,required=True)])
@dislash.cooldown(1, 60, commands.BucketType.user)
async def rob(inter, amount, user):
    problems_ono = False
    
    output = f"{str(inter.author.id)}.json"
    input = f"{str(user.id)}.json"

    with open(input, 'r') as f_i:
        ok_i = json.load(f_i)
    
    if amount < 1 or not ok_i['cash'] > amount - 1:
        problems_ono = True
        await inter.reply("You can't lol")
    
    if problems_ono == False:
        with open(output, 'r') as f_o:
            ok_o = json.load(f_o)
        
        ues = random.randint(1,100)

        if ues < 30:
            ok_i['cash'] -= amount
            ok_o['cash'] += amount

            with open(input, 'w') as f_i:
                json.dump(ok_i, f_i)
            
            with open(output, 'w') as f_o:
                json.dump(ok_o, f_o)
            
            await inter.reply("Boom")
        else:
            unu = random.randint(1,100)

            ok_o['cash'] -= unu

            with open(output, 'w') as f_o:
                json.dump(ok_o, f_o)
            
            await inter.reply(f"You failed and lost {unu} <:lelgold:888933451410075689>")

@client.command()
async def set_money(ctx, cash, bank, user_id):
    if ctx.author.id == 748560377763201185:
        with open(f"{user_id}.json",'r') as f:
            ok = json.load(f)
        
        ok['cash'] = int(cash)
        ok['bank'] = int(bank)

        with open(f"{user_id}.json",'w') as f:
            json.dump(ok, f)
        
        await ctx.reply("Boom")
    else:
        await ctx.reply("You can't use this command lol")

@client.command()
async def random_status(ctx):
    if ctx.author.id == 748560377763201185:
        cook_loop.start()
        await ctx.send("Boom")
    else:
        await ctx.send("You can't use this command lol")

@client.command(aliases=['fact'])
async def fact2(ctx, index = None):
    the_chosen_one = "nothing"
    with open("facts.txt", "r") as f:
        sweatsmiles_txt = f.read()
    sweatsmilesl = sweatsmiles_txt.split("\n")
    if not index == None:
        try:
            Index = int(index)
            if 1 <= Index < len(sweatsmilesl)+1:
                the_chosen_one = sweatsmilesl[Index-1]
            else:
                await ctx.send(f"Invalid index. Please enter a number between 1 and {len(sweatsmilesl)}!")
        except ValueError:
            the_chosen_one = random.choice(sweatsmilesl)
    else:
        the_chosen_one = random.choice(sweatsmilesl)
    if not the_chosen_one == "nothing":
        cook_data = the_chosen_one.split("&&")
        embed = discord.Embed(title=f"Fact #{cook_data[0]}", description=f"{cook_data[1]}", color=0xFECC4D)
        embed.set_footer(text=f"Fact by {cook_data[2]}")
        await ctx.send(embed=embed)

@inter_client.slash_command(description="See a random fact!", options=[Option("index","The index that you want. If not present, the index will be random",OptionType.INTEGER,required=False)])
async def fact(inter, index=None):
    the_chosen_one = "nothing"
    with open("facts.txt", "r") as f:
        sweatsmiles_txt = f.read()
    sweatsmilesl = sweatsmiles_txt.split("\n")
    if not index == None:
        Index = int(index)
        if 1 <= Index < len(sweatsmilesl)+1:
            the_chosen_one = sweatsmilesl[Index-1]
        else:
            await inter.send(f"Invalid index. Please enter a number between 1 and {len(sweatsmilesl)}!")
    else:
        the_chosen_one = random.choice(sweatsmilesl)
    if not the_chosen_one == "nothing":
        cook_data = the_chosen_one.split("&&")
        embed = discord.Embed(title=f"Fact #{cook_data[0]}", description=f"{cook_data[1]}", color=0xFECC4D)
        embed.set_footer(text=f"Fact by {cook_data[2]}")
        await inter.send(embed=embed)

@client.command(aliases=['work'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def work2(inter):
    filename = str(inter.author.id) + '.json'
    
    create_user_if_it_dont_exist(inter.author.id)
    
    with open(filename, 'r') as f:
        ok = json.load(f)
    
    cash = ok['cash']
    ok['cash'] = cash + random.randint(10,75)

    with open(filename, 'w') as f:
        json.dump(ok, f)
    
    replies=['You helped hellory4n explode his super boom machine.',
    'You was using your PC like a normal person and then somehow suddenly many moneys started appearing from the screen.',
    'You made a ｔａｃｏ ｉｃｅ ｃｒｅａｍ.',
    'You exploded your house.(wait how this can give money)',
    'You bought a sandwich.',
    'You used `/work`.',
    'You helped some people make an ultra boom machine.',
    'You found money in your toilet.',
    'You made a Fancade game.',
    'You.',
    'Your opinion is invalid.',
    'hellory4n joined the server.',
    'You hacked UES GAMEPLAYS\' PC and selled their data.',
    'You made a YouTube channel and started spamming videos that are exactly the same thing.',
    'You made 42 games and published all of them once.',
    'You [Message only available for WhatsApp 2 users].']

    await inter.reply(f"{random.choice(replies)} Your cash is now {ok['cash']} <:lelgold:888933451410075689>")

@client.command(aliases=['balance'])
async def bal(inter, user:discord.User=None):
    if user==None:
        filename = str(inter.author.id) + '.json'
        user=inter.author
    else:
        filename = str(user.id) + '.json'
    
    create_user_if_it_dont_exist(inter.author.id)

    with open(filename, 'r') as f:
        ok = json.load(f)
    
    embed = discord.Embed(title=f"{user}'s balance", description="", color=0xFECC4D)
    embed.add_field(name="Cash", value=f"{ok['cash']} <:lelgold:888933451410075689>", inline=True)
    embed.add_field(name="Bank",value=f"{ok['bank']} <:lelgold:888933451410075689>", inline=True)
    embed.add_field(name="Total",value=f"{ok['cash'] + ok['bank']} <:lelgold:888933451410075689>", inline=True)
    embed.set_footer(text=str(inter.author.id))
    await inter.reply(embed=embed)

@client.command(aliases=['deposit'])
async def dep(inter, value:int):
    filename = str(inter.author.id) + '.json'

    create_user_if_it_dont_exist(inter.author.id)
        
    with open(filename, 'r') as f:
        ok = json.load(f)
        
    if value > 0 and value < ok['cash'] + 1:
        ok['cash'] -= value
        ok['bank'] += value

        with open(filename, 'w') as f:
            json.dump(ok, f)
        
        await inter.reply("Boom")
    else:
        await inter.reply("Lol no")

@client.command(aliases=['with','withdraw'])
async def with2(inter, value:int):
    filename = str(inter.author.id) + '.json'

    create_user_if_it_dont_exist(inter.author.id)
    
    with open(filename, 'r') as f:
        ok = json.load(f)
    
    if value > 0 and value < ok['bank'] + 1:
        ok['cash'] += value
        ok['bank'] -= value

        with open(filename, 'w') as f:
            json.dump(ok, f)
    
        await inter.reply("Boom")
    else:
        await inter.reply("Lol no")

@client.command(aliases=['leaderboard'])
async def lb(inter):
    page = 0
    lb_uwu = ""
    cook_list = {}
    when_the = []

    with open("users.txt",'r') as f:
        txt = f.read()

    t_x_t = txt.split("\n")
    t_x_t.remove("nothing lol xd")

    for i in t_x_t:
        with open(f"{i}.json",'r') as f:
            ok = json.load(f)
        when_the.append(ok['cash'] + ok['bank'])

        for i_ in when_the:
            cook_list[i] = i_

    def split_dict_into_chunks(input_dict, chunk_size):
        res = []
        new_dict = {}
        for k, v in input_dict.items():
            if len(new_dict) < chunk_size:
                new_dict[k] = v
            else:
                res.append(new_dict)
                new_dict = {k: v}
        res.append(new_dict)
        return res

    cook_list = dict(sorted(cook_list.items(), key=lambda item: item[1]))
    cook_list = dict(reversed(list(cook_list.items())))

    users_chunks = split_dict_into_chunks(cook_list,10)

    for key,value in users_chunks[page].items():
        lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

    embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
    embed.set_footer(text=str(inter.author.id))

    can_go_back = True
    can_go_forward = True

    if page+1 == 1:
        can_go_back = False

    if page+1 == len(users_chunks):
        can_go_forward = False

    row = ActionRow(
        Button(
            style=ButtonStyle.blurple,
            label="Previous page",
            custom_id="prev_button",
            disabled=not can_go_back
        ),
        Button(
            style=ButtonStyle.blurple,
            label="Next page",
            custom_id="next_button",
            disabled=not can_go_forward
        )
    )
    msg = await inter.reply(embed=embed, components=[row])

    on_click = msg.create_click_listener(timeout=120)

    @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
    async def on_wrong_user(inter):
        await inter.reply("You're not the author :P", ephemeral=True)

    @on_click.matching_id("prev_button")
    async def on_prev_button(inter):
      nonlocal page
      can_go_back = True
      can_go_forward = True
      page -= 1

      if page == 0:
        can_go_back = False

      if page == len(users_chunks)-1:
        can_go_forward = False

      newrow = ActionRow(
        Button(
          style=ButtonStyle.blurple,
          label="Previous page",
          custom_id="prev_button",
          disabled=not can_go_back
        ),
        Button(
          style=ButtonStyle.blurple,
          label="Next page",
          custom_id="next_button",
          disabled=not can_go_forward
          )
        )

      lb_uwu = ""

      for key,value in users_chunks[page].items():
        lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

      embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
      embed.set_footer(text=str(inter.author.id))

      await msg.edit(embed=embed, components=[newrow])

    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])
    
    @on_click.matching_id("next_button")
    async def on_next_button(inter):
      nonlocal page
      can_go_back = True
      can_go_forward = True
      page += 1

      if page == 0:
        can_go_back = False

      if page == len(users_chunks)-1:
        can_go_forward = False

      newrow = ActionRow(
        Button(
          style=ButtonStyle.blurple,
          label="Previous page",
          custom_id="prev_button",
          disabled=not can_go_back
        ),
        Button(
          style=ButtonStyle.blurple,
          label="Next page",
          custom_id="next_button",
          disabled=not can_go_forward
          )
        )

      lb_uwu = ""

      for key,value in users_chunks[page].items():
        lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

      embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
      embed.set_footer(text=str(inter.author.id))

      await msg.edit(embed=embed, components=[newrow])

    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])

@client.command(aliases=['shop'])
async def shop2(inter):
    items = ""

    with open("items.txt", 'r') as f:
        txt = f.read()
    
    txt2 = txt.split("\n")

    for i in txt2:
        item_info = i.split("&&")
        items = items + item_info[3] + " `" + item_info[0] + "` (" + item_info[1] + " <:lelgold:888933451410075689>)" + "\n" + item_info[2] + "\n\n"
    
    await inter.reply(items)

@client.command(aliases=['buy'])
async def buy2(inter, amount="1"):
    oh_nice = False

    try:
      amount = int(amount)
      oh_nice = True
    except:
      oh_nice = False
      await inter.reply("You are supposed to put a number as the amount (If you are trying to specify the item, you will do it after sending the command!)")

    if oh_nice == True:
      msg = await inter.reply("Choose an item.",components=[
              SelectMenu(
                  custom_id="list",
                  placeholder="Click here to choose the item you want",
                  max_values=1,
                  options=[
                      SelectOption("Void", "Void"),
                      SelectOption("Cooki", "Cooki"),
                      SelectOption("Arnold cooki", "Arnold cooki"),
                      SelectOption("Linux","Linux"),
                      SelectOption("Lelcube plushie","Lelcube plushie"),
                      SelectOption("Windows Vista", "Windows Vista"),
                      SelectOption("Terrible laptop","Terrible laptop"),
                      SelectOption("Free bobux","Free bobux"),
                      SelectOption("Top secret lelcube images","Top secret lelcube images"),
                      SelectOption("Internet Explorer 12","Internet Explorer 12"),
                      SelectOption("Clippy","Clippy"),
                      SelectOption("Illegal DVD","Illegal DVD"),
                      SelectOption("eyePhone","eyePhone"),
                      SelectOption("iMark","iMark"),
                      SelectOption("Super snowman","Super snowman"),
                      SelectOption("Metal cake","Metal cake")
                  ]
              )
          ]
      )

      oldinter = inter
      inter = await msg.wait_for_dropdown()

      if inter.author.id == oldinter.author.id:
          labels = [option.label for option in inter.select_menu.selected_options]
          item = "#".join(labels)

          create_user_if_it_dont_exist(inter.author.id)

          if not amount < 1:
              with open("items.txt") as f:
                  txt = f.read()
              
              txt2 = txt.split("\n")

              for i in txt2:
                  txt3 = i.split("&&")

                  if txt3[0] == item:
                      with open(f"{inter.author.id}.json", 'r') as f:
                          ok = json.load(f)
                      
                      if ok['cash'] > int(txt3[1]) * amount - 1:
                          ok['cash'] -= int(txt3[1]) * amount
                          
                          with open(f"{inter.author.id}.json", 'w') as f:
                              json.dump(ok, f)

                          oh_nice = True
              
              if oh_nice == True:
                  with open(f"{inter.author.id}_items.json", 'r') as file:
                      ues = json.load(file)
                  
                  try:
                      ues[item] = ues[item] + amount
                  except:
                      ues[item] = amount
                  
                  with open(f"{inter.author.id}_items.json", 'w') as file:
                      json.dump(ues, file)

                  await msg.edit(content="Boom",components=[])
              else:
                  await msg.edit(content="Lol you can't buy this",components=[])
          else:
              await inter.reply("Lol wot")
      else:
          await inter.reply("You're not the author :P", ephemeral=True)

@client.command(aliases=['inventory'])
async def inv(inter, user:discord.User=None):
    if user==None:
        filename = str(inter.author.id) + '_items.json'
        user=inter.author
    else:
        filename = str(user.id) + '_items.json'

    try:
        super_cook_text = ""

        create_user_if_it_dont_exist(inter.author.id)
        create_user_if_it_dont_exist(user.id)

        with open(filename, 'r') as f:
            items = json.load(f)
        
        for value, key in items.items():
            if not key < 1:
                super_cook_text = super_cook_text + str(value) + " (" + str(key) + ")\n"

        embed=discord.Embed(title=f"{user}'s inventory", description=super_cook_text, color=0xFECC4D)
        embed.set_footer(text=str(inter.author.id))
        await inter.reply(embed=embed)
    except:
        await inter.reply("It looks like you don't have items. (If you actually have then this is a bug)")

@client.command(aliases=['use'])
async def use2(inter, amount="1"):
    ono = False

    try:
      amount = int(amount)
    except:
      ono = True
      await inter.reply("You are supposed to put a number as the amount (If you are trying to specify the item, you will do it after sending the command!)")

    if ono == False:
      msg = await inter.reply("Choose an item.",components=[
              SelectMenu(
                  custom_id="list",
                  placeholder="Click here to choose the item you want",
                  max_values=1,
                  options=[
                      SelectOption("Void", "Void"),
                      SelectOption("Cooki", "Cooki"),
                      SelectOption("Arnold cooki", "Arnold cooki"),
                      SelectOption("Linux","Linux"),
                      SelectOption("Lelcube plushie","Lelcube plushie"),
                      SelectOption("Windows Vista", "Windows Vista"),
                      SelectOption("Terrible laptop","Terrible laptop"),
                      SelectOption("Free bobux","Free bobux"),
                      SelectOption("Top secret lelcube images","Top secret lelcube images"),
                      SelectOption("Internet Explorer 12","Internet Explorer 12"),
                      SelectOption("Clippy","Clippy"),
                      SelectOption("Illegal DVD","Illegal DVD"),
                      SelectOption("eyePhone","eyePhone"),
                      SelectOption("iMark","iMark"),
                      SelectOption("Super snowman","Super snowman"),
                      SelectOption("Metal cake","Metal cake")
                  ]
              )
          ]
      )

      oldinter = inter
      inter = await msg.wait_for_dropdown()
      if inter.author.id == oldinter.author.id:
          labels = [option.label for option in inter.select_menu.selected_options]
          item = "#".join(labels)

          create_user_if_it_dont_exist(inter.author.id)

          with open(f"{str(inter.author.id)}_items.json", 'r') as f:
              items = json.load(f)
          
          if item not in items or items[item] < amount:
              ono = True
              await inter.reply("Lol you don't have this item")

          if ono == False:
              items[item] = items[item] - amount

              with open(f"{str(inter.author.id)}_items.json", 'w') as f:
                  json.dump(items, f)
              
              await msg.edit(components=[])

              if item == "Cooki":
                  await inter.reply(":yum:")
              elif item == "Linux":
                  await inter.reply("Congratulations you was scammed :clap: <:lelcube:811058465383514132>")
              elif item == "Lelcube plushie":
                  row = ActionRow(
                      Button(
                          style=ButtonStyle.green,
                          label="Hug it :)",
                          custom_id="hug"
                      ),
                      Button(
                          style=ButtonStyle.green,
                          label="Play with it :)",
                          custom_id="play"
                      ),
                      Button(
                          style=ButtonStyle.red,
                          label="Explode it",
                          custom_id="boom"
                      )
                  )
                  msg = await inter.reply("What you want to do with the lelcube plushie?", components=[row])

                  on_click = msg.create_click_listener(timeout=120)

                  @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
                  async def on_wrong_user(inter):
                      await inter.reply("You're not the author :P", ephemeral=True)

                  @on_click.matching_id("hug")
                  async def on_hug(inter):
                      await msg.edit(content="You hugged the plushie! <:Hello_UwU:822546152402321428>")
                  
                  @on_click.matching_id("play")
                  async def on_play(inter):
                      await msg.edit(content="You played with the plushie! <:Hello_OwO:822546151010074694>")
                  
                  @on_click.matching_id("boom")
                  async def on_boom(inter):
                      await msg.edit(content="You exploded the plushie, no buttons for you >:(", components=[])

                  @on_click.timeout
                  async def on_timeout():
                      await msg.edit(components=[])

              elif item == "Windows Vista":
                  msg = await inter.reply("Starting Windows...")
                  await asyncio.sleep(30)
                  await msg.edit(content="Still starting Windows...")
                  await asyncio.sleep(30)
                  choices = ['Why you bought Windows Vista in the first place?',
                  'STILL STARTING WINDOWS...',
                  'What you expected',
                  '1 minute left lol',
                  'A NASA PC is required to run Windows Vista properly',
                  'lol',
                  'You are quite patient, huh?',
                  '"While Windows Vista is starting, I think you should buy Microsoft 365, Office, Microsoft Surface, and Windows 11!" - Microsoft, 100% True',
                  'Go get something to eat or something, idk, Windows Vista still needs one more minute...',
                  'One more thing...',
                  'Such speed.',
                  'Such good OS',
                  '10/10 best OS',
                  '**ｂｅｓｔ ｏｓ ｅｖｅｒ**']
                  await msg.edit(content=random.choice(choices))
                  await asyncio.sleep(60)
                  await msg.edit(content="https://cdn.discordapp.com/attachments/778461818686406678/903425146990247966/unknown.png")
              elif item == "Terrible laptop":
                  row = ActionRow(
                      Button(
                          style=ButtonStyle.green,
                          label="Use its OS (Which is Windows 10)",
                          custom_id="use"
                      ),
                      Button(
                          style=ButtonStyle.green,
                          label="Show its specifications",
                          custom_id="specs"
                      ),
                      Button(
                          style=ButtonStyle.red,
                          label="Destroy it lol",
                          custom_id="boom"
                      )
                  )
                  msg = await inter.reply("What you want to do with the ~~terrible~~ laptop", components=[row])

                  on_click = msg.create_click_listener(timeout=120)

                  @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
                  async def on_wrong_user(inter):
                      await inter.reply("You're not the author :P", ephemeral=True)

                  @on_click.matching_id("use")
                  async def on_use(inter):
                      await msg.edit(content="https://cdn.discordapp.com/attachments/778461818686406678/903431704197337178/unknown.png")
                  
                  @on_click.matching_id("specs")
                  async def on_specs(inter):
                      await msg.edit(content="RAM: 2GB RAM\nHDD: 32GB\nCPU: Intel Atom\nGPU: Nonexistent\nOthers: Its design was made in 3 minutes :thumbsup:")
                  
                  @on_click.matching_id("boom")
                  async def on_boom(inter):
                      await msg.edit(content="That's a good choice", components=[])

                  @on_click.timeout
                  async def on_timeout():
                      await msg.edit(components=[])
              elif item == "Free bobux":
                  row = ActionRow(
                      Button(
                          style=ButtonStyle.green,
                          label="CONFIRM FREE BOBUX 🤑🤑🤑🤑🤑🤑🤑🤑🤑",
                          custom_id="hax"
                      )
                  )
                  msg = await inter.reply("CLICK IN \"CONFIRM FREE BOBUX\" TO CONFIRM FREE BOBUX :money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth:", components=[row])

                  on_click = msg.create_click_listener(timeout=120)

                  @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
                  async def on_wrong_user(inter):
                      await inter.reply("You're not the author :P", ephemeral=True)

                  @on_click.matching_id("hax")
                  async def on_hax(inter):
                      await hack(inter, inter.author.name)

                  @on_click.timeout
                  async def on_timeout():
                      await msg.edit(components=[])
              elif item == "Top secret lelcube images":
                  await inter.reply(":soap: <:lelcube:811058465383514132>")
                  await inter.send("You know what this means?????????? It means Lelcube has soap!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111111111111111111!!1!!1!!!1!")
              elif item == "Void":
                  await inter.reply("** **")
              elif item == "Internet Explorer 12":
                  await inter.reply("Starting Internet Explorer...\n\nTip: Get a better browser")
              elif item == "Clippy":
                  row = ActionRow(
                      Button(
                          style=ButtonStyle.blurple,
                          label="Get help with writing the letter",
                          custom_id="help"
                      ),
                      Button(
                          style=ButtonStyle.blurple,
                          label="Write the letter without help",
                          custom_id="nohelp"
                      )
                  )

                  row2 = ActionRow(
                      Button(
                          style=ButtonStyle.blurple,
                          label="More useful tips with Clippy!",
                          custom_id="more"
                      )
                  )
                  msg = await inter.reply("It looks like you're writing a letter.", components=[row])

                  on_click = msg.create_click_listener(timeout=120)

                  @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
                  async def on_wrong_user(inter):
                      await inter.reply("You're not the author :P", ephemeral=True)

                  @on_click.matching_id("help")
                  async def on_help(inter):
                      await msg.edit(content="To write letters, it's very easy! You just press a letter, or any character, and boom!", components=[row2])

                  @on_click.matching_id("nohelp")
                  async def on_nohelp(inter):
                      await msg.edit(content="unu",components=[])

                  @on_click.matching_id("more")
                  async def on_more(inter):
                      await msg.edit(content="Failed to load more useful tips.",components=[])

                  @on_click.timeout
                  async def on_timeout():
                      await msg.edit(components=[])
              elif item == "Illegal DVD":
                  await inter.reply(":police_car:")
                  await asyncio.sleep(5)
                  await inter.reply("The police is here, and you will be bammed!")
                  await asyncio.sleep(5)
                  await bam(inter, inter.author.name, "Buying illegal DVDs")
              elif item == "Arnold cooki":
                  await inter.reply(":yum::yum:")
              elif item == "eyePhone":
                await inter.reply("Move your eye to use your eyePhone.")
                await asyncio.sleep(1)
                await inter.reply("*phone explodes cuz the sensor thinks you want to explode the phone*")
              elif item == "iMark":
                await inter.reply(":apple:")
                await asyncio.sleep(3)

                ues = ['Wait das not a mac >:ccccc',
                '*iMark explodes*',
                'iMark: I don\'t want to start today >:c',
                'Uh oh. Looks like this hardware is from 1982.',
                'Windows: Oh, is that a Windows computer?',
                'https://cdn.discordapp.com/attachments/877602677394124820/877603176138817556/Welcome.mp4',
                '*burns*',
                '*screen shoots laser*',
                '*iMark becomes an egg*']
                lol_wot = await inter.reply(random.choice(ues))
                await asyncio.sleep(3)
                await lol_wot.edit(content="https://cdn.discordapp.com/attachments/811051812638556221/928413032634257428/unknown.png")
              elif item == "Super snowman":
                ads = ['**[AD] - Oreo**\nSTOP WHAT ARE YOU DOING!!!!!!!!!!\nSAY IMMA BUY AN OREO NOWWWWWWWWWWWWWW',
                '**[AD] - Void**\nWant nothing? Then I can help you! Buy a void today! It\'s free!!!!',
                '**[AD] - Cookis**\nWe all love cookis. But what if you could get a cooki now? Get a cooki now then, but, get our deliciously delicious cookis made by my mom!',
                '**[AD] - Arnold cookis**\nThis is a very cook cooki made by the snake himself, Arnold!\n\nWhich is :\n• Super cook stuff for you!\n• Delicious! Everyone likes it!\n• Its also looks very good!\n\nLook what other people said 🤔\n> 🟧 Harold said : it\'s so cook! Even Jeremy likes it!\n>👩‍🦲 Mark said : A really nice cooki! It makes me fell so good!',
                '**[AD] - Linux**\ndis os prety cook uwu pls by me',
                '**[AD] - Lelcube plushie**\nLelcube, now as a marketable plushie!\nHug it! Punch it! Burn it! The possibilities aren\'t endless!',
                '**[AD] - Windows Vista**\nThe wow starts now.\n\nMany new technologies, that will help build the future of Windows. There\'s the new Aero theme, which looks so good, that it makes you say "wow" 50 times. The start menu has been improved, and now it has a search bar, which you can use to find all of your stuff easily. We added gadgets, an incredible way of getting info, like the weather, or maybe a bunch of photos you have! Multitasking was taken to the next level. Imagine if all of your apps were on a 3D space, and you could switch between them. That\'s possible with Windows Vista. Office 2007 is here, and it is beautiful, and has a lot of new stuff. Easier. Safer. Better connected. More entertaining. Wow.',
                '**[AD] - Terrible laptop**\n"Terrible" laptop? NO IT ACTUALLY IS GOOD IT HAS FANCY SUTFF WE USED A TABLET BOARD BUT TBATSOK EVERYONE DOE S THAT WHAT ARE Y OU DOING NOOOOOOO TRDUST ME THSI AGOOD',
                '**[AD] - Free bobux**\nAlways wanted bobux, but you don\'t have money to buy it? Don\'t worry! Free bobux allows you get a lot of bobux, with just a couple of clicks.',
                '**[AD] - eyePhone**\nWell it\'s an iPhone, but, with revolutionary eye trackers.\nNow you can use your phone, making weird eye gestures!\nEven tho no one asked for this feature, we decided to set new industry standards.\n\n:apple:\nThink different.',
                '**[AD] - Top secret lelcube images**\nGIMME BOBUX :rage:',
                '**[AD] - Internet Explorer 12**\nThe next evolution of the internet. Internet Explorer is back, more revolutionary than ever. Here\'s a list of the new features that will completely change everything.\n- Fluent Design theme\n- Removed many features\n- Browser is slower',
                '**[AD] - Clippy**\nHello! I\'m clippy! I can help you! Ask anything to me, I have an answer!',
                '**[AD] - Illegal DVD**\nwh-',
                '**[AD] - iMark**\nSay hello to the new iMark.\nInspired by the best of apples (literally, apples). Transformed by the MM1 chip. Stands out in any space. Fits perfectly into your life.\n\nOne boring color.\nYou do boring silver\nOnly 10m. Now that\'s thin.\nAnd more than 1,000 pounds. Abracadabra.\nBrilliant 240p retina display.\n144p FaceTime HD camera.\nStudio-quality mic. (if that studio is garbage)\nNo speaker, who needs sounds\nThere are less apps for iMark than ever before.\niMark + eyePhone. Quite the pair.',
                '**[AD] - Super snowman**\nHigh quality ad machine',
                '**[AD] - Metal cake**\nWe love cakes, and we love metal, so we made a metal cake! It\'s extremely tasty, and it\'s good for the environment!']
                await inter.reply(random.choice(ads))
              elif item == "Metal cake":
                await inter.reply("Hmm, metal tastes so good! I love it! Tasty! Delicious! Incredible!")
                await asyncio.sleep(3)
                await inter.reply("*explodes*")
      else:
          await inter.reply("You're not the author :P", ephemeral=True)

@client.command(aliases=['give-money','give_money'])
async def give_money2(inter, user:discord.User, amount:int):
    problems_ono = False

    if user.id == inter.author.id:
        problems_ono = True
        await inter.reply("You can't give money for yourself")
    
    input = f"{str(inter.author.id)}.json"
    output = f"{str(user.id)}.json"

    with open(input, 'r') as f_i:
        ok_i = json.load(f_i)
    
    if amount < 1 or not ok_i['cash'] > amount - 1:
        problems_ono = True
        await inter.reply("You can't lol")
    
    if problems_ono == False:
        with open(output, 'r') as f_o:
            ok_o = json.load(f_o)
        
        ok_i['cash'] -= amount
        ok_o['cash'] += amount

        with open(input, 'w') as f_i:
            json.dump(ok_i, f_i)
        
        with open(output, 'w') as f_o:
            json.dump(ok_o, f_o)
        
        await inter.reply("Boom")

@client.command(aliases=['reset-money','reset','reset_money'])
async def reset_money2(inter):
    input_received = False

    filename = str(inter.author.id) + ".json"

    create_user_if_it_dont_exist(inter.author.id)

    row = ActionRow(
        Button(
            style=ButtonStyle.red,
            label="Yes, reset my money!",
            custom_id="yes_button"
        ),
        Button(
            style=ButtonStyle.blurple,
            label="Nevermind.",
            custom_id="no_button"
        )
    )
    msg = await inter.reply("Are you sure you want to reset your money??", components=[row])

    on_click = msg.create_click_listener(timeout=120)

    @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
    async def on_wrong_user(inter):
        await inter.reply("You're not the author :P", ephemeral=True)

    @on_click.matching_id("yes_button")
    async def on_yes_button(inter):
        with open(filename, 'r') as f:
            ok = json.load(f)

        ok['cash'] = 0
        ok['bank'] = 0

        with open(filename, 'w') as f:
            json.dump(ok, f)

        await msg.edit(content="Successfully reseted.", components=[])
        input_received = True
    
    @on_click.matching_id("no_button")
    async def on_no_button(inter):
        await msg.edit(content="Ok", components=[])
        input_received = True

    @on_click.timeout
    async def on_timeout():
        if input_received == False:
            await msg.edit(components=[])
        else:
            pass

@client.command(aliases=['give_item','give-item'])
async def give_item2(inter, user:discord.Member, amount="1"):
    problems_ono = False

    try:
      amount = int(amount)
    except:
      problems_ono = True
      await inter.reply("You are supposed to put a number as the amount (If you are trying to specify the item, you will do it after sending the command!)")
    
    if problems_ono == False:
      msg = await inter.reply("Choose an item.",components=[
              SelectMenu(
                  custom_id="list",
                  placeholder="Click here to choose the item you want",
                  max_values=1,
                  options=[
                      SelectOption("Void", "Void"),
                      SelectOption("Cooki", "Cooki"),
                      SelectOption("Arnold cooki", "Arnold cooki"),
                      SelectOption("Linux","Linux"),
                      SelectOption("Lelcube plushie","Lelcube plushie"),
                      SelectOption("Windows Vista", "Windows Vista"),
                      SelectOption("Terrible laptop","Terrible laptop"),
                      SelectOption("Free bobux","Free bobux"),
                      SelectOption("Top secret lelcube images","Top secret lelcube images"),
                      SelectOption("Internet Explorer 12","Internet Explorer 12"),
                      SelectOption("Clippy","Clippy"),
                      SelectOption("Illegal DVD","Illegal DVD"),
                      SelectOption("eyePhone","eyePhone"),
                      SelectOption("iMark","iMark"),
                      SelectOption("Super snowman","Super snowman"),
                      SelectOption("Metal cake","Metal cake")
                  ]
              )
          ]
      )

      oldinter = inter
      inter = await msg.wait_for_dropdown()
      if inter.author.id == oldinter.author.id:
          labels = [option.label for option in inter.select_menu.selected_options]
          item = "#".join(labels)

          input = f"{str(inter.author.id)}_items.json"
          output = f"{str(user.id)}_items.json"

          with open(input, 'r') as f_i:
              ok_i = json.load(f_i)
      
          if amount < 1 or not ok_i[item] > amount - 1:
              problems_ono = True
              await inter.reply("You can't lol")
      
          if problems_ono == False:
              with open(output, 'r') as f_o:
                  ok_o = json.load(f_o)
          
              ok_i[item] -= amount

              if item in ok_o:
                  ok_o[item] += amount
              else:
                  ok_o[item] = amount

              with open(input, 'w') as f_i:
                  json.dump(ok_i, f_i)
          
              with open(output, 'w') as f_o:
                  json.dump(ok_o, f_o)
              
              await msg.edit(content="Boom", components=[])

@client.command(aliases=['rob','steal','rob-money','rob_money','steal-money','steal_money'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def rob2(inter, user:discord.User, amount):
    problems_ono = False

    try:
      amount = int(amount)
    except:
      problems_ono = True
      await inter.reply("You are supposed to put a number as the amount")
    
    if problems_ono == False:
      output = f"{str(inter.author.id)}.json"
      input = f"{str(user.id)}.json"

      with open(input, 'r') as f_i:
          ok_i = json.load(f_i)
      
      if amount < 1 or not ok_i['cash'] > amount - 1:
          problems_ono = True
          await inter.reply("You can't lol")
      
      if problems_ono == False:
          with open(output, 'r') as f_o:
              ok_o = json.load(f_o)
          
          ues = random.randint(1,100)

          if ues < 30:
              ok_i['cash'] -= amount
              ok_o['cash'] += amount

              with open(input, 'w') as f_i:
                  json.dump(ok_i, f_i)
              
              with open(output, 'w') as f_o:
                  json.dump(ok_o, f_o)
              
              await inter.reply("Boom")
          else:
              unu = random.randint(1,100)

              ok_o['cash'] -= unu

              with open(output, 'w') as f_o:
                  json.dump(ok_o, f_o)
              
              await inter.reply(f"You failed and lost {unu} <:lelgold:888933451410075689>")

@inter_client.slash_command(description="For the people that don't like the new help command")
async def classic_help(inter):
    embed=discord.Embed(title="Help", description="`<>` = required, `[]` = optional.", color=0xFECC4D)
    embed.add_field(name="Commands", value="`l!hello`, `l!ping`, `l!8ball <question>`, `l!boom <user>`, `l!invite`, `l!chat <text>`, `l!fact [index]`, `l!randomstory`, `l!aboutme`, `l!when <question>`, `l!helloyesorno <question>`, `l!say <text>`, `l!hug <user>`, `l!attack <user>`, `l!bam <user>`, `l!roll`, `l!hack <user>`, `l!server`, `l!randomsandwich`, `l!poll <text>`, `l!suggest <text>`, `l!weirdtext`, `l!dostuff`, `l!embed <title> | <description>`, `l!math <number> <operation> <number>`, `l!sweatsmile`, `l!randnum <min> <max>`, `l!bobux`, `l!morecookis`, `l!work`, `l!bal [user]`, `l!dep <value>`, `l!with <value>`, `l!lb`, `l!shop`, `l!buy [amount]`, `l!inv [user]`, `l!use [amount]`, `l!give_money <user> <amount>`, `l!reset_money`, `l!give_item <user> [amount]`, `l!rob <user> <amount>`, `l!text_to_wotcode <user>`, `l!wotcode_to_text <user>`, `l!name`, `l!sandwich <size>`", inline=False)
    embed.set_footer(text="lel")
    await inter.send(embed=embed)

@client.command(aliases=['classic_help'])
async def classic_help2(inter):
    embed=discord.Embed(title="Help", description="`<>` = required, `[]` = optional.", color=0xFECC4D)
    embed.add_field(name="Commands", value="`l!hello`, `l!ping`, `l!8ball <question>`, `l!boom <user>`, `l!invite`, `l!chat <text>`, `l!fact [index]`, `l!randomstory`, `l!aboutme`, `l!when <question>`, `l!helloyesorno <question>`, `l!say <text>`, `l!hug <user>`, `l!attack <user>`, `l!bam <user>`, `l!roll`, `l!hack <user>`, `l!server`, `l!randomsandwich`, `l!poll <text>`, `l!suggest <text>`, `l!weirdtext`, `l!dostuff`, `l!embed <title> | <description>`, `l!math <number> <operation> <number>`, `l!sweatsmile`, `l!randnum <min> <max>`, `l!bobux`, `l!morecookis`, `l!work`, `l!bal [user]`, `l!dep <value>`, `l!with <value>`, `l!lb`, `l!shop`, `l!buy [amount]`, `l!inv [user]`, `l!use [amount]`, `l!give_money <user> <amount>`, `l!reset_money`, `l!give_item <user> [amount]`, `l!rob <user> <amount>`, `l!text_to_wotcode <user>`, `l!wotcode_to_text <user>`, `l!name`, `l!sandwich <size>`", inline=False)
    embed.set_footer(text="lel")
    await inter.send(embed=embed)

@inter_client.slash_command(description="Children of tommorow will have no understanding of the english language")
async def wotcode(inter):
    pass

@wotcode.sub_command(description="Convert your text to wotcode",options=[Option("text","The text that will be converted",OptionType.STRING,required=True)])
async def text_to_wotcode(inter,text):
    text = text.lower()
    text = text.replace("a","⏬")
    text = text.replace("b","⛺")
    text = text.replace("c","⚫")
    text = text.replace("d","❌")
    text = text.replace("e","➕")
    text = text.replace("f","⛳")
    text = text.replace("g","⏪")
    text = text.replace("h","☝")
    text = text.replace("i","⏳")
    text = text.replace("j","☕")
    text = text.replace("k","⛹")
    text = text.replace("l","⛲")
    text = text.replace("m","✋")
    text = text.replace("n","⚓")
    text = text.replace("o","✊")
    text = text.replace("p","⚽")
    text = text.replace("q","♋")
    text = text.replace("r","⬛")
    text = text.replace("s","⏰")
    text = text.replace("t","❎")
    text = text.replace("u","⛪")
    text = text.replace("v","♎")
    text = text.replace("w","☔")
    text = text.replace("x","✍")
    text = text.replace("y","⛔")
    text = text.replace("z","⚡")
    await inter.reply(f"`{text}`\n\n- {inter.author.mention}")

@wotcode.sub_command(description="Convert wotcode to text",options=[Option("text","The text that will be converted",OptionType.STRING,required=True)])
async def wotcode_to_text(inter,text):
    text = text.replace("⏬","a")
    text = text.replace("⛺","b")
    text = text.replace("⚫","c")
    text = text.replace("❌","d")
    text = text.replace("➕","e")
    text = text.replace("⛳","f")
    text = text.replace("⏪","g")
    text = text.replace("☝","h")
    text = text.replace("⏳","i")
    text = text.replace("☕","j")
    text = text.replace("⛹","k")
    text = text.replace("⛲","l")
    text = text.replace("✋","m")
    text = text.replace("⚓","n")
    text = text.replace("✊","o")
    text = text.replace("⚽","p")
    text = text.replace("♋","q")
    text = text.replace("⬛","r")
    text = text.replace("⏰","s")
    text = text.replace("❎","t")
    text = text.replace("⛪","u")
    text = text.replace("♎","v")
    text = text.replace("☔","w")
    text = text.replace("✍","x")
    text = text.replace("⛔","y")
    text = text.replace("⚡","z")
    text = text.upper()
    await inter.reply(f"`{text}`\n\n- {inter.author.mention}")

@inter_client.slash_command(description="Give random name to a random thing")
async def name(inter):
    thing = [':cat:',":dog:",":chair:",":package:",":bed:",":wastebasket:",":coffee:",":printer:",":couch:","👩","🧑","👧","👩‍🦰","👶","👴","👨‍🦳","👨‍🦲","👱‍♂️","🙎","🧏","🤦","🤷","💇","🏃","🤸","🐵","🐺","🐯","🦒","🦊","🦝","🐮","🐷","🐹","🐰","🐻","🐼","🐸","🦓","🐴","🐔","🐳","🐟","🐘"]
    name = ["Michael","Steve","Bob","Henry","Carl","Mark","Tom","John","Alan","James","Jack","Thomas","Martin","Susan","Paul","Mike","Michalan","Alanalex","Alex"]
    await inter.send(f"{random.choice(thing)}\n:point_up: {random.choice(name)}")

@client.command(aliases=['name'])
async def name2(inter):
    thing = [':cat:',":dog:",":chair:",":package:",":bed:",":wastebasket:",":coffee:",":printer:",":couch:","👩","🧑","👧","👩‍🦰","👶","👴","👨‍🦳","👨‍🦲","👱‍♂️","🙎","🧏","🤦","🤷","💇","🏃","🤸","🐵","🐺","🐯","🦒","🦊","🦝","🐮","🐷","🐹","🐰","🐻","🐼","🐸","🦓","🐴","🐔","🐳","🐟","🐘"]
    name = ["Michael","Steve","Bob","Henry","Carl","Mark","Tom","John","Alan","James","Jack","Thomas","Martin","Susan","Paul","Mike","Michalan","Alex"]
    await inter.send(f"{random.choice(thing)}\n:point_up: {random.choice(name)}")

@inter_client.slash_command(description="Build a sandwich",options=[Option("size","The size of your sandwich",OptionType.INTEGER,required=True)])
async def sandwich(inter,size):
    stuff = [":tomato:",":leafy_green:",":cucumber:",":hot_pepper:",":corn:",":carrot:",":onion:",":potato:",":cheese:",":egg:",":butter:",":bacon:",":cut_of_meat:",":poultry_leg:",":meat_on_bone:"]
    counter = 0
    sandwich = ""
    if size < 26:
        while counter < size:
            sandwich = sandwich + "\n" + random.choice(stuff)
            counter += 1
        await inter.reply(f":bread:{sandwich}\n:bread:")
    else:
        await inter.reply("How you're gonna eat that <:lelcube:811058465383514132>")

@client.command(aliases=['sandwich'])
async def sandwich2(inter,size):
    try:
        size = int(size)
        stuff = [":tomato:",":leafy_green:",":cucumber:",":hot_pepper:",":corn:",":carrot:",":onion:",":potato:",":cheese:",":egg:",":butter:",":bacon:",":cut_of_meat:",":poultry_leg:",":meat_on_bone:"]
        counter = 0
        sandwich = ""
        if size < 26:
            while counter < size:
                sandwich = sandwich + "\n" + random.choice(stuff)
                counter += 1
            await inter.reply(f":bread:{sandwich}\n:bread:")
        else:
            await inter.reply("How you're gonna eat that <:lelcube:811058465383514132>")
    except:
        await inter.reply("The size needs to be a number")

@client.command(aliases=['text_to_wotcode'])
async def text_to_wotcode2(inter,*,text):
    text = text.lower()
    text = text.replace("a","⏬")
    text = text.replace("b","⛺")
    text = text.replace("c","⚫")
    text = text.replace("d","❌")
    text = text.replace("e","➕")
    text = text.replace("f","⛳")
    text = text.replace("g","⏪")
    text = text.replace("h","☝")
    text = text.replace("i","⏳")
    text = text.replace("j","☕")
    text = text.replace("k","⛹")
    text = text.replace("l","⛲")
    text = text.replace("m","✋")
    text = text.replace("n","⚓")
    text = text.replace("o","✊")
    text = text.replace("p","⚽")
    text = text.replace("q","♋")
    text = text.replace("r","⬛")
    text = text.replace("s","⏰")
    text = text.replace("t","❎")
    text = text.replace("u","⛪")
    text = text.replace("v","♎")
    text = text.replace("w","☔")
    text = text.replace("x","✍")
    text = text.replace("y","⛔")
    text = text.replace("z","⚡")
    await inter.reply(f"`{text}`\n\n- {inter.author.mention}")

@client.command(aliases=['wotcode_to_text'])
async def wotcode_to_text2(inter,*,text):
    text = text.replace("⏬","a")
    text = text.replace("⛺","b")
    text = text.replace("⚫","c")
    text = text.replace("❌","d")
    text = text.replace("➕","e")
    text = text.replace("⛳","f")
    text = text.replace("⏪","g")
    text = text.replace("☝","h")
    text = text.replace("⏳","i")
    text = text.replace("☕","j")
    text = text.replace("⛹","k")
    text = text.replace("⛲","l")
    text = text.replace("✋","m")
    text = text.replace("⚓","n")
    text = text.replace("✊","o")
    text = text.replace("⚽","p")
    text = text.replace("♋","q")
    text = text.replace("⬛","r")
    text = text.replace("⏰","s")
    text = text.replace("❎","t")
    text = text.replace("⛪","u")
    text = text.replace("♎","v")
    text = text.replace("☔","w")
    text = text.replace("✍","x")
    text = text.replace("⛔","y")
    text = text.replace("⚡","z")
    text = text.upper()
    await inter.reply(f"`{text}`\n\n- {inter.author.mention}")

@inter_client.slash_command(description="Make a sentence, will it be nonsense? (yes)",options=[Option("dumbness","How smort lelbot will be when making the sentence",OptionType.INTEGER,required=True,choices=[OptionChoice("Smart",1),OptionChoice("n ot so smaort",2),OptionChoice("fjhsdkmnfbekjnsdnfjls",3)])])
async def sentence(inter,dumbness):
    nouns = ['eye', 'thought', 'hospital', 'bath', 'order', 'finger', 'drink', 'development', 'run', 'rabbit', 'quartz', 'baseball', 'spark', 'point', 'square', 'boat', 'shape', 'dock', 'vegetable', 'play', 'stream', 'boot', 'plantation', 'visitor', 'industry', 'work', 'lunchroom', 'view', 'hair', 'temper', 'passenger', 'price', 'food', 'gate', 'toothbrush', 'ice', 'shame', 'cherries', 'island', 'butter', 'receipt', 'friend', 'action', 'seat', 'van', 'hope', 'regret', 'cactus', 'peace', 'discussion', 'ghost', 'team', 'measure', 'idea', 'children', 'oil', 'pipe', 'bomb', 'car', 'wind', 'shirt', 'trade', 'wine', 'eyes', 'friends', 'rose', 'spring', 'acoustics', 'leg', 'edge', 'sugar', 'stretch', 'meat', 'daughter', 'surprise', 'science', 'behavior', 'argument', 'chance', 'size', 'suit', 'hand', 'marble', 'number', 'canvas', 'fish', 'bone', 'cup', 'grade', 'sidewalk', 'root', 'trucks', 'women', 'flowers', 'rat', 'fog', 'tooth', 'bed', 'week', 'hat', 'mom', 'interest', 'fork', 'notebook', 'celery', 'fold', 'pot', 'ray', 'camera', 'sail', 'quiet', 'blow', 'jam', 'rule', 'position', 'front', 'condition', 'zoo', 'minister', 'year', 'thumb', 'route', 'umbrella', 'farm', 'wing', 'hole', 'stocking', 'dust', 'ants', 'doctor', 'destruction', 'water', 'birthday', 'cloth', 'border', 'laugh', 'show', 'fireman', 'town', 'appliance', 'knowledge', 'sofa', 'afternoon', 'attack', 'pan', 'bee', 'rhythm', 'blade', 'man', 'steam', 'drop', 'roll', 'potato', 'string', 'teaching', 'cent', 'card', 'honey', 'grape', 'kiss', 'eggs', 'beef', 'religion', 'dinner', 'ocean', 'story', 'sound', 'camp', 'smash', 'current', 'driving', 'shake', 'basket', 'baby', 'adjustment', 'wire', 'arithmetic', 'cat', 'esophagus']
    adj = ['tangible', 'delightful', 'lyrical', 'wakeful', 'free', 'relieved', 'arrogant', 'worthless', 'awesome', 'stupendous', 'mixed', 'rough', 'long-term', 'illustrious', 'anxious', 'typical', 'straight', 'tremendous', 'striped', 'overt', 'jittery', 'empty', 'stereotyped', 'impolite', 'broken', 'superficial', 'open', 'cheerful', 'fixed', 'equable', 'large', 'hanging', 'hungry', 'unaccountable', 'bizarre', 'few', 'wealthy', 'successful', 'depressed', 'grey', 'deep', 'enchanting', 'married', 'huge', 'black-and-white', 'sincere', 'receptive', 'hard', 'marvelous', 'tired', 'handsomely', 'hilarious', 'clear', 'drunk', 'dependent', 'glossy', 'noxious', 'untidy', 'hot', 'snotty', 'magenta', 'chilly', 'organic', 'dangerous', 'sad', 'different', 'overconfident', 'understood', 'wonderful', 'utopian', 'fascinated', 'boring', 'lame', 'bouncy', 'apathetic', 'materialistic', 'lazy', 'adorable', 'selfish', 'lucky', 'sneaky', 'witty', 'possessive', 'rotten', 'parallel', 'disgusting', 'medical', 'harmonious', 'tested', 'important', 'unnatural', 'uncovered', 'clever', 'habitual', 'kindly', 'daily', 'busy', 'fine', 'enchanted', 'brave', 'two', 'enthusiastic', 'pointless', 'easy', 'inconclusive', 'abject', 'fantastic', 'spicy', 'normal', 'damaged', 'dry', 'disastrous', 'difficult', 'lethal', 'valuable', 'silent', 'lonely', 'square', 'female', 'grumpy', 'slow', 'innocent', 'poor', 'thirsty', 'embarrassed', 'messy', 'necessary', 'sleepy', 'even', 'best']
    verbs = ['trouble', 'memorize', 'force', 'label', 'return', 'practice', 'punch', 'disapprove', 'serve', 'separate', 'paint', 'plug', 'exercise', 'squeeze', 'pretend', 'attempt', 'command', 'copy', 'form', 'time', 'note', 'taste', 'question', 'plant', 'jail', 'manage', 'reduce', 'rescue', 'list', 'grab', 'regret', 'obtain', 'interest', 'shade', 'nod', 'hang', 'ruin', 'cheer', 'harm', 'rely', 'record', 'unpack', 'deliver', 'cough', 'listen', 'doubt', 'include', 'gather', 'cheat', 'call', 'trap', 'protect', 'connect', 'cover', 'fix', 'reply', 'remain', 'long', 'blind', 'clap', 'encourage', 'help', 'start', 'identify', 'offend', 'embarrass', 'supply', 'try', 'ban', 'compare', 'please', 'welcome', 'dream', 'attract', 'move', 'impress', 'float', 'plan', 'double', 'remind', 'support', 'level', 'desert', 'part', 'contain', 'unlock', 'judge', 'scream', 'rob', 'develop', 'suspend', 'annoy', 'reproduce', 'rain', 'program', 'launch', 'burn', 'hop', 'dance', 'last', 'accept', 'push', 'press', 'heal', 'permit', 'load', 'melt', 'rock', 'talk', 'notice', 'learn', 'match', 'breathe', 'polish', 'undress', 'interfere', 'succeed', 'like', 'twist', 'happen', 'smell', 'slap', 'hate', 'worry', 'handle', 'report', 'complete', 'lie', 'want', 'phone', 'marry', 'analyze', 'smoke']
    amount = ['some', 'a lot', 'many', 'almost all', 'all', 'every single', 'quite a lot', 'not quite a lot', 'a huge amount of', 'a small amount of', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'hundreds of', 'thousands of', 'millions of', 'billions of', 'infinity']
    
    if dumbness == 3:
        tha_ultimate_combo_lol = [nouns,adj,verbs,amount,amount]

        c = 0
        when_the = ""
        while c < 10:
            ues = random.choice(tha_ultimate_combo_lol)
            more_ues = random.choice(ues)
            when_the = when_the + more_ues + " "
            c += 1
    
        await inter.reply(when_the)
    if dumbness == 2:
        when_the = random.choice(amount) + " " + random.choice(adj) + " " + random.choice(nouns) + " " + random.choice(verbs) + " " + random.choice(nouns)
        await inter.reply(when_the)
    if dumbness == 1:
        nouns = ['eye', 'thought', 'hospital', 'bath', 'order', 'finger', 'drink', 'development', 'run', 'rabbit', 'quartz', 'baseball', 'spark', 'point', 'square', 'boat', 'shape', 'dock', 'vegetable', 'play', 'stream', 'boot', 'plantation', 'visitor', 'industry', 'work', 'lunchroom', 'view', 'hair', 'temper', 'passenger', 'price', 'food', 'gate', 'toothbrush', 'ice', 'shame', 'cherries', 'island', 'butter', 'receipt', 'friend', 'action', 'seat', 'van', 'hope', 'regret', 'cactus', 'peace', 'discussion', 'ghost', 'team', 'measure', 'idea', 'children', 'oil', 'pipe', 'bomb', 'car', 'wind', 'shirt', 'trade', 'wine', 'eyes', 'friends', 'rose', 'spring', 'acoustics', 'leg', 'edge', 'sugar', 'stretch', 'meat', 'daughter', 'surprise', 'science', 'behavior', 'argument', 'chance', 'size', 'suit', 'hand', 'marble', 'number', 'canvas', 'fish', 'bone', 'cup', 'grade', 'sidewalk', 'root', 'trucks', 'women', 'flowers', 'rat', 'fog', 'tooth', 'bed', 'week', 'hat', 'mom', 'interest', 'fork', 'notebook', 'celery', 'fold', 'pot', 'ray', 'camera', 'sail', 'quiet', 'blow', 'jam', 'rule', 'position', 'front', 'condition', 'zoo', 'minister', 'year', 'thumb', 'route', 'umbrella', 'farm', 'wing', 'hole', 'stocking', 'dust', 'ants', 'doctor', 'destruction', 'water', 'birthday', 'cloth', 'border', 'laugh', 'show', 'fireman', 'town', 'appliance', 'knowledge', 'sofa', 'afternoon', 'attack', 'pan', 'bee', 'rhythm', 'blade', 'man', 'steam', 'drop', 'roll', 'potato', 'string', 'teaching', 'cent', 'card', 'honey', 'grape', 'kiss', 'eggs', 'beef', 'religion', 'dinner', 'ocean', 'story', 'sound', 'camp', 'smash', 'current', 'driving', 'shake', 'basket', 'baby', 'adjustment', 'wire', 'arithmetic', 'cat', 'esophagus']
        plural_nouns = ['eyes', 'thoughts', 'hospitals', 'baths', 'orders', 'fingers', 'drinks', 'developments', 'runs', 'rabbits', 'quartz', 'baseballs', 'sparks', 'points', 'squares', 'boats', 'shapes', 'docks', 'vegetables', 'plays', 'streams', 'boots', 'plantations', 'visitors', 'industrys', 'works', 'lunchrooms', 'views', 'hairs', 'tempers', 'passengers', 'prices', 'foods', 'gates', 'toothbrushes', 'ices', 'shames', 'cherries', 'islands', 'butters', 'receipts', 'friends', 'actions', 'seats', 'vans', 'hopes', 'regrets', 'cactuses', 'peaces', 'discussions', 'ghosts', 'teams', 'measures', 'ideas', 'childrens', 'oils', 'pipes', 'bombs', 'cars', 'winds', 'shirts', 'trades', 'wines', 'eyes', 'friends', 'roses', 'springs', 'acoustics', 'legs', 'edges', 'sugars', 'stretchs', 'meats', 'daughters', 'surprises', 'sciences', 'behaviors', 'arguments', 'chances', 'sizes', 'suits', 'hands', 'marbles', 'numbers', 'canvases', 'fishes', 'bones', 'cups', 'grades', 'sidewalks', 'roots', 'trucks', 'womens', 'flowers', 'rats', 'fogs', 'tooths', 'beds', 'weeks', 'hats', 'moms', 'interests', 'forks', 'notebooks', 'celerys', 'folds', 'pots', 'rays', 'cameras', 'sails', 'quiets', 'blows', 'jams', 'rules', 'positions', 'fronts', 'conditions', 'zoos', 'ministers', 'years', 'thumbs', 'routes', 'umbrellas', 'farms', 'wings', 'holes', 'stockings', 'dusts', 'ants', 'doctors', 'destructions', 'waters', 'birthdays', 'clothes', 'borders', 'laughs', 'shows', 'firemans', 'towns', 'appliances', 'knowledges', 'sofas', 'afternoons', 'attacks', 'pans', 'bees', 'rhythms', 'blades', 'mans', 'steams', 'drops', 'rolls', 'potatos', 'strings', 'teachings', 'cents', 'cards', 'honeys', 'grapes', 'kisses', 'eggs', 'beefs', 'religions', 'dinners', 'oceans', 'stories', 'sounds', 'camps', 'smashes', 'currents', 'drivings', 'shakes', 'baskets', 'babies', 'adjustments', 'wires', 'arithmetics', 'cats', 'esophaguses']
        adj = ['tangible', 'delightful', 'lyrical', 'wakeful', 'free', 'relieved', 'arrogant', 'worthless', 'awesome', 'stupendous', 'mixed', 'rough', 'long-term', 'illustrious', 'anxious', 'typical', 'straight', 'tremendous', 'striped', 'overt', 'jittery', 'empty', 'stereotyped', 'impolite', 'broken', 'superficial', 'open', 'cheerful', 'fixed', 'equable', 'large', 'hanging', 'hungry', 'unaccountable', 'bizarre', 'few', 'wealthy', 'successful', 'depressed', 'grey', 'deep', 'enchanting', 'married', 'huge', 'black-and-white', 'sincere', 'receptive', 'hard', 'marvelous', 'tired', 'handsomely', 'hilarious', 'clear', 'drunk', 'dependent', 'glossy', 'noxious', 'untidy', 'hot', 'snotty', 'magenta', 'chilly', 'organic', 'dangerous', 'sad', 'different', 'overconfident', 'understood', 'wonderful', 'utopian', 'fascinated', 'boring', 'lame', 'bouncy', 'apathetic', 'materialistic', 'lazy', 'adorable', 'selfish', 'lucky', 'sneaky', 'witty', 'possessive', 'rotten', 'parallel', 'disgusting', 'medical', 'harmonious', 'tested', 'important', 'unnatural', 'uncovered', 'clever', 'habitual', 'kindly', 'daily', 'busy', 'fine', 'enchanted', 'brave', 'two', 'enthusiastic', 'pointless', 'easy', 'inconclusive', 'abject', 'fantastic', 'spicy', 'normal', 'damaged', 'dry', 'disastrous', 'difficult', 'lethal', 'valuable', 'silent', 'lonely', 'square', 'female', 'grumpy', 'slow', 'innocent', 'poor', 'thirsty', 'embarrassed', 'messy', 'necessary', 'sleepy', 'even', 'best']
        verbs = ['trouble', 'memorize', 'force', 'label', 'return', 'practice', 'punch', 'disapprove', 'serve', 'separate', 'paint', 'plug', 'exercise', 'squeeze', 'pretend', 'attempt', 'command', 'copy', 'form', 'time', 'note', 'taste', 'question', 'plant', 'jail', 'manage', 'reduce', 'rescue', 'list', 'grab', 'regret', 'obtain', 'interest', 'shade', 'nod', 'hang', 'ruin', 'cheer', 'harm', 'rely', 'record', 'unpack', 'deliver', 'cough', 'listen', 'doubt', 'include', 'gather', 'cheat', 'call', 'trap', 'protect', 'connect', 'cover', 'fix', 'reply', 'remain', 'long', 'blind', 'clap', 'encourage', 'help', 'start', 'identify', 'offend', 'embarrass', 'supply', 'try', 'ban', 'compare', 'please', 'welcome', 'dream', 'attract', 'move', 'impress', 'float', 'plan', 'double', 'remind', 'support', 'level', 'desert', 'part', 'contain', 'unlock', 'judge', 'scream', 'rob', 'develop', 'suspend', 'annoy', 'reproduce', 'rain', 'program', 'launch', 'burn', 'hop', 'dance', 'last', 'accept', 'push', 'press', 'heal', 'permit', 'load', 'melt', 'rock', 'talk', 'notice', 'learn', 'match', 'breathe', 'polish', 'undress', 'interfere', 'succeed', 'like', 'twist', 'happen', 'smell', 'slap', 'hate', 'worry', 'handle', 'report', 'complete', 'lie', 'want', 'phone', 'marry', 'analyze', 'smoke']
        multiple_amount = ['some', 'a lot of', 'many', 'almost all of the', 'all', 'quite a lot of', 'not quite a lot of', 'a huge amount of', 'a small amount of', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'hundreds of', 'thousands of', 'millions of', 'billions of', 'infinity']
        not_multiple_amount = ['a','1','every single']

        is_plural = random.randint(0,1)
        if is_plural == 0:
            noun = random.choice(nouns)
            amount = random.choice(not_multiple_amount)
            a = random.choice(adj)
            if amount == "a":
                if a.startswith("a") == True or a.startswith("e") == True or a.startswith("i") == True or a.startswith("o") == True or a.startswith("u") == True:
                    amount = "an"
        else:
            noun = random.choice(plural_nouns)
            amount = random.choice(multiple_amount)
            a = random.choice(adj)
        
        print(is_plural)
        message = amount + " " + a + " " + noun + " " + random.choice(verbs) + " " + random.choice(plural_nouns)
        message = message.capitalize()
        await inter.reply(message)

@client.command(aliases=["sentence"])
async def sentence2(inter):
    msg = await inter.reply("How smort lelbot will be when making the sentence?",components=[
              SelectMenu(
                  custom_id="list",
                  placeholder="ues",
                  max_values=1,
                  options=[
                      SelectOption("Smart", 1),
                      SelectOption("notso smort", 2),
                      SelectOption("fjhsdkmnfbekjnsdnfjls", 3)
                  ]
              )
          ]
    )

    oldinter = inter
    inter = await msg.wait_for_dropdown()
    if inter.author.id == oldinter.author.id:
        labels = [option.label for option in inter.select_menu.selected_options]
        dumbness = "#".join(labels)
        
        nouns = ['eye', 'thought', 'hospital', 'bath', 'order', 'finger', 'drink', 'development', 'run', 'rabbit', 'quartz', 'baseball', 'spark', 'point', 'square', 'boat', 'shape', 'dock', 'vegetable', 'play', 'stream', 'boot', 'plantation', 'visitor', 'industry', 'work', 'lunchroom', 'view', 'hair', 'temper', 'passenger', 'price', 'food', 'gate', 'toothbrush', 'ice', 'shame', 'cherries', 'island', 'butter', 'receipt', 'friend', 'action', 'seat', 'van', 'hope', 'regret', 'cactus', 'peace', 'discussion', 'ghost', 'team', 'measure', 'idea', 'children', 'oil', 'pipe', 'bomb', 'car', 'wind', 'shirt', 'trade', 'wine', 'eyes', 'friends', 'rose', 'spring', 'acoustics', 'leg', 'edge', 'sugar', 'stretch', 'meat', 'daughter', 'surprise', 'science', 'behavior', 'argument', 'chance', 'size', 'suit', 'hand', 'marble', 'number', 'canvas', 'fish', 'bone', 'cup', 'grade', 'sidewalk', 'root', 'trucks', 'women', 'flowers', 'rat', 'fog', 'tooth', 'bed', 'week', 'hat', 'mom', 'interest', 'fork', 'notebook', 'celery', 'fold', 'pot', 'ray', 'camera', 'sail', 'quiet', 'blow', 'jam', 'rule', 'position', 'front', 'condition', 'zoo', 'minister', 'year', 'thumb', 'route', 'umbrella', 'farm', 'wing', 'hole', 'stocking', 'dust', 'ants', 'doctor', 'destruction', 'water', 'birthday', 'cloth', 'border', 'laugh', 'show', 'fireman', 'town', 'appliance', 'knowledge', 'sofa', 'afternoon', 'attack', 'pan', 'bee', 'rhythm', 'blade', 'man', 'steam', 'drop', 'roll', 'potato', 'string', 'teaching', 'cent', 'card', 'honey', 'grape', 'kiss', 'eggs', 'beef', 'religion', 'dinner', 'ocean', 'story', 'sound', 'camp', 'smash', 'current', 'driving', 'shake', 'basket', 'baby', 'adjustment', 'wire', 'arithmetic', 'cat', 'esophagus']
        adj = ['tangible', 'delightful', 'lyrical', 'wakeful', 'free', 'relieved', 'arrogant', 'worthless', 'awesome', 'stupendous', 'mixed', 'rough', 'long-term', 'illustrious', 'anxious', 'typical', 'straight', 'tremendous', 'striped', 'overt', 'jittery', 'empty', 'stereotyped', 'impolite', 'broken', 'superficial', 'open', 'cheerful', 'fixed', 'equable', 'large', 'hanging', 'hungry', 'unaccountable', 'bizarre', 'few', 'wealthy', 'successful', 'depressed', 'grey', 'deep', 'enchanting', 'married', 'huge', 'black-and-white', 'sincere', 'receptive', 'hard', 'marvelous', 'tired', 'handsomely', 'hilarious', 'clear', 'drunk', 'dependent', 'glossy', 'noxious', 'untidy', 'hot', 'snotty', 'magenta', 'chilly', 'organic', 'dangerous', 'sad', 'different', 'overconfident', 'understood', 'wonderful', 'utopian', 'fascinated', 'boring', 'lame', 'bouncy', 'apathetic', 'materialistic', 'lazy', 'adorable', 'selfish', 'lucky', 'sneaky', 'witty', 'possessive', 'rotten', 'parallel', 'disgusting', 'medical', 'harmonious', 'tested', 'important', 'unnatural', 'uncovered', 'clever', 'habitual', 'kindly', 'daily', 'busy', 'fine', 'enchanted', 'brave', 'two', 'enthusiastic', 'pointless', 'easy', 'inconclusive', 'abject', 'fantastic', 'spicy', 'normal', 'damaged', 'dry', 'disastrous', 'difficult', 'lethal', 'valuable', 'silent', 'lonely', 'square', 'female', 'grumpy', 'slow', 'innocent', 'poor', 'thirsty', 'embarrassed', 'messy', 'necessary', 'sleepy', 'even', 'best']
        verbs = ['trouble', 'memorize', 'force', 'label', 'return', 'practice', 'punch', 'disapprove', 'serve', 'separate', 'paint', 'plug', 'exercise', 'squeeze', 'pretend', 'attempt', 'command', 'copy', 'form', 'time', 'note', 'taste', 'question', 'plant', 'jail', 'manage', 'reduce', 'rescue', 'list', 'grab', 'regret', 'obtain', 'interest', 'shade', 'nod', 'hang', 'ruin', 'cheer', 'harm', 'rely', 'record', 'unpack', 'deliver', 'cough', 'listen', 'doubt', 'include', 'gather', 'cheat', 'call', 'trap', 'protect', 'connect', 'cover', 'fix', 'reply', 'remain', 'long', 'blind', 'clap', 'encourage', 'help', 'start', 'identify', 'offend', 'embarrass', 'supply', 'try', 'ban', 'compare', 'please', 'welcome', 'dream', 'attract', 'move', 'impress', 'float', 'plan', 'double', 'remind', 'support', 'level', 'desert', 'part', 'contain', 'unlock', 'judge', 'scream', 'rob', 'develop', 'suspend', 'annoy', 'reproduce', 'rain', 'program', 'launch', 'burn', 'hop', 'dance', 'last', 'accept', 'push', 'press', 'heal', 'permit', 'load', 'melt', 'rock', 'talk', 'notice', 'learn', 'match', 'breathe', 'polish', 'undress', 'interfere', 'succeed', 'like', 'twist', 'happen', 'smell', 'slap', 'hate', 'worry', 'handle', 'report', 'complete', 'lie', 'want', 'phone', 'marry', 'analyze', 'smoke']
        amount = ['some', 'a lot', 'many', 'almost all', 'all', 'every single', 'quite a lot', 'not quite a lot', 'a huge amount of', 'a small amount of', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'hundreds of', 'thousands of', 'millions of', 'billions of', 'infinity']
        
        if dumbness == "fjhsdkmnfbekjnsdnfjls":
            tha_ultimate_combo_lol = [nouns,adj,verbs,amount,amount]

            c = 0
            when_the = ""
            while c < 10:
                ues = random.choice(tha_ultimate_combo_lol)
                more_ues = random.choice(ues)
                when_the = when_the + more_ues + " "
                c += 1
        
            await msg.edit(content=when_the,components=[])
        if dumbness == "notso smort":
            when_the = random.choice(amount) + " " + random.choice(adj) + " " + random.choice(nouns) + " " + random.choice(verbs) + " " + random.choice(nouns)
            await msg.edit(content=when_the,components=[])
        if dumbness == "Smart":
            nouns = ['eye', 'thought', 'hospital', 'bath', 'order', 'finger', 'drink', 'development', 'run', 'rabbit', 'quartz', 'baseball', 'spark', 'point', 'square', 'boat', 'shape', 'dock', 'vegetable', 'play', 'stream', 'boot', 'plantation', 'visitor', 'industry', 'work', 'lunchroom', 'view', 'hair', 'temper', 'passenger', 'price', 'food', 'gate', 'toothbrush', 'ice', 'shame', 'cherries', 'island', 'butter', 'receipt', 'friend', 'action', 'seat', 'van', 'hope', 'regret', 'cactus', 'peace', 'discussion', 'ghost', 'team', 'measure', 'idea', 'children', 'oil', 'pipe', 'bomb', 'car', 'wind', 'shirt', 'trade', 'wine', 'eyes', 'friends', 'rose', 'spring', 'acoustics', 'leg', 'edge', 'sugar', 'stretch', 'meat', 'daughter', 'surprise', 'science', 'behavior', 'argument', 'chance', 'size', 'suit', 'hand', 'marble', 'number', 'canvas', 'fish', 'bone', 'cup', 'grade', 'sidewalk', 'root', 'trucks', 'women', 'flowers', 'rat', 'fog', 'tooth', 'bed', 'week', 'hat', 'mom', 'interest', 'fork', 'notebook', 'celery', 'fold', 'pot', 'ray', 'camera', 'sail', 'quiet', 'blow', 'jam', 'rule', 'position', 'front', 'condition', 'zoo', 'minister', 'year', 'thumb', 'route', 'umbrella', 'farm', 'wing', 'hole', 'stocking', 'dust', 'ants', 'doctor', 'destruction', 'water', 'birthday', 'cloth', 'border', 'laugh', 'show', 'fireman', 'town', 'appliance', 'knowledge', 'sofa', 'afternoon', 'attack', 'pan', 'bee', 'rhythm', 'blade', 'man', 'steam', 'drop', 'roll', 'potato', 'string', 'teaching', 'cent', 'card', 'honey', 'grape', 'kiss', 'eggs', 'beef', 'religion', 'dinner', 'ocean', 'story', 'sound', 'camp', 'smash', 'current', 'driving', 'shake', 'basket', 'baby', 'adjustment', 'wire', 'arithmetic', 'cat', 'esophagus']
            plural_nouns = ['eyes', 'thoughts', 'hospitals', 'baths', 'orders', 'fingers', 'drinks', 'developments', 'runs', 'rabbits', 'quartz', 'baseballs', 'sparks', 'points', 'squares', 'boats', 'shapes', 'docks', 'vegetables', 'plays', 'streams', 'boots', 'plantations', 'visitors', 'industrys', 'works', 'lunchrooms', 'views', 'hairs', 'tempers', 'passengers', 'prices', 'foods', 'gates', 'toothbrushes', 'ices', 'shames', 'cherries', 'islands', 'butters', 'receipts', 'friends', 'actions', 'seats', 'vans', 'hopes', 'regrets', 'cactuses', 'peaces', 'discussions', 'ghosts', 'teams', 'measures', 'ideas', 'childrens', 'oils', 'pipes', 'bombs', 'cars', 'winds', 'shirts', 'trades', 'wines', 'eyes', 'friends', 'roses', 'springs', 'acoustics', 'legs', 'edges', 'sugars', 'stretchs', 'meats', 'daughters', 'surprises', 'sciences', 'behaviors', 'arguments', 'chances', 'sizes', 'suits', 'hands', 'marbles', 'numbers', 'canvases', 'fishes', 'bones', 'cups', 'grades', 'sidewalks', 'roots', 'trucks', 'womens', 'flowers', 'rats', 'fogs', 'tooths', 'beds', 'weeks', 'hats', 'moms', 'interests', 'forks', 'notebooks', 'celerys', 'folds', 'pots', 'rays', 'cameras', 'sails', 'quiets', 'blows', 'jams', 'rules', 'positions', 'fronts', 'conditions', 'zoos', 'ministers', 'years', 'thumbs', 'routes', 'umbrellas', 'farms', 'wings', 'holes', 'stockings', 'dusts', 'ants', 'doctors', 'destructions', 'waters', 'birthdays', 'clothes', 'borders', 'laughs', 'shows', 'firemans', 'towns', 'appliances', 'knowledges', 'sofas', 'afternoons', 'attacks', 'pans', 'bees', 'rhythms', 'blades', 'mans', 'steams', 'drops', 'rolls', 'potatos', 'strings', 'teachings', 'cents', 'cards', 'honeys', 'grapes', 'kisses', 'eggs', 'beefs', 'religions', 'dinners', 'oceans', 'stories', 'sounds', 'camps', 'smashes', 'currents', 'drivings', 'shakes', 'baskets', 'babies', 'adjustments', 'wires', 'arithmetics', 'cats', 'esophaguses']
            adj = ['tangible', 'delightful', 'lyrical', 'wakeful', 'free', 'relieved', 'arrogant', 'worthless', 'awesome', 'stupendous', 'mixed', 'rough', 'long-term', 'illustrious', 'anxious', 'typical', 'straight', 'tremendous', 'striped', 'overt', 'jittery', 'empty', 'stereotyped', 'impolite', 'broken', 'superficial', 'open', 'cheerful', 'fixed', 'equable', 'large', 'hanging', 'hungry', 'unaccountable', 'bizarre', 'few', 'wealthy', 'successful', 'depressed', 'grey', 'deep', 'enchanting', 'married', 'huge', 'black-and-white', 'sincere', 'receptive', 'hard', 'marvelous', 'tired', 'handsomely', 'hilarious', 'clear', 'drunk', 'dependent', 'glossy', 'noxious', 'untidy', 'hot', 'snotty', 'magenta', 'chilly', 'organic', 'dangerous', 'sad', 'different', 'overconfident', 'understood', 'wonderful', 'utopian', 'fascinated', 'boring', 'lame', 'bouncy', 'apathetic', 'materialistic', 'lazy', 'adorable', 'selfish', 'lucky', 'sneaky', 'witty', 'possessive', 'rotten', 'parallel', 'disgusting', 'medical', 'harmonious', 'tested', 'important', 'unnatural', 'uncovered', 'clever', 'habitual', 'kindly', 'daily', 'busy', 'fine', 'enchanted', 'brave', 'two', 'enthusiastic', 'pointless', 'easy', 'inconclusive', 'abject', 'fantastic', 'spicy', 'normal', 'damaged', 'dry', 'disastrous', 'difficult', 'lethal', 'valuable', 'silent', 'lonely', 'square', 'female', 'grumpy', 'slow', 'innocent', 'poor', 'thirsty', 'embarrassed', 'messy', 'necessary', 'sleepy', 'even', 'best']
            verbs = ['trouble', 'memorize', 'force', 'label', 'return', 'practice', 'punch', 'disapprove', 'serve', 'separate', 'paint', 'plug', 'exercise', 'squeeze', 'pretend', 'attempt', 'command', 'copy', 'form', 'time', 'note', 'taste', 'question', 'plant', 'jail', 'manage', 'reduce', 'rescue', 'list', 'grab', 'regret', 'obtain', 'interest', 'shade', 'nod', 'hang', 'ruin', 'cheer', 'harm', 'rely', 'record', 'unpack', 'deliver', 'cough', 'listen', 'doubt', 'include', 'gather', 'cheat', 'call', 'trap', 'protect', 'connect', 'cover', 'fix', 'reply', 'remain', 'long', 'blind', 'clap', 'encourage', 'help', 'start', 'identify', 'offend', 'embarrass', 'supply', 'try', 'ban', 'compare', 'please', 'welcome', 'dream', 'attract', 'move', 'impress', 'float', 'plan', 'double', 'remind', 'support', 'level', 'desert', 'part', 'contain', 'unlock', 'judge', 'scream', 'rob', 'develop', 'suspend', 'annoy', 'reproduce', 'rain', 'program', 'launch', 'burn', 'hop', 'dance', 'last', 'accept', 'push', 'press', 'heal', 'permit', 'load', 'melt', 'rock', 'talk', 'notice', 'learn', 'match', 'breathe', 'polish', 'undress', 'interfere', 'succeed', 'like', 'twist', 'happen', 'smell', 'slap', 'hate', 'worry', 'handle', 'report', 'complete', 'lie', 'want', 'phone', 'marry', 'analyze', 'smoke']
            multiple_amount = ['some', 'a lot of', 'many', 'almost all of the', 'all', 'quite a lot of', 'not quite a lot of', 'a huge amount of', 'a small amount of', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'hundreds of', 'thousands of', 'millions of', 'billions of', 'infinity']
            not_multiple_amount = ['a','1','every single']

            is_plural = random.randint(0,1)
            if is_plural == 0:
                noun = random.choice(nouns)
                amount = random.choice(not_multiple_amount)
                a = random.choice(adj)
                if amount == "a":
                    if a.startswith("a") == True or a.startswith("e") == True or a.startswith("i") == True or a.startswith("o") == True or a.startswith("u") == True:
                        amount = "an"
            else:
                noun = random.choice(plural_nouns)
                amount = random.choice(multiple_amount)
                a = random.choice(adj)
            
            print(is_plural)
            message = amount + " " + a + " " + noun + " " + random.choice(verbs) + " " + random.choice(plural_nouns)
            message = message.capitalize()
            await msg.edit(content=message,components=[])

@inter_client.slash_command(description="Who is [insert someone here]?",options=[Option("someone","The",OptionType.STRING,required=True)])
async def who(inter,someone):
    thing = ['popilol', 'lelcube', 'cube', 'cat', '`furry`', 'dog', 'human', 'banana', 'couch', 'printer', 'monke', 'muffin', 'bot', 'computer', 'snek', 'bread', 'tree', 'box', 'flower', 'planet']
    adj = ['rich', 'poor', 'nonsense', 'lel', 'digital', 'blue', 'red', 'yellow', 'green', 'orange', 'purple', 'pink', 'black', 'white', 'gray', 'boring', 'completely normal', 'fantastic', 'awesome', 'big', 'huge', 'small', 'tiny', 'giant', 'toxic', 'weird', 'heavy', 'simple', 'tall', 'ugly', 'butiful', 'thin', 'invisible']
    place = ['candy land', 'the lelverse', '__**brazil**__', 'another universe', 'a hard drive', 'your imagination', "hellory5n's bot lab with a lot of trash", 'bobux secret laboratory', 'mars', 'the moon', '***a place***', '(x=nan, y=nan, z=nan)', "the place where there's an infinity thing generator", "Windows XP's wallpaper", 'blue void']

    the = "A " + random.choice(adj) + " " + random.choice(thing) + " in " + random.choice(place)
    embed = discord.Embed(title=f"Who {someone}?",description=the,color=0xFECC4D)
    embed.set_footer(text=f"{inter.author} ({str(inter.author.id)})")
    await inter.reply(embed=embed)

@client.command(aliases=['who'])
async def who2(inter,*,someone):
    thing = ['popilol', 'lelcube', 'cube', 'cat', '`furry`', 'dog', 'human', 'banana', 'couch', 'printer', 'monke', 'muffin', 'bot', 'computer', 'snek', 'bread', 'tree', 'box', 'flower', 'planet']
    adj = ['A rich', 'A poor', 'A nonsense', 'A lel', 'A digital', 'A blue', 'A red', 'A yellow', 'A green', 'A orange', 'A purple', 'A pink', 'A black', 'A white', 'A gray', 'A boring', 'A completely normal', 'A fantastic', 'An awesome', 'A big', 'A huge', 'A small', 'A tiny', 'A giant', 'A toxic', 'A weird', 'A heavy', 'A simple', 'A tall', 'An ugly', 'A butiful', 'A thin', 'An invisible']
    place = ['candy land', 'the lelverse', '__**brazil**__', 'another universe', 'a hard drive', 'your imagination', "hellory5n's bot lab with a lot of trash", 'bobux secret laboratory', 'mars', 'the moon', '***a place***', '(x=nan, y=nan, z=nan)', "the place where there's an infinity thing generator", "Windows XP's wallpaper", 'blue void']

    the = random.choice(adj) + " " + random.choice(thing) + " in " + random.choice(place)
    embed = discord.Embed(title=f"Who {someone}?",description=the,color=0xFECC4D)
    embed.set_footer(text=f"{inter.author} ({str(inter.author.id)})")
    await inter.reply(embed=embed)

@inter_client.slash_command(description="ues")
async def snowball(inter):
    pass

@snowball.sub_command(description="Collect snowballs")
@dislash.cooldown(1, 10, commands.BucketType.user)
async def collect(inter):
    with open("snowball_users.txt",'r') as file:
        txt = file.read()
    
    if not str(inter.author.id) in txt:
        txt = txt + "\n" + str(inter.author.id)
        with open("snowball_hits.json",'r') as f:
                b_a_l_l_s = json.load(f)

        b_a_l_l_s[str(inter.author.id)] = 0

        with open("snowball_hits.json",'w') as f:
           json.dump(b_a_l_l_s,f)

    with open("snowball_users.txt",'w') as file:
        file.write(txt)

    with open("snowball_thing.json",'r') as f:
        balls = json.load(f)
    
    ono = False

    try:
        if not balls[str(inter.author.id)] == 5:
            balls[str(inter.author.id)] = balls[str(inter.author.id)] + 1
        else:
            await inter.reply("You have too many snowballs!")
            ono = True
    except:
        balls[str(inter.author.id)] = 1
    
    with open("snowball_thing.json",'w') as f:
        json.dump(balls,f)

    if ono == False:
        if balls[str(inter.author.id)] == 1:
            await inter.reply(":white_circle: <:lelcube:811058465383514132>")
            await inter.reply("You got a snowball!")
        elif balls[str(inter.author.id)] == 2:
            await inter.reply(":white_circle: <:lelcube:811058465383514132> :white_circle:")
            await inter.reply("You got another snowball!")
        elif balls[str(inter.author.id)] == 3:
            await inter.reply("<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n:white_circle: <:lelcube:811058465383514132> :white_circle:")
            await inter.reply("You got another another snowball!")
        elif balls[str(inter.author.id)] == 4:
            await inter.reply("<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n:white_circle: <:lelcube:811058465383514132> :white_circle:")
            await inter.reply("Ok you are getting too many snowballs")
        elif balls[str(inter.author.id)] == 5:
            await inter.reply("<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n:white_circle: <:lelcube:811058465383514132> :white_circle:")
            await inter.reply("Das a lot of snowballs")

@snowball.sub_command(description="Throw snowballs",options=[Option("target","ues",OptionType.STRING,required=True)])
async def throw(inter,target):
    with open("snowball_thing.json",'r') as f:
        balls = json.load(f)
    
    ono = False

    try:
        if not balls[str(inter.author.id)] < 1:
            balls[str(inter.author.id)] = balls[str(inter.author.id)] - 1
        else:
            await inter.reply("<:lelcube:811058465383514132> :thumbsup:")
            await inter.reply("You don't have snowballs")
            ono = True
    except:
        await inter.reply("<:lelcube:811058465383514132> :thumbsup:")
        await inter.reply("You don't have snowballs")
        ono = True

    if ono == False:
        with open("snowball_thing.json",'w') as f:
            json.dump(balls,f)

        ues = random.randint(1,1000)

        if ues > 500:
            with open("snowball_hits.json",'r') as f:
                b_a_l_l_s = json.load(f)

            try:
                b_a_l_l_s[str(inter.author.id)] = b_a_l_l_s[str(inter.author.id)] + 1
            except:
                b_a_l_l_s[str(inter.author.id)] = 1

            with open("snowball_hits.json",'w') as f:
                json.dump(b_a_l_l_s,f)

            await inter.reply(":deaf_person: :arrow_left: :white_circle: <:lelcube:811058465383514132>")
            await inter.reply(f"{inter.author.mention} attacked {target}!")
        else:
            await inter.reply("<:void:834904392008335360> :arrow_upper_left:\n:deaf_person: <:void:834904392008335360> :white_circle: <:lelcube:811058465383514132>")
            await inter.reply(f"{inter.author.mention} missed lol")

@client.command(aliases=['collect','snowball_collect','snow_collect','snowball-collect','snow-collect'])
@commands.cooldown(1, 10, commands.BucketType.user)
async def collect2(inter):
    with open("snowball_users.txt",'r') as file:
        txt = file.read()
    
    if not str(inter.author.id) in txt:
        txt = txt + "\n" + str(inter.author.id)
        with open("snowball_hits.json",'r') as f:
                b_a_l_l_s = json.load(f)

        b_a_l_l_s[str(inter.author.id)] = 0

        with open("snowball_hits.json",'w') as f:
           json.dump(b_a_l_l_s,f)

    with open("snowball_users.txt",'w') as file:
        file.write(txt)

    with open("snowball_thing.json",'r') as f:
        balls = json.load(f)
    
    ono = False

    try:
        if not balls[str(inter.author.id)] == 5:
            balls[str(inter.author.id)] = balls[str(inter.author.id)] + 1
        else:
            await inter.reply("You have too many snowballs!")
            ono = True
    except:
        balls[str(inter.author.id)] = 1
    
    with open("snowball_thing.json",'w') as f:
        json.dump(balls,f)

    if ono == False:
        if balls[str(inter.author.id)] == 1:
            await inter.reply(":white_circle: <:lelcube:811058465383514132>")
            await inter.send("You got a snowball!")
        elif balls[str(inter.author.id)] == 2:
            await inter.reply(":white_circle: <:lelcube:811058465383514132> :white_circle:")
            await inter.send("You got another snowball!")
        elif balls[str(inter.author.id)] == 3:
            await inter.reply("<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n:white_circle: <:lelcube:811058465383514132> :white_circle:")
            await inter.send("You got another another snowball!")
        elif balls[str(inter.author.id)] == 4:
            await inter.reply("<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n:white_circle: <:lelcube:811058465383514132> :white_circle:")
            await inter.send("Ok you are getting too many snowballs")
        elif balls[str(inter.author.id)] == 5:
            await inter.reply("<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n:white_circle: <:lelcube:811058465383514132> :white_circle:")
            await inter.send("Das a lot of snowballs")

@client.command(aliases=['throw','snowball_throw','snow_throw','snowball-throw','snow-throw'])
async def throw2(inter,*,target):
    with open("snowball_thing.json",'r') as f:
        balls = json.load(f)
    
    ono = False

    try:
        if not balls[str(inter.author.id)] < 1:
            balls[str(inter.author.id)] = balls[str(inter.author.id)] - 1
        else:
            await inter.reply("<:lelcube:811058465383514132> :thumbsup:")
            await inter.reply("You don't have snowballs")
            ono = True
    except:
        await inter.reply("<:lelcube:811058465383514132> :thumbsup:")
        await inter.reply("You don't have snowballs")
        ono = True

    if ono == False:
        with open("snowball_thing.json",'w') as f:
            json.dump(balls,f)

        ues = random.randint(1,1000)

        if ues > 500:
            with open("snowball_hits.json",'r') as f:
                b_a_l_l_s = json.load(f)

            try:
                b_a_l_l_s[str(inter.author.id)] = b_a_l_l_s[str(inter.author.id)] + 1
            except:
                b_a_l_l_s[str(inter.author.id)] = 1

            with open("snowball_hits.json",'w') as f:
                json.dump(b_a_l_l_s,f)

            await inter.reply(":deaf_person: :arrow_left: :white_circle: <:lelcube:811058465383514132>")
            await inter.send(f"{inter.author.mention} attacked {target}!")
        else:
            await inter.reply("<:void:834904392008335360> :arrow_upper_left:\n:deaf_person: <:void:834904392008335360> :white_circle: <:lelcube:811058465383514132>")
            await inter.send(f"{inter.author.mention} missed lol")

@snowball.sub_command(description="See who is the best throwing at throwing snowballs!")
async def lleaderboard(inter):
    page = 0
    lb_uwu = ""
    cook_list = {}
    when_the = []

    with open("snowball_users.txt",'r') as f:
        txt = f.read()

    t_x_t = txt.split("\n")
    t_x_t.remove("nothing lol xd")

    with open("snowball_hits.json",'r') as f:
        balls = json.load(f)

    for i in t_x_t:
        when_the.append(balls[i])

        for i_ in when_the:
            cook_list[i] = i_

    def split_dict_into_chunks(input_dict, chunk_size):
        res = []
        new_dict = {}
        for k, v in input_dict.items():
            if len(new_dict) < chunk_size:
                new_dict[k] = v
            else:
                res.append(new_dict)
                new_dict = {k: v}
        res.append(new_dict)
        return res

    cook_list = dict(sorted(cook_list.items(), key=lambda item: item[1]))
    cook_list = dict(reversed(list(cook_list.items())))

    users_chunks = split_dict_into_chunks(cook_list,10)

    for key,value in users_chunks[page].items():
        lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

    embed=discord.Embed(title=f"Snow leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
    embed.set_footer(text=str(inter.author.id))

    can_go_back = True
    can_go_forward = True

    if page+1 == 1:
        can_go_back = False

    if page+1 == len(users_chunks):
        can_go_forward = False

    row = ActionRow(
        Button(
            style=ButtonStyle.blurple,
            label="Previous page",
            custom_id="prev_button",
            disabled=not can_go_back
        ),
        Button(
            style=ButtonStyle.blurple,
            label="Next page",
            custom_id="next_button",
            disabled=not can_go_forward
        )
    )
    msg = await inter.reply(embed=embed, components=[row])

    on_click = msg.create_click_listener(timeout=120)

    @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
    async def on_wrong_user(inter):
        await inter.reply("You're not the author :P", ephemeral=True)

    @on_click.matching_id("prev_button")
    async def on_prev_button(inter):
      nonlocal page
      can_go_back = True
      can_go_forward = True
      page -= 1

      if page == 0:
        can_go_back = False

      if page == len(users_chunks)-1:
        can_go_forward = False

      newrow = ActionRow(
        Button(
          style=ButtonStyle.blurple,
          label="Previous page",
          custom_id="prev_button",
          disabled=not can_go_back
        ),
        Button(
          style=ButtonStyle.blurple,
          label="Next page",
          custom_id="next_button",
          disabled=not can_go_forward
          )
        )

      lb_uwu = ""

      for key,value in users_chunks[page].items():
        lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

      embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
      embed.set_footer(text=str(inter.author.id))

      await msg.edit(embed=embed, components=[newrow])

    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])
    
    @on_click.matching_id("next_button")
    async def on_next_button(inter):
      nonlocal page
      can_go_back = True
      can_go_forward = True
      page += 1

      if page == 0:
        can_go_back = False

      if page == len(users_chunks)-1:
        can_go_forward = False

      newrow = ActionRow(
        Button(
          style=ButtonStyle.blurple,
          label="Previous page",
          custom_id="prev_button",
          disabled=not can_go_back
        ),
        Button(
          style=ButtonStyle.blurple,
          label="Next page",
          custom_id="next_button",
          disabled=not can_go_forward
          )
        )

      lb_uwu = ""

      for key,value in users_chunks[page].items():
        lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

      embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
      embed.set_footer(text=str(inter.author.id))

      await msg.edit(embed=embed, components=[newrow])

    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])

@client.command(aliases=['snow_leaderboard','snowball_lb','snowball_leaderboard','snow-lb','snow-leaderboard','snowball-lb','snowball-leaderboard'])
async def snow_lb(inter):
    page = 0
    lb_uwu = ""
    cook_list = {}
    when_the = []

    with open("snowball_users.txt",'r') as f:
        txt = f.read()

    t_x_t = txt.split("\n")
    t_x_t.remove("nothing lol xd")

    with open("snowball_hits.json",'r') as f:
        balls = json.load(f)

    for i in t_x_t:
        when_the.append(balls[i])

        for i_ in when_the:
            cook_list[i] = i_

    def split_dict_into_chunks(input_dict, chunk_size):
        res = []
        new_dict = {}
        for k, v in input_dict.items():
            if len(new_dict) < chunk_size:
                new_dict[k] = v
            else:
                res.append(new_dict)
                new_dict = {k: v}
        res.append(new_dict)
        return res

    cook_list = dict(sorted(cook_list.items(), key=lambda item: item[1]))
    cook_list = dict(reversed(list(cook_list.items())))

    users_chunks = split_dict_into_chunks(cook_list,10)

    for key,value in users_chunks[page].items():
        lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

    embed=discord.Embed(title=f"Snow leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
    embed.set_footer(text=str(inter.author.id))

    can_go_back = True
    can_go_forward = True

    if page+1 == 1:
        can_go_back = False

    if page+1 == len(users_chunks):
        can_go_forward = False

    row = ActionRow(
        Button(
            style=ButtonStyle.blurple,
            label="Previous page",
            custom_id="prev_button",
            disabled=not can_go_back
        ),
        Button(
            style=ButtonStyle.blurple,
            label="Next page",
            custom_id="next_button",
            disabled=not can_go_forward
        )
    )
    msg = await inter.reply(embed=embed, components=[row])

    on_click = msg.create_click_listener(timeout=120)

    @on_click.not_from_user(inter.author, cancel_others=True, reset_timeout=False)
    async def on_wrong_user(inter):
        await inter.reply("You're not the author :P", ephemeral=True)

    @on_click.matching_id("prev_button")
    async def on_prev_button(inter):
      nonlocal page
      can_go_back = True
      can_go_forward = True
      page -= 1

      if page == 0:
        can_go_back = False

      if page == len(users_chunks)-1:
        can_go_forward = False

      newrow = ActionRow(
        Button(
          style=ButtonStyle.blurple,
          label="Previous page",
          custom_id="prev_button",
          disabled=not can_go_back
        ),
        Button(
          style=ButtonStyle.blurple,
          label="Next page",
          custom_id="next_button",
          disabled=not can_go_forward
          )
        )

      lb_uwu = ""

      for key,value in users_chunks[page].items():
        lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

      embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
      embed.set_footer(text=str(inter.author.id))

      await msg.edit(embed=embed, components=[newrow])

    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])
    
    @on_click.matching_id("next_button")
    async def on_next_button(inter):
      nonlocal page
      can_go_back = True
      can_go_forward = True
      page += 1

      if page == 0:
        can_go_back = False

      if page == len(users_chunks)-1:
        can_go_forward = False

      newrow = ActionRow(
        Button(
          style=ButtonStyle.blurple,
          label="Previous page",
          custom_id="prev_button",
          disabled=not can_go_back
        ),
        Button(
          style=ButtonStyle.blurple,
          label="Next page",
          custom_id="next_button",
          disabled=not can_go_forward
          )
        )

      lb_uwu = ""

      for key,value in users_chunks[page].items():
        lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

      embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
      embed.set_footer(text=str(inter.author.id))

      await msg.edit(embed=embed, components=[newrow])

    @on_click.timeout
    async def on_timeout():
        await msg.edit(components=[])

token = "Insert token here"
client.run(token)
