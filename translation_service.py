import requests
import logging_set
import logging

logger = logging.getLogger(__name__)

class TranslationService():
    def translation(self, word):
     url = "https://api.mymemory.translated.net/get"
     params = {"q": word, "langpair": "en|uk"}
     response = requests.get(url, params=params)
     if response.status_code != 200:
       logger.error(f"API returned status {response.status_code}")
       print("Translation service error.")
       return None
     else:
         data = response.json()
         return data["responseData"]["translatedText"]

# requests.get returns a http object and in data = response.json() we convert the json to a python nested dictionary. 
# So ["responseData"] and ["translatedText"] are two dictionary keys to get the value ["translatedText"]. 
# So return["responseData"]["translatedText"] returns the translated text.
