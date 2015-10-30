# astroid 470cbed45303 @/master
# pylint e0c045bf95af tip @/master

import math

class Number2Words(object):

    def __call__(self, num, as_list=False, ordinal=False):
        num_str = str(num)
        num_left = num_str
        words = []
        while num_left:
            if int(num_left) < 100:
                words.append(self.tens[int(num_left[0])])
                num_left = num_left[1:]
            else:
                mag = int(math.log10(int(num_left))/3)*3
                words += self(num_left[:-mag], True) + [self.scales[mag]]
                num_left = num_left[-mag:]

        words = [w.title() for w in words if w != '']
        if as_list:
            return words

num2words = Number2Words()
