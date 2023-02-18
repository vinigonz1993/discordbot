from config import CONFIG
import openai
import random

class OpenAI():
    key = CONFIG['OPEN_AI']
    model_engine = "text-davinci-003"
    MAX_SIZE_STRING = 800
    errors_messages = [
        'The question/answer is too big, try another one',
        'Try a shorter question please',
        'Your text is too big'
    ]

    def __init__(self, prompt):
        openai.api_key = self.key
        self.prompt = prompt

    def validate_prompt(self):
        if len(self.prompt) == 0:
            return False

        if len(self.prompt) > self.MAX_SIZE_STRING:
            return False

        return True

    def run_image(self):
        if self.validate_prompt() is False:
            return random.choice(self.errors_messages)

        try:
            image = openai.Image.create(
                prompt=self.prompt,
                n=1,
                size="512x512"
            )
            return image['data'][0]['url']
        except Exception as error:
            print(error)
            return error

    def run(self):
        if self.validate_prompt() is False:
            return random.choice(self.errors_messages)

        try:
            completion = openai.Completion.create(
                engine=self.model_engine,
                prompt=self.prompt,
                max_tokens=500,
                n=1,
                stop=None,
                temperature=0.3,
            )

            response = completion.choices[0].text

            return response
        except Exception as error:
            return error