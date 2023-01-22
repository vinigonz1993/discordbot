import requests
import discord
from api.weather import WeatherApi
from api.exchange import Exchange
from api.quotes import Quotes
from api.octranspo import OCTranspo

def handle_response(message):
    p_message = message.lower()

    if p_message.startswith('!quote'):
        quotes = Quotes()
        return quotes.run()

    if p_message.startswith('!usd'):

        find_rate = p_message.split(' ')[1].upper()

        exchange = Exchange()
        request = exchange.run()

        try:
            response = f'''
                1 USD = {request["rates"][find_rate]} {find_rate.upper()}
            '''
        except:
            return 'Symbol not found'

        return response

    if p_message.startswith('!w'):
        try:
            params =  p_message.split(' ')

            location = params[1]
            country = params[2]
        except:
            return discord.Embed(
                title="Error",
                color=0xED4245,
                description='''Invalid location. Try something like:
                    ```!w ottawa ca```
                '''
            )
        try:
            request = WeatherApi().run(
                location, country
            )

            embed = discord.Embed(
                title=f"Weather in {request['name']}",
                color=0x109319,
            )

            def calculate_celcius(value):
                k = 273.15
                return f'{round(value - k, 2)} °C'

            embed.add_field(
                name=request['weather'][0]['main'],
                value=request['weather'][0]['description'],
                inline=False
            )
            embed.add_field(
                name='Temperature',
                value='',
                inline=False
            )
            embed.add_field(
                name='',
                value=f"Now {calculate_celcius(request['main']['temp'])}",
                inline=False
            )
            embed.add_field(
                name='',
                value=f"Max {calculate_celcius(request['main']['temp_max'])}",
                inline=False
            )
            embed.add_field(
                name='',
                value=f"Min {calculate_celcius(request['main']['temp_min'])}",
                inline=False
            )
            embed.add_field(
                name='',
                value=f"Feels link {calculate_celcius(request['main']['feels_like'])}",
                inline=False
            )
            return embed
        except:
            return "Sorry I couldn't find the location"

    if p_message.startswith('!bus'):
        try:
            stopNo = p_message.split(' ')[1]
            oct = OCTranspo()
            request = oct.run(stopNo)

            embed = discord.Embed(
                title=request['GetRouteSummaryForStopResult']['StopDescription'],
                color=0x109319,
                description=f"Stop # {request['GetRouteSummaryForStopResult']['StopNo']}"
            )
            for route in request['GetRouteSummaryForStopResult']['Routes']['Route']:
                embed.add_field(
                    name=f"{route['RouteNo']} - {route['RouteHeading']}",
                    value='',
                    inline=False
                )
                for trip in route['Trips']:
                    embed.add_field(
                        name='',
                        value=f"{trip['AdjustedScheduleTime']}min",
                        inline=False
                    )

            return embed
        except:
            return "Sorry I did'nt find the stop"