# Zaskocz swoich kolegów!
#import random
#Info = ["Elo jestem Fommy_Pl","Nagrywam filmy o horrorah planuje znów dopiero za 2 lata ngrać film o poppy playtime chapter 5"]
#print(random.choice(Info))

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def zrób_mi_Kawę(ctx):
    await ctx.send('☕')

@bot.command()
async def podaj_twoją_ulubioną_piosękę(ctx):
    await ctx.send("https://www.youtube.com/watch?v=736iwxpQnDY")

@bot.command()
async def Hapyy(ctx):
    with open('Fotki/Hapyy.png', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)


bot.run("MTQ4MzE0NTMwMTMzNzU3NTUyOA.Gqkuzv.NalsaYyAAxtnoz1sRTb_quNmVJFAF_9j0Hk3aI")