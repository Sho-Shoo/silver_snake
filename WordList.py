import json


class WordList:

    def __init__(self):
        self.list = []
        # open swear_words.json to load swear word data base
        with open('swearwords.json', encoding='utf-8') as data:
            swearwords = json.load(data)
            for i in swearwords['RECORDS']:
                if i['language'] == 'en':
                    self.list.append(i['word'])

        print("swearwords.json loaded!")

    # add a swear word to the word list
    def add(self, addition):
        # test if the list already has the word
        still_add = True
        for i in self.list:
            if i == addition:
                still_add = False
                break

        if still_add:
            self.list.append(addition.casefold())
        else:
            print("Already exist")

    # return a dictionary of swear words sorted by their first letters
    # !!! not in alphabetical order !!!
    def generate_swear_word_dict(self):
        result = {}
        for word in self.list:
            if not word[0].casefold() in result.keys():
                result[word[0].casefold()] = [word]
            else:
                result[word[0].casefold()].append(word)

        return result

    def delete_word(self, word):
        try:
            self.list.remove(word)
        except:
            pass
