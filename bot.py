# bot.py
import responses
import discord
from config import CONFIG

def help_commands():
    embed = discord.Embed(
        title='Bot commands',
        color=0x109319
    )
    embed.add_field(
        name='Quotes',
        value='!quote -> Returns a random quote',
        inline=False
    )
    embed.add_field(
        name='Exchange USD value',
        value='!usd "currency_code" -> Returns the exchange value. (ex.: usd cad)',
        inline=False
    )
    embed.add_field(
        name='Weather',
        value='!w "city" "country_code" -> Returns the wheater. (ex.: w ottawa ca)',
        inline=False
    )
    embed.add_field(
        name='Ottawa OCTranspo',
        value='!bus "stop#" -> Returns the next trips for the stop. (ex.:bus 1222)',
        inline=False
    )
    return embed

async def send_message(message, is_private):
    try:
        if message.content == '!h':
            await message.channel.send(embed=help_commands())
        elif message.content == '!delete':
            await message.channel.purge()
        elif message.content.split(' ')[0] == '!bus':
            response = responses.handle_response(message.content)
            await message.channel.send(embed=response)
        elif message.content.split(' ')[0] == '!w':
            response = responses.handle_response(message.content)
            await message.channel.send(embed=response)
        else:
            response = responses.handle_response(message.content)
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_bot():
    TOKEN = CONFIG['DISCORD_TOKEN']

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print('Runnig!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        message.content = message.content.lower()

        await send_message(message, is_private=False)

    @client.event
    async def on_error(event, *args, **kwargs):
        print(f'error: {event}, {args}')

    client.run(TOKEN)