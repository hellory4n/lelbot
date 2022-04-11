import disnake as discord
import random
import asyncio
import json
import os
from disnake.ext import commands, tasks
from disnake.mentions import AllowedMentions
from disnake.ui import Button, View, Select, Modal, TextInput
from disnake import ButtonStyle, SelectMenu, SelectOption, ActionRow, TextInputStyle

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

client = commands.Bot(command_prefix = 'l!',sync_commands=True)

client.remove_command('help')

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
    'I love SandwichXP, it\'s just so well made!',
    'Spinning is my favorite activity',
    '🐢 tutel']
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
    embed.add_field(name="Very random", value="`bobux`, `dostuff [index]`, `hello [something]`, `morecookis`, `randomsandwich`, `randomstory`, `sandwich <size>`, `name`, `buildpc`, `adventure`, `cake <someone>`, `hat`", inline=False)
    embed.add_field(name="Random", value="`bam <someone>`, `boom <something>`, `fact [index]`, `hack <something>`, `sweatsmile`, `yesorno <question>`, `chat <something>`, `sentence`, `who <someone>`, `where <something>`, `image`", inline=False)
    embed.add_field(name="Not so random", value="`attack <someone>`, `hug <someone>`, `say <something>`, `8ball <question>`, `when <question>`, `weirdtext`, `text_to_wotcode`, `wotcode_to_text`", inline=False)
    embed.add_field(name="Economy",value="`work`, `bal [user]`, `dep <amount>`, `with <amount>`, `lb`, `shop`, `buy [amount]`, `inv [user]`, `use [amount]`, `give_money <user> <amount>`, `reset_money`, `give_item <user> <amount>`, `rob <user> <amount>`, `reset_items`, `sell <user> <price> [amount]`",inline=False)
    embed.add_field(name="Snowballs",value="`collect`, `throw <target>`, `snow_lb`",inline=False)
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
    ABOTME_embed=discord.Embed(title=f'About lelbot', description=f"Hello! I'm lelbot, the smartest AI in the universe, created by hellory5n, a very evil guy with very dumb plans!\nBy the way this is hellory5n: <:hellory5n:915028960604200982>\nMy birthday is on april 6, cuz lelbot 0.1 was released in april 6, 2021!", color=0xFECC4D)
    ABOTME_embed.set_footer(text="Version 1.5.1")
    ABOTME_embed.add_field(name="Credits",value="Developed by hellory4n\nMany facts from `fact`: The credits are in the command itself\nArnold cooki ad from super snowman item: JustYellow\nThanks for using me!",inline=False)
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
        lelbot_tasks_index = random.randint(1,85)
        no_NOOOOO = True
    else:
        if int_index < 1 or int_index > 85:
            await ctx.send("Invalid index! Please enter something between 1 and 85.")
        else:
            lelbot_tasks_index = int_index
            no_NOOOOO = True

    lelcube = "<:lelcube:811058465383514132>"

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
            await ctx.send(f'He is trying to see nextie *but nextie have the size of a __pixel__*')
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
        if lelbot_tasks_index == 66:
            await ctx.send(f'{lelcube} :selfie:')
            await ctx.send('He takes a selfie')
        if lelbot_tasks_index == 67:
            await ctx.send(f':left_facing_fist: {lelcube}')
            await ctx.send('He punches')
        if lelbot_tasks_index == 68:
            await ctx.send(f':mouse_three_button: :hammer: {lelcube}')
            await ctx.send('He clicks on the "get free bobux" button 999999999 times')
        if lelbot_tasks_index == 69:
            #nice
            await ctx.send(f"{lelcube}\n:evergreen_tree:")
            await ctx.send('He is on a tree')
        if lelbot_tasks_index == 70:
            await ctx.send(f"{lelcube}\n:full_moon_with_face:")
            await ctx.send('He is on the moon')
        if lelbot_tasks_index == 71:
            await ctx.send(f":arrow_left: {lelcube} :cloud_tornado:")
            await ctx.send('He runs cuz there\'s a tornado')
        if lelbot_tasks_index == 72:
            await ctx.send(f'{lelcube}\n:ship:')
            await ctx.send('He is on a ship')
        if lelbot_tasks_index == 73:
            await ctx.send(f':taco: {lelcube}')
            await ctx.send('He eats a taco')
        if lelbot_tasks_index == 74:
            await ctx.send(f':spoon: {lelcube}')
            await ctx.send('He has a super cook spoon')
        if lelbot_tasks_index == 75:
            await ctx.send(f':cup_with_straw: {lelcube}')
            await ctx.send('He drinks water')
        if lelbot_tasks_index ==  76:
            await ctx.send(lelcube)
            await ctx.send('He')
        if lelbot_tasks_index == 77:
            await ctx.send(f"🟨🟨🟨🟨🟨🟨🟨🟨\n🟫🟫🟨🟫🟫🟦⬜🟨\n🟨🟨🟨🟨🟨🟨🟦⬜\n⬜🟫🟨⬜🟫🟨🟦🟦\n🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟫⬜⬜🟫🟨🟨🟨\n🟨🟨🟫🟫🟨🟨🟨🟨\n🟨🟨🟨🟨🟨🟨🟨🟨 {lelcube}")
            await ctx.send('He made statue')
        if lelbot_tasks_index == 78:
            await ctx.send(f":ballot_box_with_check: {lelcube}")
            await ctx.send('He approves nonsenses')
        if lelbot_tasks_index == 79:
            await ctx.send(f":turtle: {lelcube}")
            await ctx.send('He has a pet called tutel')
        if lelbot_tasks_index == 80:
            await ctx.send(f"{lelcube} :medal: {lelcube}")
            await ctx.send('He gives a medal to lelcube')
        if lelbot_tasks_index == 81:
            await ctx.send(f":point_down:{lelcube}\n<:grass:951926072792981579><:grass:951926072792981579>")
            await ctx.send('He touches grass')
        if lelbot_tasks_index == 82:
            await ctx.send(f"🔪🛸🗡️\n🪝{lelcube}<:Gun:816099538619072553>\n💉📯🪛")
            await ctx.send('He is in danger')
        if lelbot_tasks_index == 83:
            await ctx.send(f":bug: <:Gun:816099538619072553> {lelcube}")
            await ctx.send('He fixes bugs')
        if lelbot_tasks_index == 84:
            await ctx.send(f":coffee: {lelcube}")
            await ctx.send('He likes coffee')
        if lelbot_tasks_index == 85:
            await ctx.send(f":circus_tent: {lelcube}")
            await ctx.send('He goes to circus')

@client.command(aliases=['embed'])
async def embed2(ctx, *, embedsay):
    embedsay2 = embedsay.split('| ')

    if '| ' not in embedsay:
        await ctx.send(f'You need a `|`!\nExample: Title | Description')
    else:
        SASBED_embed=discord.Embed(title=f'{embedsay2[0]}', description=f'{embedsay2[1]}', color=0xFECC4D)
        SASBED_embed.set_footer(text=f'Embed by {ctx.message.author}')
        webhook = await ctx.channel.create_webhook(name="Lelbot webhook", reason=f"{ctx.author} used the embed command")
        msg = await webhook.send(embed=SASBED_embed, username=ctx.author.name, avatar_url=ctx.author.avatar)
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

@client.command()
async def set_status(ctx, *, statuss):
    if ctx.author.id == 748560377763201185:
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(f'Type l!help for help! {statuss}'))
        await ctx.send(f'status changed to {statuss}')
        print(f'status changed to {statuss}')
    else:
        await ctx.send(f'{ctx.author.mention} you cant use this command')

@client.slash_command(description="Says \"/\" for no reason lol (why i even added this)")
async def slash(inter):
    await inter.send("/")

@client.slash_command(description="Pong :)")
async def ping(inter):
    await inter.send(f"{inter.author.mention} :ping_pong: Pong! {round(client.latency * 1000)}ms")

@client.slash_command(description="Get an answer to a random question")
async def eightball(inter, question: str):
    """
    Parameters
    ----------
    question: Ask a question :)
    """
    options = ['yes', 'probably yes', 'yes?', 'definitely', 'idk lol', 'Hi', 'no', 'probably not', 'no?', 'definitely not']
    embed=discord.Embed(title=question, description=f'{random.choice(options)}', color=0xFECC4D)
    embed.set_footer(text=inter.author.id)
    await inter.send(embed=embed)

@client.slash_command(description="The good old help command")
async def help(inter):
    embed = discord.Embed(title="Help", description="\n`<>` means required argument, `[]` means optional argument\nDon't include `<>` or `[]`\nMost commands are available in slash commands!", color=0xFECC4D)
    embed.add_field(name="Very random", value="`bobux`, `dostuff [index]`, `hello [something]`, `morecookis`, `randomsandwich`, `randomstory`, `sandwich <size>`, `name`, `buildpc`, `adventure`, `cake <someone>`, `hat`", inline=False)
    embed.add_field(name="Random", value="`bam <someone>`, `boom <something>`, `fact [index]`, `hack <something>`, `sweatsmile`, `yesorno <question>`, `chat <something>`, `sentence`, `who <someone>`, `where <something>`, `image`", inline=False)
    embed.add_field(name="Not so random", value="`attack <someone>`, `hug <someone>`, `say <something>`, `8ball <question>`, `when <question>`, `weirdtext`, `text_to_wotcode`, `wotcode_to_text`", inline=False)
    embed.add_field(name="Economy",value="`work`, `bal [user]`, `dep <amount>`, `with <amount>`, `lb`, `shop`, `buy [amount]`, `inv [user]`, `use [amount]`, `give_money <user> <amount>`, `reset_money`, `give_item <user> <amount>`, `rob <user> <amount>`, `reset_items`, `sell <user> <price> [amount]`")
    embed.add_field(name="Snowballs",value="`collect`, `throw <target>`, `snow_lb`",inline=False)
    embed.add_field(name="Bot stuff", value="`ping`, `invite`, `aboutme`, `server`, `help`, `classic_help`", inline=False)
    embed.add_field(name="Stuff that isn't really for fun", value="`embed <title> | <description>`, `math <expression>`, `poll <text>`, `randnum <min> <max>`, `suggest <suggestion>`, `roll`", inline=False)
    await inter.send(embed=embed)

@client.slash_command(description="Chat with lelbot! But, his replies won't make any sense! Best idea!")
async def chat(inter,message: str):
    """
    Parameters
    ----------
    message: Message :thumbsup:
    """
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
    await inter.send(random.choice(chatresponses))

@client.slash_command(description="Create a butiful story.")
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
    
    await inter.send(f'*{random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)} {random.choice(storywords)}*')

@client.slash_command(description="Ask when something will happen")
async def when(inter, question: str):
    """
    Parameters
    ----------
    question: yes
    """
    whentype = random.randint(1,8)

    if whentype == 1:
        await inter.send(f'After {random.randint(1,60)} seconds.')
    if whentype == 2:
        await inter.send(f'After {random.randint(1,60)} minutes.')
    if whentype == 3:
        await inter.send(f'After {random.randint(1,24)} hours.')
    if whentype == 4:
        await inter.send(f'After {random.randint(1,31)} days.')
    if whentype == 5:
        await inter.send(f'After {random.randint(1,12)} months.')
    if whentype == 6:
        await inter.send(f'After {random.randint(1,100)} years.')
    if whentype == 7:
        await inter.send(f'After {random.randint(1,10000)} milleniums.')
    if whentype == 8:
        await inter.send(f'After {random.randint(1,100000000000000000)} milleniums... That\'s too much!')

@client.slash_command(description="I don't know what i can put here :D")
async def yesorno(inter, question: str):
    """
    Parameters
    ----------
    question: ahbgjivker
    """
    helloyesorno = ['https://media.discordapp.net/attachments/806308041115959377/911742147655508038/hellono_but_big.png',
            'https://media.discordapp.net/attachments/806308041115959377/911742147999445052/helloyes_but_big.png']
    embed=discord.Embed(title=question, description="", color=0xFECC4D)
    embed.set_footer(text=inter.author.id)
    embed.set_image(url=random.choice(helloyesorno))
    await inter.send(embed=embed)

@client.slash_command(description="Make lelbot say something")
async def say(inter, message: str):
    """
    Parameters
    ----------
    message: message lol
    """
    await inter.send(f"{message}\n\n**- {inter.author} ({inter.author.id})**", allowed_mentions = discord.AllowedMentions(everyone = False))

@client.slash_command(description="Hug someone :)")
async def hug(inter, someone="**literally no one**"):
    """
    Parameters
    ----------
    someone: uwu
    """
    await inter.send(f"{inter.author.mention} hugged {someone}! <:Hello_UwU:822546152402321428>", allowed_mentions = discord.AllowedMentions(everyone = False))

@client.slash_command(description="Attack someone :)")
async def attack(inter, someone="**literally no one**"):
    """
    Parameters
    ----------
    someone: unu
    """
    await inter.send(f"{inter.author.mention} attacked {someone}! <:Gun:816099538619072553> <:Hello_Angry:822546148534386699>", allowed_mentions = discord.AllowedMentions(everyone = False))

@client.slash_command(description="Bam someone!")
async def bam(inter, someone: str, reason: str='None'):
    """
    Parameters
    ----------
    someone: >:c
    reason: Why you want to bam someone
    """
    await inter.send(f"{someone} has (not) been banned by {inter.author.mention} (Reason: {reason})")

@client.slash_command(description="Explode something!")
async def boom(inter, something: str):
    """
    Parameters
    ----------
    something: Yes
    """
    embed=discord.Embed(title="Boom!", description=f'{something} exploded!\nDamage: {random.randint(1,100)}', color=0xFECC4D)
    embed.set_footer(text=f'Exploded by {inter.author}')
    await inter.send(embed=embed)

@client.slash_command(description="Hackn't something!")
async def hack(inter, something: str):
    """
    Parameters
    ----------
    something: hejusidghjk
    """
    await inter.send(content=f"Getting access to {something}...")
    await asyncio.sleep(5)
    await inter.edit_original_message(content=f"Found email! ({something}{str(random.randint(10000000,99999999))}@lelmail.com)")
    await asyncio.sleep(2.5)
    await inter.edit_original_message(content="Found emojis from their phone cuz why not <:lelcube:811058465383514132>")
    await asyncio.sleep(3)
    await inter.edit_original_message(content="Drinking coffee... :coffee:")
    await asyncio.sleep(3.1)
    await inter.edit_original_message(content="Exploding my own database lol <:lelcube:811058465383514132>")
    await asyncio.sleep(4)
    await inter.edit_original_message(content="Selling their data to a random person...")
    await asyncio.sleep(3.5)
    await inter.edit_original_message(content=f"{inter.author.mention} Hacked {something} successfully!")

@client.slash_command(description="Get a random sandwich lol")
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
    await inter.send(f'You got... **{random.choice(randsandwich)}**!')

@client.slash_command(description="Make a cook poll")
async def poll(inter, text: str, option1: str, option2: str):
    """
    Parameters
    ----------
    text: Text :D
    option1: Don't include an emoji here
    option2: Don't include an emoji here²
    """
    embed=discord.Embed(title=text, description=f':one: = {option1}\n:two: = {option2}', color=0xFECC4D)
    embed.set_footer(text=f'Poll by {inter.author} ({inter.author.id})')
    await inter.send(embed=embed)
    Poll = await inter.original_message()
    await Poll.add_reaction('1️⃣')
    await Poll.add_reaction('2️⃣')

@client.slash_command(description="Suggest something, nice")
async def suggest(inter, suggestion: str):
    """
    Parameters
    ----------
    suggestion: text lol
    """
    embed=discord.Embed(title=f"{inter.author} suggestion", description=suggestion, color=0xFECC4D)
    embed.set_footer(text=inter.author.id)
    await inter.send(embed=embed)
    msg = await inter.original_message()
    await msg.add_reaction('✅')
    await msg.add_reaction('❎')
    await msg.add_reaction('🤔')
    await msg.add_reaction('❓')

@client.slash_command(description="A weird text")
async def weirdtext(inter):
    a_lot_of_characters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    await inter.send(f'{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}{random.choice(a_lot_of_characters)}')

@client.slash_command(description="See lelcube doing a random task")
async def dostuff(ctx,index="random"):
    """
    Parameters
    ----------
    index: If you don't put anything here, the index will be random
    """
    no_NOOOOO = False
    
    try:
        int_index = int(index)
    except:
        index = "random"

    if index == "random":
        lelbot_tasks_index = random.randint(1,85)
        no_NOOOOO = True
    else:
        if int_index < 1 or int_index > 85:
            await ctx.send("Invalid index! Please enter something between 1 and 85.")
        else:
            lelbot_tasks_index = int_index
            no_NOOOOO = True

    lelcube = "<:lelcube:811058465383514132>"

    #choices = [':microphone2: <:lelcube:811058465383514132>&&He sings',':frame_photo: :paintbrush: <:lelcube:811058465383514132>&&He paints',':computer: <:lelcube:811058465383514132>&&He codes',':video_game: <:lelcube:811058465383514132>&&He play games',':potato: <:Gun:816099538619072553> <:lelcube:811058465383514132>',':tv: <:lelcube:811058465383514132>&&He watches tv',':hammer: <:lelcube:811058465383514132>&&He destroy stuff',':shower:\n<:lelcube:811058465383514132>&&He showers','<:lelcube:811058465383514132> :shopping_cart:&&He goes shopping',':balloon: <:lelcube:811058465383514132>&&He plays with balloon',':wastebasket: :newspaper2: <:lelcube:811058465383514132>&&He doesnt like to read cuz reading is boring and i just noticed that to use discord you have to read which is boring so technicly using discord is boring but is not eeeeeeeeeeeee',':video_camera: <:lelcube:811058465383514132>&&He records a video',':pencil: <:lelcube:811058465383514132>&&He writes a text','<:Nextie:835598971518189621> :mag: <:lelcube:811058465383514132>&&He is trying to see nextie *but nextie has the size of a __pixel__*','<:lelcube:811058465383514132> :loudspeaker:&&He says potatopatata very loud',':cake: :fork_and_knife: <:lelcube:811058465383514132>&&He eats a cake',':iphone: <:lelcube:811058465383514132>&&He uses the phone',':pizza: <:lelcube:811058465383514132>&&He is 101% sure that pizza is pizza','<:clapping:811058070843162686> <:lelcube:811058465383514132>&&He claps','<:lelcube:811058465383514132> :vs: <:sweatsmile:811059266806480916>&&He fights',':telephone_receiver: <:lelcube:811058465383514132>&&He calls people','<:lelcube:811058465383514132> :tent:&&He goes camping',':ballet_shoes: <:lelcube:811058465383514132>&&He uses a ballet shoes','<:lelcube:811058465383514132> :toothbrush: :toilet:&&He uses a ballet shoes',':tophat:\n<:lelcube:811058465383514132> :magic_wand:&&He magic man',':saxophone: <:lelcube:811058465383514132>&&He plays the saxophone cuz saxophones are cool','<:lelcube:811058465383514132> ']
    if no_NOOOOO == True:

        if lelbot_tasks_index == 1:
            await ctx.send(f'🎙 <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He sings')
        if lelbot_tasks_index == 2:
            await ctx.send(f':frame_photo: :paintbrush: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He paints')
        if lelbot_tasks_index == 3:
            await ctx.send(f':computer: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He codes')
        if lelbot_tasks_index == 4:
            await ctx.send(f':video_game: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He play games')
        if lelbot_tasks_index == 5:
            await ctx.send(f':potato: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He kills potatos')
        if lelbot_tasks_index == 6:
            await ctx.send(f':tv: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He watches tv')
        if lelbot_tasks_index == 7:
            await ctx.send(f':hammer: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He destroy stuff')
        if lelbot_tasks_index == 8:
            await ctx.send(f':shower:\n<:lelcube:811058465383514132>')
            await ctx.channel.send(f'He showers')
        if lelbot_tasks_index == 9:
            await ctx.send(f'<:lelcube:811058465383514132> :shopping_cart:')
            await ctx.channel.send(f'He goes shopping')
        if lelbot_tasks_index == 10:
            await ctx.send(f':balloon: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He plays with balloon')
        if lelbot_tasks_index == 11:
            await ctx.send(f':wastebasket: :newspaper2: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He doesnt like to read cuz reading is boring and i just noticed that to use discord you have to read which is boring so technicly using discord is boring but is not eeeeeeeeeeeee')
        if lelbot_tasks_index == 12:
            await ctx.send(f':video_camera: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He records a video')
        if lelbot_tasks_index == 13:
            await ctx.send(f':pencil: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He writes a text')
        if lelbot_tasks_index == 14:
            await ctx.send(f'<:Nextie:835598971518189621> :mag: <:lelcube:811058465383514132>')
            worstjokeever = await ctx.channel.send(f'He is trying to see nextie *but nextie have the size of a __pixel__*')
            await worstjokeever.add_reaction('<:bassrolf:821948606701371462>')
        if lelbot_tasks_index == 15:
            await ctx.send(f'<:lelcube:811058465383514132> :loudspeaker:')
            await ctx.channel.send(f'He says potatopatata very loud')
        if lelbot_tasks_index == 16:
            await ctx.send(f':cake: :fork_and_knife: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He eats a cake')
        if lelbot_tasks_index == 17:
            await ctx.send(f':iphone: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He uses the phone')
        if lelbot_tasks_index == 18:
            await ctx.send(f':pizza: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He is 101% sure that pizza is pizza')
        if lelbot_tasks_index == 19:
            await ctx.send(f'<:clapping:811058070843162686> <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He claps')
        if lelbot_tasks_index == 20:
            await ctx.send(f'<:lelcube:811058465383514132> :vs: <:sweatsmile:811059266806480916>')
            await ctx.channel.send(f'He fights')
        if lelbot_tasks_index == 21:
            await ctx.send(f':telephone_receiver: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He calls people')
        if lelbot_tasks_index == 22:
            await ctx.send(f'<:lelcube:811058465383514132> :tent:')
            await ctx.channel.send(f'He goes camping')
        if lelbot_tasks_index == 23:
            await ctx.send(f':ballet_shoes: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He uses a ballet shoes')
        if lelbot_tasks_index == 24:
            await ctx.send(f'<:lelcube:811058465383514132> :toothbrush: :toilet:')
            await ctx.channel.send(f'He clean the toilet')
        if lelbot_tasks_index == 25:
            await ctx.send(f":tophat:\n<:lelcube:811058465383514132> :magic_wand:")
            await ctx.channel.send(f'He magic man')
        if lelbot_tasks_index == 26:
            await ctx.send(f':saxophone: <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He plays the saxophone cuz saxophones are cool')
        if lelbot_tasks_index == 27:
            await ctx.send(f'<:lelcube:811058465383514132> <:okhand:811059019828428821>')
            await ctx.channel.send(f'He likes *something*')
        if lelbot_tasks_index == 28:
            await ctx.send(f'<:sweatwide1:818622702574632970><:lelcube:811058465383514132><:sweatwide2:818622715815526481>')
            await ctx.channel.send(f'He uses a disguise')
        if lelbot_tasks_index == 29:
            await ctx.send(f':sweat_smile: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
            await ctx.channel.send(f'He kills')
        if lelbot_tasks_index == 30:
            await ctx.send(f'<:maum1:778489567036178464> <:lelcube:811058465383514132> <:maum2:778489689014403072>')
            await ctx.channel.send(f'He will catch you')
        if lelbot_tasks_index == 31:
            await ctx.send(f'<:lelcube:811058465383514132> :dash:')
            await ctx.channel.send('He fards')
        if lelbot_tasks_index == 32:
            await ctx.send(f'<:lelcube:811058465383514132>\n:blue_car:')
            await ctx.channel.send('He drives a car')
        if lelbot_tasks_index == 33:
            await ctx.send(':boom: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
            await ctx.channel.send('He commits war crimes')
        if lelbot_tasks_index == 34:
            await ctx.send(':wolf: <:Gun:816099538619072553> <:lelcube:811058465383514132>')
            await ctx.channel.send('He hunts')
        if lelbot_tasks_index == 35:
            await ctx.send(':cloud_rain:\n:umbrella:\n<:lelcube:811058465383514132>')
            await ctx.channel.send('He is on rain')
        if lelbot_tasks_index == 36:
            await ctx.send('<:lelcube:811058465383514132>\n:sailboat: :island:')
            await ctx.channel.send('He escapes island')
        if lelbot_tasks_index == 37:
            await ctx.send(':cooking: <:lelcube:811058465383514132>')
            await ctx.channel.send('He cooks')
        if lelbot_tasks_index == 38:
            await ctx.send(':ping_pong: <:lelcube:811058465383514132>')
            await ctx.channel.send('He plays ping pong')
        if lelbot_tasks_index == 39:
            await ctx.send(':guitar: <:lelcube:811058465383514132>')
            await ctx.channel.send('He plays guitar')
        if lelbot_tasks_index == 40:
            await ctx.send('<:blushing:821505454361935902> :heart: <:lelcube:811058465383514132>')
            await ctx.channel.send('He finds love')
        if lelbot_tasks_index == 41:
            await ctx.send(':desktop: :hammer: <:lelcube:811058465383514132>')
            await ctx.channel.send('He hacks')
        if lelbot_tasks_index == 42:
            await ctx.send(':telescope: <:lelcube:811058465383514132>')
            await ctx.channel.send('He sees the space')
        if lelbot_tasks_index == 43:
            await ctx.send(':microscope: <:lelcube:811058465383514132>')
            await ctx.channel.send('He finds the close ad button')
        if lelbot_tasks_index == 44:
            await ctx.send(':desktop: <:lelcube:811058465383514132>')
            await ctx.channel.send('He works on the computer')
        if lelbot_tasks_index == 45:
            await ctx.send(':moneybag: <:lelcube:811058465383514132>')
            await ctx.channel.send('He gets paid')
        if lelbot_tasks_index == 46:
            await ctx.send(':chart_with_upwards_trend: <:lelcube:811058465383514132>')
            await ctx.channel.send('He stonks')
        if lelbot_tasks_index == 47:
            await ctx.send(':house_with_garden: :money_with_wings: <:lelcube:811058465383514132>')
            await ctx.channel.send('He buys house')
        if lelbot_tasks_index == 48:
            await ctx.send('<:sweatsmile:811059266806480916> :gift: <:lelcube:811058465383514132>')
            await ctx.channel.send('He gets gift')
        if lelbot_tasks_index == 49:
            await ctx.send('🥳 🥳 🥳 🥳 <:lelcube:811058465383514132> 🥳 🥳 🥳')
            await ctx.channel.send('He goes to party')
        if lelbot_tasks_index == 50:
            await ctx.send(':airplane_departure: <:lelcube:811058465383514132>')
            await ctx.channel.send('He flies')
        if lelbot_tasks_index == 51:
            await ctx.send(':book: <:lelcube:811058465383514132>')
            await ctx.channel.send('He reads books')
        if lelbot_tasks_index == 52:
            await ctx.send(':mag: <:lelcube:811058465383514132>')
            await ctx.channel.send('He searches')
        if lelbot_tasks_index == 53:
            await ctx.send(':broom: <:lelcube:811058465383514132>')
            await ctx.channel.send('He does chores')
        if lelbot_tasks_index == 54:
            await ctx.send(':jack_o_lantern: :skull: <:lelcube:811058465383514132>')
            await ctx.channel.send('He is on spooky month')
        if lelbot_tasks_index == 55:
            await ctx.send('<:maum1:778489567036178464> :gem: <:lelcube:811058465383514132> <:maum2:778489689014403072>')
            await ctx.channel.send('He steals')
        if lelbot_tasks_index == 56:
            await ctx.send('<:lelcube:811058465383514132> :arrows_counterclockwise:')
            await ctx.channel.send('He spins')
        if lelbot_tasks_index == 57:
            await ctx.send('<:lelcube:811058465383514132> :zzz:\n:bed:')
            await ctx.channel.send('He sleeps')
        if lelbot_tasks_index == 58:
            await ctx.send('<:lelcube:811058465383514132>\n:bus:')
            await ctx.channel.send('He is on a bus')
        if lelbot_tasks_index == 59:
            await ctx.send(':placard: <:lelcube:811058465383514132>')
            await ctx.channel.send('He reads a sign')
        if lelbot_tasks_index == 60:
            await ctx.send(':bulb:\n<:lelcube:811058465383514132>')
            await ctx.channel.send('He gets an idea')
        if lelbot_tasks_index == 61:
            await ctx.send(':watch: <:lelcube:811058465383514132>')
            await ctx.channel.send('He watches a watch')
        if lelbot_tasks_index == 62:
            await ctx.send(':electric_plug: <:lelcube:811058465383514132>')
            await ctx.channel.send('He starts his new time machine')
        if lelbot_tasks_index == 63:
            await ctx.send(':test_tube: <:lelcube:811058465383514132>')
            await ctx.channel.send('He scientist')
        if lelbot_tasks_index == 64:
            await ctx.send('<:lelcube:811058465383514132>\n:couch:')
            await ctx.channel.send('He is on a couch')
        if lelbot_tasks_index == 65:
            await ctx.send('He flipped the messages')
            await ctx.channel.send(':level_slider: <:lelcube:811058465383514132>')
        if lelbot_tasks_index == 66:
            await ctx.send(f'{lelcube} :selfie:')
            await ctx.channel.send('He takes a selfie')
        if lelbot_tasks_index == 67:
            await ctx.send(f':left_facing_fist: {lelcube}')
            await ctx.channel.send('He punches')
        if lelbot_tasks_index == 68:
            await ctx.send(f':mouse_three_button: :hammer: {lelcube}')
            await ctx.channel.send('He clicks on the "get free bobux" button 999999999 times')
        if lelbot_tasks_index == 69:
            #nice
            await ctx.send(f"{lelcube}\n:evergreen_tree:")
            await ctx.channel.send('He is on a tree')
        if lelbot_tasks_index == 70:
            await ctx.send(f"{lelcube}\n:full_moon_with_face:")
            await ctx.channel.send('He is on the moon')
        if lelbot_tasks_index == 71:
            await ctx.send(f":arrow_left: {lelcube} :cloud_tornado:")
            await ctx.channel.send('He runs cuz there\'s a tornado')
        if lelbot_tasks_index == 72:
            await ctx.send(f'{lelcube}\n:ship:')
            await ctx.channel.send('He is on a ship')
        if lelbot_tasks_index == 73:
            await ctx.send(f':taco: {lelcube}')
            await ctx.channel.send('He eats a taco')
        if lelbot_tasks_index == 74:
            await ctx.send(f':spoon: {lelcube}')
            await ctx.channel.send('He has a super cook spoon')
        if lelbot_tasks_index == 75:
            await ctx.send(f':cup_with_straw: {lelcube}')
            await ctx.channel.send('He drinks water')
        if lelbot_tasks_index ==  76:
            await ctx.send(lelcube)
            await ctx.channel.send('He')
        if lelbot_tasks_index == 77:
            await ctx.send(f"🟨🟨🟨🟨🟨🟨🟨🟨\n🟫🟫🟨🟫🟫🟦⬜🟨\n🟨🟨🟨🟨🟨🟨🟦⬜\n⬜🟫🟨⬜🟫🟨🟦🟦\n🟨🟨🟨🟨🟨🟨🟨🟨\n🟨🟫⬜⬜🟫🟨🟨🟨\n🟨🟨🟫🟫🟨🟨🟨🟨\n🟨🟨🟨🟨🟨🟨🟨🟨 {lelcube}")
            await ctx.channel.send('He made statue')
        if lelbot_tasks_index == 78:
            await ctx.send(f":ballot_box_with_check: {lelcube}")
            await ctx.channel.send('He approves nonsenses')
        if lelbot_tasks_index == 79:
            await ctx.send(f":turtle: {lelcube}")
            await ctx.channel.send('He has a pet called tutel')
        if lelbot_tasks_index == 80:
            await ctx.send(f"{lelcube} :medal: {lelcube}")
            await ctx.channel.send('He gives a medal to lelcube')
        if lelbot_tasks_index == 81:
            await ctx.send(f":point_down:{lelcube}\n<:grass:951926072792981579><:grass:951926072792981579>")
            await ctx.send('He touches grass')
        if lelbot_tasks_index == 82:
            await ctx.send(f"🔪🛸🗡️\n🪝{lelcube}<:Gun:816099538619072553>\n💉📯🪛")
            await ctx.channel.send('He is in danger')
        if lelbot_tasks_index == 83:
            await ctx.send(f":bug: <:Gun:816099538619072553> {lelcube}")
            await ctx.channel.send('He fixes bugs')
        if lelbot_tasks_index == 84:
            await ctx.send(f":coffee: {lelcube}")
            await ctx.channel.send('He likes coffee')
        if lelbot_tasks_index == 85:
            await ctx.send(f":circus_tent: {lelcube}")
            await ctx.channel.send('He goes to circus')

@client.slash_command(description="Builds a custom embed")
async def embed(inter, title: str, description: str, color: str=0xFECC4D, footer: str="Super cook embed", url: str=None):
    """
    Parameters
    ----------
    title: Embed title
    description: Embed description
    color: Embed color
    footer: Embed footer
    url: Embed image url
    """
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
    await webhook.send(embed=embed, username=inter.author.name, avatar_url=inter.author.avatar)
    await webhook.delete()
    await inter.send("Posted embed!", ephemeral=True)

@client.slash_command(description="Get a random sweatsmile")
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
    await inter.send(random.choice(sweatversions))

@client.slash_command(description="Get a random number")
async def random_number(inter, min: int, max: int):
    """
    Parameters
    ----------
    min: min
    max: max
    """
    await inter.send(str(random.randint(min,max)))

@client.slash_command(description="i don't know anymore")
async def bobux(inter):
    BOBUX1 = ['b','*b*','**b**','***b***','__b__','__*b*__','__**b**__','__***b***__','B','*B*','**B**','***B***','__B__','__*B*__','__**B**__','__***B***__']
    BOBUX2 = ['o','*o*','**o**','***o***','__o__','__*o*__','__**o**__','__***o***__','O','*O*','**O**','***O***','__O__','__*O*__','__**O**__','__***O***__']
    BOBUX3 = ['u','*u*','**u**','***u***','__u__','__*u*__','__**u**__','__***u***__','U','*U*','**U**','***U***','__U__','__*U*__','__**U**__','__***U***__']
    BOBUX4 = ['x','*x*','**x**','***x***','__x__','__*x*__','__**x**__','__***x***__','X','*X*','**X**','***X***','__X__','__*X*__','__**X**__','__***X***__']

    await inter.send(f'{random.choice(BOBUX1)} {random.choice(BOBUX2)} {random.choice(BOBUX1)} {random.choice(BOBUX3)} {random.choice(BOBUX4)}')

@client.slash_command(description="Get a random hello version")
async def hello(inter, someone: str=""):
    """
    Parameters
    ----------
    someone: e
    """
    hello = ["Hello", "Hi", "Helo", "Henlo", "Yo", "Hellooo", "Helooo", "Henlooo", "Hi hello", "Hello hi", "Hellooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo", "***Hej***", "Hola", "Hewwo"]
    await inter.send(f"{random.choice(hello)} {someone}")

@client.slash_command(description="Get the bot invite!")
async def invite(inter):
    embed = discord.Embed(title="Invite", description="Click [here](https://discord.com/api/oauth2/authorize?client_id=822199023636709456&permissions=8&scope=bot%20applications.commands) to invite lelbot on your cook server!", color=0xFECC4D)
    embed.set_footer(text=":)")
    await inter.send(embed=embed)

@client.slash_command(description="About me 😉")
async def aboutme(inter):
    ABOTME_embed=discord.Embed(title=f'About lelbot', description=f"Hello! I'm lelbot, the smartest AI in the universe, created by hellory5n, a very evil guy with very dumb plans!\nBy the way this is hellory5n: <:hellory5n:915028960604200982>\nMy birthday is on april 6, cuz lelbot 0.1 was released in april 6, 2021!", color=0xFECC4D)
    ABOTME_embed.set_footer(text="Version 1.5.1")
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

@client.slash_command(description="Increase a cooki counter!")
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

    await inter.send(f'Now we have **{str(cookis)}** cookis! :cookie: {ok}')

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

@client.slash_command(description="Get money :)")
@commands.cooldown(1, 60, commands.BucketType.user)
async def work(inter):
    await inter.response.defer()
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

    await inter.send(f"{random.choice(replies)} Your cash is now {ok['cash']} <:lelgold:888933451410075689>")

@client.slash_command(description="See your money")
async def balance(inter, user: discord.User=None):
    """
    Parameters
    ----------
    user: If you don't put anything here, I'll use you!
    """
    if user==None:
        filename = str(inter.author.id) + '.json'
        user=inter.author
        create_user_if_it_dont_exist(inter.author.id)
    else:
        filename = str(user.id) + '.json'
        create_user_if_it_dont_exist(user.id)

    with open(filename, 'r') as f:
        ok = json.load(f)
    
    embed = discord.Embed(title=f"{user}'s balance", description="", color=0xFECC4D)
    embed.add_field(name="Cash", value=f"{ok['cash']} <:lelgold:888933451410075689>", inline=True)
    embed.add_field(name="Bank",value=f"{ok['bank']} <:lelgold:888933451410075689>", inline=True)
    embed.add_field(name="Total",value=f"{ok['cash'] + ok['bank']} <:lelgold:888933451410075689>", inline=True)
    embed.set_footer(text=str(inter.author.id))
    await inter.send(embed=embed)

@client.slash_command(description="Deposit your money")
async def deposit(inter, value:int):
    """
    Parameters
    ----------
    value: The value you want to deposit
    """
    filename = str(inter.author.id) + '.json'

    create_user_if_it_dont_exist(inter.author.id)
    
    with open(filename, 'r') as f:
        ok = json.load(f)
    
    if value > 0 and value < ok['cash'] + 1:
        ok['cash'] -= value
        ok['bank'] += value

        with open(filename, 'w') as f:
            json.dump(ok, f)
    
        await inter.send("Boom")
    else:
        await inter.send("Lol no")

@client.slash_command(description="Withdraw your money")
async def withdraw(inter, value: int):
    """
    Parameters
    ----------
    value: The value you want to withdraw
    """
    filename = str(inter.author.id) + '.json'

    create_user_if_it_dont_exist(inter.author.id)
    
    with open(filename, 'r') as f:
        ok = json.load(f)
    
    if value > 0 and value < ok['bank'] + 1:
        ok['cash'] += value
        ok['bank'] -= value

        with open(filename, 'w') as f:
            json.dump(ok, f)
    
        await inter.send("Boom")
    else:
        await inter.send("Lol no")

@client.slash_command(description="See the leaderboard")
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

    prevb = Button(
            style=ButtonStyle.blurple,
            label="Previous page",
            custom_id="prev_button",
            disabled=not can_go_back
        )
    nextb = Button(
            style=ButtonStyle.blurple,
            label="Next page",
            custom_id="next_button",
            disabled=not can_go_forward
        )

    interwithadifferentname = inter

    async def on_next(inter):
        if interwithadifferentname.author.id == inter.author.id:
            nonlocal page
            nonlocal prevb
            nonlocal nextb
            can_go_back = True
            can_go_forward = True
            page += 1

            prevb.disabled = not can_go_back
            nextb.disabled = not can_go_forward
            newrow = View()
            newrow.add_item(prevb)
            newrow.add_item(nextb)

            lb_uwu = ""

            for key,value in users_chunks[page].items():
                lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

            embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
            embed.set_footer(text=str(inter.author.id))

            await msg.edit(embed=embed, view=newrow)
        else:
            await inter.send("You aren't the author :P",ephemeral=True)

    async def on_previous(inter):
        if interwithadifferentname.author.id == inter.author.id:
            nonlocal page
            nonlocal prevb
            nonlocal nextb
            can_go_back = True
            can_go_forward = True
            page -= 1

            prevb.disabled = not can_go_back
            nextb.disabled = not can_go_forward
            newrow = View()
            newrow.add_item(prevb)
            newrow.add_item(nextb)

            lb_uwu = ""

            for key,value in users_chunks[page].items():
                lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

            embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
            embed.set_footer(text=str(inter.author.id))

            await msg.edit(embed=embed, view=newrow)
        else:
            await interwithadifferentname.send("You aren't the author :P",ephemeral=True)

    prevb.callback = on_previous
    nextb.callback = on_next
    row = View()
    row.add_item(prevb)
    row.add_item(nextb)
    await inter.send(embed=embed, view=row)
    msg = await inter.original_message()
    
@client.slash_command(description="See all of the shop items!")
async def shop(inter):
    items = ""

    with open("items.txt", 'r') as f:
        txt = f.read()
    
    txt2 = txt.split("\n")

    for i in txt2:
        item_info = i.split("&&")
        items = items + item_info[3] + " `" + item_info[0] + "` (" + item_info[1] + " <:lelgold:888933451410075689>)" + "\n" + item_info[2] + "\n\n"
    
    await inter.send(items)

Items = commands.option_enum(
    {"Void": "Void",
    "Cooki": "Cooki",
    "Arnold cooki": "Arnold cooki",
    "Linux": "Linux",
    "Lelcube plushie":"Lelcube plushie",
    "Windows Vista":"Windows Vista",
    "Terrible laptop":"Terrible laptop",
    "Free bobux":"Free bobux",
    "eyePhone":"eyePhone",
    "Top secret lelcube images":"Top secret lelcube images",
    "Internet Explorer 12":"Internet Explorer 12",
    "Clippy":"Clippy",
    "Illegal DVD":"Illegal DVD",
    "iMark":"iMark",
    "Super snowman":"Super snowman",
    "Metal cake":"Metal cake"}
)

@client.slash_command(description="Buy something :)")
async def buy(inter, item: Items, amount: int=1):
    """
    Parameters
    ----------
    item: The item you want to buy
    amount: The amount that you want to buy
    """
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

            await inter.send("Boom")
        else:
            await inter.send("Lol you can't buy this")
    else:
        await inter.send("Lol wot")

@client.slash_command(description="See your items")
async def inventory(inter, user: discord.User=None):
    """
    Parameters
    ----------
    user: If you don't put something here, I'll use you!
    """
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
        await inter.send(embed=embed)
    except:
        await inter.send("It looks like you don't have items. (If you actually have then this is a bug)")

@client.slash_command(description="Use an item that you have")
async def use(inter, item: Items, amount: int=1):
    """
    Parameters
    ----------
    item: The item you want to use
    amount: The amount that you want to use
    """
    create_user_if_it_dont_exist(inter.author.id)

    ono = False

    with open(f"{str(inter.author.id)}_items.json", 'r') as f:
        items = json.load(f)
    
    if item not in items or items[item] < amount:
        ono = True
        await inter.send("Lol you don't have this item")

    if amount < 1:
        ono = True
        await inter.send("Das illegal")

    if ono == False:
        items[item] = items[item] - amount

        with open(f"{str(inter.author.id)}_items.json", 'w') as f:
            json.dump(items, f)
        
        if item == "Cooki":
            await inter.send(":yum:")
        elif item == "Linux":
            await inter.send("Congratulations you was scammed :clap: <:lelcube:811058465383514132>")
        elif item == "Lelcube plushie":
            hug = Button(
                    style=ButtonStyle.green,
                    label="Hug it :)",
                    custom_id="hug"
                )
            play = Button(
                    style=ButtonStyle.green,
                    label="Play with it :)",
                    custom_id="play"
            )
            boom = Button(
                    style=ButtonStyle.red,
                    label="Explode it",
                    custom_id="boom"
            )

            interwithadifferentname = inter

            async def on_hug(inter):
                if interwithadifferentname.author.id == inter.author.id:
                    await msg.edit(content="You hugged the plushie! <:Hello_UwU:822546152402321428>")
                else:
                    await inter.send(content="You're not the author :P",ephemeral=True)
            
            async def on_play(inter):
                if interwithadifferentname.author.id == inter.author.id:
                    await msg.edit(content="You played with the plushie! <:Hello_OwO:822546151010074694>")
                else:
                    await inter.send(content="You're not the author :P",ephemeral=True)
            
            async def on_boom(inter):
                if interwithadifferentname.author.id == inter.author.id:
                    await msg.edit(content="You exploded the plushie, no buttons for you >:(", view=None)
                else:
                    await inter.send(content="You're not the author :P",ephemeral=True)

            hug.callback = on_hug
            play.callback = on_play
            boom.callback = on_boom
            row = View()
            row.add_item(hug)
            row.add_item(play)
            row.add_item(boom)
            
            await inter.send("What you want to do with the lelcube plushie?", view=row)
            msg = await inter.original_message()

        elif item == "Windows Vista":
            await inter.send("Starting Windows...")
            msg = await inter.original_message()
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
            use = Button(
                style=ButtonStyle.green,
                label="Use its OS (Which is Windows 10)",
                custom_id="use"
            )
            specs = Button(
                style=ButtonStyle.green,
                label="Show its specifications",
                custom_id="specs"
            )
            boom = Button(
                style=ButtonStyle.red,
                label="Destroy it lol",
                custom_id="boom"
            )

            interwithanothername = inter

            async def on_use(inter):
                if interwithanothername.author.id == inter.author.id:
                    await msg.edit(content="https://cdn.discordapp.com/attachments/778461818686406678/903431704197337178/unknown.png")
                else:
                    await inter.send(content="You're not the author :P",ephemeral=True)
            
            async def on_specs(inter):
                if interwithanothername.author.id == inter.author.id:
                    await msg.edit(content="RAM: 2GB RAM\nHDD: 32GB\nCPU: Intel Atom\nGPU: Nonexistent\nOthers: Its design was made in 3 minutes :thumbsup:")
                else:
                    await inter.send(content="You're not the author :P",ephemeral=True)
            
            async def on_boom(inter):
                if interwithanothername.author.id == inter.author.id:
                    await msg.edit(content="That's a good choice",view=None)
                else:
                    await inter.send(content="You're not the author :P",ephemeral=True)
            
            use.callback = on_use
            specs.callback = on_specs
            boom.callback = on_boom

            view = View()
            view.add_item(use)
            view.add_item(specs)
            view.add_item(boom)
            await inter.send("What you want to do with the ~~terrible~~ laptop?",view=view)
            msg = await inter.original_message()

        elif item == "Free bobux":
            hax = Button(
                    style=ButtonStyle.green,
                    label="CONFIRM FREE BOBUX 🤑🤑🤑🤑🤑🤑🤑🤑🤑",
                    custom_id="hax"
                )

            definitelynotinter = inter
            async def on_hax(inter):
                if definitelynotinter.author.id == inter.author.id:
                    await msg.edit(content=f"Getting access to {inter.author.name}...",view=None)
                    await asyncio.sleep(5)
                    await msg.edit(content=f"Found email! ({inter.author.name}{str(random.randint(10000000,99999999))}@lelmail.com)")
                    await asyncio.sleep(2.5)
                    await msg.edit(content="Found emojis from their phone cuz why not <:lelcube:811058465383514132>")
                    await asyncio.sleep(3)
                    await msg.edit(content="Drinking coffee... :coffee:")
                    await asyncio.sleep(3.1)
                    await msg.edit(content="Exploding my own database lol <:lelcube:811058465383514132>")
                    await asyncio.sleep(4)
                    await msg.edit(content="Selling their data to a random person...")
                    await asyncio.sleep(3.5)
                    await msg.edit(content=f"<@822199023636709456> Hacked {inter.author.name} successfully!")
                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            hax.callback = on_hax
            view = View()
            view.add_item(hax)
            await inter.send("CLICK IN \"CONFIRM FREE BOBUX\" TO CONFIRM FREE BOBUX :money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth:",view=view)
            msg = await inter.original_message()

        elif item == "Top secret lelcube images":
            await inter.send(":soap: <:lelcube:811058465383514132>\nYou know what this means?????????? It means Lelcube has soap!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111111111111111111!!1!!1!!!1!")
        elif item == "Void":
            await inter.send("** **")
        elif item == "Internet Explorer 12":
            await inter.send("Starting Internet Explorer...\n\nTip: Get a better browser")
        elif item == "Clippy":
            helpb = Button(
                    style=ButtonStyle.blurple,
                    label="Get help with writing the letter",
                    custom_id="help"
                )
            nohelp = Button(
                    style=ButtonStyle.blurple,
                    label="Write the letter without help",
                    custom_id="nohelp"
                )

            more = Button(
                    style=ButtonStyle.blurple,
                    label="More useful tips with Clippy!",
                    custom_id="more"
                )
            
            urmom = inter

            async def on_help(inter):
                if urmom.author.id == inter.author.id:
                    await msg.edit(content="To write letters, it's very easy! You just press a letter, or any character, and boom!",view=view2)
                else:
                    await inter.send(content="You're not the author :P",ephemeral=True)
            
            async def on_nohelp(inter):
                if urmom.author.id == inter.author.id:
                    await msg.edit(content="unu",view=None)
                else:
                    await inter.send(content="You're not the author :P",ephemeral=True)
            
            async def on_more(inter):
                if urmom.author.id == inter.author.id:
                    await msg.edit(content="Failed to load more tips.",view=None)
                else:
                    await inter.send(content="You're not the author :P",ephemeral=True)
            
            helpb.callback = on_help
            nohelp.callback = on_nohelp
            more.callback = on_more
            view = View()
            view2 = View()
            view.add_item(helpb)
            view.add_item(nohelp)
            view2.add_item(more)
            await inter.send("It looks like you're writing a letter.",view=view)
            msg = await inter.original_message()

        elif item == "Illegal DVD":
            await inter.send(":police_car:")
            msg = await inter.original_message()
            await asyncio.sleep(5)
            await msg.edit(content="The police is here, and you will be bammed!")
            await asyncio.sleep(5)
            await msg.edit(content=f"{inter.author.mention} has (not) been banned by <@822199023636709456> (Reason: Buying illegal DVDs)")
        elif item == "Arnold cooki":
            await inter.send(":yum::yum:")
        elif item == "eyePhone":
            await inter.send("Move your eye to use your eyePhone.")
            await asyncio.sleep(1)
            await inter.send("*phone explodes cuz the sensor thinks you want to explode the phone*")
        elif item == "iMark":
            await inter.send(":apple:")
            lol_wot = await inter.original_message()
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
            await lol_wot.edit(random.choice(ues))
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
            await inter.send(random.choice(ads))
        elif item == "Metal cake":
            await inter.send("Hmm, metal tastes so good! I love it! Tasty! Delicious! Incredible!")
            await asyncio.sleep(3)
            await inter.send("*explodes*")
        
        elif item == "Lelcube":
            items[item] = items[item] + amount*2

            with open(f"{str(inter.author.id)}_items.json", 'w') as f:
                json.dump(items, f)
            
            await inter.send("<:lelcube:811058465383514132>")
            await inter.channel.send(f"Now you have {items[item]} lelcubes :D")
        
        elif item == "Free lelgolds":
            values = {}
            modaluwu = Modal(
                title="Form where you put your info",
                custom_id="epok_cook_modal",
                components=[
                    TextInput(
                        label="Email address",
                        placeholder="Placeholder",
                        custom_id="email_address",
                        style=TextInputStyle.short,
                        max_length=150,
                    ),
                    TextInput(
                        label="Password lol",
                        placeholder="Placeholder",
                        custom_id="password_lol",
                        style=TextInputStyle.short,
                        max_length=150,
                    ),
                    TextInput(
                        label="IP address",
                        placeholder="Placeholder",
                        custom_id="ip_address",
                        style=TextInputStyle.short,
                        max_length=32,
                    ),
                    TextInput(
                        label="Why you want free lelgolds?",
                        placeholder="Placeholder",
                        custom_id="why",
                        style=TextInputStyle.paragraph,
                        max_length=512,
                    ),
                    TextInput(
                        label="Did you like this form?",
                        placeholder="Placeholder",
                        custom_id="yesorno",
                        style=TextInputStyle.short,
                        max_length=32,
                    )
                ]
            )

            await inter.response.send_modal(modaluwu)

            # Wait until the user submits the modal
            try:
                modal_inter: discord.ModalInteraction = await client.wait_for(
                    "modal_submit",
                    check=lambda i: i.custom_id == "epok_cook_modal" and i.author.id == inter.author.id,
                    timeout=1024,
                )
            except asyncio.TimeoutError:
                # lol took too much
                return
            
            '''for custom_id, value in modal_inter.text_values.items():
                values[custom_id] = value'''

            await modal_inter.response.send_message("Getting access to lelbot's servers...")
            msg = await modal_inter.original_message()
            await asyncio.sleep(3)
            await msg.edit(content="Bypassing firewall...")
            await asyncio.sleep(3)
            await msg.edit(content="Connecting to SQL database...")
            await asyncio.sleep(3)
            await msg.edit(content=f"Searching for database key \"{str(modal_inter.author.id)}_MONE\"")
            await asyncio.sleep(3)
            await msg.edit(content="Connecting to SQL database again...")
            await asyncio.sleep(3)
            await msg.edit(content=f"Modifying {random.randint(2,30000)} database keys...")
            await asyncio.sleep(3)
            await msg.edit(content=f"Stealing your discord account lol...")
            await asyncio.sleep(3)
            await msg.edit(content=f"I gave {random.randint(1,9999999999999)} lelgolds to your account BUT now your account is mine >:DDDDDDDD\nNow I finally can buy 942482 metal cakes :D")
        
        elif item == "Macrohard Doors 11":
            await inter.send(":door:\n\n:o:")
            msg = await inter.original_message()
            await asyncio.sleep(60)
            await msg.edit(content="Please wait... :o: (this will take 25 minutes)")
            await asyncio.sleep(720)
            await msg.edit(content="**11:11**\nhttps://cdn.discordapp.com/attachments/811060176265805825/962452691685101598/best-banner-ever-lol.png")
            await asyncio.sleep(10)
            await msg.edit(content=f"Logging to {inter.author.name}'s account...")
            await asyncio.sleep(720)
            await msg.edit(content="```ues\n:(\ntrololol doors 11 crashed trololol you have to restart :wink:```")
        
        elif item == "Pancakes":
            await inter.send(":pancakes: <:lelcube:811058465383514132>")
            await inter.channel.send("He eats pancakes")
        
        elif item == "The best movie out there":
            await inter.send("<:lelcube:811058465383514132>")
            scn = await inter.original_message()
            msg = await inter.channel.send("LELCUBE MOVIE PRODUCTIONS")
            await asyncio.sleep(6)
            await scn.edit(content=":deaf_person:")
            await msg.edit(content="FROM THE CREATORS OF /ADVENTURE AND THE BEST MOVIE OUT THERE")
            await asyncio.sleep(6)
            await msg.edit(content="INTRODUCING...")
            await asyncio.sleep(6)
            await msg.edit(content="THE BEST MOVIE OUT THERE")
            await asyncio.sleep(6)
            await scn.edit(content="<:lelcube:811058465383514132> :cookie:")
            await msg.edit(content="**Lelcube**\nI like cookis")
            await asyncio.sleep(6)
            await scn.edit(content="<:lelcube:811058465383514132>")
            await msg.edit(content="** **")
            await asyncio.sleep(3)
            await msg.edit(content="**Lelcube**\nono where is ma cooki")
            await asyncio.sleep(3)
            await scn.edit(content="<:lelcube:811058465383514132> <:void:834904392008335360> <:hellory5n:915028960604200982>")
            await msg.edit(content="**hellory5n**\ni stealed it lol")
            await asyncio.sleep(5)
            await scn.edit(content="<:lelcube:811058465383514132> <:nuG:915809814947463168> <:hellory5n:915028960604200982>")
            await msg.edit(content="** **")
            await asyncio.sleep(5)
            await msg.edit(content="A MOVIE BY LELCUBE MOVIE PRODUCTIONS")
            await asyncio.sleep(10)
            await msg.edit(content="WHY\nWHY I MADE THIS MOVIE")

@client.slash_command(description="Give money to another person")
async def give_money(inter, user: discord.User, amount: int):
    """
    Parameters
    ----------
    user: The user that will get your money
    amount: The amount of money that you will give
    """
    problems_ono = False

    create_user_if_it_dont_exist(inter.author.id)

    if user.id == inter.author.id:
        problems_ono = True
        await inter.send("You can't give money for yourself", ephemeral=True)
    
    input = f"{str(inter.author.id)}.json"
    output = f"{str(user.id)}.json"

    with open(input, 'r') as f_i:
        ok_i = json.load(f_i)
    
    if amount < 1 or not ok_i['cash'] > amount - 1:
        problems_ono = True
        await inter.send("You can't lol")
    
    if problems_ono == False:
        create_user_if_it_dont_exist(user.id)
        
        with open(output, 'r') as f_o:
            ok_o = json.load(f_o)
        
        ok_i['cash'] -= amount
        ok_o['cash'] += amount

        with open(input, 'w') as f_i:
            json.dump(ok_i, f_i)
        
        with open(output, 'w') as f_o:
            json.dump(ok_o, f_o)
        
        await inter.send("Boom")

@client.slash_command(description="Reset YOUR money")
async def reset_money(inter):
    filename = str(inter.author.id) + ".json"

    create_user_if_it_dont_exist(inter.author.id)

    yes = Button(
            style=ButtonStyle.red,
            label="Yes, reset my money!",
            custom_id="yes_button"
        )
    no = Button(
            style=ButtonStyle.blurple,
            label="Nevermind.",
            custom_id="no_button"
        )
    
    pain = inter

    async def on_yes(inter):
        if pain.author.id == inter.author.id:
            with open(filename, 'r') as f:
                ok = json.load(f)

            ok['cash'] = 0
            ok['bank'] = 0

            with open(filename, 'w') as f:
                json.dump(ok, f)

            await msg.edit(content="Successfully reseted.", view=None)
        else:
            await inter.send(content="You're not the author :P",ephemeral=True)
    
    async def on_no(inter):
        if pain.author.id == inter.author.id:
            await msg.edit(content="Ok",view=None)
        else:
            await inter.send(content="You're not the author :P",ephemeral=True)

    yes.callback = on_yes
    no.callback = on_no
    view = View()
    view.add_item(yes)
    view.add_item(no)

    await inter.send("Are you sure you want to reset your money??", view=view)
    msg = await inter.original_message()

@client.slash_command(description="Give an item to someone")
async def give_item(inter, user: discord.User, item: Items, amount: int=1):
    """
    Parameters
    ----------
    user: The user that will get the item
    item: The item that you will give
    amount: The amount that you will give
    """
    problems_ono = False
    
    create_user_if_it_dont_exist(inter.author.id)

    input = f"{str(inter.author.id)}_items.json"
    output = f"{str(user.id)}_items.json"

    with open(input, 'r') as f_i:
        ok_i = json.load(f_i)
    
    if amount < 1 or not ok_i[item] > amount - 1:
        problems_ono = True
        await inter.send("You can't lol")

    if user == inter.author:
        problems_ono = True
        await inter.send("You can't give items to yourself xd",ephemeral=True)

    if problems_ono == False:
        create_user_if_it_dont_exist(user.id)

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
        
        await inter.send("Boom")

@client.slash_command(description="Math")
async def math(ctx, expression:str):
    """
    Parameters
    ----------
    expression: Ues
    """
    expression = "".join(filter(lambda i: i in "9876543210+-×÷^*/()", expression))
    expression = expression.replace("^", "**").replace("÷", "/").replace("×", "*")
    await ctx.send(f"Math: {expression}\nResults: {float(eval(expression))}")

@client.command()
async def not_say(ctx, *, msg):
    if ctx.author.id == 748560377763201185:
        await ctx.send(msg)
    else:
        await ctx.send("You can't use this command lol")

@client.slash_command(description="Steal someone's money (don't do that, das bad >:c)")
@commands.cooldown(1, 60, commands.BucketType.user)
async def rob(inter, amount: int, user: discord.User):
    """
    Parameters
    ----------
    amount: The amount that you will steal
    user: The user that you will steal
    """
    problems_ono = False
    
    create_user_if_it_dont_exist(inter.author.id)

    output = f"{str(inter.author.id)}.json"
    input = f"{str(user.id)}.json"

    with open(input, 'r') as f_i:
        ok_i = json.load(f_i)
    
    if amount < 1 or not ok_i['cash'] > amount - 1:
        problems_ono = True
        await inter.send("You can't lol")
    
    if problems_ono == False:
        create_user_if_it_dont_exist(user.id)

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
            
            await inter.send("Boom")
        else:
            unu = random.randint(1,100)

            ok_o['cash'] -= unu

            with open(output, 'w') as f_o:
                json.dump(ok_o, f_o)
            
            await inter.send(f"You failed and lost {unu} <:lelgold:888933451410075689>")

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

@client.slash_command(description="See a random fact!")
async def fact(inter, index: int=None):
    """
    Parameters
    ----------
    index: The index that you want. If not present, the index will be random
    """
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
        create_user_if_it_dont_exist(inter.author.id)
    else:
        filename = str(user.id) + '.json'
        create_user_if_it_dont_exist(user.id)
    
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

    prevb = Button(
            style=ButtonStyle.blurple,
            label="Previous page",
            custom_id="prev_button",
            disabled=not can_go_back
        )
    nextb = Button(
            style=ButtonStyle.blurple,
            label="Next page",
            custom_id="next_button",
            disabled=not can_go_forward
        )

    interwithadifferentname = inter

    async def on_next(inter):
        if interwithadifferentname.author.id == inter.author.id:
            nonlocal page
            nonlocal prevb
            nonlocal nextb
            can_go_back = True
            can_go_forward = True
            page += 1

            prevb.disabled = not can_go_back
            nextb.disabled = not can_go_forward
            newrow = View()
            newrow.add_item(prevb)
            newrow.add_item(nextb)

            lb_uwu = ""

            for key,value in users_chunks[page].items():
                lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

            embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
            embed.set_footer(text=str(inter.author.id))

            await msg.edit(embed=embed, view=newrow)
        else:
            await inter.send("You aren't the author :P",ephemeral=True)

    async def on_previous(inter):
        if interwithadifferentname.author.id == inter.author.id:
            nonlocal page
            nonlocal prevb
            nonlocal nextb
            can_go_back = True
            can_go_forward = True
            page -= 1

            prevb.disabled = not can_go_back
            nextb.disabled = not can_go_forward
            newrow = View()
            newrow.add_item(prevb)
            newrow.add_item(nextb)

            lb_uwu = ""

            for key,value in users_chunks[page].items():
                lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

            embed=discord.Embed(title=f"Leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
            embed.set_footer(text=str(inter.author.id))

            await msg.edit(embed=embed, view=newrow)
        else:
            await interwithadifferentname.send("You aren't the author :P",ephemeral=True)

    prevb.callback = on_previous
    nextb.callback = on_next
    row = View()
    row.add_item(prevb)
    row.add_item(nextb)
    msg = await inter.send(embed=embed, view=row)

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

itemselect = [
    discord.SelectOption(label="Void"),
    discord.SelectOption(label="Cooki"),
    discord.SelectOption(label="Arnold cooki"),
    discord.SelectOption(label="Linux"),
    discord.SelectOption(label="Lelcube plushie"),
    discord.SelectOption(label="Terrible laptop"),
    discord.SelectOption(label="Free bobux"),
    discord.SelectOption(label="Top secret lelcube images"),
    discord.SelectOption(label="Internet Explorer 12"),
    discord.SelectOption(label="Clippy"),
    discord.SelectOption(label="Illegal DVD"),
    discord.SelectOption(label="eyePhone"),
    discord.SelectOption(label="iMark"),
    discord.SelectOption(label="Super snowman"),
    discord.SelectOption(label="Metal cake")
]

'''@client.command()
async def selectmenutest(ctx):
    yourmom = Select(
        custom_id="yourmom",
        placeholder="Selkctmrns icoete,",
        max_values=1,
        options=itemselect
    )

    amogus = ctx

    async def epokcallbackomg(interaction):
        if amogus.author.id == ctx.author.id:
            value = yourmom.values[0]
            await interaction.response.send_message(f"Your chose {value} omgndnxnnhcfgvjhfuiodksnrdtjhioçgln")
        else:
            await interaction.response.send_message("no u",ephemeral=True)
    
    yourmom.callback = epokcallbackomg
    view = View()
    view.add_item(yourmom)
    await ctx.send("rhjitpýlkrjtiekop",view=view)'''

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
        select = Select(
            custom_id="select",
            placeholder="Click here to choose the item you want",
            max_values=1,
            options=itemselect
        )

        amogus = inter

        async def epokcallbackomg(inter):
            if amogus.author.id == inter.author.id:
                oh_nice = False
                item = select.values[0]
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

                        await msg.edit(content="Boom",view=None)
                    else:
                        await msg.edit(content="Lol you can't buy this",view=None)
                else:
                    await inter.send("Lol wot")
            else:
                await inter.send("You're not the author :P",ephemeral=True)
    
        select.callback = epokcallbackomg
        view = View()
        view.add_item(select)
        msg = await inter.send("Choose an item.",view=view)

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
        await inter.send(embed=embed)
    except:
        await inter.send("It looks like you don't have items. (If you actually have then this is a bug)")

@client.command(aliases=['use'])
async def use2(inter, amount="1"):
    oh_nice = False

    try:
        amount = int(amount)
        oh_nice = True
    except:
        oh_nice = False
        await inter.reply("You are supposed to put a number as the amount (If you are trying to specify the item, you will do it after sending the command!)")


    if oh_nice == True:
        select = Select(
            custom_id="select",
            placeholder="Click here to choose the item you want",
            max_values=1,
            options=itemselect
        )

        amogus = inter

        async def epokcallbackomg(inter):
            nonlocal msg
            if amogus.author.id == inter.author.id:
                ono = False
                item = select.values[0]
                
                create_user_if_it_dont_exist(inter.author.id)

                with open(f"{str(inter.author.id)}_items.json",'r') as f:
                    items = json.load(f)
                
                if item not in items or items[item] < amount:
                    ono = True
                    await inter.send("Lol you don't have this item")
                
                if amount < 1:
                    ono = True
                    await msg.edit(content="Das illegal",view=None)
                
                if ono == False:
                    items[item] = items[item] - amount

                    with open(f"{str(inter.author.id)}_items.json", 'w') as f:
                        json.dump(items, f)
                    
                    await msg.edit(view=None)

                    if item == "Cooki":
                        await inter.send(":yum:")
                    elif item == "Linux":
                        await inter.send("Congratulations you was scammed :clap: <:lelcube:811058465383514132>")
                    elif item == "Lelcube plushie":
                        hug = Button(
                                style=ButtonStyle.green,
                                label="Hug it :)",
                                custom_id="hug"
                            )
                        play = Button(
                                style=ButtonStyle.green,
                                label="Play with it :)",
                                custom_id="play"
                        )
                        boom = Button(
                                style=ButtonStyle.red,
                                label="Explode it",
                                custom_id="boom"
                        )

                        interwithadifferentname = inter

                        async def on_hug(inter):
                            if interwithadifferentname.author.id == inter.author.id:
                                await msg.edit(content="You hugged the plushie! <:Hello_UwU:822546152402321428>")
                            else:
                                await inter.send(content="You're not the author :P",ephemeral=True)
                        
                        async def on_play(inter):
                            if interwithadifferentname.author.id == inter.author.id:
                                await msg.edit(content="You played with the plushie! <:Hello_OwO:822546151010074694>")
                            else:
                                await inter.send(content="You're not the author :P",ephemeral=True)
                        
                        async def on_boom(inter):
                            if interwithadifferentname.author.id == inter.author.id:
                                await msg.edit(content="You exploded the plushie, no buttons for you >:(", view=None)
                            else:
                                await inter.send(content="You're not the author :P",ephemeral=True)

                        hug.callback = on_hug
                        play.callback = on_play
                        boom.callback = on_boom
                        row = View()
                        row.add_item(hug)
                        row.add_item(play)
                        row.add_item(boom)
                        
                        await inter.send("What you want to do with the lelcube plushie?", view=row)
                        msg = await inter.original_message()

                    elif item == "Windows Vista":
                        await inter.send("Starting Windows...")
                        msg = await inter.original_message()
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
                        use = Button(
                            style=ButtonStyle.green,
                            label="Use its OS (Which is Windows 10)",
                            custom_id="use"
                        )
                        specs = Button(
                            style=ButtonStyle.green,
                            label="Show its specifications",
                            custom_id="specs"
                        )
                        boom = Button(
                            style=ButtonStyle.red,
                            label="Destroy it lol",
                            custom_id="boom"
                        )

                        interwithanothername = inter

                        async def on_use(inter):
                            if interwithanothername.author.id == inter.author.id:
                                await msg.edit(content="https://cdn.discordapp.com/attachments/778461818686406678/903431704197337178/unknown.png")
                            else:
                                await inter.send(content="You're not the author :P",ephemeral=True)
                        
                        async def on_specs(inter):
                            if interwithanothername.author.id == inter.author.id:
                                await msg.edit(content="RAM: 2GB RAM\nHDD: 32GB\nCPU: Intel Atom\nGPU: Nonexistent\nOthers: Its design was made in 3 minutes :thumbsup:")
                            else:
                                await inter.send(content="You're not the author :P",ephemeral=True)
                        
                        async def on_boom(inter):
                            if interwithanothername.author.id == inter.author.id:
                                await msg.edit(content="That's a good choice",view=None)
                            else:
                                await inter.send(content="You're not the author :P",ephemeral=True)
                        
                        use.callback = on_use
                        specs.callback = on_specs
                        boom.callback = on_boom

                        view = View()
                        view.add_item(use)
                        view.add_item(specs)
                        view.add_item(boom)
                        await inter.send("What you want to do with the ~~terrible~~ laptop?",view=view)
                        msg = await inter.original_message()

                    elif item == "Free bobux":
                        hax = Button(
                                style=ButtonStyle.green,
                                label="CONFIRM FREE BOBUX 🤑🤑🤑🤑🤑🤑🤑🤑🤑",
                                custom_id="hax"
                            )

                        definitelynotinter = inter
                        async def on_hax(inter):
                            if definitelynotinter.author.id == inter.author.id:
                                await msg.edit(content=f"Getting access to {inter.author.name}...",view=None)
                                await asyncio.sleep(5)
                                await msg.edit(content=f"Found email! ({inter.author.name}{str(random.randint(10000000,99999999))}@lelmail.com)")
                                await asyncio.sleep(2.5)
                                await msg.edit(content="Found emojis from their phone cuz why not <:lelcube:811058465383514132>")
                                await asyncio.sleep(3)
                                await msg.edit(content="Drinking coffee... :coffee:")
                                await asyncio.sleep(3.1)
                                await msg.edit(content="Exploding my own database lol <:lelcube:811058465383514132>")
                                await asyncio.sleep(4)
                                await msg.edit(content="Selling their data to a random person...")
                                await asyncio.sleep(3.5)
                                await msg.edit(content=f"<@822199023636709456> Hacked {inter.author.name} successfully!")
                            else:
                                await inter.send("You're not the author :P",ephemeral=True)
                        
                        hax.callback = on_hax
                        view = View()
                        view.add_item(hax)
                        await inter.send("CLICK IN \"CONFIRM FREE BOBUX\" TO CONFIRM FREE BOBUX :money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth::money_mouth:",view=view)
                        msg = await inter.original_message()

                    elif item == "Top secret lelcube images":
                        await inter.send(":soap: <:lelcube:811058465383514132>\nYou know what this means?????????? It means Lelcube has soap!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1111111111111111111!!1!!1!!!1!")
                    elif item == "Void":
                        await inter.send("** **")
                    elif item == "Internet Explorer 12":
                        await inter.send("Starting Internet Explorer...\n\nTip: Get a better browser")
                    elif item == "Clippy":
                        helpb = Button(
                                style=ButtonStyle.blurple,
                                label="Get help with writing the letter",
                                custom_id="help"
                            )
                        nohelp = Button(
                                style=ButtonStyle.blurple,
                                label="Write the letter without help",
                                custom_id="nohelp"
                            )

                        more = Button(
                                style=ButtonStyle.blurple,
                                label="More useful tips with Clippy!",
                                custom_id="more"
                            )
                        
                        urmom = inter

                        async def on_help(inter):
                            if urmom.author.id == inter.author.id:
                                await msg.edit(content="To write letters, it's very easy! You just press a letter, or any character, and boom!",view=view2)
                            else:
                                await inter.send(content="You're not the author :P",ephemeral=True)
                        
                        async def on_nohelp(inter):
                            if urmom.author.id == inter.author.id:
                                await msg.edit(content="unu",view=None)
                            else:
                                await inter.send(content="You're not the author :P",ephemeral=True)
                        
                        async def on_more(inter):
                            if urmom.author.id == inter.author.id:
                                await msg.edit(content="Failed to load more tips.",view=None)
                            else:
                                await inter.send(content="You're not the author :P",ephemeral=True)
                        
                        helpb.callback = on_help
                        nohelp.callback = on_nohelp
                        more.callback = on_more
                        view = View()
                        view2 = View()
                        view.add_item(helpb)
                        view.add_item(nohelp)
                        view2.add_item(more)
                        await inter.send("It looks like you're writing a letter.",view=view)
                        msg = await inter.original_message()

                    elif item == "Illegal DVD":
                        await inter.send(":police_car:")
                        msg = await inter.original_message()
                        await asyncio.sleep(5)
                        await msg.edit(content="The police is here, and you will be bammed!")
                        await asyncio.sleep(5)
                        await msg.edit(content=f"{inter.author.mention} has (not) been banned by <@822199023636709456> (Reason: Buying illegal DVDs)")
                    elif item == "Arnold cooki":
                        await inter.send(":yum::yum:")
                    elif item == "eyePhone":
                        await inter.send("Move your eye to use your eyePhone.")
                        await asyncio.sleep(1)
                        await inter.send("*phone explodes cuz the sensor thinks you want to explode the phone*")
                    elif item == "iMark":
                        await inter.send(":apple:")
                        lol_wot = await inter.original_message()
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
                        await lol_wot.edit(random.choice(ues))
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
                        await inter.send(random.choice(ads))
                    elif item == "Metal cake":
                        await inter.send("Hmm, metal tastes so good! I love it! Tasty! Delicious! Incredible!")
                        await asyncio.sleep(3)
                        await inter.send("*explodes*")
                    
                    elif item == "Lelcube":
                        items[item] = items[item] + amount*2

                        with open(f"{str(inter.author.id)}_items.json", 'w') as f:
                            json.dump(items, f)
                        
                        await inter.send("<:lelcube:811058465383514132>")
                        await inter.channel.send(f"Now you have {items[item]} lelcubes :D")
                    
                    elif item == "Free lelgolds":
                        values = {}
                        modaluwu = Modal(
                            title="Form where you put your info",
                            custom_id="epok_cook_modal",
                            components=[
                                TextInput(
                                    label="Email address",
                                    placeholder="Placeholder",
                                    custom_id="email_address",
                                    style=TextInputStyle.short,
                                    max_length=150,
                                ),
                                TextInput(
                                    label="Password lol",
                                    placeholder="Placeholder",
                                    custom_id="password_lol",
                                    style=TextInputStyle.short,
                                    max_length=150,
                                ),
                                TextInput(
                                    label="IP address",
                                    placeholder="Placeholder",
                                    custom_id="ip_address",
                                    style=TextInputStyle.short,
                                    max_length=32,
                                ),
                                TextInput(
                                    label="Why you want free lelgolds?",
                                    placeholder="Placeholder",
                                    custom_id="why",
                                    style=TextInputStyle.paragraph,
                                    max_length=512,
                                ),
                                TextInput(
                                    label="Did you like this form?",
                                    placeholder="Placeholder",
                                    custom_id="yesorno",
                                    style=TextInputStyle.short,
                                    max_length=32,
                                )
                            ]
                        )

                        await inter.response.send_modal(modaluwu)

                        # Wait until the user submits the modal
                        try:
                            modal_inter: discord.ModalInteraction = await client.wait_for(
                                "modal_submit",
                                check=lambda i: i.custom_id == "epok_cook_modal" and i.author.id == inter.author.id,
                                timeout=1024,
                            )
                        except asyncio.TimeoutError:
                            # lol took too much
                            return
                        
                        '''for custom_id, value in modal_inter.text_values.items():
                            values[custom_id] = value'''

                        await modal_inter.response.send_message("Getting access to lelbot's servers...")
                        msg = await modal_inter.original_message()
                        await asyncio.sleep(3)
                        await msg.edit(content="Bypassing firewall...")
                        await asyncio.sleep(3)
                        await msg.edit(content="Connecting to SQL database...")
                        await asyncio.sleep(3)
                        await msg.edit(content=f"Searching for database key \"{str(modal_inter.author.id)}_MONE\"")
                        await asyncio.sleep(3)
                        await msg.edit(content="Connecting to SQL database again...")
                        await asyncio.sleep(3)
                        await msg.edit(content=f"Modifying {random.randint(2,30000)} database keys...")
                        await asyncio.sleep(3)
                        await msg.edit(content=f"Stealing your discord account lol...")
                        await asyncio.sleep(3)
                        await msg.edit(content=f"I gave {random.randint(1,9999999999999)} lelgolds to your account BUT now your account is mine >:DDDDDDDD\nNow I finally can buy 942482 metal cakes :D")
                    
                    elif item == "Macrohard Doors 11":
                        await inter.send(":door:\n\n:o:")
                        msg = await inter.original_message()
                        await asyncio.sleep(60)
                        await msg.edit(content="Please wait... :o: (this will take 25 minutes)")
                        await asyncio.sleep(720)
                        await msg.edit(content="**11:11**\nhttps://cdn.discordapp.com/attachments/811060176265805825/962452691685101598/best-banner-ever-lol.png")
                        await asyncio.sleep(10)
                        await msg.edit(content=f"Logging to {inter.author.name}'s account...")
                        await asyncio.sleep(720)
                        await msg.edit(content="```ues\n:(\ntrololol doors 11 crashed trololol you have to restart :wink:```")
                    
                    elif item == "Pancakes":
                        await inter.send(":pancakes: <:lelcube:811058465383514132>")
                        await inter.channel.send("He eats pancakes")
                    
                    elif item == "The best movie out there":
                        await inter.send("<:lelcube:811058465383514132>")
                        scn = await inter.original_message()
                        msg = await inter.channel.send("LELCUBE MOVIE PRODUCTIONS")
                        await asyncio.sleep(6)
                        await scn.edit(content=":deaf_person:")
                        await msg.edit(content="FROM THE CREATORS OF /ADVENTURE AND THE BEST MOVIE OUT THERE")
                        await asyncio.sleep(6)
                        await msg.edit(content="INTRODUCING...")
                        await asyncio.sleep(6)
                        await msg.edit(content="THE BEST MOVIE OUT THERE")
                        await asyncio.sleep(6)
                        await scn.edit(content="<:lelcube:811058465383514132> :cookie:")
                        await msg.edit(content="**Lelcube**\nI like cookis")
                        await asyncio.sleep(6)
                        await scn.edit(content="<:lelcube:811058465383514132>")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\nono where is ma cooki")
                        await asyncio.sleep(3)
                        await scn.edit(content="<:lelcube:811058465383514132> <:void:834904392008335360> <:hellory5n:915028960604200982>")
                        await msg.edit(content="**hellory5n**\ni stealed it lol")
                        await asyncio.sleep(5)
                        await scn.edit(content="<:lelcube:811058465383514132> <:nuG:915809814947463168> <:hellory5n:915028960604200982>")
                        await msg.edit(content="** **")
                        await asyncio.sleep(5)
                        await msg.edit(content="A MOVIE BY LELCUBE MOVIE PRODUCTIONS")
                        await asyncio.sleep(10)
                        await msg.edit(content="WHY\nWHY I MADE THIS MOVIE")

            else:
                await inter.send("You're not the author :P",ephemeral=True)
    
        select.callback = epokcallbackomg
        view = View()
        view.add_item(select)
        msg = await inter.send("Choose an item.",view=view)

@client.command(aliases=['give-money','give_money'])
async def give_money2(inter, user:discord.User, amount:int):
    problems_ono = False

    create_user_if_it_dont_exist(inter.author.id)

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
        create_user_if_it_dont_exist(user.id)

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
    filename = str(inter.author.id) + ".json"

    create_user_if_it_dont_exist(inter.author.id)

    yes = Button(
            style=ButtonStyle.red,
            label="Yes, reset my money!",
            custom_id="yes_button"
        )
    no = Button(
            style=ButtonStyle.blurple,
            label="Nevermind.",
            custom_id="no_button"
        )
    
    pain = inter

    async def on_yes(inter):
        if pain.author.id == inter.author.id:
            with open(filename, 'r') as f:
                ok = json.load(f)

            ok['cash'] = 0
            ok['bank'] = 0

            with open(filename, 'w') as f:
                json.dump(ok, f)

            await msg.edit(content="Successfully reseted.", view=None)
        else:
            await inter.send(content="You're not the author :P",ephemeral=True)
    
    async def on_no(inter):
        if pain.author.id == inter.author.id:
            await msg.edit(content="Ok",view=None)
        else:
            await inter.send(content="You're not the author :P",ephemeral=True)

    yes.callback = on_yes
    no.callback = on_no
    view = View()
    view.add_item(yes)
    view.add_item(no)

    msg = await inter.send("Are you sure you want to reset your money??", view=view)

@client.command(aliases=['give_item','give-item'])
async def give_item2(inter, user:discord.Member, amount="1"):
    oh_nice = False

    create_user_if_it_dont_exist(inter.author.id)

    try:
        amount = int(amount)
        oh_nice = True
    except:
        oh_nice = False
        await inter.reply("You are supposed to put a number as the amount (If you are trying to specify the item, you will do it after sending the command!)")

    if oh_nice == True:
        select = Select(
            custom_id="select",
            placeholder="Click here to choose the item you want",
            max_values=1,
            options=itemselect
        )

        amogus = inter

        async def epokcallbackomg(inter):
            if amogus.author.id == inter.author.id:
                item = select.values[0]
                problems_ono = False
    
                input = f"{str(inter.author.id)}_items.json"
                output = f"{str(user.id)}_items.json"

                with open(input, 'r') as f_i:
                    ok_i = json.load(f_i)
                
                if amount < 1 or not ok_i[item] > amount - 1:
                    problems_ono = True
                    await msg.edit(content="You can't lol",view=None)

                if user == inter.author:
                    problems_ono = True
                    await msg.edit(content="You can't give items to yourself xd",view=None)

                if problems_ono == False:
                    create_user_if_it_dont_exist(user.id)

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
                    
                    await msg.edit(content="Boom",view=None)
                
            else:
                await inter.send("You're not the author :P",ephemeral=True)
    
        select.callback = epokcallbackomg
        view = View()
        view.add_item(select)
        msg = await inter.send("Choose an item.",view=view)

@client.command(aliases=['rob','steal','rob-money','rob_money','steal-money','steal_money'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def rob2(inter, user:discord.User, amount):
    problems_ono = False

    create_user_if_it_dont_exist(inter.author.id)

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
          create_user_if_it_dont_exist(user.id)
          
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

@client.slash_command(description="For the people that don't like the new help command")
async def classic_help(inter):
    embed=discord.Embed(title="Help", description="`<>` = required, `[]` = optional.", color=0xFECC4D)
    embed.add_field(name="Commands", value="`l!hello`, `l!ping`, `l!8ball <question>`, `l!boom <user>`, `l!invite`, `l!chat <text>`, `l!fact [index]`, `l!randomstory`, `l!aboutme`, `l!when <question>`, `l!helloyesorno <question>`, `l!say <text>`, `l!hug <user>`, `l!attack <user>`, `l!bam <user>`, `l!roll`, `l!hack <user>`, `l!server`, `l!randomsandwich`, `l!poll <text>`, `l!suggest <text>`, `l!weirdtext`, `l!dostuff`, `l!embed <title> | <description>`, `l!math <number> <operation> <number>`, `l!sweatsmile`, `l!randnum <min> <max>`, `l!bobux`, `l!morecookis`, `l!work`, `l!bal [user]`, `l!dep <value>`, `l!with <value>`, `l!lb`, `l!shop`, `l!buy [amount]`, `l!inv [user]`, `l!use [amount]`, `l!give_money <user> <amount>`, `l!reset_money`, `l!give_item <user> [amount]`, `l!rob <user> <amount>`, `l!text_to_wotcode <user>`, `l!wotcode_to_text <user>`, `l!name`, `l!sandwich <size>`, `l!collect`, `l!throw <target>`, `l!snow-lb`, `l!where <something>`, `l!buildpc`, `l!adventure`, `l!cake <someone>`, `l!hat`, `l!reset_items`, `l!sell <user> <price> [amount]`", inline=False)
    embed.set_footer(text="lel")
    await inter.send(embed=embed)

@client.command(aliases=['classic_help'])
async def classic_help2(inter):
    embed=discord.Embed(title="Help", description="`<>` = required, `[]` = optional.", color=0xFECC4D)
    embed.add_field(name="Commands", value="`l!hello`, `l!ping`, `l!8ball <question>`, `l!boom <user>`, `l!invite`, `l!chat <text>`, `l!fact [index]`, `l!randomstory`, `l!aboutme`, `l!when <question>`, `l!helloyesorno <question>`, `l!say <text>`, `l!hug <user>`, `l!attack <user>`, `l!bam <user>`, `l!roll`, `l!hack <user>`, `l!server`, `l!randomsandwich`, `l!poll <text>`, `l!suggest <text>`, `l!weirdtext`, `l!dostuff`, `l!embed <title> | <description>`, `l!math <number> <operation> <number>`, `l!sweatsmile`, `l!randnum <min> <max>`, `l!bobux`, `l!morecookis`, `l!work`, `l!bal [user]`, `l!dep <value>`, `l!with <value>`, `l!lb`, `l!shop`, `l!buy [amount]`, `l!inv [user]`, `l!use [amount]`, `l!give_money <user> <amount>`, `l!reset_money`, `l!give_item <user> [amount]`, `l!rob <user> <amount>`, `l!text_to_wotcode <user>`, `l!wotcode_to_text <user>`, `l!name`, `l!sandwich <size>`, `l!collect`, `l!throw <target>`, `l!snow-lb`, `l!where <something>`, `l!buildpc`, `l!adventure`, `l!cake <someone>`, `l!hat`, `l!reset_items`, `l!sell <user> <price> [amount]`", inline=False)
    embed.set_footer(text="lel")
    await inter.send(embed=embed)

@client.slash_command(description="Children of tommorow will have no understanding of the english language")
async def wotcode(inter):
    pass

@wotcode.sub_command(description="Convert your text to wotcode")
async def text_to_wotcode(inter,text:str):
    """
    Parameters
    ----------
    text: The text that will be converted
    """
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
    await inter.send(f"`{text}`\n\n- {inter.author.mention}")

@wotcode.sub_command(description="Convert wotcode to text")
async def wotcode_to_text(inter,text:str):
    """
    Parameters
    ----------
    text: The text that will be converted
    """
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
    await inter.send(f"`{text}`\n\n- {inter.author.mention}")

@client.slash_command(description="Give random name to a random thing")
async def name(inter):
    thing = [':cat:',":dog:",":chair:",":package:",":bed:",":wastebasket:",":coffee:",":printer:",":couch:","👩","🧑","👧","👩‍🦰","👶","👴","👨‍🦳","👨‍🦲","👱‍♂️","🙎","🧏","🤦","🤷","💇","🏃","🤸","🐵","🐺","🐯","🦒","🦊","🦝","🐮","🐷","🐹","🐰","🐻","🐼","🐸","🦓","🐴","🐔","🐳","🐟","🐘"]
    name = ["Michael","Steve","Bob","Henry","Carl","Mark","Tom","John","Alan","James","Jack","Thomas","Martin","Susan","Paul","Mike","Michalan","Alanalex","Alex"]
    await inter.send(f"{random.choice(thing)}\n:point_up: {random.choice(name)}")

@client.command(aliases=['name'])
async def name2(inter):
    thing = [':cat:',":dog:",":chair:",":package:",":bed:",":wastebasket:",":coffee:",":printer:",":couch:","👩","🧑","👧","👩‍🦰","👶","👴","👨‍🦳","👨‍🦲","👱‍♂️","🙎","🧏","🤦","🤷","💇","🏃","🤸","🐵","🐺","🐯","🦒","🦊","🦝","🐮","🐷","🐹","🐰","🐻","🐼","🐸","🦓","🐴","🐔","🐳","🐟","🐘"]
    name = ["Michael","Steve","Bob","Henry","Carl","Mark","Tom","John","Alan","James","Jack","Thomas","Martin","Susan","Paul","Mike","Michalan","Alex"]
    await inter.send(f"{random.choice(thing)}\n:point_up: {random.choice(name)}")

@client.slash_command(description="Build a sandwich")
async def sandwich(inter,size:int):
    """
    Parameters
    ----------
    size: The size of your sandwich
    """
    stuff = [":tomato:",":leafy_green:",":cucumber:",":hot_pepper:",":corn:",":carrot:",":onion:",":potato:",":cheese:",":egg:",":butter:",":bacon:",":cut_of_meat:",":poultry_leg:",":meat_on_bone:"]
    counter = 0
    sandwich = ""
    if size < 26:
        while counter < size:
            sandwich = sandwich + "\n" + random.choice(stuff)
            counter += 1
        await inter.send(f":bread:{sandwich}\n:bread:")
    else:
        await inter.send("How you're gonna eat that <:lelcube:811058465383514132>")

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

Dumbness = commands.option_enum(
    {"Smart": 1,
    "n ot so smaort": 2,
    "fjhsdkmnfbekjnsdnfjls": 3
    }
)

@client.slash_command(description="Make a sentence, will it be nonsense? (yes)")
async def sentence(inter,dumbness: Dumbness):
    """
    Parameters
    ----------
    dumbness: How smort lelbot will be when making the sentence
    """
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
    
        await inter.send(when_the)
    if dumbness == 2:
        when_the = random.choice(amount) + " " + random.choice(adj) + " " + random.choice(nouns) + " " + random.choice(verbs) + " " + random.choice(nouns)
        await inter.send(when_the)
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
        
        message = amount + " " + a + " " + noun + " " + random.choice(verbs) + " " + random.choice(plural_nouns)
        message = message.capitalize()
        await inter.send(message)

@client.command(aliases=["sentence"])
async def sentence2(inter):
    lelbotissosmort = Select(
        custom_id="lelbotissosmort",
        placeholder="ues",
        max_values=1,
        options=[
            discord.SelectOption(label="Smart"),
            discord.SelectOption(label="n ot so smaort"),
            discord.SelectOption(label="fjhsdkmnfbekjnsdnfjls")
        ]
    )

    amogus = inter

    async def epokcallbackomg(inter):
        nonlocal msg
        if amogus.author.id == inter.author.id:
            dumbness = lelbotissosmort.values[0]
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
            
                await msg.edit(content=when_the,view=None)
            if dumbness == "n ot so smaort":
                when_the = random.choice(amount) + " " + random.choice(adj) + " " + random.choice(nouns) + " " + random.choice(verbs) + " " + random.choice(nouns)
                await msg.edit(content=when_the,view=None)
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
                
                message = amount + " " + a + " " + noun + " " + random.choice(verbs) + " " + random.choice(plural_nouns)
                message = message.capitalize()
                await msg.edit(content=message,view=None)
            
        else:
            await inter.send("You're not the author :P",ephemeral=True)
    
    lelbotissosmort.callback = epokcallbackomg
    view = View()
    view.add_item(lelbotissosmort)
    msg = await inter.send("How smort lelbot will be when making the sentence?",view=view)

@client.slash_command(description="Who is [insert someone here]?")
async def who(inter,someone:str):
    """
    Parameters
    ----------
    someone: The
    """
    thing = ['popilol', 'lelcube', 'cube', 'cat', '`furry`', 'dog', 'human', 'banana', 'couch', 'printer', 'monke', 'muffin', 'bot', 'computer', 'snek', 'bread', 'tree', 'box', 'flower', 'planet']
    adj = ['rich', 'poor', 'nonsense', 'lel', 'digital', 'blue', 'red', 'yellow', 'green', 'orange', 'purple', 'pink', 'black', 'white', 'gray', 'boring', 'completely normal', 'fantastic', 'awesome', 'big', 'huge', 'small', 'tiny', 'giant', 'toxic', 'weird', 'heavy', 'simple', 'tall', 'ugly', 'butiful', 'thin', 'invisible']
    place = ['candy land', 'the lelverse', '__**brazil**__', 'another universe', 'a hard drive', 'your imagination', "hellory5n's bot lab with a lot of trash", 'bobux secret laboratory', 'mars', 'the moon', '***a place***', '(x=nan, y=nan, z=nan)', "the place where there's an infinity thing generator", "Windows XP's wallpaper", 'blue void']

    the = "A " + random.choice(adj) + " " + random.choice(thing) + " in " + random.choice(place)
    embed = discord.Embed(title=f"Who {someone}?",description=the,color=0xFECC4D)
    embed.set_footer(text=f"{inter.author} ({str(inter.author.id)})")
    await inter.send(embed=embed)

@client.command(aliases=['who'])
async def who2(inter,*,someone):
    thing = ['popilol', 'lelcube', 'cube', 'cat', '`furry`', 'dog', 'human', 'banana', 'couch', 'printer', 'monke', 'muffin', 'bot', 'computer', 'snek', 'bread', 'tree', 'box', 'flower', 'planet']
    adj = ['A rich', 'A poor', 'A nonsense', 'A lel', 'A digital', 'A blue', 'A red', 'A yellow', 'A green', 'A orange', 'A purple', 'A pink', 'A black', 'A white', 'A gray', 'A boring', 'A completely normal', 'A fantastic', 'An awesome', 'A big', 'A huge', 'A small', 'A tiny', 'A giant', 'A toxic', 'A weird', 'A heavy', 'A simple', 'A tall', 'An ugly', 'A butiful', 'A thin', 'An invisible']
    place = ['candy land', 'the lelverse', '__**brazil**__', 'another universe', 'a hard drive', 'your imagination', "hellory5n's bot lab with a lot of trash", 'bobux secret laboratory', 'mars', 'the moon', '***a place***', '(x=nan, y=nan, z=nan)', "the place where there's an infinity thing generator", "Windows XP's wallpaper", 'blue void']

    the = random.choice(adj) + " " + random.choice(thing) + " in " + random.choice(place)
    embed = discord.Embed(title=f"Who {someone}?",description=the,color=0xFECC4D)
    embed.set_footer(text=f"{inter.author} ({str(inter.author.id)})")
    await inter.reply(embed=embed)

@client.slash_command(description="ues")
async def snowball(inter):
    pass

@snowball.sub_command(description="Collect snowballs")
@commands.cooldown(1, 10, commands.BucketType.user)
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
            await inter.send("You have too many snowballs!")
            ono = True
    except:
        balls[str(inter.author.id)] = 1
    
    with open("snowball_thing.json",'w') as f:
        json.dump(balls,f)

    if ono == False:

        if balls[str(inter.author.id)] == 1:
            await inter.send(":white_circle: <:lelcube:811058465383514132>")
            await inter.channel.send("You got a snowball!")
        elif balls[str(inter.author.id)] == 2:
            await inter.send(":white_circle: <:lelcube:811058465383514132> :white_circle:")
            await inter.channel.send("You got another snowball!")
        elif balls[str(inter.author.id)] == 3:
            await inter.send("<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n:white_circle: <:lelcube:811058465383514132> :white_circle:")
            await inter.channel.send("You got another another snowball!")
        elif balls[str(inter.author.id)] == 4:
            await inter.send("<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n:white_circle: <:lelcube:811058465383514132> :white_circle:")
            await inter.channel.send("Ok you are getting too many snowballs")
        elif balls[str(inter.author.id)] == 5:
            await inter.send("<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n<:void:834904392008335360> <:void:834904392008335360> :white_circle:\n:white_circle: <:lelcube:811058465383514132> :white_circle:")
            await inter.channel.send("Das a lot of snowballs")

@snowball.sub_command(description="Throw snowballs")
async def throw(inter,target: str):
    """
    Parameters
    ----------
    target: ues
    """
    with open("snowball_thing.json",'r') as f:
        balls = json.load(f)
    
    ono = False

    try:
        if not balls[str(inter.author.id)] < 1:
            balls[str(inter.author.id)] = balls[str(inter.author.id)] - 1
        else:
            await inter.send("<:lelcube:811058465383514132> :thumbsup:")
            await inter.channel.send("You don't have snowballs")
            ono = True
    except:
        await inter.send("<:lelcube:811058465383514132> :thumbsup:")
        await inter.channel.send("You don't have snowballs")
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

            await inter.send(":deaf_person: :arrow_left: :white_circle: <:lelcube:811058465383514132>")
            await inter.channel.send(f"{inter.author.mention} attacked {target}!")
        else:
            await inter.send("<:void:834904392008335360> :arrow_upper_left:\n:deaf_person: <:void:834904392008335360> :white_circle: <:lelcube:811058465383514132>")
            await inter.channel.send(f"{inter.author.mention} missed lol")

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
            await inter.send("You don't have snowballs")
            ono = True
    except:
        await inter.reply("<:lelcube:811058465383514132> :thumbsup:")
        await inter.send("You don't have snowballs")
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

    prevb = Button(
            style=ButtonStyle.blurple,
            label="Previous page",
            custom_id="prev_button",
            disabled=not can_go_back
        )
    nextb = Button(
            style=ButtonStyle.blurple,
            label="Next page",
            custom_id="next_button",
            disabled=not can_go_forward
        )

    interwithadifferentname = inter

    async def on_next(inter):
        if interwithadifferentname.author.id == inter.author.id:
            nonlocal page
            nonlocal prevb
            nonlocal nextb
            can_go_back = True
            can_go_forward = True
            page += 1

            prevb.disabled = not can_go_back
            nextb.disabled = not can_go_forward
            newrow = View()
            newrow.add_item(prevb)
            newrow.add_item(nextb)

            lb_uwu = ""

            for key,value in users_chunks[page].items():
                lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

            embed=discord.Embed(title=f"Snow leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
            embed.set_footer(text=str(inter.author.id))

            await msg.edit(embed=embed, view=newrow)
        else:
            await inter.send("You aren't the author :P",ephemeral=True)

    async def on_previous(inter):
        if interwithadifferentname.author.id == inter.author.id:
            nonlocal page
            nonlocal prevb
            nonlocal nextb
            can_go_back = True
            can_go_forward = True
            page -= 1

            prevb.disabled = not can_go_back
            nextb.disabled = not can_go_forward
            newrow = View()
            newrow.add_item(prevb)
            newrow.add_item(nextb)

            lb_uwu = ""

            for key,value in users_chunks[page].items():
                lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

            embed=discord.Embed(title=f"Snow leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
            embed.set_footer(text=str(inter.author.id))

            await msg.edit(embed=embed, view=newrow)
        else:
            await interwithadifferentname.send("You aren't the author :P",ephemeral=True)

    prevb.callback = on_previous
    nextb.callback = on_next
    row = View()
    row.add_item(prevb)
    row.add_item(nextb)
    await inter.send(embed=embed, view=row)
    msg = await inter.original_message()

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

    prevb = Button(
            style=ButtonStyle.blurple,
            label="Previous page",
            custom_id="prev_button",
            disabled=not can_go_back
        )
    nextb = Button(
            style=ButtonStyle.blurple,
            label="Next page",
            custom_id="next_button",
            disabled=not can_go_forward
        )

    interwithadifferentname = inter

    async def on_next(inter):
        if interwithadifferentname.author.id == inter.author.id:
            nonlocal page
            nonlocal prevb
            nonlocal nextb
            can_go_back = True
            can_go_forward = True
            page += 1

            prevb.disabled = not can_go_back
            nextb.disabled = not can_go_forward
            newrow = View()
            newrow.add_item(prevb)
            newrow.add_item(nextb)

            lb_uwu = ""

            for key,value in users_chunks[page].items():
                lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

            embed=discord.Embed(title=f"Snow leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
            embed.set_footer(text=str(inter.author.id))

            await msg.edit(embed=embed, view=newrow)
        else:
            await inter.send("You aren't the author :P",ephemeral=True)

    async def on_previous(inter):
        if interwithadifferentname.author.id == inter.author.id:
            nonlocal page
            nonlocal prevb
            nonlocal nextb
            can_go_back = True
            can_go_forward = True
            page -= 1

            prevb.disabled = not can_go_back
            nextb.disabled = not can_go_forward
            newrow = View()
            newrow.add_item(prevb)
            newrow.add_item(nextb)

            lb_uwu = ""

            for key,value in users_chunks[page].items():
                lb_uwu = lb_uwu + "<@" + str(key) + ">: " + str(value) + "\n"

            embed=discord.Embed(title=f"Snow leaderboard (Page {page+1}/{len(users_chunks)})",description=lb_uwu,color=0xFECC4D)
            embed.set_footer(text=str(inter.author.id))

            await msg.edit(embed=embed, view=newrow)
        else:
            await interwithadifferentname.send("You aren't the author :P",ephemeral=True)

    prevb.callback = on_previous
    nextb.callback = on_next
    row = View()
    row.add_item(prevb)
    row.add_item(nextb)
    msg = await inter.send(embed=embed, view=row)

@client.slash_command(description="Where is [insert something here]")
async def where(inter,something:str):
    """
    Parameters
    ----------
    something: the
    """
    place = ['candy land', 'the lelverse', '__**brazil**__', 'another universe', 'a hard drive', 'your imagination', "hellory5n's bot lab with a lot of trash", 'bobux secret laboratory', 'mars', 'the moon', '***a place***', '(x=nan, y=nan, z=nan)', "the place where there's an infinity thing generator", "Windows XP's wallpaper", 'blue void','ues dimension','weirdimension','lelbot\'s basement']
    embed = discord.Embed(title=f"Where {something}?",description=f"In {random.choice(place)}",color=0xFECC4D)
    embed.set_footer(text=f"{inter.author} ({inter.author.id})")
    await inter.send(embed=embed)

@client.command(aliases=['where'])
async def where2(inter,*,something):
    place = ['candy land', 'the lelverse', '__**brazil**__', 'another universe', 'a hard drive', 'your imagination', "hellory5n's bot lab with a lot of trash", 'bobux secret laboratory', 'mars', 'the moon', '***a place***', '(x=nan, y=nan, z=nan)', "the place where there's an infinity thing generator", "Windows XP's wallpaper", 'blue void','ues dimension','weirdimension','lelbot\'s basement']
    embed = discord.Embed(title=f"Where {something}?",description=f"In {random.choice(place)}",color=0xFECC4D)
    embed.set_footer(text=f"{inter.author} ({inter.author.id})")
    await inter.reply(embed=embed)

@client.slash_command(description="Build a PC that probably wouldn't work irl")
async def buildpc(inter):
    oses = ['Windows','macOS','Linux']
    OS = random.choice(oses)
    if OS == 'Windows':
        os_version = ['1.0','2.0','3.0','3.1','NT 3.1','95','NT 4.0','98','98 SE','2000','Me','XP','Vista','7','8','8.1','10','11']
        OSVER = random.choice(os_version)
    if OS == 'macOS':
        os_version = ['1.0','2.0','3.0','4.0','5.0','6.0','7','8','9','10.0 Cheetah','10.1 Puma','10.2 Jaguar','10.3 Panther','10.4 Tiger','10.5 Leopard','10.6 Snow Leopard','10.7 Lion','10.8 Mountain Lion','10.9 Mavericks','10.10 Yosemite','10.11 El Capitan','10.12 Sierra','10.13 High Sierra','10.14 Mojave','10.15 Catalina','11 Big Sur','12 Monterey']
        OSVER = random.choice(os_version)
    if OS == 'Linux':
        os_distros = ['Mint','Ubuntu','Pop_OS!','elementary OS','Fedora','Zorin','Deepin','Solus','Manjaro','Debian','MX','OpenSUSE','CentOS']
        OSVER = random.choice(os_distros)
    ram = random.randint(1,1024)
    ram2 = ['KB','MB','GB']
    if random.choice(['DDR','SDR']) == 'DDR':
        ramtype = 'DDR' + str(random.randint(1,5))
    else:
        ramtype = 'SDR'
    RAM = str(ram) + random.choice(ram2) + " " + ramtype
    HDD = random.choice(['','None'])
    if HDD == '':
        hdd = random.randint(1,1024)
        hdd2 = ['KB','MB','GB','TB']
        HDD = str(hdd) + random.choice(hdd2)
    SSD = random.choice(['','None'])
    if SSD == '':
        ssd = random.randint(1,1024)
        ssd2 = ['KB','MB','GB','TB']
        SSD = str(ssd) + random.choice(ssd2)
    cpu1 = ['Intel','AMD','PowerPC','Apple']
    CPU1 = random.choice(cpu1)
    if CPU1 == 'Intel':
        cpu2 = ['Pentium I','Pentium II','Pentium III','Pentium IV','Celeron','Atom','Core Duo','Core i3','Core i5','Core i7','Core i9']
        CPU2 = random.choice(cpu2)
    elif CPU1 == 'AMD':
        cpu2 = ['Ryzen 1000','Ryzen 2000','Ryzen 3000','Ryzen 4000','Ryzen 5000']
        CPU2 = random.choice(cpu2)
    elif CPU1 == 'PowerPC':
        cpu2 = ['600','700','7400','970','G1','G2','G3','G4','G5','G6']
        CPU2 = random.choice(cpu2)
    elif CPU1 == 'Apple':
        CPU2 = 'M1'
    cpu3 = random.randint(1,1000)
    cpu4 = ['KHz','MHz','GHz']
    CPU = CPU1 + " " + CPU2 + " " + str(cpu3) + " " + random.choice(cpu4)
    gpu1 = ['NVIDIA GeForce','AMD Radeon']
    GPU1 = random.choice(gpu1)
    if GPU1 == 'NVIDIA GeForce':
        GPU2 = ['256','2 MX200','3 Ti200','4 MX420','FX 5100','6200A','7900 GTX','8800 GTX','9800 GTX','GTS 150','GTX 260','GT 340','GTX 460','GTX 555','GTX 645','GTX 745','GTX 950','GTX 1050','TITAN V','GTX 1650','RTX 2060','RTX 3050']
    elif GPU1 == 'AMD Radeon':
        GPU2 = ['7000','320','8500','9000','9500','X300','Xpress 200','X700','X550 XT','Xpress X1200','X1300','HD 2350','HD 3410','3000 Graphics','HD 4350','HD 4200 Graphics','HD 5450','HD 6350','HD 6370D','HD 7350','HD 7310','HD 3750','R5 220','R5 330','R5 430','520','RX Vega 56','VII','RX 5300','RX 6400']
    gpu2043 = random.randint(1,1000)
    gpu2943 = ['KB','MB','GB']
    GPU = GPU1 + " " + random.choice(GPU2) + " " + str(gpu2043) + random.choice(gpu2943)
    screenres = str(random.randint(1,5000)) + "x" + str(random.randint(1,5000))
    screensiz = str(random.randint(1,20)) + " inches"
    screentype = random.choice(['CRT','OLED','DLPT','LCD','plasma display','LED'])
    screencolors = str(random.randint(1,16000000))
    SCREEN = screenres + " " + screensiz + " " + screentype + " screen with " + screencolors + " colors"

    embed = discord.Embed(title=f"Very cook PC",description=f"OS: {OS} {OSVER}\nRAM: {RAM}\nHDD: {HDD}\nSSD: {SSD}\nCPU: {CPU}\nGPU: {GPU}\nScreen: {SCREEN}",color=0xFECC4D)
    embed.set_footer(text=f"{inter.author} ({inter.author.id})")
    await inter.send(embed=embed)

@client.command(aliases=['buildpc','build_pc','build-pc'])
async def buildpc2(inter):
    oses = ['Windows','macOS','Linux']
    OS = random.choice(oses)
    if OS == 'Windows':
        os_version = ['1.0','2.0','3.0','3.1','NT 3.1','95','NT 4.0','98','98 SE','2000','Me','XP','Vista','7','8','8.1','10','11']
        OSVER = random.choice(os_version)
    if OS == 'macOS':
        os_version = ['1.0','2.0','3.0','4.0','5.0','6.0','7','8','9','10.0 Cheetah','10.1 Puma','10.2 Jaguar','10.3 Panther','10.4 Tiger','10.5 Leopard','10.6 Snow Leopard','10.7 Lion','10.8 Mountain Lion','10.9 Mavericks','10.10 Yosemite','10.11 El Capitan','10.12 Sierra','10.13 High Sierra','10.14 Mojave','10.15 Catalina','11 Big Sur','12 Monterey']
        OSVER = random.choice(os_version)
    if OS == 'Linux':
        os_distros = ['Mint','Ubuntu','Pop_OS!','elementary OS','Fedora','Zorin','Deepin','Solus','Manjaro','Debian','MX','OpenSUSE','CentOS']
        OSVER = random.choice(os_distros)
    ram = random.randint(1,1024)
    ram2 = ['KB','MB','GB']
    if random.choice(['DDR','SDR']) == 'DDR':
        ramtype = 'DDR' + str(random.randint(1,5))
    else:
        ramtype = 'SDR'
    RAM = str(ram) + random.choice(ram2) + " " + ramtype
    HDD = random.choice(['','None'])
    if HDD == '':
        hdd = random.randint(1,1024)
        hdd2 = ['KB','MB','GB','TB']
        HDD = str(hdd) + random.choice(hdd2)
    SSD = random.choice(['','None'])
    if SSD == '':
        ssd = random.randint(1,1024)
        ssd2 = ['KB','MB','GB','TB']
        SSD = str(ssd) + random.choice(ssd2)
    cpu1 = ['Intel','AMD','PowerPC','Apple']
    CPU1 = random.choice(cpu1)
    if CPU1 == 'Intel':
        cpu2 = ['Pentium I','Pentium II','Pentium III','Pentium IV','Celeron','Atom','Core Duo','Core i3','Core i5','Core i7','Core i9']
        CPU2 = random.choice(cpu2)
    elif CPU1 == 'AMD':
        cpu2 = ['Ryzen 1000','Ryzen 2000','Ryzen 3000','Ryzen 4000','Ryzen 5000']
        CPU2 = random.choice(cpu2)
    elif CPU1 == 'PowerPC':
        cpu2 = ['600','700','7400','970','G1','G2','G3','G4','G5','G6']
        CPU2 = random.choice(cpu2)
    elif CPU1 == 'Apple':
        CPU2 = 'M1'
    cpu3 = random.randint(1,1000)
    cpu4 = ['KHz','MHz','GHz']
    CPU = CPU1 + " " + CPU2 + " " + str(cpu3) + " " + random.choice(cpu4)
    gpu1 = ['NVIDIA GeForce','AMD Radeon']
    GPU1 = random.choice(gpu1)
    if GPU1 == 'NVIDIA GeForce':
        GPU2 = ['256','2 MX200','3 Ti200','4 MX420','FX 5100','6200A','7900 GTX','8800 GTX','9800 GTX','GTS 150','GTX 260','GT 340','GTX 460','GTX 555','GTX 645','GTX 745','GTX 950','GTX 1050','TITAN V','GTX 1650','RTX 2060','RTX 3050']
    elif GPU1 == 'AMD Radeon':
        GPU2 = ['7000','320','8500','9000','9500','X300','Xpress 200','X700','X550 XT','Xpress X1200','X1300','HD 2350','HD 3410','3000 Graphics','HD 4350','HD 4200 Graphics','HD 5450','HD 6350','HD 6370D','HD 7350','HD 7310','HD 3750','R5 220','R5 330','R5 430','520','RX Vega 56','VII','RX 5300','RX 6400']
    gpu2043 = random.randint(1,1000)
    gpu2943 = ['KB','MB','GB']
    GPU = GPU1 + " " + random.choice(GPU2) + " " + str(gpu2043) + random.choice(gpu2943)
    screenres = str(random.randint(1,5000)) + "x" + str(random.randint(1,5000))
    screensiz = str(random.randint(1,20)) + " inches"
    screentype = random.choice(['CRT','OLED','DLPT','LCD','plasma display','LED'])
    screencolors = str(random.randint(1,16000000))
    SCREEN = screenres + " " + screensiz + " " + screentype + " screen with " + screencolors + " colors"

    embed = discord.Embed(title=f"Very cook PC",description=f"OS: {OS} {OSVER}\nRAM: {RAM}\nHDD: {HDD}\nSSD: {SSD}\nCPU: {CPU}\nGPU: {GPU}\nScreen: {SCREEN}",color=0xFECC4D)
    embed.set_footer(text=f"{inter.author} ({inter.author.id})")
    await inter.reply(embed=embed)

@client.slash_command(description="A really cook adventure")
@commands.cooldown(1, 120, commands.BucketType.user)
async def adventure(inter):
    #Easily get emojis
    lelcube = "<:lelcube:811058465383514132>"
    left_gun = "<:Gun:816099538619072553>"
    right_gun = "<:nuG:915809814947463168>"
    hellory5n = "<:hellory5n:915028960604200982>"
    sweatsmileHD = "<:sweatsmile_hd:916863610096062514>"
    button = "<:stoppedsweatbutton:916336148446601257>"
    left_punch = ":left_facing_fist:"
    right_punch = ":right_facing_fist:"
    castle = ":european_castle:"
    lelthink = "<:lelthink:915041532636201031>"
    void = "<:void:834904392008335360>"
    sweatgun = "<:sweatgun:917083708576657449>"
    sweathmm = "<:sweathmm:941526218170314753>"
    sweatidkanymore = "<:sweatidontknowanymore:941526218094837841>"
    hellory4n = "<:hellory4n:821460090225426482>"
    sweatcube = "<:sweatcube:868356676661686289>"
    superlelcube = "<:superlelcube:916875806746226698>"

    async def story():
        pain = inter

        await inter.send(lelthink)
        scn = await inter.original_message()
        msg = await inter.channel.send("See the intro?")

        async def hellory5nfightlol(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = hellory5nfightlol
            view = View() 
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="Chairs exist?",
                max_values=1,
                options=[
                    SelectOption(label="Become lelcube",emoji=lelcube),
                    SelectOption(label="Die",emoji="💀"),
                    SelectOption(label="Continue",emoji="⏩"),
                    SelectOption(label="Give up",emoji="🧦")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Become lelcube":
                        await msg.edit(content="**Superlelcube**\nOOOOOOOOOOOOOOOOOOOOOOOOO",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :hand_splayed: {hellory5n} :door: {castle}")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {left_punch} {hellory5n} :door: {castle}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} {castle}\n{lelcube}\n{void}\n{void}")
                        await msg.edit(content="**You lost**\nseriously",view=view)

                    if value == "Die":
                        await scn.edit(content=f":headstone: :hand_splayed: {hellory5n} :door: {castle}")
                        await msg.edit(content="**You lost**",view=view)

                    if value == "Give up":
                        await scn.edit(content=f"{superlelcube} :loudspeaker: :hand_splayed: {hellory5n} :door: {castle}")
                        await msg.edit(content="**Superlelcube**\n**__H E Y   S W E A T S M I L E   H D   I   N E E D   Y O U R   H E L P__**",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} {castle}\n{superlelcube}\n{void}\n:helicopter:")
                        await msg.edit(content="*SUPER_MEGA_ULTRA_COOK_MUSIC.MP3*")
                        await asyncio.sleep(5)
                        await scn.edit(content=f"{superlelcube} {void} {sweatsmileHD}")
                        await msg.edit(content="**Sweatsmile HD**\nOk so the castle is gonna explode?")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Superlelcube**\nNo, I gave up")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{superlelcube} {left_gun} {sweatsmileHD}")
                        await msg.edit(content="**You lost**\n*won!!1!!111",view=view)

                    if value == "Continue":
                        help = "> EVERYONE IN THE CHAT SEND LELCUBES"
                        await msg.edit(content="**Superlelcube**\nEVERYONE IN THE CHAT SEND LELCUBES",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**hellory5n**\nlol\n\n> EVERYONE IN THE CHAT SEND LELCUBES")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{superlelcube} {left_punch} {hellory5n} :door: {castle}")
                        await msg.edit(content=help)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} {castle}\n{superlelcube}\n{void}\n{void}\n:mountain:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} :fire:\n:fire: {superlelcube} :fire:\n{void} :fire:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{superlelcube} :fire: :fire: :fire: :fire: :fire: {castle}")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await msg.edit(content="Ok you don't need to send more lelcubes")
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You won**\nCook :cook:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{superlelcube}\n:helicopter:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{superlelcube} {sweatsmileHD}")
                        await msg.edit(content="**Sweatsmile HD**\nOh ma gawd tha castle exploded")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":cat2: {superlelcube} {sweatsmileHD}")
                        await msg.edit(content="**Superlelcube**\nI also spawned a cat")
                        await asyncio.sleep(3)
                        await msg.edit(content=f"Congrats {inter.author.mention} :clap:")

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f"{superlelcube} :hand_splayed: {hellory5n} :door: {castle}")
            await msg.edit(content="** **",view=theletterh)








        async def lab(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = lab
            view = View() 
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="Doors brings you closer to the things you hate.",
                max_values=1,
                options=[
                    SelectOption(label="Become superlelcube",emoji=superlelcube),
                    SelectOption(label="Punch the test tube",emoji="🤛"),
                    SelectOption(label="Watch a tutorial",emoji="📺"),
                    SelectOption(label="Go down",emoji="⬇️")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Punch the test tube":
                        await scn.edit(content=f":test_tube: {left_punch} {lelcube} :scientist: :cat2:")
                        await msg.edit(content="**Scientist**\nHEY WHAT ARE YOU DOING",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":boom: {left_punch} {lelcube} :scientist: :cat2:")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Scientist**\nHmm, this smells like apples")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You lost**\nI ran out of ways of commenting your low amount of intelligence without violating a rule in many servers that lelbot joined",view=view)

                    if value == "Go down":
                        await scn.edit(content=f":hammer: {lelcube} :cat2:")
                        await msg.edit(view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":hole: {lelcube}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":hole:\n{lelcube}\n{void}\n:cyclone:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {void} {void} {void} :name_badge: :beginner:")
                        await asyncio.sleep(5)
                        await msg.edit(content="**You lost**\nescf1f2f3f4f5f6f7f8f9f10f11f12fnlockinsertprtscdelbackspace/\*\"'1!2@3#4$5%6¨7&8\*9(0)-_=+backspacenumlock-+tabqwertyuiop`´[{enter7home8up9pgupcapslockasdfghjklç^~]}4left56rightshift|\\zxcvbnm,<.>;:shift1end2down3pgdnctrlfnwindowsaltspacealtgrleftupdownright0ins,delenter",view=view)

                    if value == "Watch a tutorial":
                        await scn.edit(content=f":test_tube: :scientist: :iphone: {lelcube} :cat2:")
                        await msg.edit(view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Phone**\nhello guys today i'm [incomprehensible sounds]")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":test_tube: :scientist: {right_gun} :iphone: {lelcube} :cat2:")
                        await msg.edit(content="**You lost**\nTip: Always lower the volume of your phone when you're gonna watch a tutorial when you are in a flying castle full of people that want to kill you hold on that's too specific",view=view)

                    if value == "Become superlelcube":
                        amogus = Button(
                            style=ButtonStyle.blurple,
                            label="But I want to become superlelcube :(",
                            custom_id="retry_button",
                            emoji="🔄"
                        )

                        async def sussy(inter):
                            if pain.author.id == inter.author.id:
                                await msg.edit(content="**You lost**\nOk fine",view=None)
                                await asyncio.sleep(3)
                                await msg.edit(content="**Lelcube**\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{void} {void} :satellite_orbital:\n{void} {void} :fist:\n:test_tube: :scientist: {superlelcube} :cat2:")
                                await msg.edit(content="*super_epok_music.mp3*")
                                await asyncio.sleep(3)
                                await scn.edit(content=f":cyclone:\n{superlelcube} :cat2:")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{hellory5n}\n:chair: {void} {superlelcube}")
                                await asyncio.sleep(3)
                                await msg.edit(content="**hellory5n**\nWait how you got here like that")
                                await asyncio.sleep(3)
                                await msg.edit(content="**Superlelcube**\nI became superlelcube, a clone of myself that is powered by messages with lelcube.")
                                await asyncio.sleep(5)
                                await msg.edit(content="**Superlelcube**\nThere's so many lelcubes in messages that now I'm able of teleporting and other stuff.")
                                await asyncio.sleep(5)
                                await msg.edit(content="**hellory5n**\nOk.")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{hellory5n} {right_gun} {superlelcube}")
                                await msg.edit(content="** **")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{hellory5n}\n:fire: :fire: :fire: :fire: :fire: {superlelcube}")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{hellory5n}\n:chair:\n{void} {void} {void} {superlelcube}")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{superlelcube} {left_punch} {hellory5n}")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{superlelcube} :hand_splayed: {hellory5n} :door: {castle}")
                                await msg.edit(content="**hellory5n**\nNow you have 3 options.")
                                await asyncio.sleep(3)
                                await msg.edit(content="**hellory5n**\n1: Die")
                                await asyncio.sleep(3)
                                await msg.edit(content="**hellory5n**\n2: Continue")
                                await asyncio.sleep(3)
                                await msg.edit(content="**hellory5n**\nAnd 3: Give up.")
                                await asyncio.sleep(3)
                                await hellory5nfightlol(inter)
                            else:
                                await inter.send("You're not the author :P",ephemeral=True)

                        amogus.callback = sussy
                        microwave = View() 
                        microwave.add_item(amogus)
                        await scn.edit(content=f"{void} {void} :satellite_orbital:\n:test_tube: :scientist: {lelcube} :cat2:")
                        await msg.edit(content="**You lost**\nSTOP",view=microwave)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":test_tube: :scientist: {lelthink} :cat2:")
            await msg.edit(content="** **",view=theletterh)






        async def gaems(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = gaems
            view = View() 
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="hjyukl",
                max_values=1,
                options=[
                    SelectOption(label="Become superlelcube",emoji=superlelcube),
                    SelectOption(label="Do nothing",emoji=lelcube),
                    SelectOption(label="Play the first game that the stop store shows you",emoji="🙂"),
                    SelectOption(label="Ignore this guy",emoji="👍")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Become superlelcube":
                        await scn.edit(content=f":tv: :video_game: {sweathmm} {lelcube} :cat2:")
                        await msg.edit(content="**Lelcube**\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":tv: :video_game: {sweathmm} {lelcube} {left_gun} :cat2:")
                        await msg.edit(content="**You lost**\nWhy you're still trying",view=view)

                    if value == "Do nothing":
                        await scn.edit(content=f":tv: :video_game: {sweathmm} {lelcube} :cat2:")
                        await msg.edit(view=None)
                        await asyncio.sleep(60)
                        await msg.edit(content="**You lost**\nHow can a room full of married people be empty? There's not a single person there",view=view)

                    if value == "Ignore this guy":
                        await scn.edit(content=f":door:  {lelcube} :cat2:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(1)
                        await scn.edit(content=f":door: :satellite_orbital: {lelcube} :cat2:")
                        await msg.edit(content="**You lost**\naeiou",view=view)

                    if value == "Play the first game that the stop store shows you":
                        await scn.edit(content=f":tv: :video_game: {sweathmm} :iphone: {lelcube} :cat2:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(5)
                        await scn.edit(content=f":cat2: {right_punch} {button}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":iphone: {lelcube} :cat2: {void} :magic_wand: :robot:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":test_tube: :scientist: {lelcube} :cat2:")
                        await asyncio.sleep(3)
                        await lab(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":tv: :video_game: {sweathmm} {lelthink} :cat2:")
            await msg.edit(content="** **",view=theletterh)






        async def whysomanycomputerslol(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = whysomanycomputerslol
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="Hola",
                max_values=1,
                options=[
                    SelectOption(label="Become superlelcube",emoji=superlelcube),
                    SelectOption(label="Spawn a cat",emoji="🐈"),
                    SelectOption(label="Monke",emoji="🐒"),
                    SelectOption(label="Magically create a dragon",emoji="🐉")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Become superlelcube":
                        await scn.edit(content=f"{lelcube} :man: :desktop:")
                        await msg.edit(content="**Lelcube**\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {left_gun} :man: :desktop:")
                        await msg.edit(content="**You lost**\nSilence, please",view=view)

                    if value == "Monke":
                        await scn.edit(content=f":test_tube: {lelcube}")
                        await msg.edit(view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=":monkey: :man: :desktop:")
                        await asyncio.sleep(3)
                        await scn.edit(content=":monkey: :monkey: :desktop:")
                        await asyncio.sleep(3)
                        await scn.edit(content=":monkey: :monkey: :monkey:")
                        await asyncio.sleep(3)
                        await msg.edit(content="**:monkey: :monkey:**\n:monkey:",view=view)

                    if value == "Magically create a dragon":
                        await scn.edit(content=f":tophat:\n{lelcube} :magic_wand: :man: :desktop:")
                        await msg.edit(view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :dragon: :man: :desktop:")
                        await asyncio.sleep(3)
                        await scn.edit(content=":fire: :dragon: :man: :desktop:")
                        await msg.edit(content="**You lost**\nIt's impressive the ways you find to die",view=view)

                    if value == "Spawn a cat":
                        await scn.edit(content=f"{lelcube} :satellite: :man: :desktop:")
                        await msg.edit(view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :cat2: :man: :desktop:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":desktop: {left_punch} :cat2:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":door: :arrow_left: {lelcube} :cat2:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":level_slider: {lelcube} :cat2:")
                        await msg.edit(content="*elevator_music.mp3*")
                        await asyncio.sleep(3)
                        await gaems(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f"{lelthink} :man: :desktop:")
            await msg.edit(content="** **",view=theletterh)










        async def alotofboxesomguwuveryepok(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = alotofboxesomguwuveryepok
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="WUjjuhersrnmymo yujkoiw wi vwi ll doew/?",
                max_values=1,
                options=[
                    SelectOption(label="Become superlelcube",emoji=superlelcube),
                    SelectOption(label="Go to the hole",emoji="🕳"),
                    SelectOption(label="Open the box",emoji="📦"),
                    SelectOption(label="Punch everything lol",emoji="🤛")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Become superlelcube":
                        await msg.edit(content="**Lelcube**\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":hole: {superlelcube} :package: :package: :package:")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":hole: {superlelcube} {left_gun} :package: :package: :package:")
                        await msg.edit(content="**Box (don't ask which one lollllllllll)**\nBruh I was sleeping")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nTechnology.",view=view)
                    
                    if value == "Go to the hole":
                        await scn.edit(content=f"{lelcube}\n:arrow_down:\n:hole:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {void} {left_gun} :person_bald:")
                        await msg.edit(content="**You lost**\nIt's like going to the market then when you get there, you return to home",view=view)

                    if value == "Open the box":
                        await scn.edit(content=f"{lelcube} :point_right: :package:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Box**\nhey i was sleeping!")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {left_gun} :package:")
                        await msg.edit(content="**You lost**\nEveryone here has a gun, even boxes",view=view)

                    if value == "Punch everything lol":
                        await scn.edit(content=f"{lelcube} {right_punch} {void}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await whysomanycomputerslol(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":hole: {lelcube} :package: :package: :package:")
            await msg.edit(content="** **",view=theletterh)







        async def cafeteria(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = cafeteria
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="Whnthdrj tyyhouh uylwil l ldow?",
                max_values=1,
                options=[
                    SelectOption(label="Become superlelcube",emoji=superlelcube),
                    SelectOption(label="Steal the food",emoji="🍛"),
                    SelectOption(label="Hack the physics",emoji="🧑‍💻"),
                    SelectOption(label="Constantly say \"I refuse\"",emoji="❌")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Become superlelcube":
                        await msg.edit(content="**Lelcube**\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{superlelcube} {left_gun} :deaf_person: :curry:")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{hellory5n} {right_gun} {superlelcube} {left_gun} :deaf_person: :curry:")
                        await msg.edit(content="**You lost**\nBigger numbers are better, 2 people that want to shoot you is better than 1!",view=view)
                    
                    if value == "Steal the food":
                        await scn.edit(content=f"{left_gun} :deaf_person: {lelcube} :curry:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":deaf_person: {right_gun} {lelcube} :curry:")
                        await msg.edit(content="**You lost**\nYe this didn't really help",view=view)

                    if value == "Hack the physics":
                        await scn.edit(content=f"{lelcube} :computer: {left_gun} :deaf_person: :curry:")
                        await msg.edit(content="**Lelcube**\nI'm gonna hack physics!",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube}\n:arrow_down:\n{void}\n{void}\n:mountain:")
                        await msg.edit(content="**You lost**\nOops",view=view)

                    if value == "Constantly say \"I refuse\"":
                        irefuse = "**Lelcube**\nI refuse"
                        await msg.edit(content=irefuse,view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Michael**\nYou are *that* idiot?? That will never work! *shoots*")
                        await asyncio.sleep(3)
                        await msg.edit(content=irefuse)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :person_bald: {sweatgun} :man:")
                        await msg.edit(content="**Sweatgun**\nHEY WHAT ARE YOU DOING YOU'RE GONNA DIE")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\n***__I refuse__***")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube}\n:cup_with_straw:\n:chair: {void}")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":bricks:\n:fist:\n{lelcube}")
                        await asyncio.sleep(3)
                        await alotofboxesomguwuveryepok(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f"{lelcube} {left_gun} :deaf_person: :curry:")
            await msg.edit(content="**Michael (deaf person)**\nHEY WHAT THE FANCADE ARE YOU DOING",view=theletterh)










        async def hellory5n_defender(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = hellory5n_defender
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="W h a t   y o u   w i l l   d o ?",
                max_values=1,
                options=[
                    SelectOption(label="Install Doors XP",emoji="💿"),
                    SelectOption(label="Ask who is sweatcube",emoji="👤"),
                    SelectOption(label="Magically create 20000 turtles",emoji="🐢"),
                    SelectOption(label="Make a music",emoji="🎶")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Install Doors XP":
                        await scn.edit(content=f"{lelcube} :cd: :desktop: {sweatcube}")
                        await msg.edit(content="**Lelcube**\nHey, can I install Doors XP?",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatcube**\nSure")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{sweatcube} {void} :desktop: {lelcube}")
                        await msg.edit(content="*title.wma*")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatcube**\nhold on")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nWhat is the limit of dumbness?",view=view)
                    
                    if value == "Ask who is sweatcube":
                        await scn.edit(content=f"{lelcube} {void} :desktop: {sweatcube}")
                        await msg.edit(content="**Lelcube**\nWho are you?",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatcube**\nI am...")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {void} :desktop: {lelcube}")
                        await msg.edit(content="**Lelcube?**\nYOU!!!")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nTop 10 biggest plot twists",view=view)

                    if value == "Make a music":
                        await scn.edit(content=f":headphones:\n{lelcube} :iphone:")
                        await msg.edit(content="*epok_music.mp3*",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":headphones:\n{lelcube} :iphone: :desktop: {sweatcube}")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatcube**\nThat's a nice music, I wonder what is playing it")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatcube**\nOh")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nHey, at least you made a nice music!",view=view)
                        
                    if value == "Magically create 20000 turtles":
                        await scn.edit(content=f"{lelcube} :ballot_box: :desktop: {sweatcube}")
                        await msg.edit(content="**Lelcube**\nImma create a bunch of turtles",view=None)
                        await asyncio.sleep(5)
                        await msg.edit(content="**Sweatcube**\n??????????")
                        await asyncio.sleep(1)
                        await scn.edit(content=":turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle:")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :level_slider:")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\nThe collision is quite buggy")
                        await asyncio.sleep(3) #man this program sleeps a lot
                        await msg.edit(content="*elevator_music.mp3*")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :curry: :deaf_person: {void}")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await cafeteria(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f"{lelthink} {void} :desktop: {sweatcube}")
            await msg.edit(content="** **",view=theletterh)






        async def thecookestbotroomevermadeomgveryepok(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = thecookestbotroomevermadeomgveryepok
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Use a rocket",emoji="🚀"),
                    SelectOption(label="Ask what is 0 divided by 0",emoji="❔"),
                    SelectOption(label="Punch the bots",emoji="🤛"),
                    SelectOption(label="Build a skyscraper",emoji="🔧")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Ask what is 0 divided by 0":
                        await msg.edit(content="**Bot (don't ask which one)**\nImagine that you have 0 cookis, and you split them evenly among 0 friends.",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Bot (don't ask which one)**\nHow many cookis each person get?")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Bot (don't ask which one)**\nSee? It doesn't make sense.")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Bot (don't ask which one)**\nAnd cooki monster is sad because there are no cookis!")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Bot (don't ask which one)**\nAnd you are sad because you have no friends!")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nOh wow, this escalated quickly",view=view)
                    
                    if value == "Punch the bots":
                        await scn.edit(content=f":robot: :robot: {left_punch} {lelcube}")
                        await msg.edit(content="*epok_music_ues.mp3*",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":robot: {right_gun} {left_punch} {lelcube}")
                        await msg.edit(content="**You lost**\nGet a mechanical arm",view=view)

                    if value == "Build a skyscraper":
                        await scn.edit(content=f":robot: :robot: {lelcube}")
                        await msg.edit(content="**You lost**\nNo, I won't say anything funny just cuz you made something infinitely stupid",view=view)
                        
                    if value == "Use a rocket":
                        await scn.edit(content=f":robot: :robot: {lelcube} :rocket:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {void} :bricks:\n:rocket: :arrow_right: :bricks:")
                        await asyncio.sleep(3)
                        await hellory5n_defender(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":robot: :robot: {lelthink}")
            await msg.edit(content="ertytreshrdtjrehrj",view=theletterh)








        async def hellory5n_room(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = hellory5n_room
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Throw the moneybag",emoji="🚀"),
                    SelectOption(label="Watch stuff",emoji="👀"),
                    SelectOption(label="Give the money",emoji="🤝"),
                    SelectOption(label="Scream",emoji="😱")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Throw the moneybag":
                        await scn.edit(content=f"{hellory5n} :arrow_left: :moneybag:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{hellory5n} {right_gun} {lelcube}")
                        await msg.edit(content="**You lost**\nAre you trying to make a death speedrun? A normal person wouldn't do this. Oh, considering how dumb you are, this makes a lot of sense",view=view)
                    
                    if value == "Watch stuff":
                        await scn.edit(content=f":tv: {hellory5n} {sweatgun} {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":timer:")
                        await msg.edit(content="*10 minutes later...*")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{hellory5n} {right_gun} {lelcube}")
                        await msg.edit(content="**You lost**\nI need a new word to describe your insane amount of dumbness",view=view)

                    if value == "Scream":
                        await scn.edit(content=f":tv: {hellory5n} {sweatgun} {lelcube}")
                        await msg.edit(content="**Lelcube**\nAAAAAAAAAAAAAAAAAAAAAAAAA",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{hellory5n} {right_gun} {lelcube}")
                        await msg.edit(content="**You lost**\nWhy did the worker get fired from the orange juice factory? Lack of concentration.",view=view)
                        
                    if value == "Give the money":
                        await scn.edit(content=f":tv: {hellory5n} {sweatgun} :moneybag: {lelcube}")
                        await msg.edit(content="**Lelcube**\nI want to give money to you guys!",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**hellory5n**\nWait, by analyzing the 1337th pixel of this moneybag, that is *our* money!")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatgun**\nIdc i want mone lollllll")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{button} {void} {void} {sweatgun} :moneybag: {lelcube}")
                        await msg.edit(content="**Lelcube**\nOk imma only give tha mone if you press that button")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatgun**\nOk")
                        await scn.edit(content=f":wave: {lelcube}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{button} {left_punch} {sweatgun}")
                        await msg.edit(content="**hellory5n**\nHEY WHAT ARE YOU DOINGGGGGGGGGGGG")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You won**\nCook")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube}\n:arrow_down:\n{void}\n{void}\n:mountain:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube}\n:helicopter:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{sweatsmileHD} {lelcube}")
                        await msg.edit(content="**Sweatsmile HD**\nᴠᴇʀʏ ᴇᴘᴏᴋ")

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":tv: {hellory5n} {sweatgun} :moneybag: {lelthink}")
            await msg.edit(content=":arrow_down: look at dis",view=theletterh)








        async def computer_room(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = computer_room
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Ask to use the computer",emoji="🖥️"),
                    SelectOption(label="Eat pretty delicious stuff",emoji="😋"),
                    SelectOption(label="Throw watermelons",emoji="🍉"),
                    SelectOption(label="Play ping pong",emoji="🏓")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Ask to use the computer":
                        await scn.edit(content=f":desktop: {sweathmm} :desktop: {sweatidkanymore} {lelcube}")
                        await msg.edit(content="**Lelcube**\nCan I use the computer?",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweathmm**\nI'M LITERALLY FIXING A PROBLEM THAT CAN DESTROY THE ENTIRE CASTLE ARE YOU CRAZY\n\n**Sweatidkanymore**\nWait, isn't him lelcube?")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You lost**\nsmort:brain:",view=view)
                    
                    if value == "Throw watermelons":
                        await scn.edit(content=f":desktop: :arrow_left: :watermelon: {lelcube}")
                        await msg.edit(content="***EPOK_MUSIC.MP3***",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":boom: {sweathmm}")
                        await msg.edit(content="**Sweathmm**\nOH NOOOOOOOOOOOOO THE CASTLE WIL LL EPLOXLDO EDJHDKFLKGHK")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You lost**\nI'm speechless- wait...")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":telephone: :grey_question:")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{hellory4n} :telephone: :grey_question:")
                        await msg.edit(content="**hellory4n**\nHello!")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost guy**\nHi, can I give the \"dumbest person\" trophy to lelcube?")
                        await asyncio.sleep(3)
                        await msg.edit(content="**hellory4n**\nok")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":grey_question:")
                        await msg.edit(content="**You lost guy**\nAnd the dumbest person trophy goes to...")
                        await asyncio.sleep(3)
                        await msg.edit(content=f"**You lost guy**\nLELCUBE!!!")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":clap: {sweatsmileHD} :clap: :deaf_person: :clap: :person_bald:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":trophy: {lelcube}")
                        await msg.edit(content="**You lost**\nAt least you got a trophy for being the dumbest person!",view=view)

                    if value == "Play ping pong":
                        await scn.edit(content=f":desktop: {sweathmm} :desktop: {sweatidkanymore} {lelcube}")
                        await msg.edit(content="**Lelcube**\nHey let's play ping pong",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatidontknowanymore**\nYes!")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{sweatidkanymore} :ping_pong: {lelcube}")
                        await msg.edit(content="**You lost**\nWho doesn't like ping pong?",view=view)
                        
                    if value == "Eat pretty delicious stuff":
                        await scn.edit(content=f":fries: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{sweathmm} :fries: {lelcube}")
                        await msg.edit(content="**Sweathmm**\nHi can I eat your fries")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\nOnly if you allow me go to the next room without me commiting ded")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweathmm**\nOk")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":level_slider: :wastebasket: {lelcube}")
                        await msg.edit(content="**Lelcube**\nThis is trash")
                        await asyncio.sleep(3)
                        await hellory5n_room(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":desktop: {sweathmm} :desktop: {sweatidkanymore} {lelthink}")
            await msg.edit(content="**Sweathmm**\nOh no, the program is broken!\n\n**Sweatidkanymore**\nWe need to fix it fast before the entire castle breaks!",view=theletterh)







        async def electrical(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = electrical
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Manage energy",emoji="🧠"),
                    SelectOption(label="Create an entire OS from scratch",emoji="💻"),
                    SelectOption(label="Shutdown power",emoji="🔌"),
                    SelectOption(label="Destroy stuff",emoji="💥")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Manage energy":
                        await scn.edit(content=castle)
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You lost**\nSo smart!",view=view)
                    
                    if value == "Create an entire OS from scratch":
                        await scn.edit(content=f":keyboard: :hammer: {lelcube}")
                        await msg.edit(content="**Lelcube**\n*programming*",view=None)
                        await asyncio.sleep(10)
                        await msg.edit(content="**You lost**\nYou know this one? A robot and a human walk into a bar *`Message only available for WhatsApp 2 userss`*",view=view)

                    if value == "Shutdown power":
                        await scn.edit(content=f":electric_plug: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle}\n:arrow_down:{void}\n{void}\n:volcano:")
                        await msg.edit(content="**You lost**\nWe do a large amount of trolling",view=view)
                        
                    if value == "Destroy stuff":
                        await scn.edit(content=f":ant: :hammer: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":level_slider: {lelcube} :clock10:")
                        await msg.edit(content="*elevator music*")
                        await asyncio.sleep(3)
                        await computer_room(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":electric_plug: :control_knobs: :control_knobs: :control_knobs: {lelthink}")
            await msg.edit(content="** ** ",view=theletterh)







        async def bank(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = bank
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="ono you don't have card wat u will do",
                max_values=1,
                options=[
                    SelectOption(label="Do nothing",emoji="🙅"),
                    SelectOption(label="Play RPS",emoji="👊"),
                    SelectOption(label="Throw a bunch of bombs",emoji="💣"),
                    SelectOption(label="Plant trees",emoji="🌲")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Do nothing":
                        await scn.edit(content=f":moneybag: :robot: {lelcube}")
                        await msg.edit(content="(the game didn't broke)",view=None)
                        await asyncio.sleep(60)
                        await msg.edit(content="**You lost**\nI wish there was an achievements system so I could give you one",view=view)
                    
                    if value == "Play RPS":
                        await scn.edit(content=f":moneybag: :robot: :scissors: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":moneybag: :robot: {right_gun} :scissors: {lelcube}")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nThey released a new RPS update???", view=view)

                    if value == "Throw a bunch of bombs":
                        await scn.edit(content=f":moneybag: :robot: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You lost**\nlelbot story mode speedrun any%",view=view)
                        
                    if value == "Plant trees":
                        await scn.edit(content=f":moneybag: :robot: :evergreen_tree: {lelcube} :thumbsup:")
                        await msg.edit(content="**Bot**\neiuryb4 ie ty48t8ibu4nwiuteyh4iwuoeurui4jweuygrhi94ywgeuyt8y74",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Bot**\nI HATE TREEESSSSSSSSS THEY EXPLODED ALL OF MY SANDWICHES AAAAAAAAAA FIOSRKJIIJRIUGHJSROI")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":moneybag: :boom: :evergreen_tree: {lelcube}")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":moneybag: {void} :evergreen_tree: :hammer: {lelcube}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":moneybag: {lelcube} :thumbsup:")
                        await asyncio.sleep(3)
                        await electrical(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":moneybag: :robot: {lelthink}")
            await msg.edit(content="**Bot**\nInsert a card.",view=theletterh)






        async def super_gun_room(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = super_gun_room
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="Which super mega ultra gun you'll use?",
                max_values=1,
                options=[
                    SelectOption(label="Super laser machine",emoji="📡"),
                    SelectOption(label="Ultra shooting thing 3000",emoji=left_gun),
                    SelectOption(label="Boom collection",emoji="💣"),
                    SelectOption(label="Mega musical pain",emoji="🎸")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Super laser machine":
                        await scn.edit(content=f":satellite: {button} {left_punch} {lelcube} :joystick:")
                        await msg.edit(content="***ULTRA_INTENSE_EPOK_MUSIC.MP3***",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void}{castle}\n:satellite:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void}:boom:\n:satellite:")
                        await msg.edit(content="**You lost**\nCongrats! You did it! :clap: :clap: :clap:",view=view)
                    
                    if value == "Ultra shooting thing 3000":
                        await scn.edit(content=f"{left_gun} :joystick: {lelcube}")
                        await msg.edit(content="***SUPER_MEGA_ULTRA_INTENSE_EPOK_MUSIC_THAT_TOOK_700_YEARS_TO_MAKE.MP3***",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle} {left_gun}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{left_gun}\n{castle}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":helicopter: {void} {left_gun} {castle}")
                        await msg.edit(content="**You lost**\nNice aim! :clap:",view=view)

                    if value == "Mega musical pain":
                        await scn.edit(content=f":guitar: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":fire: :loudspeaker: :guitar: {lelcube} :loudspeaker: :fire:")
                        await msg.edit(content="***INSANELY_INSANE_AND_GOOD_MUSIC.MP3***")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":anger: {castle} :anger:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":anger: :earth_americas: :anger: {left_gun} :new_moon_with_face:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":guitar: {lelcube} {left_gun} {hellory5n}")
                        await msg.edit(content="**You lost**\nCongrats! Your music sucks so much that hellory5n came here to kill you! :clap:",view=view)
                        
                    if value == "Boom collection":
                        await scn.edit(content=f"{button} {left_gun} {lelcube}")
                        await msg.edit(content="***SUPER_SUPER_SUPER_SUPER_SUPER_SUPER_EPICCC_MUSICCCCCCCC.MP3***",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle}\n:bomb:\n{void}\n{void}\n{void}\n{void}\n{void}\n:mountain:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :desktop:")
                        await msg.edit(content="**Lelcube**\nwas dis?")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle}\n{void}\n{void}\n{void}\n{void}\n{void}\n:bomb:\n:mountain:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle}\n{void}\n{void}\n{void}\n{void}\n:arrow_up:\n:bomb:\n:mountain:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":rotating_light: {lelcube} :rotating_light:")
                        await msg.edit(content=f"**Lelcube**\nOH NO WHAT HAVE I DONE\n\n**Castle security system**\nWARNING: BOMBS ARE GETTING CLOSE TO THE CASTLE!!!!!!!!!!!!!!! DO SOMETHING ABOUT IT!!!!!!!!!!!!!!!111")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :arrow_right: :window:")
                        await msg.edit(content="**Castle security system**\nWARNING: BOMBS ARE GETTING CLOSE TO THE CASTLE!!!!!!!!!!!!!!! DO SOMETHING ABOUT IT!!!!!!!!!!!!!!!111")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle}\n{void}{lelcube}\n{void}\n{void}:helicopter:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":iphone: {sweatsmileHD}")
                        await msg.edit(content=f"*Sweatsmile HD making a new Drive Mad Kit 2*")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube's phone**\n**__`NEVER GONNA GIVE YOU UP\nNEVER GONNA LET YOU DOWN\nNEVER GONNA RUN AROUND AND DESERT YOU\nNEVER GONNA MAKE YOU CRY\nNEVER GONNA SAY GOODBYE\nNEVER GONNA TELL A LIE AND HURT YOU`__**")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatsmile HD**\nOK OK OK")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube}\n:helicopter:")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {sweatsmileHD}")
                        await msg.edit(content="**Sweatsmile HD**\nOk, the castle will explode?")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\nYes, I hope!")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":fire: :fire: {hellory5n} :fire: :fire:")
                        await msg.edit(content="**hellory5n**\nNOOOOOOOOOOOOOOOOOOOOO")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You won!**\n...somehow")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":boom:\n{void}:helicopter:")
                        await msg.edit(content=f"**Sweatsmile HD**\nYay, it really exploded!")
                        await asyncio.sleep(5)
                        await msg.edit(content=f"Congrats {inter.author.mention}! :clap:")

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":satellite: {left_gun} :bomb: :guitar: {lelthink}")
            await msg.edit(content="** **",view=theletterh)







        async def server(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = server
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Look what's on the server",emoji="👀"),
                    SelectOption(label="Destroy everything",emoji="🔨"),
                    SelectOption(label="Play games on the supercomputers",emoji="🎮"),
                    SelectOption(label="Just go to another room",emoji="🏃")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Look what's on the server":
                        await scn.edit(content=f":file_cabinet: :desktop: {lelcube}")
                        await msg.edit(content=f"**Lelcomputer**\nStarting lelcubeOS 39 for servers...",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content=f"**Welcome!**\n\n**Apps**\n> :file_folder: Lelfinder\n> :keyboard: Lelterminal\n> :file_cabinet: Leldatabase\n> :cloud: Lelcloud\n> :arrows_counterclockwise: Restart\n> :octagonal_sign: Shutdown\n> :mag: Search")
                        await asyncio.sleep(3)
                        await msg.edit(content=f":file_folder: Lelfinder\n\n/home/Server3/\n> :page_facing_up: Documents\n> :arrow_down: Downloads\n> :frame_photo: Images\n> :musical_note: Musics\n> :film_frames: Videos")
                        await asyncio.sleep(3)
                        await msg.edit(content=f"/home/Server3/Documents/\n\n> :file_cabinet: database.leldb\n> :page_facing_up: HOW_TO_DESTROY_CASTLE.txt")
                        await asyncio.sleep(3)
                        await msg.edit(content=f":notepad_spiral: Lelnotepad\nscream \"EMERGENCY EVERYONE RUN WE NEED TO GET OUT OF THE CASTLEEEEEEEEEE\"")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\nEMERGENCY EVERYONE RUN WE NEED TO GET OUT OF THE CASTLEEEEEEEEEEEE")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":file_cabinet: :desktop: {lelcube} {sweatgun}")
                        await msg.edit(content="**You lost**\nuwu he's gonna shoot you",view=view)
                    
                    if value == "Destroy everything":
                        await scn.edit(content=f":file_cabinet: :file_cabinet: :boom: {left_gun} {lelcube}")
                        await msg.edit(content=f"** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":file_cabinet: :file_cabinet: :boom: {left_gun} {lelcube} {sweatgun}")
                        await msg.edit(content="**You lost**\n**__B O O M__**",view=view)

                    if value == "Just go to another room":
                        await scn.edit(content=f":door: {void} {void} {void} {lelcube}")
                        await asyncio.sleep(1)
                        await scn.edit(content=f":door: :fire: :boom: :fire: :boom: :fire: {lelcube}")
                        await msg.edit(content="**You lost**\nThe door doesn't like you",view=view)
                        
                    if value == "Play games on the supercomputers":
                        await scn.edit(content=f":file_cabinet: :desktop: :video_game: {lelcube}")
                        await msg.edit(content="**Lelcube**\nCan't wait to play cyberlel 2077 here!",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":file_cabinet: :hole: :video_game: {lelcube}")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube}\n:arrow_down:\n:hole:")
                        await asyncio.sleep(3)
                        await super_gun_room(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":door: :file_cabinet: :file_cabinet: :file_cabinet: {left_gun} {lelthink}")
            await msg.edit(content="** **",view=theletterh)







        async def gun_room(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = gun_room
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Insert credit card details",emoji="📥"),
                    SelectOption(label="Ask a hamburger",emoji="🍔"),
                    SelectOption(label="Rickroll the bot",emoji="🎤"),
                    SelectOption(label="Steal a card",emoji="🥷"),
                    SelectOption(label="Go to another room",emoji="🏃")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Insert credit card details":
                        await scn.edit(content=f":toolbox: :robot: :credit_card: {lelcube}")
                        await msg.edit(content=f"**Lelcube**\nHey here's my credit card",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":toolbox: :robot: {void} {lelcube}")
                        await msg.edit(content="**Bot**\nThank you!")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nBots are evolving, this one likes money!",view=view)
                    
                    if value == "Rickroll the bot":
                        await scn.edit(content=f":toolbox: :robot: {lelcube}")
                        await msg.edit(content="**Lelcube**\nWe're no strangers to love",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":toolbox: :robot: {right_gun} {lelcube}")
                        await msg.edit(content="**You lost**\nBots are evolving, this one hates rickrolls!",view=view)

                    if value == "Steal a card":
                        await scn.edit(content=f"{lelcube} {void} {void}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {void} {void} :woman_beard:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :arrow_left: :credit_card: :woman_beard:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":toolbox: :robot: :credit_card: {lelcube}")
                        await msg.edit(content="**Lelcube**\nHere is ma card")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Bot**\nWhat?! Steve is not on the room for brainless people?????")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nBots are evolving, this one thinks you are Steve!",view=view)
                        
                    if value == "Go to another room":
                        await bank(inter)
                    
                    if value == "Ask a hamburger":
                        await scn.edit(content=f":toolbox: :robot: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(5)
                        await msg.edit(content="**Bot**\nTraceback (most recent call last):\n  File \"bot.ues\", line 69, in \"ues\"\nBotError: help what me supposed to do when tha user wants to get guns and it asks for a hamburger")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":toolbox: :boom: {lelcube}")
                        await asyncio.sleep(3)
                        await server(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":toolbox: :robot: {lelthink}")
            await msg.edit(content="**Bot**\nInsert your card to access guns.",view=theletterh)








        async def right_path_start(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = right_path_start
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="How you will open tha door",
                max_values=1,
                options=[
                    SelectOption(label="Use a key",emoji="🔑"),
                    SelectOption(label="Shoot the door",emoji=left_gun),
                    SelectOption(label="Delete the door object",emoji="💥"),
                    SelectOption(label="High-speed train",emoji="🚄")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Use a key":
                        await scn.edit(content=f":door: {void} {lelcube}")
                        await msg.edit(content="**You lost**\nBut what key?",view=view)
                    
                    if value == "Shoot the door":
                        await scn.edit(content=f":door: :gun: {lelcube}")
                        await msg.edit(content="**Lelcube**\nI'm gonna destroy this door!",view=None)
                        await asyncio.sleep(5)
                        await msg.edit(content="**Lelcube**\nwhat")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :iphone:")
                        await msg.edit(content="**eyePhone**\nCalling...")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":joystick: {sweatsmileHD} {void} :iphone:")
                        await msg.edit(content="**eyePhone**\nLelcube is calling you!")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :telephone: {sweatsmileHD}")
                        await msg.edit(content="**Lelcube**\nYou gave me a toy gun")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatsmile HD**\nWhat the")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatsmile HD**\nLike, can't you just steal a gun?")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\nI need a gun to destroy a locked door")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatsmile HD**\nOk, fine, gonna you give you a real gun!")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle} {void} {void} {void} {left_gun} :helicopter:\n{void} {void} {void} :arrow_lower_left:")
                        await msg.edit(content="**You lost**\nnice",view=view)

                    if value == "High-speed train":
                        await scn.edit(content=f"{void} {void} {lelcube}\n:door: {void} 🚄")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} {void} {lelcube}\n{left_gun} :boom: 🚄")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":moneybag: :moneybag: {lelcube}\n:moneybag: :boom: 🚄")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} {void} {lelcube}\n:person_standing: :desktop: 🚄")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} {void} {lelcube}\n:level_slider: :boom: 🚄")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":video_game: :video_game: {lelcube}\n:video_game: :boom: 🚄")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":test_tube: :test_tube: {lelcube}\n:scientist: :boom: 🚄")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":radio: :control_knobs: {lelcube}\n:level_slider: :boom: 🚄")
                        await msg.edit(content="**Lelcube**\nOH WAIT I DESTROYED THE REACTOR NOOOOOOOOOOOOOOO")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":boom:")
                        await msg.edit(content="**You lost**\nWell, you destroyed the castle, so you technically won even tho you will fall into a mountain?",view=view)
                
                    if value == "Delete the door object":
                        await scn.edit(content=f":door: :computer: {lelcube}")
                        await msg.edit(content="**Lelptop**\n:balloon: Object manager\n\nroom=outside_of_the_castle.room\n> lelcube.obj\n> sweatsmileHD.obj\n> door.obj\n> lelptop.obj\n> helicopter\n> castle.obj",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelptop**\n:balloon: Object manager\n\nobj=door.obj\n> Delete\n> Position\n> More")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} :computer: {lelcube}")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":toolbox: :robot: {lelcube}")
                        await asyncio.sleep(3)
                        await gun_room(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":door: {void} {lelthink}")
            await msg.edit(content="**Lelcube**\nono tha door locked",view=theletterh)





        async def bathroom(inter):
            nonlocal scn
            nonlocal msg

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Toilet",emoji="🚽"),
                    SelectOption(label="Take a shower immediately",emoji="🚿"),
                    SelectOption(label="Go down",emoji="⬇️")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Toilet":
                        again = Button(
                            style=ButtonStyle.blurple,
                            label="Again",
                            custom_id="retry_button",
                            emoji="🔄"
                        )
                        again.callback = bathroom
                        view = View()
                        view.add_item(again)

                        await scn.edit(content=f"{lelcube}\n:toilet:")
                        await msg.edit(content="**You lost**\nare you kidding me",view=view)
                    
                    if value == "Take a shower immediately":
                        again = Button(
                            style=ButtonStyle.blurple,
                            label="Again",
                            custom_id="retry_button",
                            emoji="🔄"
                        )
                        again.callback = bathroom
                        view = View()
                        view.add_item(again)

                        await scn.edit(content=f":shower:\n{lelcube}")
                        await msg.edit(content="**You lost**\nOk :thumbsup:",view=view)

                    if value == "Go down":
                        await scn.edit(content=f"{lelcube}\n:arrow_down:\n:toilet:")
                        await msg.edit(view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":man_bald: {left_gun} :deaf_person: {lelcube}")
                        await asyncio.sleep(3)

                        again = Button(
                            style=ButtonStyle.blurple,
                            label="Again",
                            custom_id="retry_button",
                            emoji="🔄"
                        )
                        again.callback = bathroom
                        view = View()
                        view.add_item(again)

                        await scn.edit(content=f":man_bald: :deaf_person: {right_gun} {lelcube}")
                        await msg.edit(content="**You lost**\nasdfghjklñ.",view=view)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            view = View()
            view.add_item(ues)
            await scn.edit(content=f"{lelthink} :toilet: :shower:")
            await msg.edit(content="*very_intense_epok_music.mp3*",view=view)
        


        async def path_chooser_3000(inter):
            nonlocal scn
            nonlocal msg

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Top",emoji="⬆️"),
                    SelectOption(label="Left",emoji="⬅️"),
                    SelectOption(label="Right",emoji="➡️")
                ]
            )

            async def abcd2(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Top":
                        await scn.edit(content=f":helicopter:\n{lelcube}\n:arrow_down:\n{castle}")
                        await msg.edit(content="*epok_tension_music_thing.mp3*",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {right_punch} :door:")
                        await asyncio.sleep(3)
                        await bathroom(inter)
                    if value == "Right":
                        await scn.edit(content=f"{castle} :arrow_left: {lelcube} :helicopter:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"🚪 {void} {lelcube}")
                        await asyncio.sleep(3)
                        await right_path_start(inter)
                    if value == "Left":
                        await scn.edit(content=f":helicopter: {lelcube} :arrow_right: {castle}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":window: {left_punch} {lelcube}")
                        await asyncio.sleep(3)
                        await thecookestbotroomevermadeomgveryepok(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd2
            view = View()
            view.add_item(ues)
            await scn.edit(content=f":european_castle: {sweatsmileHD} {lelthink}")
            await msg.edit(content="**Sweatsmile HD**\nWhere you'll jump?",view=view)







        async def intro(inter):
            nonlocal msg
            nonlocal scn

            await scn.edit(content=":helicopter:")
            await msg.edit(content="** **",components=[])
            await asyncio.sleep(3)
            await scn.edit(content=f"{sweatsmileHD} {lelcube}")
            await msg.edit(content="**Lelcube**\ny mii on helicopter")
            await asyncio.sleep(3)
            await scn.edit(content=":european_castle:")
            await msg.edit(content="**Sweatsmile HD**\nRecently, hellory5n built a huge castle. It'll be used to help him take over the world.")
            await asyncio.sleep(3)
            await msg.edit(content="**Sweatsmile HD**\nThis castle will have all of his allies, and extremely powerful weapons.")
            await asyncio.sleep(3)
            await scn.edit(content=f"{sweatsmileHD} {lelcube}")
            await msg.edit(content="**Sweatsmile HD**\nWe need to stop him.")
            await asyncio.sleep(3)
            await path_chooser_3000(inter)








        yes = Button(
            style=ButtonStyle.blurple,
            label="Yes",
            custom_id="yes_button"
        )
        no = Button(
            style=ButtonStyle.blurple,
            label="No",
            custom_id="no_button"
        )

        yes.callback = intro
        no.callback = path_chooser_3000
        view = View()
        view.add_item(yes)
        view.add_item(no)
        await msg.edit(view=view)
    
    await story()



























































@client.command(aliases=['adventure'])
@commands.cooldown(1, 120, commands.BucketType.user)
async def adventure2(inter):
    #Easily get emojis
    lelcube = "<:lelcube:811058465383514132>"
    left_gun = "<:Gun:816099538619072553>"
    right_gun = "<:nuG:915809814947463168>"
    hellory5n = "<:hellory5n:915028960604200982>"
    sweatsmileHD = "<:sweatsmile_hd:916863610096062514>"
    button = "<:stoppedsweatbutton:916336148446601257>"
    left_punch = ":left_facing_fist:"
    right_punch = ":right_facing_fist:"
    castle = ":european_castle:"
    lelthink = "<:lelthink:915041532636201031>"
    void = "<:void:834904392008335360>"
    sweatgun = "<:sweatgun:917083708576657449>"
    sweathmm = "<:sweathmm:941526218170314753>"
    sweatidkanymore = "<:sweatidontknowanymore:941526218094837841>"
    hellory4n = "<:hellory4n:821460090225426482>"
    sweatcube = "<:sweatcube:868356676661686289>"
    superlelcube = "<:superlelcube:916875806746226698>"

    async def story():
        pain = inter

        scn = await inter.send(lelthink)
        msg = await inter.send("See the intro?")

        async def hellory5nfightlol(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = hellory5nfightlol
            view = View() 
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="Chairs exist?",
                max_values=1,
                options=[
                    SelectOption(label="Become lelcube",emoji=lelcube),
                    SelectOption(label="Die",emoji="💀"),
                    SelectOption(label="Continue",emoji="⏩"),
                    SelectOption(label="Give up",emoji="🧦")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Become lelcube":
                        await msg.edit(content="**Superlelcube**\nOOOOOOOOOOOOOOOOOOOOOOOOO",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :hand_splayed: {hellory5n} :door: {castle}")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {left_punch} {hellory5n} :door: {castle}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} {castle}\n{lelcube}\n{void}\n{void}")
                        await msg.edit(content="**You lost**\nseriously",view=view)

                    if value == "Die":
                        await scn.edit(content=f":headstone: :hand_splayed: {hellory5n} :door: {castle}")
                        await msg.edit(content="**You lost**",view=view)

                    if value == "Give up":
                        await scn.edit(content=f"{superlelcube} :loudspeaker: :hand_splayed: {hellory5n} :door: {castle}")
                        await msg.edit(content="**Superlelcube**\n**__H E Y   S W E A T S M I L E   H D   I   N E E D   Y O U R   H E L P__**",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} {castle}\n{superlelcube}\n{void}\n:helicopter:")
                        await msg.edit(content="*SUPER_MEGA_ULTRA_COOK_MUSIC.MP3*")
                        await asyncio.sleep(5)
                        await scn.edit(content=f"{superlelcube} {void} {sweatsmileHD}")
                        await msg.edit(content="**Sweatsmile HD**\nOk so the castle is gonna explode?")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Superlelcube**\nNo, I gave up")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{superlelcube} {left_gun} {sweatsmileHD}")
                        await msg.edit(content="**You lost**\n*won!!1!!111",view=view)

                    if value == "Continue":
                        help = "> EVERYONE IN THE CHAT SEND LELCUBES"
                        await msg.edit(content="**Superlelcube**\nEVERYONE IN THE CHAT SEND LELCUBES",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**hellory5n**\nlol\n\n> EVERYONE IN THE CHAT SEND LELCUBES")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{superlelcube} {left_punch} {hellory5n} :door: {castle}")
                        await msg.edit(content=help)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} {castle}\n{superlelcube}\n{void}\n{void}\n:mountain:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} :fire:\n:fire: {superlelcube} :fire:\n{void} :fire:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{superlelcube} :fire: :fire: :fire: :fire: :fire: {castle}")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await msg.edit(content="Ok you don't need to send more lelcubes")
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You won**\nCook :cook:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{superlelcube}\n:helicopter:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{superlelcube} {sweatsmileHD}")
                        await msg.edit(content="**Sweatsmile HD**\nOh ma gawd tha castle exploded")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":cat2: {superlelcube} {sweatsmileHD}")
                        await msg.edit(content="**Superlelcube**\nI also spawned a cat")
                        await asyncio.sleep(3)
                        await msg.edit(content=f"Congrats {inter.author.mention} :clap:")

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f"{superlelcube} :hand_splayed: {hellory5n} :door: {castle}")
            await msg.edit(content="** **",view=theletterh)








        async def lab(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = lab
            view = View() 
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="Doors brings you closer to the things you hate.",
                max_values=1,
                options=[
                    SelectOption(label="Become superlelcube",emoji=superlelcube),
                    SelectOption(label="Punch the test tube",emoji="🤛"),
                    SelectOption(label="Watch a tutorial",emoji="📺"),
                    SelectOption(label="Go down",emoji="⬇️")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Punch the test tube":
                        await scn.edit(content=f":test_tube: {left_punch} {lelcube} :scientist: :cat2:")
                        await msg.edit(content="**Scientist**\nHEY WHAT ARE YOU DOING",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":boom: {left_punch} {lelcube} :scientist: :cat2:")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Scientist**\nHmm, this smells like apples")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You lost**\nI ran out of ways of commenting your low amount of intelligence without violating a rule in many servers that lelbot joined",view=view)

                    if value == "Go down":
                        await scn.edit(content=f":hammer: {lelcube} :cat2:")
                        await msg.edit(view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":hole: {lelcube}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":hole:\n{lelcube}\n{void}\n:cyclone:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {void} {void} {void} :name_badge: :beginner:")
                        await asyncio.sleep(5)
                        await msg.edit(content="**You lost**\nescf1f2f3f4f5f6f7f8f9f10f11f12fnlockinsertprtscdelbackspace/\*\"'1!2@3#4$5%6¨7&8\*9(0)-_=+backspacenumlock-+tabqwertyuiop`´[{enter7home8up9pgupcapslockasdfghjklç^~]}4left56rightshift|\\zxcvbnm,<.>;:shift1end2down3pgdnctrlfnwindowsaltspacealtgrleftupdownright0ins,delenter",view=view)

                    if value == "Watch a tutorial":
                        await scn.edit(content=f":test_tube: :scientist: :iphone: {lelcube} :cat2:")
                        await msg.edit(view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Phone**\nhello guys today i'm [incomprehensible sounds]")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":test_tube: :scientist: {right_gun} :iphone: {lelcube} :cat2:")
                        await msg.edit(content="**You lost**\nTip: Always lower the volume of your phone when you're gonna watch a tutorial when you are in a flying castle full of people that want to kill you hold on that's too specific",view=view)

                    if value == "Become superlelcube":
                        amogus = Button(
                            style=ButtonStyle.blurple,
                            label="But I want to become superlelcube :(",
                            custom_id="retry_button",
                            emoji="🔄"
                        )

                        async def sussy(inter):
                            if pain.author.id == inter.author.id:
                                await msg.edit(content="**You lost**\nOk fine",view=None)
                                await asyncio.sleep(3)
                                await msg.edit(content="**Lelcube**\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{void} {void} :satellite_orbital:\n{void} {void} :fist:\n:test_tube: :scientist: {superlelcube} :cat2:")
                                await msg.edit(content="*super_epok_music.mp3*")
                                await asyncio.sleep(3)
                                await scn.edit(content=f":cyclone:\n{superlelcube} :cat2:")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{hellory5n}\n:chair: {void} {superlelcube}")
                                await asyncio.sleep(3)
                                await msg.edit(content="**hellory5n**\nWait how you got here like that")
                                await asyncio.sleep(3)
                                await msg.edit(content="**Superlelcube**\nI became superlelcube, a clone of myself that is powered by messages with lelcube.")
                                await asyncio.sleep(5)
                                await msg.edit(content="**Superlelcube**\nThere's so many lelcubes in messages that now I'm able of teleporting and other stuff.")
                                await asyncio.sleep(5)
                                await msg.edit(content="**hellory5n**\nOk.")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{hellory5n} {right_gun} {superlelcube}")
                                await msg.edit(content="** **")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{hellory5n}\n:fire: :fire: :fire: :fire: :fire: {superlelcube}")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{hellory5n}\n:chair:\n{void} {void} {void} {superlelcube}")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{superlelcube} {left_punch} {hellory5n}")
                                await asyncio.sleep(3)
                                await scn.edit(content=f"{superlelcube} :hand_splayed: {hellory5n} :door: {castle}")
                                await msg.edit(content="**hellory5n**\nNow you have 3 options.")
                                await asyncio.sleep(3)
                                await msg.edit(content="**hellory5n**\n1: Die")
                                await asyncio.sleep(3)
                                await msg.edit(content="**hellory5n**\n2: Continue")
                                await asyncio.sleep(3)
                                await msg.edit(content="**hellory5n**\nAnd 3: Give up.")
                                await asyncio.sleep(3)
                                await hellory5nfightlol(inter)
                            else:
                                await inter.send("You're not the author :P",ephemeral=True)

                        amogus.callback = sussy
                        microwave = View() 
                        microwave.add_item(amogus)
                        await scn.edit(content=f"{void} {void} :satellite_orbital:\n:test_tube: :scientist: {lelcube} :cat2:")
                        await msg.edit(content="**You lost**\nSTOP",view=microwave)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":test_tube: :scientist: {lelthink} :cat2:")
            await msg.edit(content="** **",view=theletterh)






        async def gaems(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = gaems
            view = View() 
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="hjyukl",
                max_values=1,
                options=[
                    SelectOption(label="Become superlelcube",emoji=superlelcube),
                    SelectOption(label="Do nothing",emoji=lelcube),
                    SelectOption(label="Play the first game that the stop store shows you",emoji="🙂"),
                    SelectOption(label="Ignore this guy",emoji="👍")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Become superlelcube":
                        await scn.edit(content=f":tv: :video_game: {sweathmm} {lelcube} :cat2:")
                        await msg.edit(content="**Lelcube**\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":tv: :video_game: {sweathmm} {lelcube} {left_gun} :cat2:")
                        await msg.edit(content="**You lost**\nWhy you're still trying",view=view)

                    if value == "Do nothing":
                        await scn.edit(content=f":tv: :video_game: {sweathmm} {lelcube} :cat2:")
                        await msg.edit(view=None)
                        await asyncio.sleep(60)
                        await msg.edit(content="**You lost**\nHow can a room full of married people be empty? There's not a single person there",view=view)

                    if value == "Ignore this guy":
                        await scn.edit(content=f":door:  {lelcube} :cat2:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(1)
                        await scn.edit(content=f":door: :satellite_orbital: {lelcube} :cat2:")
                        await msg.edit(content="**You lost**\naeiou",view=view)

                    if value == "Play the first game that the stop store shows you":
                        await scn.edit(content=f":tv: :video_game: {sweathmm} :iphone: {lelcube} :cat2:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(5)
                        await scn.edit(content=f":cat2: {right_punch} {button}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":iphone: {lelcube} :cat2: {void} :magic_wand: :robot:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":test_tube: :scientist: {lelcube} :cat2:")
                        await asyncio.sleep(3)
                        await lab(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":tv: :video_game: {sweathmm} {lelthink} :cat2:")
            await msg.edit(content="** **",view=theletterh)






        async def whysomanycomputerslol(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = whysomanycomputerslol
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="Hola",
                max_values=1,
                options=[
                    SelectOption(label="Become superlelcube",emoji=superlelcube),
                    SelectOption(label="Spawn a cat",emoji="🐈"),
                    SelectOption(label="Monke",emoji="🐒"),
                    SelectOption(label="Magically create a dragon",emoji="🐉")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Become superlelcube":
                        await scn.edit(content=f"{lelcube} :man: :desktop:")
                        await msg.edit(content="**Lelcube**\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {left_gun} :man: :desktop:")
                        await msg.edit(content="**You lost**\nSilence, please",view=view)

                    if value == "Monke":
                        await scn.edit(content=f":test_tube: {lelcube}")
                        await msg.edit(view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=":monkey: :man: :desktop:")
                        await asyncio.sleep(3)
                        await scn.edit(content=":monkey: :monkey: :desktop:")
                        await asyncio.sleep(3)
                        await scn.edit(content=":monkey: :monkey: :monkey:")
                        await asyncio.sleep(3)
                        await msg.edit(content="**:monkey: :monkey:**\n:monkey:",view=view)

                    if value == "Magically create a dragon":
                        await scn.edit(content=f":tophat:\n{lelcube} :magic_wand: :man: :desktop:")
                        await msg.edit(view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :dragon: :man: :desktop:")
                        await asyncio.sleep(3)
                        await scn.edit(content=":fire: :dragon: :man: :desktop:")
                        await msg.edit(content="**You lost**\nIt's impressive the ways you find to die",view=view)

                    if value == "Spawn a cat":
                        await scn.edit(content=f"{lelcube} :satellite: :man: :desktop:")
                        await msg.edit(view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :cat2: :man: :desktop:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":desktop: {left_punch} :cat2:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":door: :arrow_left: {lelcube} :cat2:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":level_slider: {lelcube} :cat2:")
                        await msg.edit(content="*elevator_music.mp3*")
                        await asyncio.sleep(3)
                        await gaems(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f"{lelthink} :man: :desktop:")
            await msg.edit(content="** **",view=theletterh)










        async def alotofboxesomguwuveryepok(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = alotofboxesomguwuveryepok
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="WUjjuhersrnmymo yujkoiw wi vwi ll doew/?",
                max_values=1,
                options=[
                    SelectOption(label="Become superlelcube",emoji=superlelcube),
                    SelectOption(label="Go to the hole",emoji="🕳"),
                    SelectOption(label="Open the box",emoji="📦"),
                    SelectOption(label="Punch everything lol",emoji="🤛")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Become superlelcube":
                        await msg.edit(content="**Lelcube**\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":hole: {superlelcube} :package: :package: :package:")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":hole: {superlelcube} {left_gun} :package: :package: :package:")
                        await msg.edit(content="**Box (don't ask which one lollllllllll)**\nBruh I was sleeping")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nTechnology.",view=view)
                    
                    if value == "Go to the hole":
                        await scn.edit(content=f"{lelcube}\n:arrow_down:\n:hole:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {void} {left_gun} :person_bald:")
                        await msg.edit(content="**You lost**\nIt's like going to the market then when you get there, you return to home",view=view)

                    if value == "Open the box":
                        await scn.edit(content=f"{lelcube} :point_right: :package:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Box**\nhey i was sleeping!")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {left_gun} :package:")
                        await msg.edit(content="**You lost**\nEveryone here has a gun, even boxes",view=view)

                    if value == "Punch everything lol":
                        await scn.edit(content=f"{lelcube} {right_punch} {void}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await whysomanycomputerslol(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":hole: {lelcube} :package: :package: :package:")
            await msg.edit(content="** **",view=theletterh)







        async def cafeteria(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = cafeteria
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="Whnthdrj tyyhouh uylwil l ldow?",
                max_values=1,
                options=[
                    SelectOption(label="Become superlelcube",emoji=superlelcube),
                    SelectOption(label="Steal the food",emoji="🍛"),
                    SelectOption(label="Hack the physics",emoji="🧑‍💻"),
                    SelectOption(label="Constantly say \"I refuse\"",emoji="❌")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Become superlelcube":
                        await msg.edit(content="**Lelcube**\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{superlelcube} {left_gun} :deaf_person: :curry:")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{hellory5n} {right_gun} {superlelcube} {left_gun} :deaf_person: :curry:")
                        await msg.edit(content="**You lost**\nBigger numbers are better, 2 people that want to shoot you is better than 1!",view=view)
                    
                    if value == "Steal the food":
                        await scn.edit(content=f"{left_gun} :deaf_person: {lelcube} :curry:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":deaf_person: {right_gun} {lelcube} :curry:")
                        await msg.edit(content="**You lost**\nYe this didn't really help",view=view)

                    if value == "Hack the physics":
                        await scn.edit(content=f"{lelcube} :computer: {left_gun} :deaf_person: :curry:")
                        await msg.edit(content="**Lelcube**\nI'm gonna hack physics!",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube}\n:arrow_down:\n{void}\n{void}\n:mountain:")
                        await msg.edit(content="**You lost**\nOops",view=view)

                    if value == "Constantly say \"I refuse\"":
                        irefuse = "**Lelcube**\nI refuse"
                        await msg.edit(content=irefuse,view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Michael**\nYou are *that* idiot?? That will never work! *shoots*")
                        await asyncio.sleep(3)
                        await msg.edit(content=irefuse)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :person_bald: {sweatgun} :man:")
                        await msg.edit(content="**Sweatgun**\nHEY WHAT ARE YOU DOING YOU'RE GONNA DIE")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\n***__I refuse__***")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube}\n:cup_with_straw:\n:chair: {void}")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":bricks:\n:fist:\n{lelcube}")
                        await asyncio.sleep(3)
                        await alotofboxesomguwuveryepok(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f"{lelcube} {left_gun} :deaf_person: :curry:")
            await msg.edit(content="**Michael (deaf person)**\nHEY WHAT THE FANCADE ARE YOU DOING",view=theletterh)










        async def hellory5n_defender(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = hellory5n_defender
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="W h a t   y o u   w i l l   d o ?",
                max_values=1,
                options=[
                    SelectOption(label="Install Doors XP",emoji="💿"),
                    SelectOption(label="Ask who is sweatcube",emoji="👤"),
                    SelectOption(label="Magically create 20000 turtles",emoji="🐢"),
                    SelectOption(label="Make a music",emoji="🎶")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Install Doors XP":
                        await scn.edit(content=f"{lelcube} :cd: :desktop: {sweatcube}")
                        await msg.edit(content="**Lelcube**\nHey, can I install Doors XP?",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatcube**\nSure")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{sweatcube} {void} :desktop: {lelcube}")
                        await msg.edit(content="*title.wma*")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatcube**\nhold on")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nWhat is the limit of dumbness?",view=view)
                    
                    if value == "Ask who is sweatcube":
                        await scn.edit(content=f"{lelcube} {void} :desktop: {sweatcube}")
                        await msg.edit(content="**Lelcube**\nWho are you?",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatcube**\nI am...")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {void} :desktop: {lelcube}")
                        await msg.edit(content="**Lelcube?**\nYOU!!!")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nTop 10 biggest plot twists",view=view)

                    if value == "Make a music":
                        await scn.edit(content=f":headphones:\n{lelcube} :iphone:")
                        await msg.edit(content="*epok_music.mp3*",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":headphones:\n{lelcube} :iphone: :desktop: {sweatcube}")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatcube**\nThat's a nice music, I wonder what is playing it")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatcube**\nOh")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nHey, at least you made a nice music!",view=view)
                        
                    if value == "Magically create 20000 turtles":
                        await scn.edit(content=f"{lelcube} :ballot_box: :desktop: {sweatcube}")
                        await msg.edit(content="**Lelcube**\nImma create a bunch of turtles",view=None)
                        await asyncio.sleep(5)
                        await msg.edit(content="**Sweatcube**\n??????????")
                        await asyncio.sleep(1)
                        await scn.edit(content=":turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle: :turtle:")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :level_slider:")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\nThe collision is quite buggy")
                        await asyncio.sleep(3) #man this program sleeps a lot
                        await msg.edit(content="*elevator_music.mp3*")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :curry: :deaf_person: {void}")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await cafeteria(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f"{lelthink} {void} :desktop: {sweatcube}")
            await msg.edit(content="** **",view=theletterh)






        async def thecookestbotroomevermadeomgveryepok(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = thecookestbotroomevermadeomgveryepok
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Use a rocket",emoji="🚀"),
                    SelectOption(label="Ask what is 0 divided by 0",emoji="❔"),
                    SelectOption(label="Punch the bots",emoji="🤛"),
                    SelectOption(label="Build a skyscraper",emoji="🔧")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Ask what is 0 divided by 0":
                        await msg.edit(content="**Bot (don't ask which one)**\nImagine that you have 0 cookis, and you split them evenly among 0 friends.",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Bot (don't ask which one)**\nHow many cookis each person get?")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Bot (don't ask which one)**\nSee? It doesn't make sense.")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Bot (don't ask which one)**\nAnd cooki monster is sad because there are no cookis!")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Bot (don't ask which one)**\nAnd you are sad because you have no friends!")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nOh wow, this escalated quickly",view=view)
                    
                    if value == "Punch the bots":
                        await scn.edit(content=f":robot: :robot: {left_punch} {lelcube}")
                        await msg.edit(content="*epok_music_ues.mp3*",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":robot: {right_gun} {left_punch} {lelcube}")
                        await msg.edit(content="**You lost**\nGet a mechanical arm",view=view)

                    if value == "Build a skyscraper":
                        await scn.edit(content=f":robot: :robot: {lelcube}")
                        await msg.edit(content="**You lost**\nNo, I won't say anything funny just cuz you made something infinitely stupid",view=view)
                        
                    if value == "Use a rocket":
                        await scn.edit(content=f":robot: :robot: {lelcube} :rocket:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {void} :bricks:\n:rocket: :arrow_right: :bricks:")
                        await asyncio.sleep(3)
                        await hellory5n_defender(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":robot: :robot: {lelthink}")
            await msg.edit(content="ertytreshrdtjrehrj",view=theletterh)








        async def hellory5n_room(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = hellory5n_room
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Throw the moneybag",emoji="🚀"),
                    SelectOption(label="Watch stuff",emoji="👀"),
                    SelectOption(label="Give the money",emoji="🤝"),
                    SelectOption(label="Scream",emoji="😱")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Throw the moneybag":
                        await scn.edit(content=f"{hellory5n} :arrow_left: :moneybag:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{hellory5n} {right_gun} {lelcube}")
                        await msg.edit(content="**You lost**\nAre you trying to make a death speedrun? A normal person wouldn't do this. Oh, considering how dumb you are, this makes a lot of sense",view=view)
                    
                    if value == "Watch stuff":
                        await scn.edit(content=f":tv: {hellory5n} {sweatgun} {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":timer:")
                        await msg.edit(content="*10 minutes later...*")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{hellory5n} {right_gun} {lelcube}")
                        await msg.edit(content="**You lost**\nI need a new word to describe your insane amount of dumbness",view=view)

                    if value == "Scream":
                        await scn.edit(content=f":tv: {hellory5n} {sweatgun} {lelcube}")
                        await msg.edit(content="**Lelcube**\nAAAAAAAAAAAAAAAAAAAAAAAAA",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{hellory5n} {right_gun} {lelcube}")
                        await msg.edit(content="**You lost**\nWhy did the worker get fired from the orange juice factory? Lack of concentration.",view=view)
                        
                    if value == "Give the money":
                        await scn.edit(content=f":tv: {hellory5n} {sweatgun} :moneybag: {lelcube}")
                        await msg.edit(content="**Lelcube**\nI want to give money to you guys!",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**hellory5n**\nWait, by analyzing the 1337th pixel of this moneybag, that is *our* money!")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatgun**\nIdc i want mone lollllll")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{button} {void} {void} {sweatgun} :moneybag: {lelcube}")
                        await msg.edit(content="**Lelcube**\nOk imma only give tha mone if you press that button")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatgun**\nOk")
                        await scn.edit(content=f":wave: {lelcube}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{button} {left_punch} {sweatgun}")
                        await msg.edit(content="**hellory5n**\nHEY WHAT ARE YOU DOINGGGGGGGGGGGG")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You won**\nCook")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube}\n:arrow_down:\n{void}\n{void}\n:mountain:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube}\n:helicopter:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{sweatsmileHD} {lelcube}")
                        await msg.edit(content="**Sweatsmile HD**\nᴠᴇʀʏ ᴇᴘᴏᴋ")

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":tv: {hellory5n} {sweatgun} :moneybag: {lelthink}")
            await msg.edit(content=":arrow_down: look at dis",view=theletterh)








        async def computer_room(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = computer_room
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Ask to use the computer",emoji="🖥️"),
                    SelectOption(label="Eat pretty delicious stuff",emoji="😋"),
                    SelectOption(label="Throw watermelons",emoji="🍉"),
                    SelectOption(label="Play ping pong",emoji="🏓")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Ask to use the computer":
                        await scn.edit(content=f":desktop: {sweathmm} :desktop: {sweatidkanymore} {lelcube}")
                        await msg.edit(content="**Lelcube**\nCan I use the computer?",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweathmm**\nI'M LITERALLY FIXING A PROBLEM THAT CAN DESTROY THE ENTIRE CASTLE ARE YOU CRAZY\n\n**Sweatidkanymore**\nWait, isn't him lelcube?")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You lost**\nsmort:brain:",view=view)
                    
                    if value == "Throw watermelons":
                        await scn.edit(content=f":desktop: :arrow_left: :watermelon: {lelcube}")
                        await msg.edit(content="***EPOK_MUSIC.MP3***",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":boom: {sweathmm}")
                        await msg.edit(content="**Sweathmm**\nOH NOOOOOOOOOOOOO THE CASTLE WIL LL EPLOXLDO EDJHDKFLKGHK")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You lost**\nI'm speechless- wait...")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":telephone: :grey_question:")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{hellory4n} :telephone: :grey_question:")
                        await msg.edit(content="**hellory4n**\nHello!")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost guy**\nHi, can I give the \"dumbest person\" trophy to lelcube?")
                        await asyncio.sleep(3)
                        await msg.edit(content="**hellory4n**\nok")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":grey_question:")
                        await msg.edit(content="**You lost guy**\nAnd the dumbest person trophy goes to...")
                        await asyncio.sleep(3)
                        await msg.edit(content=f"**You lost guy**\nLELCUBE!!!")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":clap: {sweatsmileHD} :clap: :deaf_person: :clap: :person_bald:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":trophy: {lelcube}")
                        await msg.edit(content="**You lost**\nAt least you got a trophy for being the dumbest person!",view=view)

                    if value == "Play ping pong":
                        await scn.edit(content=f":desktop: {sweathmm} :desktop: {sweatidkanymore} {lelcube}")
                        await msg.edit(content="**Lelcube**\nHey let's play ping pong",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatidontknowanymore**\nYes!")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{sweatidkanymore} :ping_pong: {lelcube}")
                        await msg.edit(content="**You lost**\nWho doesn't like ping pong?",view=view)
                        
                    if value == "Eat pretty delicious stuff":
                        await scn.edit(content=f":fries: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{sweathmm} :fries: {lelcube}")
                        await msg.edit(content="**Sweathmm**\nHi can I eat your fries")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\nOnly if you allow me go to the next room without me commiting ded")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweathmm**\nOk")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":level_slider: :wastebasket: {lelcube}")
                        await msg.edit(content="**Lelcube**\nThis is trash")
                        await asyncio.sleep(3)
                        await hellory5n_room(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":desktop: {sweathmm} :desktop: {sweatidkanymore} {lelthink}")
            await msg.edit(content="**Sweathmm**\nOh no, the program is broken!\n\n**Sweatidkanymore**\nWe need to fix it fast before the entire castle breaks!",view=theletterh)







        async def electrical(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = electrical
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Manage energy",emoji="🧠"),
                    SelectOption(label="Create an entire OS from scratch",emoji="💻"),
                    SelectOption(label="Shutdown power",emoji="🔌"),
                    SelectOption(label="Destroy stuff",emoji="💥")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Manage energy":
                        await scn.edit(content=castle)
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You lost**\nSo smart!",view=view)
                    
                    if value == "Create an entire OS from scratch":
                        await scn.edit(content=f":keyboard: :hammer: {lelcube}")
                        await msg.edit(content="**Lelcube**\n*programming*",view=None)
                        await asyncio.sleep(10)
                        await msg.edit(content="**You lost**\nYou know this one? A robot and a human walk into a bar *`Message only available for WhatsApp 2 userss`*",view=view)

                    if value == "Shutdown power":
                        await scn.edit(content=f":electric_plug: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle}\n:arrow_down:{void}\n{void}\n:volcano:")
                        await msg.edit(content="**You lost**\nWe do a large amount of trolling",view=view)
                        
                    if value == "Destroy stuff":
                        await scn.edit(content=f":ant: :hammer: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":level_slider: {lelcube} :clock10:")
                        await msg.edit(content="*elevator music*")
                        await asyncio.sleep(3)
                        await computer_room(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":electric_plug: :control_knobs: :control_knobs: :control_knobs: {lelthink}")
            await msg.edit(content="** ** ",view=theletterh)







        async def bank(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = bank
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="ono you don't have card wat u will do",
                max_values=1,
                options=[
                    SelectOption(label="Do nothing",emoji="🙅"),
                    SelectOption(label="Play RPS",emoji="👊"),
                    SelectOption(label="Throw a bunch of bombs",emoji="💣"),
                    SelectOption(label="Plant trees",emoji="🌲")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Do nothing":
                        await scn.edit(content=f":moneybag: :robot: {lelcube}")
                        await msg.edit(content="(the game didn't broke)",view=None)
                        await asyncio.sleep(60)
                        await msg.edit(content="**You lost**\nI wish there was an achievements system so I could give you one",view=view)
                    
                    if value == "Play RPS":
                        await scn.edit(content=f":moneybag: :robot: :scissors: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":moneybag: :robot: {right_gun} :scissors: {lelcube}")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nThey released a new RPS update???", view=view)

                    if value == "Throw a bunch of bombs":
                        await scn.edit(content=f":moneybag: :robot: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: :bomb: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You lost**\nlelbot story mode speedrun any%",view=view)
                        
                    if value == "Plant trees":
                        await scn.edit(content=f":moneybag: :robot: :evergreen_tree: {lelcube} :thumbsup:")
                        await msg.edit(content="**Bot**\neiuryb4 ie ty48t8ibu4nwiuteyh4iwuoeurui4jweuygrhi94ywgeuyt8y74",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Bot**\nI HATE TREEESSSSSSSSS THEY EXPLODED ALL OF MY SANDWICHES AAAAAAAAAA FIOSRKJIIJRIUGHJSROI")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":moneybag: :boom: :evergreen_tree: {lelcube}")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":moneybag: {void} :evergreen_tree: :hammer: {lelcube}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":moneybag: {lelcube} :thumbsup:")
                        await asyncio.sleep(3)
                        await electrical(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":moneybag: :robot: {lelthink}")
            await msg.edit(content="**Bot**\nInsert a card.",view=theletterh)






        async def super_gun_room(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = super_gun_room
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="Which super mega ultra gun you'll use?",
                max_values=1,
                options=[
                    SelectOption(label="Super laser machine",emoji="📡"),
                    SelectOption(label="Ultra shooting thing 3000",emoji=left_gun),
                    SelectOption(label="Boom collection",emoji="💣"),
                    SelectOption(label="Mega musical pain",emoji="🎸")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Super laser machine":
                        await scn.edit(content=f":satellite: {button} {left_punch} {lelcube} :joystick:")
                        await msg.edit(content="***ULTRA_INTENSE_EPOK_MUSIC.MP3***",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void}{castle}\n:satellite:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void}:boom:\n:satellite:")
                        await msg.edit(content="**You lost**\nCongrats! You did it! :clap: :clap: :clap:",view=view)
                    
                    if value == "Ultra shooting thing 3000":
                        await scn.edit(content=f"{left_gun} :joystick: {lelcube}")
                        await msg.edit(content="***SUPER_MEGA_ULTRA_INTENSE_EPOK_MUSIC_THAT_TOOK_700_YEARS_TO_MAKE.MP3***",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle} {left_gun}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{left_gun}\n{castle}")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":helicopter: {void} {left_gun} {castle}")
                        await msg.edit(content="**You lost**\nNice aim! :clap:",view=view)

                    if value == "Mega musical pain":
                        await scn.edit(content=f":guitar: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":fire: :loudspeaker: :guitar: {lelcube} :loudspeaker: :fire:")
                        await msg.edit(content="***INSANELY_INSANE_AND_GOOD_MUSIC.MP3***")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":anger: {castle} :anger:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":anger: :earth_americas: :anger: {left_gun} :new_moon_with_face:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":guitar: {lelcube} {left_gun} {hellory5n}")
                        await msg.edit(content="**You lost**\nCongrats! Your music sucks so much that hellory5n came here to kill you! :clap:",view=view)
                        
                    if value == "Boom collection":
                        await scn.edit(content=f"{button} {left_gun} {lelcube}")
                        await msg.edit(content="***SUPER_SUPER_SUPER_SUPER_SUPER_SUPER_EPICCC_MUSICCCCCCCC.MP3***",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle}\n:bomb:\n{void}\n{void}\n{void}\n{void}\n{void}\n:mountain:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :desktop:")
                        await msg.edit(content="**Lelcube**\nwas dis?")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle}\n{void}\n{void}\n{void}\n{void}\n{void}\n:bomb:\n:mountain:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle}\n{void}\n{void}\n{void}\n{void}\n:arrow_up:\n:bomb:\n:mountain:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":rotating_light: {lelcube} :rotating_light:")
                        await msg.edit(content=f"**Lelcube**\nOH NO WHAT HAVE I DONE\n\n**Castle security system**\nWARNING: BOMBS ARE GETTING CLOSE TO THE CASTLE!!!!!!!!!!!!!!! DO SOMETHING ABOUT IT!!!!!!!!!!!!!!!111")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :arrow_right: :window:")
                        await msg.edit(content="**Castle security system**\nWARNING: BOMBS ARE GETTING CLOSE TO THE CASTLE!!!!!!!!!!!!!!! DO SOMETHING ABOUT IT!!!!!!!!!!!!!!!111")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle}\n{void}{lelcube}\n{void}\n{void}:helicopter:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":iphone: {sweatsmileHD}")
                        await msg.edit(content=f"*Sweatsmile HD making a new Drive Mad Kit 2*")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube's phone**\n**__`NEVER GONNA GIVE YOU UP\nNEVER GONNA LET YOU DOWN\nNEVER GONNA RUN AROUND AND DESERT YOU\nNEVER GONNA MAKE YOU CRY\nNEVER GONNA SAY GOODBYE\nNEVER GONNA TELL A LIE AND HURT YOU`__**")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatsmile HD**\nOK OK OK")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube}\n:helicopter:")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {sweatsmileHD}")
                        await msg.edit(content="**Sweatsmile HD**\nOk, the castle will explode?")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\nYes, I hope!")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":fire: :fire: {hellory5n} :fire: :fire:")
                        await msg.edit(content="**hellory5n**\nNOOOOOOOOOOOOOOOOOOOOO")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await asyncio.sleep(3)
                        await scn.edit(content=":boom:")
                        await msg.edit(content="**You won!**\n...somehow")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":boom:\n{void}:helicopter:")
                        await msg.edit(content=f"**Sweatsmile HD**\nYay, it really exploded!")
                        await asyncio.sleep(5)
                        await msg.edit(content=f"Congrats {inter.author.mention}! :clap:")

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":satellite: {left_gun} :bomb: :guitar: {lelthink}")
            await msg.edit(content="** **",view=theletterh)







        async def server(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = server
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Look what's on the server",emoji="👀"),
                    SelectOption(label="Destroy everything",emoji="🔨"),
                    SelectOption(label="Play games on the supercomputers",emoji="🎮"),
                    SelectOption(label="Just go to another room",emoji="🏃")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Look what's on the server":
                        await scn.edit(content=f":file_cabinet: :desktop: {lelcube}")
                        await msg.edit(content=f"**Lelcomputer**\nStarting lelcubeOS 39 for servers...",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content=f"**Welcome!**\n\n**Apps**\n> :file_folder: Lelfinder\n> :keyboard: Lelterminal\n> :file_cabinet: Leldatabase\n> :cloud: Lelcloud\n> :arrows_counterclockwise: Restart\n> :octagonal_sign: Shutdown\n> :mag: Search")
                        await asyncio.sleep(3)
                        await msg.edit(content=f":file_folder: Lelfinder\n\n/home/Server3/\n> :page_facing_up: Documents\n> :arrow_down: Downloads\n> :frame_photo: Images\n> :musical_note: Musics\n> :film_frames: Videos")
                        await asyncio.sleep(3)
                        await msg.edit(content=f"/home/Server3/Documents/\n\n> :file_cabinet: database.leldb\n> :page_facing_up: HOW_TO_DESTROY_CASTLE.txt")
                        await asyncio.sleep(3)
                        await msg.edit(content=f":notepad_spiral: Lelnotepad\nscream \"EMERGENCY EVERYONE RUN WE NEED TO GET OUT OF THE CASTLEEEEEEEEEE\"")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\nEMERGENCY EVERYONE RUN WE NEED TO GET OUT OF THE CASTLEEEEEEEEEEEE")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":file_cabinet: :desktop: {lelcube} {sweatgun}")
                        await msg.edit(content="**You lost**\nuwu he's gonna shoot you",view=view)
                    
                    if value == "Destroy everything":
                        await scn.edit(content=f":file_cabinet: :file_cabinet: :boom: {left_gun} {lelcube}")
                        await msg.edit(content=f"** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":file_cabinet: :file_cabinet: :boom: {left_gun} {lelcube} {sweatgun}")
                        await msg.edit(content="**You lost**\n**__B O O M__**",view=view)

                    if value == "Just go to another room":
                        await scn.edit(content=f":door: {void} {void} {void} {lelcube}")
                        await asyncio.sleep(1)
                        await scn.edit(content=f":door: :fire: :boom: :fire: :boom: :fire: {lelcube}")
                        await msg.edit(content="**You lost**\nThe door doesn't like you",view=view)
                        
                    if value == "Play games on the supercomputers":
                        await scn.edit(content=f":file_cabinet: :desktop: :video_game: {lelcube}")
                        await msg.edit(content="**Lelcube**\nCan't wait to play cyberlel 2077 here!",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":file_cabinet: :hole: :video_game: {lelcube}")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube}\n:arrow_down:\n:hole:")
                        await asyncio.sleep(3)
                        await super_gun_room(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":door: :file_cabinet: :file_cabinet: :file_cabinet: {left_gun} {lelthink}")
            await msg.edit(content="** **",view=theletterh)







        async def gun_room(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = gun_room
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Insert credit card details",emoji="📥"),
                    SelectOption(label="Ask a hamburger",emoji="🍔"),
                    SelectOption(label="Rickroll the bot",emoji="🎤"),
                    SelectOption(label="Steal a card",emoji="🥷"),
                    SelectOption(label="Go to another room",emoji="🏃")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Insert credit card details":
                        await scn.edit(content=f":toolbox: :robot: :credit_card: {lelcube}")
                        await msg.edit(content=f"**Lelcube**\nHey here's my credit card",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":toolbox: :robot: {void} {lelcube}")
                        await msg.edit(content="**Bot**\nThank you!")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nBots are evolving, this one likes money!",view=view)
                    
                    if value == "Rickroll the bot":
                        await scn.edit(content=f":toolbox: :robot: {lelcube}")
                        await msg.edit(content="**Lelcube**\nWe're no strangers to love",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":toolbox: :robot: {right_gun} {lelcube}")
                        await msg.edit(content="**You lost**\nBots are evolving, this one hates rickrolls!",view=view)

                    if value == "Steal a card":
                        await scn.edit(content=f"{lelcube} {void} {void}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {void} {void} :woman_beard:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :arrow_left: :credit_card: :woman_beard:")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":toolbox: :robot: :credit_card: {lelcube}")
                        await msg.edit(content="**Lelcube**\nHere is ma card")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Bot**\nWhat?! Steve is not on the room for brainless people?????")
                        await asyncio.sleep(3)
                        await msg.edit(content="**You lost**\nBots are evolving, this one thinks you are Steve!",view=view)
                        
                    if value == "Go to another room":
                        await bank(inter)
                    
                    if value == "Ask a hamburger":
                        await scn.edit(content=f":toolbox: :robot: {lelcube}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(5)
                        await msg.edit(content="**Bot**\nTraceback (most recent call last):\n  File \"bot.ues\", line 69, in \"ues\"\nBotError: help what me supposed to do when tha user wants to get guns and it asks for a hamburger")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":toolbox: :boom: {lelcube}")
                        await asyncio.sleep(3)
                        await server(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":toolbox: :robot: {lelthink}")
            await msg.edit(content="**Bot**\nInsert your card to access guns.",view=theletterh)








        async def right_path_start(inter):
            nonlocal scn
            nonlocal msg

            again = Button(
                style=ButtonStyle.blurple,
                label="Again",
                custom_id="retry_button",
                emoji="🔄"
            )
            again.callback = right_path_start
            view = View()
            view.add_item(again)

            ues = Select(
                custom_id="ues",
                placeholder="How you will open tha door",
                max_values=1,
                options=[
                    SelectOption(label="Use a key",emoji="🔑"),
                    SelectOption(label="Shoot the door",emoji=left_gun),
                    SelectOption(label="Delete the door object",emoji="💥"),
                    SelectOption(label="High-speed train",emoji="🚄")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Use a key":
                        await scn.edit(content=f":door: {void} {lelcube}")
                        await msg.edit(content="**You lost**\nBut what key?",view=view)
                    
                    if value == "Shoot the door":
                        await scn.edit(content=f":door: :gun: {lelcube}")
                        await msg.edit(content="**Lelcube**\nI'm gonna destroy this door!",view=None)
                        await asyncio.sleep(5)
                        await msg.edit(content="**Lelcube**\nwhat")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :iphone:")
                        await msg.edit(content="**eyePhone**\nCalling...")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":joystick: {sweatsmileHD} {void} :iphone:")
                        await msg.edit(content="**eyePhone**\nLelcube is calling you!")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} :telephone: {sweatsmileHD}")
                        await msg.edit(content="**Lelcube**\nYou gave me a toy gun")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatsmile HD**\nWhat the")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatsmile HD**\nLike, can't you just steal a gun?")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelcube**\nI need a gun to destroy a locked door")
                        await asyncio.sleep(3)
                        await msg.edit(content="**Sweatsmile HD**\nOk, fine, gonna you give you a real gun!")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{castle} {void} {void} {void} {left_gun} :helicopter:\n{void} {void} {void} :arrow_lower_left:")
                        await msg.edit(content="**You lost**\nnice",view=view)

                    if value == "High-speed train":
                        await scn.edit(content=f"{void} {void} {lelcube}\n:door: {void} 🚄")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} {void} {lelcube}\n{left_gun} :boom: 🚄")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":moneybag: :moneybag: {lelcube}\n:moneybag: :boom: 🚄")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} {void} {lelcube}\n:person_standing: :desktop: 🚄")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} {void} {lelcube}\n:level_slider: :boom: 🚄")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":video_game: :video_game: {lelcube}\n:video_game: :boom: 🚄")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":test_tube: :test_tube: {lelcube}\n:scientist: :boom: 🚄")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":radio: :control_knobs: {lelcube}\n:level_slider: :boom: 🚄")
                        await msg.edit(content="**Lelcube**\nOH WAIT I DESTROYED THE REACTOR NOOOOOOOOOOOOOOO")
                        await asyncio.sleep(3)
                        await scn.edit(content=castle)
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":boom:")
                        await msg.edit(content="**You lost**\nWell, you destroyed the castle, so you technically won even tho you will fall into a mountain?",view=view)
                
                    if value == "Delete the door object":
                        await scn.edit(content=f":door: :computer: {lelcube}")
                        await msg.edit(content="**Lelptop**\n:balloon: Object manager\n\nroom=outside_of_the_castle.room\n> lelcube.obj\n> sweatsmileHD.obj\n> door.obj\n> lelptop.obj\n> helicopter\n> castle.obj",view=None)
                        await asyncio.sleep(3)
                        await msg.edit(content="**Lelptop**\n:balloon: Object manager\n\nobj=door.obj\n> Delete\n> Position\n> More")
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{void} :computer: {lelcube}")
                        await msg.edit(content="** **")
                        await asyncio.sleep(3)
                        await scn.edit(content=f":toolbox: :robot: {lelcube}")
                        await asyncio.sleep(3)
                        await gun_room(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            theletterh = View()
            theletterh.add_item(ues)
            await scn.edit(content=f":door: {void} {lelthink}")
            await msg.edit(content="**Lelcube**\nono tha door locked",view=theletterh)





        async def bathroom(inter):
            nonlocal scn
            nonlocal msg

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Toilet",emoji="🚽"),
                    SelectOption(label="Take a shower immediately",emoji="🚿"),
                    SelectOption(label="Go down",emoji="⬇️")
                ]
            )

            async def abcd1(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Toilet":
                        again = Button(
                            style=ButtonStyle.blurple,
                            label="Again",
                            custom_id="retry_button",
                            emoji="🔄"
                        )
                        again.callback = bathroom
                        view = View()
                        view.add_item(again)

                        await scn.edit(content=f"{lelcube}\n:toilet:")
                        await msg.edit(content="**You lost**\nare you kidding me",view=view)
                    
                    if value == "Take a shower immediately":
                        again = Button(
                            style=ButtonStyle.blurple,
                            label="Again",
                            custom_id="retry_button",
                            emoji="🔄"
                        )
                        again.callback = bathroom
                        view = View()
                        view.add_item(again)

                        await scn.edit(content=f":shower:\n{lelcube}")
                        await msg.edit(content="**You lost**\nOk :thumbsup:",view=view)

                    if value == "Go down":
                        await scn.edit(content=f"{lelcube}\n:arrow_down:\n:toilet:")
                        await msg.edit(view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":man_bald: {left_gun} :deaf_person: {lelcube}")
                        await asyncio.sleep(3)

                        again = Button(
                            style=ButtonStyle.blurple,
                            label="Again",
                            custom_id="retry_button",
                            emoji="🔄"
                        )
                        again.callback = bathroom
                        view = View()
                        view.add_item(again)

                        await scn.edit(content=f":man_bald: :deaf_person: {right_gun} {lelcube}")
                        await msg.edit(content="**You lost**\nasdfghjklñ.",view=view)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd1
            view = View()
            view.add_item(ues)
            await scn.edit(content=f"{lelthink} :toilet: :shower:")
            await msg.edit(content="*very_intense_epok_music.mp3*",view=view)
        


        async def path_chooser_3000(inter):
            nonlocal scn
            nonlocal msg

            ues = Select(
                custom_id="ues",
                placeholder="What you will do?",
                max_values=1,
                options=[
                    SelectOption(label="Top",emoji="⬆️"),
                    SelectOption(label="Left",emoji="⬅️"),
                    SelectOption(label="Right",emoji="➡️")
                ]
            )

            async def abcd2(inter):
                if pain.author.id == inter.author.id:
                    value = ues.values[0]
                    if value == "Top":
                        await scn.edit(content=f":helicopter:\n{lelcube}\n:arrow_down:\n{castle}")
                        await msg.edit(content="*epok_tension_music_thing.mp3*",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"{lelcube} {right_punch} :door:")
                        await asyncio.sleep(3)
                        await bathroom(inter)
                    if value == "Right":
                        await scn.edit(content=f"{castle} :arrow_left: {lelcube} :helicopter:")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f"🚪 {void} {lelcube}")
                        await asyncio.sleep(3)
                        await right_path_start(inter)
                    if value == "Left":
                        await scn.edit(content=f":helicopter: {lelcube} :arrow_right: {castle}")
                        await msg.edit(content="** **",view=None)
                        await asyncio.sleep(3)
                        await scn.edit(content=f":window: {left_punch} {lelcube}")
                        await asyncio.sleep(3)
                        await thecookestbotroomevermadeomgveryepok(inter)

                else:
                    await inter.send("You're not the author :P",ephemeral=True)
            
            ues.callback = abcd2
            view = View()
            view.add_item(ues)
            await scn.edit(content=f":european_castle: {sweatsmileHD} {lelthink}")
            await msg.edit(content="**Sweatsmile HD**\nWhere you'll jump?",view=view)







        async def intro(inter):
            nonlocal msg
            nonlocal scn

            await scn.edit(content=":helicopter:")
            await msg.edit(content="** **",components=[])
            await asyncio.sleep(3)
            await scn.edit(content=f"{sweatsmileHD} {lelcube}")
            await msg.edit(content="**Lelcube**\ny mii on helicopter")
            await asyncio.sleep(3)
            await scn.edit(content=":european_castle:")
            await msg.edit(content="**Sweatsmile HD**\nRecently, hellory5n built a huge castle. It'll be used to help him take over the world.")
            await asyncio.sleep(3)
            await msg.edit(content="**Sweatsmile HD**\nThis castle will have all of his allies, and extremely powerful weapons.")
            await asyncio.sleep(3)
            await scn.edit(content=f"{sweatsmileHD} {lelcube}")
            await msg.edit(content="**Sweatsmile HD**\nWe need to stop him.")
            await asyncio.sleep(3)
            await path_chooser_3000(inter)








        yes = Button(
            style=ButtonStyle.blurple,
            label="Yes",
            custom_id="yes_button"
        )
        no = Button(
            style=ButtonStyle.blurple,
            label="No",
            custom_id="no_button"
        )

        yes.callback = intro
        no.callback = path_chooser_3000
        view = View()
        view.add_item(yes)
        view.add_item(no)
        await msg.edit(view=view)
    
    await story()

@client.slash_command(description="Get a random image")
async def image(inter):
    with open("images.txt",'r') as f:
        ues = f.read()
    
    stuff = ues.split("\n")
    #banana = stuff[index]
    banana = random.choice(stuff)
    m = banana.split("&&")
    embed = discord.Embed(title=m[0], color=0xFECC4D)
    embed.set_image(url=m[1])
    await inter.send(embed=embed)

@client.command(aliases=['image'])
async def image2(ctx):
    with open("images.txt",'r') as f:
        ues = f.read()
    
    stuff = ues.split("\n")
    #banana = stuff[index]
    banana = random.choice(stuff)
    m = banana.split("&&")
    embed = discord.Embed(title=m[0], color=0xFECC4D)
    embed.set_image(url=m[1])
    await ctx.send(embed=embed)

@client.slash_command(description="Give a cake")
async def cake(inter, someone:str):
    """
    Parameters
    ----------
    someone: Who will get tha cake
    """
    credits = "If you're seeing this text then something has gone wrong"
    image = "https://cdn.discordapp.com/attachments/811051988992524299/950044067444686848/emoji.png"
    index = random.randint(1,50)

    if index == 1:
        credits="Photo by American Heritage Chocolate on Unsplash"
        image="https://images.unsplash.com/photo-1588195538326-c5b1e9f80a1b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=750&q=80"
    if index == 2:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1562440499-64c9a111f713?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 3:
        credits="Photo by Alexandra Gornago on Unsplash"
        image="https://images.unsplash.com/photo-1535141192574-5d4897c12636?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=688&q=80"
    if index == 4:
        credits="Photo by Anthony Espinosa on Unsplash"
        image="https://images.unsplash.com/photo-1571115177098-24ec42ed204d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 5:
        credits="Photo by David Holifield on Unsplash"
        image="https://images.unsplash.com/photo-1578985545062-69928b1d9587?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8Y2FrZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=700&q=60"
    if index == 6:
        credits="Photo by kaouther djouada on Unsplash"
        image="https://images.unsplash.com/photo-1602351447937-745cb720612f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=686&q=80"
    if index == 7:
        credits="Photo by Katie Rosario on Unsplash"
        image="https://images.unsplash.com/photo-1621303837174-89787a7d4729?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=736&q=80"
    if index == 8:
        credits="Photo by Annie Spratt on Unsplash"
        image="https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=936&q=80"
    if index == 9:
        credits="Photo by American Heritage Chocolate on Unsplash"
        image="https://images.unsplash.com/photo-1586985289688-ca3cf47d3e6e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 10:
        credits="Photo by Swapnll Dwivedi on Unsplash"
        image="https://images.unsplash.com/photo-1542826438-bd32f43d626f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=992&q=80"
    if index == 11:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1558301211-0d8c8ddee6ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=936&q=80"
    if index == 12:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1562777717-dc6984f65a63?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 13:
        credits="Photo by Karly Gomez on Unsplash"
        image="https://images.unsplash.com/photo-1488477304112-4944851de03d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 14:
        credits="Photo by Slashio Photography on Unsplash"
        image="https://images.unsplash.com/photo-1627834377411-8da5f4f09de8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=701&q=80"
    if index == 15:
        credits="Photo by Slashio Photography on Unplash"
        image="https://images.unsplash.com/photo-1622896784083-cc051313dbab?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 16:
        credits="Photo by Heather Barnes on Unsplash"
        image="https://images.unsplash.com/photo-1559620192-032c4bc4674e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=729&q=80"
    if index == 17:
        credits="Photo by Kim Daniels on Unsplash"
        image="https://images.unsplash.com/photo-1560180474-e8563fd75bab?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 18:
        credits="Photo by Will Echols on Unsplash"
        image="https://images.unsplash.com/photo-1517427294546-5aa121f68e8a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80"
    if index == 19:
        credits="Photo by Natallia Nagorniak on Unsplash"
        image="https://images.unsplash.com/photo-1595272568891-123402d0fb3b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 20:
        credits="Photo by Alex Lvrs on Unsplash"
        image="https://images.unsplash.com/photo-1519915028121-7d3463d20b13?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 21:
        credits="Photo by Alexandra Khudyntseva on Unsplash"
        image="https://images.unsplash.com/photo-1622621746668-59fb299bc4d7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=933&q=80"
    if index == 22:
        credits="Photo by Jacob Thomas on Unsplash"
        image="https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=803&q=80"
    if index == 23:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1557164158-11e97f2bb220?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=694&q=80"
    if index == 24:
        credits="Photo by Ellieelien on Unsplash"
        image="https://images.unsplash.com/photo-1557308536-ee471ef2c390?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 25:
        credits="Photo by Dessy Dimcheva on Unsplash"
        image="https://images.unsplash.com/photo-1575919361890-69028a013637?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 26:
        credits="Photo by Phinehas Adams on Unsplash"
        image="https://images.unsplash.com/photo-1579306194872-64d3b7bac4c2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=817&q=80"
    if index == 27:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1616690710400-a16d146927c5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 28:
        credits="Photo by David Holifield on Unsplash"
        image="https://images.unsplash.com/photo-1604413191066-4dd20bedf486?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=720&q=80"
    if index == 29:
        credits="Photo by Slashio Photography on Unsplash"
        image="https://images.unsplash.com/photo-1623842529695-f056295fd8e4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 30:
        credits="Photo by Diana Light on Unsplash"
        image="https://images.unsplash.com/photo-1562023692-9283c11284bd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 31:
        credits="Photo by Aneta Voborilova on Unsplash"
        image="https://images.unsplash.com/photo-1615735487485-e52b9af610c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 32:
        credits="Photo by Jasmine Bartel on Unsplash"
        image="https://images.unsplash.com/photo-1568827999250-3f6afff96e66?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=871&q=80"
    if index == 33:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1569289522127-c0452f372d46?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=762&q=80"
    if index == 34:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1552689486-f6773047d19f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=871&q=80"
    if index == 35:
        credits="Photo by Julia Peretiatko on Unsplash"
        image="https://images.unsplash.com/photo-1596529267076-07866e3655cc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 36:
        credits="Photo by Diana Light on Unsplash"
        image="https://images.unsplash.com/photo-1586244897823-988c9ad48c7a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 37:
        credits="Photo by Aneta Voborilova on Unsplash"
        image="https://images.unsplash.com/photo-1618426703623-c1b335803e07?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 38:
        credits="Photo by Jenny Galloway on Unsplash"
        image="https://images.unsplash.com/photo-1612809075925-230725151da2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=788&q=80"
    if index == 39:
        credits="Photo by micheile || visual stories on Unsplash"
        image="https://images.unsplash.com/photo-1608830597604-619220679440?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 40:
        credits="Photo by Pranjall Kumar on Unsplash"
        image="https://images.unsplash.com/photo-1615796701805-2094ac54bbf9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=736&q=80"
    if index == 41:
        credits="Photo by Alina Karpenko on Unsplash"
        image="https://images.unsplash.com/photo-1557925923-33b27f891f88?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=686&q=80"
    if index == 42:
        credits="Photo by leyli sadeqian on Unsplash"
        image="https://images.unsplash.com/photo-1629389861081-43cc4f172b0c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 43:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1557776959-f066eb37857f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 44:
        credits="Photo by Vicky Ng on Unsplash"
        image="https://images.unsplash.com/photo-1627308595171-d1b5d67129c4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80"
    if index == 45:
        credits="Photo by Takuya Nagaoka on Unsplash"
        image="https://images.unsplash.com/photo-1602663491496-73f07481dbea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"
    if index == 46:
        credits="Photo by amirali mirhashemian on Unsplash"
        image="https://images.unsplash.com/photo-1611293388250-580b08c4a145?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=838&q=80"
    if index == 47:
        credits="Photo by Melissa Walker Horn on Unsplash"
        image="https://images.unsplash.com/photo-1565661834013-d196ca46e14e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=688&q=80"
    if index == 48:
        credits="Photo by Deva Williamson on Unplash"
        image="https://images.unsplash.com/photo-1552689486-ce080445fbb6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=731&q=80"
    if index == 49:
        credits="Photo by Taylor Kiser on Unsplash"
        image="https://images.unsplash.com/photo-1505253149613-112d21d9f6a9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 50:
        credits="Photo by amirali mirhashemian on Unsplash"
        image="https://images.unsplash.com/photo-1586788680434-30d324b2d46f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=951&q=80"

    embed = discord.Embed(title="Cake :)",description=f"{someone} got a cake from {inter.author.mention} :)", color=0xFECC4D)
    embed.set_image(url=image)
    embed.set_footer(text=credits)
    await inter.send(embed=embed)

@client.command(aliases=['cake'])
async def cake2(inter, *, someone):
    credits = "If you're seeing this text then something has gone wrong"
    image = "https://cdn.discordapp.com/attachments/811051988992524299/950044067444686848/emoji.png"
    index = random.randint(1,50)

    if index == 1:
        credits="Photo by American Heritage Chocolate on Unsplash"
        image="https://images.unsplash.com/photo-1588195538326-c5b1e9f80a1b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=750&q=80"
    if index == 2:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1562440499-64c9a111f713?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 3:
        credits="Photo by Alexandra Gornago on Unsplash"
        image="https://images.unsplash.com/photo-1535141192574-5d4897c12636?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=688&q=80"
    if index == 4:
        credits="Photo by Anthony Espinosa on Unsplash"
        image="https://images.unsplash.com/photo-1571115177098-24ec42ed204d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 5:
        credits="Photo by David Holifield on Unsplash"
        image="https://images.unsplash.com/photo-1578985545062-69928b1d9587?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8Y2FrZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=700&q=60"
    if index == 6:
        credits="Photo by kaouther djouada on Unsplash"
        image="https://images.unsplash.com/photo-1602351447937-745cb720612f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=686&q=80"
    if index == 7:
        credits="Photo by Katie Rosario on Unsplash"
        image="https://images.unsplash.com/photo-1621303837174-89787a7d4729?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=736&q=80"
    if index == 8:
        credits="Photo by Annie Spratt on Unsplash"
        image="https://images.unsplash.com/photo-1464349095431-e9a21285b5f3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=936&q=80"
    if index == 9:
        credits="Photo by American Heritage Chocolate on Unsplash"
        image="https://images.unsplash.com/photo-1586985289688-ca3cf47d3e6e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 10:
        credits="Photo by Swapnll Dwivedi on Unsplash"
        image="https://images.unsplash.com/photo-1542826438-bd32f43d626f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=992&q=80"
    if index == 11:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1558301211-0d8c8ddee6ec?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=936&q=80"
    if index == 12:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1562777717-dc6984f65a63?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 13:
        credits="Photo by Karly Gomez on Unsplash"
        image="https://images.unsplash.com/photo-1488477304112-4944851de03d?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 14:
        credits="Photo by Slashio Photography on Unsplash"
        image="https://images.unsplash.com/photo-1627834377411-8da5f4f09de8?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=701&q=80"
    if index == 15:
        credits="Photo by Slashio Photography on Unplash"
        image="https://images.unsplash.com/photo-1622896784083-cc051313dbab?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 16:
        credits="Photo by Heather Barnes on Unsplash"
        image="https://images.unsplash.com/photo-1559620192-032c4bc4674e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=729&q=80"
    if index == 17:
        credits="Photo by Kim Daniels on Unsplash"
        image="https://images.unsplash.com/photo-1560180474-e8563fd75bab?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 18:
        credits="Photo by Will Echols on Unsplash"
        image="https://images.unsplash.com/photo-1517427294546-5aa121f68e8a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=764&q=80"
    if index == 19:
        credits="Photo by Natallia Nagorniak on Unsplash"
        image="https://images.unsplash.com/photo-1595272568891-123402d0fb3b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 20:
        credits="Photo by Alex Lvrs on Unsplash"
        image="https://images.unsplash.com/photo-1519915028121-7d3463d20b13?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 21:
        credits="Photo by Alexandra Khudyntseva on Unsplash"
        image="https://images.unsplash.com/photo-1622621746668-59fb299bc4d7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=933&q=80"
    if index == 22:
        credits="Photo by Jacob Thomas on Unsplash"
        image="https://images.unsplash.com/photo-1606890737304-57a1ca8a5b62?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=803&q=80"
    if index == 23:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1557164158-11e97f2bb220?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=694&q=80"
    if index == 24:
        credits="Photo by Ellieelien on Unsplash"
        image="https://images.unsplash.com/photo-1557308536-ee471ef2c390?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 25:
        credits="Photo by Dessy Dimcheva on Unsplash"
        image="https://images.unsplash.com/photo-1575919361890-69028a013637?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 26:
        credits="Photo by Phinehas Adams on Unsplash"
        image="https://images.unsplash.com/photo-1579306194872-64d3b7bac4c2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=817&q=80"
    if index == 27:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1616690710400-a16d146927c5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 28:
        credits="Photo by David Holifield on Unsplash"
        image="https://images.unsplash.com/photo-1604413191066-4dd20bedf486?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=720&q=80"
    if index == 29:
        credits="Photo by Slashio Photography on Unsplash"
        image="https://images.unsplash.com/photo-1623842529695-f056295fd8e4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 30:
        credits="Photo by Diana Light on Unsplash"
        image="https://images.unsplash.com/photo-1562023692-9283c11284bd?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 31:
        credits="Photo by Aneta Voborilova on Unsplash"
        image="https://images.unsplash.com/photo-1615735487485-e52b9af610c1?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 32:
        credits="Photo by Jasmine Bartel on Unsplash"
        image="https://images.unsplash.com/photo-1568827999250-3f6afff96e66?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=871&q=80"
    if index == 33:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1569289522127-c0452f372d46?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=762&q=80"
    if index == 34:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1552689486-f6773047d19f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=871&q=80"
    if index == 35:
        credits="Photo by Julia Peretiatko on Unsplash"
        image="https://images.unsplash.com/photo-1596529267076-07866e3655cc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 36:
        credits="Photo by Diana Light on Unsplash"
        image="https://images.unsplash.com/photo-1586244897823-988c9ad48c7a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 37:
        credits="Photo by Aneta Voborilova on Unsplash"
        image="https://images.unsplash.com/photo-1618426703623-c1b335803e07?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 38:
        credits="Photo by Jenny Galloway on Unsplash"
        image="https://images.unsplash.com/photo-1612809075925-230725151da2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=788&q=80"
    if index == 39:
        credits="Photo by micheile || visual stories on Unsplash"
        image="https://images.unsplash.com/photo-1608830597604-619220679440?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 40:
        credits="Photo by Pranjall Kumar on Unsplash"
        image="https://images.unsplash.com/photo-1615796701805-2094ac54bbf9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=736&q=80"
    if index == 41:
        credits="Photo by Alina Karpenko on Unsplash"
        image="https://images.unsplash.com/photo-1557925923-33b27f891f88?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=686&q=80"
    if index == 42:
        credits="Photo by leyli sadeqian on Unsplash"
        image="https://images.unsplash.com/photo-1629389861081-43cc4f172b0c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 43:
        credits="Photo by Deva Williamson on Unsplash"
        image="https://images.unsplash.com/photo-1557776959-f066eb37857f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 44:
        credits="Photo by Vicky Ng on Unsplash"
        image="https://images.unsplash.com/photo-1627308595171-d1b5d67129c4?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80"
    if index == 45:
        credits="Photo by Takuya Nagaoka on Unsplash"
        image="https://images.unsplash.com/photo-1602663491496-73f07481dbea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80"
    if index == 46:
        credits="Photo by amirali mirhashemian on Unsplash"
        image="https://images.unsplash.com/photo-1611293388250-580b08c4a145?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=838&q=80"
    if index == 47:
        credits="Photo by Melissa Walker Horn on Unsplash"
        image="https://images.unsplash.com/photo-1565661834013-d196ca46e14e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=688&q=80"
    if index == 48:
        credits="Photo by Deva Williamson on Unplash"
        image="https://images.unsplash.com/photo-1552689486-ce080445fbb6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=731&q=80"
    if index == 49:
        credits="Photo by Taylor Kiser on Unsplash"
        image="https://images.unsplash.com/photo-1505253149613-112d21d9f6a9?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80"
    if index == 50:
        credits="Photo by amirali mirhashemian on Unsplash"
        image="https://images.unsplash.com/photo-1586788680434-30d324b2d46f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=951&q=80"

    embed = discord.Embed(title="Cake :)",description=f"{someone} got a cake from {inter.author.mention} :)", color=0xFECC4D)
    embed.set_image(url=image)
    embed.set_footer(text=credits)
    await inter.send(embed=embed)

@client.slash_command(description="Hats are cook :)")
async def hat(inter):
    thing = [':cat:',":dog:",":chair:",":package:",":bed:",":wastebasket:",":coffee:",":printer:",":couch:","👩","🧑","👧","👩‍🦰","👶","👴","👨‍🦳","👨‍🦲","👱‍♂️","🙎","🧏","🤦","🤷","💇","🏃","🐵","🐺","🐯","🦒","🦊","🦝","🐮","🐷","🐹","🐰","🐻","🐼","🐸","🦓","🐴","🐔","🐳","🐟","🐘","<:lelcube:811058465383514132>","<:lelbot:811058423604576306>","<:superlelcube:916875806746226698>"]
    hat = ['🎩','🧢','👒','🎓','⛑️','🪖','👑','🔥','☔']
    await inter.send(f"{random.choice(hat)}\n{random.choice(thing)}")

@client.command(aliases=['hat'])
async def hat2(inter):
    thing = [':cat:',":dog:",":chair:",":package:",":bed:",":wastebasket:",":coffee:",":printer:",":couch:","👩","🧑","👧","👩‍🦰","👶","👴","👨‍🦳","👨‍🦲","👱‍♂️","🙎","🧏","🤦","🤷","💇","🏃","🐵","🐺","🐯","🦒","🦊","🦝","🐮","🐷","🐹","🐰","🐻","🐼","🐸","🦓","🐴","🐔","🐳","🐟","🐘","<:lelcube:811058465383514132>","<:lelbot:811058423604576306>","<:superlelcube:916875806746226698>"]
    hat = ['🎩','🧢','👒','🎓','⛑️','🪖','👑','🔥','☔']
    await inter.send(f"{random.choice(hat)}\n{random.choice(thing)}")

@client.slash_command(description="Reset YOUR items")
async def reset_items(inter):
    filename = str(inter.author.id) + "_items.json"

    create_user_if_it_dont_exist(inter.author.id)

    yes = Button(
            style=ButtonStyle.red,
            label="Yes, reset my money!",
            custom_id="yes_button"
        )
    no = Button(
            style=ButtonStyle.blurple,
            label="Nevermind.",
            custom_id="no_button"
        )
    
    pain = inter

    async def on_yes(inter):
        if pain.author.id == inter.author.id:
            with open(filename, 'r') as f:
                ok = json.load(f)

            ok = {}

            with open(filename, 'w') as f:
                json.dump(ok, f)

            await msg.edit(content="Successfully reseted.", view=None)
        else:
            await inter.send(content="You're not the author :P",ephemeral=True)
    
    async def on_no(inter):
        if pain.author.id == inter.author.id:
            await msg.edit(content="Ok",view=None)
        else:
            await inter.send(content="You're not the author :P",ephemeral=True)

    yes.callback = on_yes
    no.callback = on_no
    view = View()
    view.add_item(yes)
    view.add_item(no)

    await inter.send("Are you sure you want to reset your items??", view=view)
    msg = await inter.original_message()

@client.command(aliases=['reset_items'])
async def reset_items2(inter):
    filename = str(inter.author.id) + "_items.json"

    create_user_if_it_dont_exist(inter.author.id)

    yes = Button(
            style=ButtonStyle.red,
            label="Yes, reset my money!",
            custom_id="yes_button"
        )
    no = Button(
            style=ButtonStyle.blurple,
            label="Nevermind.",
            custom_id="no_button"
        )
    
    pain = inter

    async def on_yes(inter):
        if pain.author.id == inter.author.id:
            with open(filename, 'r') as f:
                ok = json.load(f)

            ok = {}

            with open(filename, 'w') as f:
                json.dump(ok, f)

            await msg.edit(content="Successfully reseted.", view=None)
        else:
            await inter.send(content="You're not the author :P",ephemeral=True)
    
    async def on_no(inter):
        if pain.author.id == inter.author.id:
            await msg.edit(content="Ok",view=None)
        else:
            await inter.send(content="You're not the author :P",ephemeral=True)

    yes.callback = on_yes
    no.callback = on_no
    view = View()
    view.add_item(yes)
    view.add_item(no)

    msg = await inter.send("Are you sure you want to reset your items??", view=view)

@client.slash_command(description="Sell items")
@commands.cooldown(1, 60, commands.BucketType.user)
async def sell(inter, user: discord.User, item: Items, price:int, amount:int=1):
    """
    Parameters
    ----------
    user: Who will buy the item
    item: The item you will sell
    price: The price.
    amount: How many items you will sell
    """
    xd = False

    with open(f"{str(inter.author.id)}_items.json", 'r') as f:
        items = json.load(f)
    
    # Does the author have this item?
    if item not in items or items[item] < amount:
        xd = True
        await inter.send("Lol you don't have this item")
    
    # Illegal stuff
    if amount < 1 or user.id == inter.author.id:
        xd = True
        await inter.send("Das illegal")
    
    if xd == False:
        #Get the price using the price the items have in the shop
        '''# I should make items.txt a json file
        with open("items.txt", 'r') as f:
            txt = f.read()
        
        txt2 = txt.split("\n")

        for i in txt2:
            txt3 = i.split("&&")
        
            if txt3[0] == item:
                price = int(txt3[1])'''

        yes = Button(
            style=ButtonStyle.blurple,
            label="Yes",
            custom_id="yes_button"
        )
        no = Button(
            style=ButtonStyle.red,
            label="No",
            custom_id="no_button"
        )

        async def on_yes(epokinter):
            if epokinter.author.id == user.id:
                # Does the user have enough money?
                with open(f"{str(user.id)}.json", 'r') as f:
                    mone = json.load(f)
                
                if mone['cash'] >= price:
                    # Give the item
                    items[item] -= amount

                    with open(f"{str(inter.author.id)}_items.json", 'w') as f:
                        json.dump(items, f)
                    
                    with open(f"{str(user.id)}_items.json", 'r') as f:
                        items_but_it_has_a_different_value_i_know_this_is_a_pretty_good_variable_name = json.load(f)
                    
                    items_but_it_has_a_different_value_i_know_this_is_a_pretty_good_variable_name[item] += amount

                    with open(f"{str(user.id)}_items.json", 'w') as f:
                        json.dump(items_but_it_has_a_different_value_i_know_this_is_a_pretty_good_variable_name, f)

                    # Mone 🤑
                    with open(f"{str(inter.author.id)}.json", 'r') as f:
                        monehrjieodkgro = json.load(f)
                    
                    monehrjieodkgro['cash'] += price
                    mone['cash'] -= price

                    with open(f"{str(inter.author.id)}.json", 'w') as f:
                        json.dump(monehrjieodkgro, f)
                    
                    with open(f"{str(user.id)}.json", 'w') as f:
                        json.dump(mone, f)
                    
                    await msg.edit(content=f"{item} was successfully sold!", view=None)

                else:
                    await msg.edit(content=f"{user.mention} You don't have enough lelgolds xdd", view=None)
            else:
                await epokinter.send(content="Yes",ephemeral=True)
        
        async def on_no(epokinter):
            if epokinter.author.id == user.id:
                await msg.edit(content="Canceled operation.",view=None)
            else:
                await epokinter.send(content="Yes",ephemeral=True)

        yes.callback = on_yes
        no.callback = on_no
        view = View(timeout=None)
        view.add_item(yes)
        view.add_item(no)

        await inter.send(f"{user.mention} Do you want to buy {amount} {item}s for {price} <:lelgold:888933451410075689>?", view=view)
        msg = await inter.original_message()

@client.command(aliases=['sell'])
@commands.cooldown(1, 60, commands.BucketType.user)
async def sell2(inter, user: discord.User, price, amount=1):
    numbernt = False
    xd = False

    try:
        price = int(price)
        amount = int(amount)
    except:
        numbernt = True
        await inter.reply("You are supposed to put a number as the amount (If you are trying to specify the item, you will do it after sending the command!)")

    if numbernt == False:

        select = Select(
            custom_id="select",
            placeholder="Click here to choose the item you want",
            max_values=1,
            options=itemselect
        )

        async def clallbakc(interr):
            nonlocal xd
            if interr.author.id == inter.author.id:
                item = select.values[0]
                with open(f"{str(inter.author.id)}_items.json", 'r') as f:
                    items = json.load(f)
                
                # Does the author have this item?
                if item not in items or items[item] < amount:
                    xd = True
                    await msg.edit(content="Lol you don't have this item",view=None)
                
                # Illegal stuff
                if amount < 1 or user.id == inter.author.id:
                    xd = True
                    await msg.edit(content="Das illegal",view=None)

                if xd == False:
                    #Get the price using the price the items have in the shop
                    '''# I should make items.txt a json file
                    with open("items.txt", 'r') as f:
                        txt = f.read()
                    
                    txt2 = txt.split("\n")

                    for i in txt2:
                        txt3 = i.split("&&")
                    
                        if txt3[0] == item:
                            price = int(txt3[1])'''

                    yes = Button(
                        style=ButtonStyle.blurple,
                        label="Yes",
                        custom_id="yes_button"
                    )
                    no = Button(
                        style=ButtonStyle.red,
                        label="No",
                        custom_id="no_button"
                    )

                    async def on_yes(epokinter):
                        if epokinter.author.id == user.id:
                            # Does the user have enough money?
                            with open(f"{str(user.id)}.json", 'r') as f:
                                mone = json.load(f)
                            
                            if mone['cash'] >= price:
                                # Give the item
                                items[item] -= amount

                                with open(f"{str(inter.author.id)}_items.json", 'w') as f:
                                    json.dump(items, f)
                                
                                with open(f"{str(user.id)}_items.json", 'r') as f:
                                    items_but_it_has_a_different_value_i_know_this_is_a_pretty_good_variable_name = json.load(f)
                                
                                items_but_it_has_a_different_value_i_know_this_is_a_pretty_good_variable_name[item] += amount

                                with open(f"{str(user.id)}_items.json", 'w') as f:
                                    json.dump(items_but_it_has_a_different_value_i_know_this_is_a_pretty_good_variable_name, f)

                                # Mone 🤑
                                with open(f"{str(inter.author.id)}.json", 'r') as f:
                                    monehrjieodkgro = json.load(f)
                                
                                monehrjieodkgro['cash'] += price
                                mone['cash'] -= price

                                with open(f"{str(inter.author.id)}.json", 'w') as f:
                                    json.dump(monehrjieodkgro, f)
                                
                                with open(f"{str(user.id)}.json", 'w') as f:
                                    json.dump(mone, f)
                                
                                await msg.edit(content=f"{item} was successfully sold!", view=None)

                            else:
                                await msg.edit(content=f"{user.mention} You don't have enough lelgolds xdd", view=None)
                        else:
                            await epokinter.send(content="Yes",ephemeral=True)
                    
                    async def on_no(epokinter):
                        if epokinter.author.id == user.id:
                            await msg.edit(content="Canceled operation.",view=None)
                        else:
                            await epokinter.send(content="Yes",ephemeral=True)

                    yes.callback = on_yes
                    no.callback = on_no
                    view = View(timeout=None)
                    view.add_item(yes)
                    view.add_item(no)

                    await msg.edit(content=f"{user.mention} Do you want to buy {amount} {item}s for {price} <:lelgold:888933451410075689>?", view=view)
            else:
                await interr.send(content="You're not the author :P",ephemeral=True)

        select.callback = clallbakc
        view = View()
        view.add_item(select)

        msg = await inter.send("What item you want to sell?", view=view)

EXTREMELYSECRETSETOFCHARACTERS = "insert token here"
client.run(EXTREMELYSECRETSETOFCHARACTERS)
