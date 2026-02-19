import requests
import logging



class Translation():
    def translation(self, word):
     url = ""
     params = {"q": word, "langpair": "en|uk"}
     response = requests.get(url, params=params)
     data = response.json()
     return data["responseData"]["translatedText"]
