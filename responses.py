import requests
import discord
from api.weather import WeatherApi
from api.exchange import Exchange
from api.quotes import Quotes
from api.octranspo import OCTranspo

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'quote':
        quotes = Quotes()
        return quotes.run()

    if p_message.split(' ')[0] == 'usd':

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

    if p_message.split(' ')[0] == 'w':
        list =  p_message.split(' ')

        location = list[1]
        country = list[2]

        request = WeatherApi().run(
            location, country
        )

        return request

    if p_message.split(' ')[0] == 'bus':
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