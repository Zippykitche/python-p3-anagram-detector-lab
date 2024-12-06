# your code goes here!
class Anagram:
    def __init__(self, word):
       self.word = word.lower()

    def match(self, list):
        sorted_word = sorted(self.word)
        return [word for word in list if sorted(word.lower()) == sorted_word]