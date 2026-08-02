import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Ayrışma verileri
AYRISMA_VERILERI = {
    "plastik": {"sure": "450 - 500 yıl", "gaz": "82 gram karbondioksit"},
    "alüminyum": {"sure": "200 - 500 yıl", "gaz": "170 gram karbondioksit"},
    "cam": {"sure": "4.000 yıl", "gaz": "300 - 350 gram karbondioksit"},
    "poşet": {"sure": "1.000 yıl", "gaz": "10 - 30 gram karbondioksit"},
    "karton": {"sure": "30 yıl", "gaz": "11 gram karbondioksit"},
    "sigara": {"sure": "10 - 12 yıl", "gaz": "14 gram karbondioksit"},
    "teneke": {"sure": "50 - 100 yıl", "gaz": "150 - 200 gram karbondioksit"},
    "ahşap": {"sure": "10 - 15 yıl", "gaz": "50 gram karbondioksit"},
    "tişört": {"sure": "1 - 5 ay", "gaz": "3 - 5 kg karbondioksit"},
    "ayakkabı": {"sure": "25 - 40 yıl", "gaz": "14 kg karbondioksit"}
}

# Geri dönüşüm kutusu eşleşmeleri
KUTU_VERILERI = {
    "karton": ("🔵 Mavi Kutu", "Karton kutular kırılıp katlanarak bu kutuya atılmalıdır."),
    "plastik": ("🟡 Sarı Kutu", "Plastik şişeler, kapaklar ve ambalajlar durulanarak buraya atılır."),
    "poşet": ("🟡 Sarı Kutu", "Temiz plastik poşet ve ambalajlar sarı kutuya atılır."),
    "cam": ("🟢 Yeşil Kutu", "Cam şişeler ve kavanozlar (kapakları çıkarılarak) buraya atılır."),
    "alüminyum": ("Gri / Gümüş Kutu", "Alüminyum kutu ve folyolar metal kutusuna atılır."),
    "teneke": ("Gri / Gümüş Kutu", "Temizlenmiş teneke kutular metal ayrıştırma kutusuna atılır."),
}

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')

@bot.command(name='ayrisma')
async def ayrisma(ctx, malzeme: str = None):
    if not malzeme:
        await ctx.send("Eksik bilgi girdiniz! Örnek kullanım: `$ayrisma plastik`")
        return

    malzeme = malzeme.lower()
    
    if malzeme in AYRISMA_VERILERI:
        veri = AYRISMA_VERILERI[malzeme]
        await ctx.send(f"{malzeme.capitalize()} doğada yaklaşık {veri['sure']} sürede ayrışır ve üretilirken yaklaşık {veri['gaz']} salınır.")
    else:
        await ctx.send("Bilinmeyen malzeme!")

@bot.command(name='nereye')
async def nereye(ctx, atik: str = None):
    if not atik:
        await ctx.send("Eksik bilgi girdiniz! Örnek kullanım: `$nereye plastik`")
        return

    atik = atik.lower()

    if atik in KUTU_VERILERI:
        kutu, detay = KUTU_VERILERI[atik]
        await ctx.send(f"{atik.capitalize()} atığı **{kutu}** içerisine atılmalıdır. ({detay})")
    else:
        await ctx.send("Bilinmeyen atık türü!")

bot.run("token")
