class Anagram:


    def __init__(self, word):
        self.word = word

    def match(self, list):
        matching_words = []
        sorted_word = "".join(sorted(self.word))
        for word in list:
            if "".join(sorted(word)) == sorted_word:
                matching_words.append(word)
        return matching_words