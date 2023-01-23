from config import CONFIG
import openai

class OpenAI():
    key = CONFIG['OPEN_AI']
    model_engine = "text-davinci-003"
    MAX_SIZE_STRING = 300

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
            return "Sorry, try a shorter question"

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
