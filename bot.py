import discord
from discord.ext import commands, tasks
from discord import app_commands
import asyncio
import config
import db

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree
db.init_db()

class VoteButton(discord.ui.View):
    def __init__(self, message_id):
        super().__init__(timeout=None)
        self.message_id = message_id

    @discord.ui.button(label="I agree", style=discord.ButtonStyle.success)
    async def agree(self, interaction: discord.Interaction, button: discord.ui.Button):
        db.record_vote(self.message_id, "agree")
        await interaction.response.send_message("Your vote for ✅ I agree has been recorded.", ephemeral=True)

    @discord.ui.button(label="I disagree", style=discord.ButtonStyle.danger)
    async def disagree(self, interaction: discord.Interaction, button: discord.ui.Button):
        db.record_vote(self.message_id, "disagree")
        await interaction.response.send_message("Your vote for ❌ I disagree has been recorded.", ephemeral=True)

@tree.command(name="vote", description="Start a vote. Only users with a specific role can vote.")
@app_commands.describe(
    question="The question to vote on.",
    role="Role allowed to vote",
    duration="Vote duration in minutes (default: 10080 = 7 days)"
)
async def vote(interaction: discord.Interaction, question: str, role: discord.Role, duration: int = 10080):
    if not interaction.user.guild_permissions.manage_guild:
        await interaction.response.send_message("You don’t have permission to use this command.", ephemeral=True)
        return

    embed = discord.Embed(title="📊 Anonymous Vote", description=question, color=0x00cc66)
    embed.set_footer(text=f"Only users with the role {role.name} can vote. Ends in {duration} minutes.")

    message = await interaction.channel.send(embed=embed, view=VoteButton(str(interaction.id)))
    db.save_vote(str(message.id), question)

    async def end_vote():
        await asyncio.sleep(duration * 60)
        agree, disagree = db.get_results(str(message.id))
        result_embed = discord.Embed(
            title="🗳️ Voting Complete",
            description=question,
            color=0xcccccc
        )
        result_embed.add_field(name="✅ I agree", value=str(agree), inline=True)
        result_embed.add_field(name="❌ I disagree", value=str(disagree), inline=True)
        await interaction.channel.send(embed=result_embed)

    bot.loop.create_task(end_vote())
    await interaction.response.send_message("Vote created!", ephemeral=True)

@bot.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=config.GUILD_ID))
    print(f"Logged in as {bot.user}")

bot.run(config.TOKEN)
