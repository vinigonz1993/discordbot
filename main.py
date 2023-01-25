import bot
from config import CONFIG

from flask import Flask
from flask_discord_interactions import DiscordInteractions

app = Flask(__name__)
discord = DiscordInteractions(app)


app.config["DISCORD_CLIENT_ID"] = CONFIG["DISCORD_APP_ID"]
app.config["DISCORD_PUBLIC_KEY"] = CONFIG["DISCORD_PUBLIC_KEY"]
app.config["DISCORD_CLIENT_SECRET"] = CONFIG["DISCORD_CLIENT_SECRET"]

def run_chain():
    discord.set_route('/interactions')
    discord.update_commands(guild_id=CONFIG['SERVER_GUIlD'])
    bot.run_bot()

if __name__ == '__main__':
    run_chain()
    app.run()