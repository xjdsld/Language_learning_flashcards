import requests
from session import Card

class Translation():
    def translation(self):
     url = ""
     params = {"q": self.word, "langpair": "en|uk"}
     response = requests.get(url, params=params)
     data = response.json()
     return data["responseData"]["translatedText"]
