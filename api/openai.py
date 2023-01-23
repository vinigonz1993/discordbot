from config import CONFIG
import openai
import random

class OpenAI():
    key = CONFIG['OPEN_AI']
    model_engine = "text-davinci-003"
    MAX_SIZE_STRING = 300
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

    def run(self):
        if self.validate_prompt() is False:
            return random.choice(self.errors_messages)

        completion = openai.Completion.create(
            engine=self.model_engine,
            prompt=self.prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )

        response = completion.choices[0].text

        return response
