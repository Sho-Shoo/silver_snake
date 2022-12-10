from WordList import WordList


class Text:

    def __init__(self, txt):
        self.txt = txt

    def generate_analysis(self, word_list):
        arr = self.txt.split()
        result = {}

        # go through every swear word in the WordList class
        for swearword in word_list.list:
            has_it = False   # variable that shows if this swear word occurs
            position = []   # variable that shows the position[s] of this swear word in the text
            count = 0       # variable that shows how many times it occurs

            # go through every word in the text
            for i in range(0, len(arr)):
                if swearword.casefold() == arr[i].casefold():
                    has_it = True
                    position.append(i)
                    count += 1

            if has_it:
                result[swearword.casefold()] = {
                                    'position': position,
                                    'count': count
                                    }

        return result
