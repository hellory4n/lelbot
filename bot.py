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

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Type l!help for help! Slash commands are here!'))
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
    embed=discord.Embed(title="Help", description="`<>` = required, `[]` = optional. You can also use slash commands!", color=0xFECC4D)
    embed.add_field(name="Commands", value="`l!hello`, `l!ping`, `l!8ball <question>`, `l!boom <user>`, `l!invite`, `l!chat <text>`, `l!fact [index]`, `l!randomstory`, `l!aboutme`, `l!when <question>`, `l!helloyesorno <question>`, `l!say <text>`, `l!hug <user>`, `l!attack <user>`, `l!bam <user>`, `l!roll`, `l!hack <user>`, `l!server`, `l!randomsandwich`, `l!poll <text>`, `l!suggest <text>`, `l!weirdtext`, `l!dostuff`, `l!embed <title> | <description>`, `l!math <number> <operation> <number>`, `l!sweatsmile`, `l!randnum <min> <max>`, `l!bobux`, `l!morecookis`, `l!work`, `l!bal [user]`, `l!dep <value>`, `l!with <value>`, `l!lb`, `l!shop`, `l!buy [amount]`, `l!inv [user]`, `l!use [amount]`, `l!give_money <user> <amount>`, `l!reset_money`, `l!give_item <user> [amount]`, `l!rob <user> <amount>`", inline=False)
    embed.set_footer(text="lel")
    await ctx.send(embed=embed)

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
        ABOTME_embed=discord.Embed(title=f'About Lelbot', description=f'Hello! Im lelbot! Im an AI created by hellory5n! (hellory5n is character, who really created me is hellory4n lel)\n\nthis is hellory5n: https://cdn.discordapp.com/attachments/811060678277333023/819620061869244426/Screenshot_20210311-141624_Fancade.jpg \n\nCREDITS\nDeveloped by hellory4n\nsome fun facts: SrMuffin136, Senjienji, Dylan Brew, shartok, Rubi, Nextie\nHosted in Discloud\nAnd thank you for using my commands!\n\nCurrent version: 1.1.6', color=0xFECC4D)
        ABOTME_embed.set_footer(text="lel")
        await ctx.send(embed=ABOTME_embed)

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
    helloyesorno = ['https://cdn.discordapp.com/attachments/811060678277333023/828721589981806632/Screenshot_20210405-141259_Fancade.jpg',
            'https://cdn.discordapp.com/attachments/811060678277333023/828721531768012820/Screenshot_20210405-141109_Fancade.png']
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
    poll_embed=discord.Embed(title=f'Poll by {ctx.message.author}', description=f'{owopoll}', color=0xFECC4D)
    poll_embed.set_footer(text=f'lel')
    Poll = await ctx.send(embed=poll_embed)
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
async def dostuff2(ctx):
    lelbot_tasks_index = random.randint(1,55)

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
        await ctx.send(f'<:pixel:827617330237669406> :mag: <:lelcube:811058465383514132>')
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

@client.command(aliases=['embed'])
async def embed2(ctx, *, embedsay):
    embedsay2 = embedsay.split('| ')

    if '| ' not in embedsay:
        await ctx.send(f'You need a `|`!\nExample: Title | Description')
    else:
        bed_embed=discord.Embed(title=f'{embedsay2[0]}', description=f'{embedsay2[1]}')
        bed_embed.set_footer(text=f'Embed by {ctx.message.author}')
        await ctx.send(embed=bed_embed)

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
    embed=discord.Embed(title="Help", description="`<>` = required, `[]` = optional.", color=0xFECC4D)
    embed.add_field(name="Commands", value="`l!hello`, `l!ping`, `l!8ball <question>`, `l!boom <user>`, `l!invite`, `l!chat <text>`, `l!fact [index]`, `l!randomstory`, `l!aboutme`, `l!when <question>`, `l!helloyesorno <question>`, `l!say <text>`, `l!hug <user>`, `l!attack <user>`, `l!bam <user>`, `l!roll`, `l!hack <user>`, `l!server`, `l!randomsandwich`, `l!poll <text>`, `l!suggest <text>`, `l!weirdtext`, `l!dostuff`, `l!embed <title> | <description>`, `l!math <number> <operation> <number>`, `l!sweatsmile`, `l!randnum <min> <max>`, `l!bobux`, `l!morecookis`, `l!work`, `l!bal [user]`, `l!dep <value>`, `l!with <value>`, `l!lb`, `l!shop`, `l!buy [amount]`, `l!inv [user]`, `l!use [amount]`, `l!give_money <user> <amount>`, `l!reset_money`, `l!give_item <user> [amount]`, `l!rob <user> <amount>`", inline=False)
    embed.set_footer(text="lel")
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
    helloyesorno = ['https://cdn.discordapp.com/attachments/811060678277333023/828721589981806632/Screenshot_20210405-141259_Fancade.jpg',
            'https://cdn.discordapp.com/attachments/811060678277333023/828721531768012820/Screenshot_20210405-141109_Fancade.png']
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
    await inter.reply(f"{someone} has (not) been banned by {inter.author.mention} (Reason: {reason})", allowed_mentions = discord.AllowedMentions(everyone = False))

@inter_client.slash_command(description="Explode something!", options=[Option('something', 'Yes', OptionType.STRING, required=True)])
async def boom(inter, something):
    embed=discord.Embed(title="Boom!", description=f'{something} exploded!\nDamage: {random.randint(1,100)}', color=0xFECC4D)
    embed.set_footer(text=f'Exploded by {inter.author}')
    await inter.reply(embed=embed)

@inter_client.slash_command(description="Hackn't something!", options=[Option('something','hejusidghjk',OptionType.STRING,required=True)])
async def hack(inter, something):
    yo = await inter.reply(f"Getting access to {something}...", allowed_mentions = discord.AllowedMentions(everyone = False))
    await asyncio.sleep(5)
    await yo.edit(content=f"Found email! ({something}{str(random.randint(10000000,99999999))}@lelmail.com)", allowed_mentions = discord.AllowedMentions(everyone = False))
    await asyncio.sleep(2.5)
    await yo.edit(content="Found emojis from their phone cuz why not <:lelcube:811058465383514132>")
    await asyncio.sleep(3)
    await yo.edit(content="Drinking coffee... :coffee:")
    await asyncio.sleep(3.1)
    await yo.edit(content="Exploding my own database lol <:lelcube:811058465383514132>")
    await asyncio.sleep(4)
    await yo.edit(content="Selling their data to a random person...")
    await asyncio.sleep(3.5)
    await yo.edit(content=f"{inter.author.mention} Hacked {something} successfully!", allowed_mentions = discord.AllowedMentions(everyone = False))

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

@inter_client.slash_command(description="See lelcube doing a random task")
async def dostuff(inter):
    lelbot_tasks_index = random.randint(1,55)

    if lelbot_tasks_index == 1:
        await inter.reply(f'🎙 <:lelcube:811058465383514132>')
        await inter.reply(f'He sings')
    if lelbot_tasks_index == 2:
        await inter.reply(f':frame_photo: :paintbrush: <:lelcube:811058465383514132>')
        await inter.reply(f'He paints')
    if lelbot_tasks_index == 3:
        await inter.reply(f':computer: <:lelcube:811058465383514132>')
        await inter.reply(f'He codes')
    if lelbot_tasks_index == 4:
        await inter.reply(f':video_game: <:lelcube:811058465383514132>')
        await inter.reply(f'He play games')
    if lelbot_tasks_index == 5:
        await inter.reply(f':potato: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
        await inter.reply(f'He kills potatos')
    if lelbot_tasks_index == 6:
        await inter.reply(f':tv: <:lelcube:811058465383514132>')
        await inter.reply(f'He watches tv')
    if lelbot_tasks_index == 7:
        await inter.reply(f':hammer: <:lelcube:811058465383514132>')
        await inter.reply(f'He destroy stuff')
    if lelbot_tasks_index == 8:
        await inter.reply(f':shower:\n<:lelcube:811058465383514132>')
        await inter.reply(f'He showers')
    if lelbot_tasks_index == 9:
        await inter.reply(f'<:lelcube:811058465383514132> :shopping_cart:')
        await inter.reply(f'He goes shopping')
    if lelbot_tasks_index == 10:
        await inter.reply(f':balloon: <:lelcube:811058465383514132>')
        await inter.reply(f'He plays with balloon')
    if lelbot_tasks_index == 11:
        await inter.reply(f':wastebasket: :newspaper2: <:lelcube:811058465383514132>')
        await inter.reply(f'He doesnt like to read cuz reading is boring and i just noticed that to use discord you have to read which is boring so technicly using discord is boring but is not eeeeeeeeeeeee')
    if lelbot_tasks_index == 12:
        await inter.reply(f':video_camera: <:lelcube:811058465383514132>')
        await inter.reply(f'He records a video')
    if lelbot_tasks_index == 13:
        await inter.reply(f':pencil: <:lelcube:811058465383514132>')
        await inter.reply(f'He writes a text')
    if lelbot_tasks_index == 14:
        await inter.reply(f'<:pixel:827617330237669406> :mag: <:lelcube:811058465383514132>')
        worstjokeever = await inter.reply(f'He is trying to see nextie *but nextie have the size of a __pixel__*')
        await worstjokeever.add_reaction('<:bassrolf:821948606701371462>')
    if lelbot_tasks_index == 15:
        await inter.reply(f'<:lelcube:811058465383514132> :loudspeaker:')
        await inter.reply(f'He says potatopatata very loud')
    if lelbot_tasks_index == 16:
        await inter.reply(f':cake: :fork_and_knife: <:lelcube:811058465383514132>')
        await inter.reply(f'He eats a cake')
    if lelbot_tasks_index == 17:
        await inter.reply(f':iphone: <:lelcube:811058465383514132>')
        await inter.reply(f'He uses the phone')
    if lelbot_tasks_index == 18:
        await inter.reply(f':pizza: <:lelcube:811058465383514132>')
        await inter.reply(f'He is 101% sure that pizza is pizza')
    if lelbot_tasks_index == 19:
        await inter.reply(f'<:clapping:811058070843162686> <:lelcube:811058465383514132>')
        await inter.reply(f'He claps')
    if lelbot_tasks_index == 20:
        await inter.reply(f'<:lelcube:811058465383514132> :vs: <:sweatsmile:811059266806480916>')
        await inter.reply(f'He fights')
    if lelbot_tasks_index == 21:
        await inter.reply(f':telephone_receiver: <:lelcube:811058465383514132>')
        await inter.reply(f'He calls people')
    if lelbot_tasks_index == 22:
        await inter.reply(f'<:lelcube:811058465383514132> :tent:')
        await inter.reply(f'He goes camping')
    if lelbot_tasks_index == 23:
        await inter.reply(f':ballet_shoes: <:lelcube:811058465383514132>')
        await inter.reply(f'He uses a ballet shoes')
    if lelbot_tasks_index == 24:
        await inter.reply(f'<:lelcube:811058465383514132> :toothbrush: :toilet:')
        await inter.reply(f'He clean the toilet')
    if lelbot_tasks_index == 25:
        await inter.reply(f":tophat:\n<:lelcube:811058465383514132> :magic_wand:")
        await inter.reply(f'He magic man')
    if lelbot_tasks_index == 26:
        await inter.reply(f':saxophone: <:lelcube:811058465383514132>')
        await inter.reply(f'He plays the saxophone cuz saxophones are cool')
    if lelbot_tasks_index == 27:
        await inter.reply(f'<:lelcube:811058465383514132> <:okhand:811059019828428821>')
        await inter.reply(f'He likes *something*')
    if lelbot_tasks_index == 28:
        await inter.reply(f'<:sweatwide1:818622702574632970><:lelcube:811058465383514132><:sweatwide2:818622715815526481>')
        await inter.reply(f'He uses a disguise')
    if lelbot_tasks_index == 29:
        await inter.reply(f':sweat_smile: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
        await inter.reply(f'He kills')
    if lelbot_tasks_index == 30:
        await inter.reply(f'<:maum1:778489567036178464> <:lelcube:811058465383514132> <:maum2:778489689014403072>')
        await inter.reply(f'He will catch you')
    if lelbot_tasks_index == 31:
        await inter.reply(f'<:lelcube:811058465383514132> :dash:')
        await inter.reply('He fards')
    if lelbot_tasks_index == 32:
        await inter.reply(f'<:lelcube:811058465383514132>\n:blue_car:')
        await inter.reply('He drives a car')
    if lelbot_tasks_index == 33:
        await inter.reply(':boom: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
        await inter.reply('He commits war crimes')
    if lelbot_tasks_index == 34:
        await inter.reply(':wolf: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
        await inter.reply('He hunts')
    if lelbot_tasks_index == 35:
        await inter.reply(':cloud_rain:\n:umbrella:\n<:lelcube:811058465383514132>')
        await inter.reply('He is on rain')
    if lelbot_tasks_index == 36:
        await inter.reply('<:lelcube:811058465383514132>\n:sailboat: :island:')
        await inter.reply('He escapes island')
    if lelbot_tasks_index == 37:
        await inter.reply(':cooking: <:lelcube:811058465383514132>')
        await inter.reply('He cooks')
    if lelbot_tasks_index == 38:
        await inter.reply(':ping_pong: <:lelcube:811058465383514132>')
        await inter.reply('He plays ping pong')
    if lelbot_tasks_index == 39:
        await inter.reply(':guitar: <:lelcube:811058465383514132>')
        await inter.reply('He plays guitar')
    if lelbot_tasks_index == 40:
        await inter.reply('<:blushing:821505454361935902> :heart: <:lelcube:811058465383514132>')
        await inter.reply('He finds love')
    if lelbot_tasks_index == 41:
        await inter.reply(':desktop: :hammer: <:lelcube:811058465383514132>')
        await inter.reply('He hacks')
    if lelbot_tasks_index == 42:
        await inter.reply(':telescope: <:lelcube:811058465383514132>')
        await inter.reply('He sees the space')
    if lelbot_tasks_index == 43:
        await inter.reply(':microscope: <:lelcube:811058465383514132>')
        await inter.reply('He finds the close ad button')
    if lelbot_tasks_index == 44:
        await inter.reply(':desktop: <:lelcube:811058465383514132>')
        await inter.reply('He works on the computer')
    if lelbot_tasks_index == 45:
        await inter.reply(':moneybag: <:lelcube:811058465383514132>')
        await inter.reply('He gets paid')
    if lelbot_tasks_index == 46:
        await inter.reply(':chart_with_upwards_trend: <:lelcube:811058465383514132>')
        await inter.reply('He stonks')
    if lelbot_tasks_index == 47:
        await inter.reply(':house_with_garden: :money_with_wings: <:lelcube:811058465383514132>')
        await inter.reply('He buys house')
    if lelbot_tasks_index == 48:
        await inter.reply('<:sweatsmile:811059266806480916> :gift: <:lelcube:811058465383514132>')
        await inter.reply('He gets gift')
    if lelbot_tasks_index == 49:
        await inter.reply('🥳 🥳 🥳 🥳 <:lelcube:811058465383514132> 🥳 🥳 🥳')
        await inter.reply('He goes to party')
    if lelbot_tasks_index == 50:
        await inter.reply(':airplane_departure: <:lelcube:811058465383514132>')
        await inter.reply('He flies')
    if lelbot_tasks_index == 51:
        await inter.reply(':book: <:lelcube:811058465383514132>')
        await inter.reply('He reads books')
    if lelbot_tasks_index == 52:
        await inter.reply(':mag: <:lelcube:811058465383514132>')
        await inter.reply('He searches')
    if lelbot_tasks_index == 53:
        await inter.reply(':broom: <:lelcube:811058465383514132>')
        await inter.reply('He does chores')
    if lelbot_tasks_index == 54:
        await inter.reply(':jack_o_lantern: :skull: <:lelcube:811058465383514132>')
        await inter.reply('He is on spooky month')
    if lelbot_tasks_index == 55:
        await inter.reply('<:maum1:778489567036178464> :gem: <:lelcube:811058465383514132> <:maum2:778489689014403072>')
        await inter.reply('He steals')

@inter_client.slash_command(description="Builds a custom embed", options=[Option('title', 'Embed title', OptionType.STRING, required=True),Option('description', 'Embed description', OptionType.STRING,required=True),Option('color', 'Embed color', OptionType.STRING),Option('footer','Embed footer',OptionType.STRING),Option('url','Embed image url',OptionType.STRING)])
async def embed(inter, title, description, color=None, footer="Super cook embed", url=None):
    if color is not None:
        try:
            color = await commands.ColorConverter().convert(inter, color)
        except:
            color = None
    if color is None:
        color = discord.Color.default()
    embed=discord.Embed(title=title, description=description, color=color)
    embed.set_footer(text=f"{footer} • {inter.author} ({inter.author.id})")
    if url is not None:
        embed.set_image(url=url)
    await inter.reply(embed=embed)

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
    ABOTME_embed=discord.Embed(title=f'About Lelbot', description=f'Hello! Im lelbot! Im an AI created by hellory5n! (hellory5n is character, who really created me is hellory4n lel)\n\nthis is hellory5n: https://cdn.discordapp.com/attachments/811060678277333023/819620061869244426/Screenshot_20210311-141624_Fancade.jpg \n\nCREDITS\nDeveloped by hellory4n\nsome fun facts: SrMuffin136, Senjienji, Dylan Brew, shartok, Rubi, Nextie\nHosted in Discloud\nAnd thank you for using my commands!\n\nCurrent version: 1.1.6', color=0xFECC4D)
    ABOTME_embed.set_footer(text="lel")
    await inter.reply(embed=ABOTME_embed)

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
    with open("users.txt",'r') as f:
        txt = f.read()
    
    users = txt.split("\n")

    def a_very_cook_function_that_split_a_list_into_chunks(l, n):
        n = max(1, n)
        return (l[i:i+n] for i in range(0, len(l), n))

    users_chunks = list(a_very_cook_function_that_split_a_list_into_chunks(users, 10))

    for i in users_chunks[page]:
        if not users.index(i) == 0:
            with open(f"{i}.json", 'r') as file:
                ok = json.load(file)
            total = ok['cash'] + ok['bank']
            #user = await client.fetch_user(int(i))
            #lb_uwu = lb_uwu + user.name + ": " + str(total) + " <:lelgold:888933451410075689>" + "\n"
            lb_uwu = lb_uwu + "<@" + i + ">: " + str(total) + " <:lelgold:888933451410075689>" + "\n"
    
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

      for i in users_chunks[page]:
        if not users_chunks[page].index(i) == 0:
          with open(f"{i}.json", 'r') as file:
            ok = json.load(file)
          total = ok['cash'] + ok['bank']
          #user = await client.fetch_user(int(i))
          #lb_uwu = lb_uwu + user.name + ": " + str(total) + " <:lelgold:888933451410075689>" + "\n"
          lb_uwu = lb_uwu + "<@" + i + ">: " + str(total) + " <:lelgold:888933451410075689>" + "\n"

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

      for i in users_chunks[page]:
        if not users_chunks[page].index(i) == 0:
          with open(f"{i}.json", 'r') as file:
            ok = json.load(file)
          total = ok['cash'] + ok['bank']
          #user = await client.fetch_user(int(i))
          #lb_uwu = lb_uwu + user.name + ": " + str(total) + " <:lelgold:888933451410075689>" + "\n"
          lb_uwu = lb_uwu + "<@" + i + ">: " + str(total) + " <:lelgold:888933451410075689>" + "\n"

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

@inter_client.slash_command(description="Buy something :)", options=[Option("item",description="The item you want to buy",type=OptionType.STRING,required=True,choices=[OptionChoice("Void","Void"),OptionChoice("Cooki","Cooki"),OptionChoice("Arnold cooki","Arnold cooki"),OptionChoice("Linux","Linux"),OptionChoice("Lelcube plushie","Lelcube plushie"),OptionChoice("Windows Vista","Windows Vista"),OptionChoice("Terrible laptop","Terrible laptop"),OptionChoice("Free bobux","Free bobux"),OptionChoice("Top secret lelcube images","Top secret lelcube images"),OptionChoice("Internet Explorer 12","Internet Explorer 12"),OptionChoice("Clippy","Clippy"),OptionChoice("Illegal DVD","Illegal DVD")]),Option("amount","The amount that you want to buy",OptionType.INTEGER,required=False)])
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

@inter_client.slash_command(description="Use an item that you have", options=[Option("item",description="The item you want to use",type=OptionType.STRING,required=True,choices=[OptionChoice("Void","Void"),OptionChoice("Cooki","Cooki"),OptionChoice("Arnold cooki","Arnold cooki"),OptionChoice("Linux","Linux"),OptionChoice("Lelcube plushie","Lelcube plushie"),OptionChoice("Windows Vista","Windows Vista"),OptionChoice("Terrible laptop","Terrible laptop"),OptionChoice("Free bobux","Free bobux"),OptionChoice("Top secret lelcube images","Top secret lelcube images"),OptionChoice("Internet Explorer 12","Internet Explorer 12"),OptionChoice("Clippy","Clippy"),OptionChoice("Illegal DVD","Illegal DVD")]),Option("amount","The amount that you want to use",OptionType.INTEGER,required=False)])
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
                await msg.edit(content="Timeout", components=[])

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
                await msg.edit(content="Timeout", components=[])
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
                await msg.edit(content="Timeout", components=[])
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
                await msg.edit(content="Timeout", components=[])
        elif item == "Illegal DVD":
            await inter.reply(":police_car:")
            await asyncio.sleep(5)
            await inter.reply("The police is here, and you will be bammed!")
            await asyncio.sleep(5)
            await bam(inter, inter.author.name, "Buying illegal DVDs")
        elif item == "Arnold cooki":
            await inter.reply(":yum::yum:")

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
        await inter.reply("No")
    
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
            await msg.edit(content="Timeout", components=[])
        else:
            pass

@inter_client.slash_command(description="Give an item to someone", options=[Option("user","The user that will get the item",OptionType.USER,required=True),Option("item","The item that you will give", OptionType.STRING, required=True, choices=[OptionChoice("Void","Void"),OptionChoice("Cooki","Cooki"),OptionChoice("Arnold cooki","Arnold cooki"),OptionChoice("Linux","Linux"),OptionChoice("Lelcube plushie","Lelcube plushie"),OptionChoice("Windows Vista","Windows Vista"),OptionChoice("Terrible laptop","Terrible laptop"),OptionChoice("Free bobux","Free bobux"),OptionChoice("Top secret lelcube images","Top secret lelcube images"),OptionChoice("Internet Explorer 12","Internet Explorer 12"),OptionChoice("Clippy","Clippy"),OptionChoice("Illegal DVD","Illegal DVD")]), Option("amount","The amount that you will give",OptionType.INTEGER,required=False)])
async def give_item(inter, user, item, amount=1):
    problems_ono = False

    if user.id == inter.author.id:
        problems_ono = True
        await inter.reply("You can't give an item for yourself", ephemeral=True)
    
    input = f"{str(inter.author.id)}_items.json"
    output = f"{str(user.id)}_items.json"

    with open(input, 'r') as f_i:
        ok_i = json.load(f_i)
    
    if amount < 1 or not ok_i[item] > amount - 1:
        problems_ono = True
        await inter.reply("No")
    
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
        await inter.reply("No")
    
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
    if ctx.author.id == "insert your ID here":
        with open(f"{user_id}.json",'r') as f:
            ok = json.load(f)
        
        ok['cash'] = int(cash)
        ok['bank'] = int(bank)

        with open(f"{user_id}.json",'w') as f:
            json.dump(ok, f)
        
        await ctx.reply("Boom")
    else:
        await ctx.reply("You can't use this command lol")

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
    'You are cook :)']
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(f'Type l!help for help! {random.choice(statuses)}'))

@client.command()
async def random_status(ctx):
    if ctx.author.id == "insert your ID here":
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
    with open("users.txt",'r') as f:
        txt = f.read()
    
    users = txt.split("\n")

    def a_very_cook_function_that_split_a_list_into_chunks(l, n):
        n = max(1, n)
        return (l[i:i+n] for i in range(0, len(l), n))

    users_chunks = list(a_very_cook_function_that_split_a_list_into_chunks(users, 10))

    for i in users_chunks[page]:
        if not users.index(i) == 0:
            with open(f"{i}.json", 'r') as file:
                ok = json.load(file)
            total = ok['cash'] + ok['bank']
            #user = await client.fetch_user(int(i))
            #lb_uwu = lb_uwu + user.name + ": " + str(total) + " <:lelgold:888933451410075689>" + "\n"
            lb_uwu = lb_uwu + "<@" + i + ">: " + str(total) + " <:lelgold:888933451410075689>" + "\n"
    
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

      for i in users_chunks[page]:
        if not users_chunks[page].index(i) == 0:
          with open(f"{i}.json", 'r') as file:
            ok = json.load(file)
          total = ok['cash'] + ok['bank']
          #user = await client.fetch_user(int(i))
          #lb_uwu = lb_uwu + user.name + ": " + str(total) + " <:lelgold:888933451410075689>" + "\n"
          lb_uwu = lb_uwu + "<@" + i + ">: " + str(total) + " <:lelgold:888933451410075689>" + "\n"

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

      for i in users_chunks[page]:
        if not users_chunks[page].index(i) == 0:
          with open(f"{i}.json", 'r') as file:
            ok = json.load(file)
          total = ok['cash'] + ok['bank']
          #user = await client.fetch_user(int(i))
          #lb_uwu = lb_uwu + user.name + ": " + str(total) + " <:lelgold:888933451410075689>" + "\n"
          lb_uwu = lb_uwu + "<@" + i + ">: " + str(total) + " <:lelgold:888933451410075689>" + "\n"

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
                      SelectOption("Illegal DVD","Illegal DVD")
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
                      SelectOption("Illegal DVD","Illegal DVD")
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
                      await msg.edit(content="Timeout", components=[])

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
                      await msg.edit(content="Timeout", components=[])
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
                      await msg.edit(content="Timeout", components=[])
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
                      await msg.edit(content="Timeout", components=[])
              elif item == "Illegal DVD":
                  await inter.reply(":police_car:")
                  await asyncio.sleep(5)
                  await inter.reply("The police is here, and you will be bammed!")
                  await asyncio.sleep(5)
                  await bam(inter, inter.author.name, "Buying illegal DVDs")
              elif item == "Arnold cooki":
                  await inter.reply(":yum::yum:")
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
        await inter.reply("No")
    
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
            await msg.edit(content="Timeout", components=[])
        else:
            pass

@client.command(aliases=['give_item','give-item'])
async def give_item2(inter, user:discord.Member, amount="1"):
    problems_ono = False

    if user.id == inter.author.id:
        problems_ono = True
        await inter.reply("You can't give an item for yourself")

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
                      SelectOption("Illegal DVD","Illegal DVD")
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
              await inter.reply("No")
      
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
          await inter.reply("No")
      
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

token = "Insert token here"
client.run(token)
