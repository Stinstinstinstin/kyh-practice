""""
20200927
Kristin
Uppgift 35
"""

import requests

ENDPOINT = 'https://mqif4s7obg.execute-api.eu-central-1.amazonaws.com/olofs_lambda'


class QuizzWebServiceAPI:

    def __init__(self):
        self.url = ENDPOINT

    def get_all_questions(self):
        r = requests.get(self.url)
        ls = r.json()['questions']
        return ls

    def add_question(self, prompt, answer, alternatives):
        data = {
            'prompt': prompt,
            'rightAnswer': answer,
            'wrongAnswers': alternatives
        }
        # Uppgift 35.2
        r = requests.post(url=self.url, json=data)
        return True if r.status_code == 200 else False
