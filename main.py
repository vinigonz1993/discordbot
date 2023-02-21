import bot
import git
import hmac
import hashlib
from threading import Thread
from config import CONFIG

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_discord_interactions import DiscordInteractions
from api.octranspo import OCTranspo
from api.openai import OpenAI

app = Flask(__name__, static_folder="./frontend/build", static_url_path="/")
CORS(app)
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
        host='0.0.0.0', port=5000
    )

def is_valid_signature(x_hub_signature, data, private_key):
    hash_algorithm, github_signature = x_hub_signature.split('=', 1)
    algorithm = hashlib.__dict__.get(hash_algorithm)
    encoded_key = bytes(private_key, 'latin-1')
    mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)
    return hmac.compare_digest(mac.hexdigest(), github_signature)

@app.route('/')
def hello():
    return app.send_static_file('index.html')

@app.route('/server_update', methods=['POST'])
def webhook():
    try:
        x_hub_signature = request.headers.get('X-Hub-Signature')
        if not is_valid_signature(x_hub_signature, request.data, CONFIG['GITHUB_WEBHOOK_SECRET']):
            return 'Error'
        repo = git.Repo('/home/vinigonz1993')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated!'
    except Exception as error:
        return str(error)

@app.route('/oct', methods=['GET'])
def get_route():
    stopNo = request.args.get('stopNo')

    oct = OCTranspo()
    response = oct.run(stopNo)

    return jsonify(response)

@app.route('/backend/gpt', methods=['POST'])
def get_gpt():
    data = request.form.get('data')

    response = OpenAI(prompt=data).run()

    return jsonify(response)

if __name__ == '__main__':
    run_thread(run)
    bot.run_bot()