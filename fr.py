Français file

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "your token"

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

# Commande pour DM tout le serveur
@bot.command()
async def dmall(ctx, *, message):
    for member in ctx.guild.members:
        if not member.bot:
            try:
                await member.send(message)
                print(f"DM envoyé à {member}")
            except Exception as e:
                print(f"Échec pour {member}: {e}")
    await ctx.send("DM envoyés à tout le serveur.")

# Commande pour DM tous les membres d’un rôle
@bot.command()
async def dmrole(ctx, role: discord.Role, *, message):
    for member in role.members:
        if not member.bot:
            try:
                await member.send(message)
                print(f"DM envoyé à {member}")
            except Exception as e:
                print(f"Échec pour {member}: {e}")
    await ctx.send(f"DM envoyés aux membres du rôle {role.name}.")

# Commande pour DM un utilisateur
@bot.command()
async def dm(ctx, user: discord.User, *, message):
    try:
        await user.send(message)
        await ctx.send(f"DM envoyé à {user}.")
    except Exception as e:
        await ctx.send(f"Erreur : {e}")

bot.run(TOKEN)
