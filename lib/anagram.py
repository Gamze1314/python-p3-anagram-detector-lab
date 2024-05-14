# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words_list):
        anagrams = []
        for word in words_list:
            # Check if the sorted letters of the word match the sorted letters of the instance word
            if sorted(word) == sorted(self.word):
                anagrams.append(word)
        return anagrams


listen = Anagram("listen")
words_list = ["enlist", "silent", "tinsel", "apple", "banana"]
print(listen.match(words_list))
