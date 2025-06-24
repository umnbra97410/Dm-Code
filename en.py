import discord
from discord.ext import commands

# Enable required intents
intents = discord.Intents.default()
intents.members = True  # Needed to access server members
intents.message_content = True  # Needed to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

# Your bot token here
TOKEN = "YOUR_BOT_TOKEN_HERE"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

# Command: DM all members in the server
@bot.command()
async def dmall(ctx, *, message):
    """Send a DM to every non-bot member of the server."""
    sent = 0
    failed = 0
    for member in ctx.guild.members:
        if not member.bot:
            try:
                await member.send(message)
                sent += 1
            except Exception as e:
                print(f"Failed to DM {member}: {e}")
                failed += 1
    await ctx.send(f"✅ DMs sent: {sent} | ❌ Failed: {failed}")

# Command: DM every member with a specific role
@bot.command()
async def dmrole(ctx, role: discord.Role, *, message):
    """Send a DM to all members with a given role."""
    sent = 0
    failed = 0
    for member in role.members:
        if not member.bot:
            try:
                await member.send(message)
                sent += 1
            except Exception as e:
                print(f"Failed to DM {member}: {e}")
                failed += 1
    await ctx.send(f"✅ DMs sent to role '{role.name}': {sent} | ❌ Failed: {failed}")

# Command: DM a specific user
@bot.command()
async def dm(ctx, user: discord.User, *, message):
    """Send a DM to a specific user."""
    try:
        await user.send(message)
        await ctx.send(f"✅ DM sent to {user.name}")
    except Exception as e:
        await ctx.send(f"❌ Failed to send DM: {e}")

bot.run(TOKEN)
