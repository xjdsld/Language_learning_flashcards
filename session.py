import logging_set 

logger = logging.getLogger(__name__)

class Card:
    def __init__(self, word, translation, sentence):
        self.word = word
        self.translation = translation
        self.sentence = sentence

  
