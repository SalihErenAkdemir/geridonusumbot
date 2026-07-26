import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')

@bot.command(name='ayrisma')
async def ayrisma(ctx, malzeme: str = None):
    if not malzeme:
        await ctx.send("Eksik bilgi girdiniz! Örnek kullanım: `$ayrisma plastik`")
        return

    malzeme = malzeme.lower()
    
    if malzeme == "plastik":
        sure = "450 - 500 yıl"
        gaz = "82 gram karbondioksit"
    elif malzeme == "alüminyum":
        sure = "200 - 500 yıl"
        gaz = "170 gram karbondioksit"
    elif malzeme == "cam":
        sure = "4.000 yıl"
        gaz = "300 - 350 gram karbondioksit"
    elif malzeme == "poşet":
        sure = "1.000 yıl"
        gaz = "10 - 30 gram karbondioksit"
    elif malzeme == "karton":
        sure = "30 yıl"
        gaz = "11 gram karbondioksit"
    elif malzeme == "sigara":
        sure = "10 - 12 yıl"
        gaz = "14 gram karbondioksit"
    elif malzeme == "teneke":
        sure = "50 - 100 yıl"
        gaz = "150 - 200 gram karbondioksit"
    elif malzeme == "ahşap":
        sure = "10 - 15 yıl"
        gaz = "50 gram karbondioksit"
    elif malzeme == "tişört":
        sure = "1 - 5 ay"
        gaz = "3 - 5 kg karbondioksit"
    elif malzeme == "ayakkabı":
        sure = "25 - 40 yıl"
        gaz = "14 kg karbondioksit"
    else:
        await ctx.send("Bilinmeyen malzeme!")
        return
        
    await ctx.send(f"{malzeme} doğada yaklaşık {sure} sürede ayrışır ve üretilirken yaklaşık {gaz} salınır.")

bot.run("Token")
