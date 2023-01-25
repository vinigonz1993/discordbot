from threading import Thread
import bot
from config import CONFIG

from flask import Flask
from flask_discord_interactions import DiscordInteractions

app = Flask(__name__)
discord = DiscordInteractions(app)


app.config["DISCORD_CLIENT_ID"] = CONFIG["DISCORD_APP_ID"]
app.config["DISCORD_PUBLIC_KEY"] = CONFIG["DISCORD_PUBLIC_KEY"]
app.config["DISCORD_CLIENT_SECRET"] = CONFIG["DISCORD_CLIENT_SECRET"]

discord.set_route('/interactions')
discord.update_commands(guild_id=CONFIG['SERVER_GUIlD'])

def run_thread(func):
    thread = Thread(
        target=func
    )
    print('Start Separate Thread From Bot')
    thread.start()

def run():
    app.run(
        host='0.0.0.0', port=8080
    )

@app.route('/')
def hello():
    return 'This is a python app!'

if __name__ == '__main__':
    run_thread(run)
    bot.run_bot()