import discord
import random
from discord.ext import commands

class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  
  #Rolls the dice. First arg = no and second arg = sides
  @commands.command(name='roll-dice', help='Simulates rolling upto 5 dice. eg: <roll_dice 2 6> is 2 six sided dice')
  async def roll(self, ctx, number_of_dice: int, number_of_sides: int):
      if number_of_dice >= 6 or number_of_sides > 20:
          return
      dice = [
          str(random.choice(range(1, number_of_sides + 1)))
          for _ in range(number_of_dice)
      ]
      await ctx.send('The dice landed: ' + ', '.join(dice))

  #Flips the coin. Arg = number of coin
  @commands.command(name='flip-coin', help='Flips between 1 and 5 coins, use <flip_coin 2> to flip 2 coins')
  async def flip_coin(self, ctx, number_of_coins: int):
      if number_of_coins >= 6:
          return
      coin = [
          str(random.choice(['Heads', 'Tails'])) for _ in range(number_of_coins)
      ]
      await ctx.send('The coins landed: ' + ', '.join(coin))

def setup(bot):
    bot.add_cog(General(bot))