import discord
from discord.ext import commands
import random
import time
import asyncio

TOKEN = 'MTExNzQwNjc2NzcwNjU1NDQwMA.G8r54p.7pTsDR3Y-n8K3cZrOJIp2nwShKF7qH9hYBspfE'
PREFIX = '<'

bot = commands.Bot(command_prefix=PREFIX)

gems = {}

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type = discord.ActivityType.watching, name = ("lol")))
    print(f"logged in as {bot.user}")
    bot.loop.create_task(gem_distribution())

@bot.event
async def on_member_join(member):
    # Assign initial gem count for new members
    gems[member.id] = 0

async def gem_distribution():
    await bot.wait_until_ready()
    while not bot.is_closed():
        for member in bot.get_all_members():
            if isinstance(member, discord.Member):
                gems[member.id] = gems.get(member.id, 0) + 1
                await asyncio.sleep(1)  # Distribute gems every 1s.

# try now 

@bot.slash_command(name= "balance", description="Show your Balance of your gems!")
async def mygems(ctx):
    user_gems = gems.get(ctx.author.id, 0)
    embed = discord.Embed(title="Balance", description="")
    embed.add_field(name = "Gems", value = f"You have {user_gems} gems currently.")
    embed.set_footer(text = f"@{ctx.author}'s balance.", icon_url= ctx.author.avatar)
    await ctx.respond(embed = embed)


@bot.slash_command(name= "coinflip", description= "bet your gems")# WHY IT DONT WORK try nowcl
async def coinflip(ctx, bet: int, side: str):
    if side.lower() not in ['head', 'tails']:
        await ctx.send('Please choose "head" or "tails".')
        return

    if bet <= 0:
        await ctx.send('Please enter a valid number of gems to bet.')
        return

    user = ctx.author
    user_gems = gems.get(user.id, 0)

    if user_gems < bet:
        await ctx.send('You do not have enough gems.')
        return

    coins = ['head', 'tails']
    result = random.choice(coins)

    if result == side.lower():
        win_amount = bet * 2
        gems[user.id] = user_gems + win_amount
        await ctx.send(f'Congratulations! You won {win_amount} gems. You now have a total of {gems[user.id]} gems.')
    else:
        gems[user.id] = user_gems - bet
        embed = discord.Embed(title="Bet", description="")
        embed.add_field(name = "Your lost!", value = f'Unfortunately, you lost {bet} gems. You now have a total of {gems[user.id]} gems.')
        await ctx.respond(embed = embed)
#_______________________________________________________________________________________________________________________________________________________________
#-------------------Roulette--------------------

@bot.slash_command(name="roulette", description="Bet gems on a color")
async def roulette(ctx, bet: int, color: str):
    if color.lower() not in ['red', 'blue', 'green']: # 
        await ctx.send('Please choose "red", "blue", or "green".')
        return

    if bet <= 0:
        await ctx.send('Please enter a valid number of gems to bet.')
        return

    user = ctx.author
    user_gems = gems.get(user.id, 0)

    if user_gems < bet:
        await ctx.send('You do not have enough gems.')
        return

    colors = ['red', 'blue', 'green']
    result = random.choices(colors, weights=[48, 48, 4], k=1)[0]

    if result == color.lower():
        if result == 'green':
            win_amount = bet * 10
        else:
            win_amount = bet * 2
        gems[user.id] = user_gems + win_amount
        await ctx.send(f'Congratulations! You won {win_amount} gems. You now have a total of {gems[user.id]} gems.')
    else:
        gems[user.id] = user_gems - bet
        embed = discord.Embed(title="Bet", description="")
        embed.add_field(name = "Your lost!", value = f'Unfortunately, you lost {bet} gems. You now have a total of {gems[user.id]} gems.')
        await ctx.respond(embed = embed) 
        
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user = message.author
    user_gems = gems.get(user.id, 0)
    gems[user.id] = user_gems + 1

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    user = message.author


bot.run(TOKEN)